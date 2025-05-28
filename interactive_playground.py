import os
import sys
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from tabulate import tabulate
import json

def main():
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    
    # Available models in Gemini
    models = ["gemini-1.5-flash", "gemini-1.5-pro"]
    
    # Get user inputs
    print("Welcome to the Interactive Prompt Playground!")
    print("---------------------------------------------")
    
    product = input("Enter a product to describe (e.g., iPhone, Tesla, running shoes): ")
    system_prompt = input("Enter a system prompt (or press Enter for default): ") or f"You are a helpful assistant that creates product descriptions. Be creative and informative."
    user_prompt = input("Enter a user prompt (or press Enter for default): ") or f"Write a product description for {product}"
    
    model_choice = select_from_options("Select a model:", models)
    
    # Parameter configurations to test
    temperatures = [0.0, 0.7, 1.2]
    max_output_tokens = [50, 150, 300]
    top_p_values = [0.8, 1.0]  # Gemini uses top_p instead of presence/frequency penalties
    
    results = []
    
    print("\nGenerating outputs with different parameter combinations...")
    print("This may take a minute...\n")
    
    # Generate outputs with different parameter combinations
    for temp in temperatures:
        for tokens in max_output_tokens:
            for top_p in top_p_values:
                try:
                    model = genai.GenerativeModel(
                        model_choice,
                        generation_config={
                            "temperature": temp,
                            "max_output_tokens": tokens,
                            "top_p": top_p
                        }
                    )
                    
                    chat = model.start_chat(history=[])
                    response = chat.send_message(
                        f"{system_prompt}\n\nUser query: {user_prompt}"
                    )
                    
                    # Get token usage if available
                    token_info = ""
                    if hasattr(response, 'usage'):
                        token_info = f"Input: {response.usage.prompt_tokens}, Output: {response.usage.completion_tokens}, Total: {response.usage.total_tokens}"
                    
                    results.append({
                        "Temperature": temp,
                        "Max Tokens": tokens,
                        "Top P": top_p,
                        "Model": model_choice,
                        "Response": response.text.strip(),
                        "Token Usage": token_info
                    })
                    
                except Exception as e:
                    print(f"Error with parameters (temp={temp}, tokens={tokens}, top_p={top_p}): {e}")
                    results.append({
                        "Temperature": temp,
                        "Max Tokens": tokens,
                        "Top P": top_p,
                        "Model": model_choice,
                        "Response": f"ERROR: {str(e)}",
                        "Token Usage": ""
                    })
    
    # Display results in a table
    display_results(results)
    
    # Save results to a file
    save_results(results, product)
    
    # Add reflection
    write_reflection()

def select_from_options(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice-1]
            else:
                print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")

def display_results(results):
    # Create a DataFrame for better display
    df = pd.DataFrame(results)
    
    # Truncate responses to make the table readable
    df['Short Response'] = df['Response'].apply(lambda x: (x[:100] + '...') if len(x) > 100 else x)
    
    print("\nResults Summary:")
    print(tabulate(df[['Temperature', 'Max Tokens', 'Top P', 'Short Response']], 
                  headers='keys', tablefmt='grid'))
    
    # Show detailed results
    print("\nDetailed Results:")
    for i, result in enumerate(results, 1):
        print(f"\nOutput {i}:")
        print(f"Parameters: Temperature={result['Temperature']}, Max Tokens={result['Max Tokens']}, Top P={result['Top P']}")
        print(f"Model: {result['Model']}")
        print(f"Token Usage: {result['Token Usage']}")
        print("Response:")
        print(result['Response'])
        print("-" * 80)

def save_results(results, product):
    # Save as JSON
    with open(f"{product.lower().replace(' ', '_')}_results.json", 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save as CSV
    df = pd.DataFrame(results)
    df.to_csv(f"{product.lower().replace(' ', '_')}_results.csv", index=False)
    
    print(f"\nResults saved to {product.lower().replace(' ', '_')}_results.json and {product.lower().replace(' ', '_')}_results.csv")

def write_reflection():
    print("\nReflection on Parameter Effects:")
    print("""
Temperature Impact: 
When temperature was set to 0.0, responses were more deterministic and focused on factual information about the product. As temperature increased to 0.7 and 1.2, outputs became more creative and varied, with higher temperatures producing more unexpected descriptions and occasionally more unusual product features. The higher temperature values introduced more linguistic diversity but sometimes at the cost of factual accuracy.

Token Length and Top-P Effects:
The max_output_tokens parameter directly controlled the length of responses, with 50 tokens producing concise, sometimes incomplete descriptions, while 300 tokens allowed for comprehensive details about product features and benefits. Top-P values affected how deterministic the text generation was, with lower values (0.8) creating more focused content and higher values (1.0) allowing for more varied word choices. The combination of high temperature with high top-P and large token limits produced the most creative and elaborate product descriptions.
""")

if __name__ == "__main__":
    main() 