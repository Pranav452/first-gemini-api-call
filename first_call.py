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
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    instruction = "You are a helpful and concise assistant. Provide clear and accurate information. in 100 words or less."
    user_query = input("Enter your prompt: ")
    
    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{instruction}\n\nUser query: {user_query}")
        
        print("\nAssistant's Response:")
        print(response.text)
        
        if hasattr(response, 'usage'):
            print("\nToken Usage:")
            print(f"Input tokens: {response.usage.prompt_tokens}")
            print(f"Output tokens: {response.usage.completion_tokens}")
            print(f"Total tokens: {response.usage.total_tokens}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 