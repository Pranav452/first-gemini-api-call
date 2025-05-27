import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load environment variables
    load_dotenv()
    
    # Configure the Gemini API with your API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
    
    genai.configure(api_key=api_key)

    # Set up the model
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # System prompt (fixed as per requirements)
    system_prompt = "You are a helpful and concise assistant. Provide clear and accurate information. in 100 words or less."
    
    # Get user input
    user_prompt = input("Enter your prompt: ")
    
    try:
        # For Gemini, we can use the system prompt as a prefix to the user's input
        # or use generation_config with the system instruction
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
        }
        
        # Create a chat session with the system prompt
        chat = model.start_chat(history=[])
        
        # Add system instruction as first message
        response = chat.send_message(f"{system_prompt}\n\nUser query: {user_prompt}")
        
        # Print the assistant's response
        print("\nAssistant's Response:")
        print(response.text)
        
        # Print token usage if available
        if hasattr(response, 'usage'):
            print("\nToken Usage:")
            print(f"Input tokens: {response.usage.prompt_tokens}")
            print(f"Output tokens: {response.usage.completion_tokens}")
            print(f"Total tokens: {response.usage.total_tokens}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 