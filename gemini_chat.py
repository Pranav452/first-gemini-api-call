import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    
    print("Welcome to Context-Aware Gemini Chat!")
    print("-----------------------------------")
    print("This chat maintains context across multiple turns.\n")
    
    # Let user choose model
    available_models = ["gemini-1.5-flash", "gemini-1.5-pro"]
    print("Available models:")
    for i, model_name in enumerate(available_models, 1):
        print(f"{i}. {model_name}")
    
    model_choice = 1  # Default to first model
    try:
        model_choice = int(input("Select a model (1-2, default=1): ") or "1")
        if model_choice < 1 or model_choice > len(available_models):
            model_choice = 1
    except ValueError:
        model_choice = 1
    
    model_name = available_models[model_choice - 1]
    print(f"Using model: {model_name}")
    
    # Let user set temperature
    temperature = 0.7  # Default temperature
    try:
        temp_input = input("Set temperature (0.0-1.0, default=0.7): ")
        if temp_input:
            temperature = float(temp_input)
            temperature = max(0.0, min(1.0, temperature))  # Clamp between 0 and 1
    except ValueError:
        temperature = 0.7
    
    print(f"Temperature set to: {temperature}")
    
    # Initialize the model with the chosen parameters
    model = genai.GenerativeModel(
        model_name,
        generation_config={
            "temperature": temperature,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 2048,
        }
    )
    
    # Start a chat session
    chat = model.start_chat(history=[])
    print("\nChat session started. Type 'exit' to end the conversation.\n")
    
    # Main chat loop
    turn_count = 0
    while True:
        turn_count += 1
        user_input = input(f"You (Turn {turn_count}): ")
        
        if user_input.lower() == 'exit':
            print("Ending chat session. Goodbye!")
            break
        
        # Send message to Gemini
        try:
            response = chat.send_message(user_input)
            
            print(f"\nAssistant (Turn {turn_count}): {response.text}\n")
            
            # Display token usage if available
            if hasattr(response, 'usage'):
                print(f"Token usage: Input={response.usage.prompt_tokens}, Output={response.usage.completion_tokens}, Total={response.usage.total_tokens}")
        
        except Exception as e:
            print(f"Error: {e}")
    
if __name__ == "__main__":
    main() 