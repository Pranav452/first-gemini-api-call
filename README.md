# First Gemini API Call

A simple Python script to interact with Google's Gemini AI using the Google Generative AI API.

## What the Script Does

This script:
1. Takes user input via the console
2. Uses a fixed system prompt to guide the AI's behavior
3. Makes an API call to Google's Gemini AI
4. Prints the assistant's response
5. Displays token usage information (if available)

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- A Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/first-gemini-api-call.git
   cd first-gemini-api-call
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory with your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   **Note:** Do not commit your `.env` file to the repository.

## Running the Script

Run the script using Python:
```
python first_call.py
```

The script will prompt you to enter your question or statement, and will then display the AI's response.

## Example Usage

```
$ python first_call.py
Enter your prompt: What is machine learning?

Assistant's Response:
Machine learning is a branch of artificial intelligence that focuses on building systems that learn from data, identify patterns, and make decisions with minimal human intervention.

Token Usage:
Input tokens: 24
Output tokens: 37
Total tokens: 61
```
