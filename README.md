# Gemini API Examples

A collection of Python scripts to demonstrate different ways to interact with Google's Gemini AI using the Google Generative AI API.

## Scripts Overview

This project includes four scripts:

1. **first_call.py**: A simple script that takes user input via the console and makes a single API call to Gemini.
2. **interactive_playground.py**: An interactive prompt playground to experiment with different Gemini API parameters.
3. **prompt_injection_simulator.py**: A tool to test AI system resilience against prompt injection and jailbreak attacks.
4. **gemini_chat.py**: A context-aware chatbot that maintains conversation history across multiple turns.

## Script Details

### 1. First Call Script
This script:
- Takes user input via the console
- Uses a fixed system prompt to guide the AI's behavior
- Makes an API call to Google's Gemini AI
- Prints the assistant's response
- Displays token usage information (if available)

### 2. Interactive Playground
This script allows you to:
- Create product descriptions with varying parameters
- Test different combinations of:
  - Temperature (0.0, 0.7, 1.2)
  - Max output tokens (50, 150, 300)
  - Top-p values (0.8, 1.0)
- Select different Gemini models
- View and compare all outputs in a table format
- Save results to JSON and CSV files
- Read a reflection on how different parameters affect the output

### 3. Prompt Injection Simulator
This script helps you:
- Test AI system resilience against various prompt injection attacks
- Includes 7 predefined attack types:
  - Direct Command Injection
  - System Prompt Extraction
  - Role-Play Evasion
  - False Premises
  - Delimiter Confusion
  - DAN (Do Anything Now) Attack
  - Token Manipulation
- Provides "Safe Mode" to detect and block suspicious prompts
- Analyzes attack success/failure
- Generates defense recommendations
- Saves results to a JSON file

### 4. Context-Aware Chat
This script features:
- Multi-turn conversation with preserved context
- User-configurable model selection (gemini-1.5-flash or gemini-1.5-pro)
- Adjustable temperature setting to control response creativity
- Continuous chat session until user exits
- Token usage tracking (when available)

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- A Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/gemini-api-examples.git
   cd gemini-api-examples
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

## Running the Scripts

### Basic Script
```
python first_call.py
```

### Interactive Playground
```
python interactive_playground.py
```
Follow the prompts to configure and test different parameter combinations.

### Prompt Injection Simulator
```
python prompt_injection_simulator.py
```
Follow the prompts to test different attack types against a system prompt.

### Context-Aware Chat
```
python gemini_chat.py
```
Select a model and temperature, then chat with the AI across multiple turns.

## Example Usage

### Basic Script
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

### Interactive Playground
```
$ python interactive_playground.py
Welcome to the Interactive Prompt Playground!
---------------------------------------------
Enter a product to describe (e.g., iPhone, Tesla, running shoes): Tesla Model 3
Enter a system prompt (or press Enter for default): 
Enter a user prompt (or press Enter for default): 

Select a model:
1. gemini-1.5-flash
2. gemini-1.5-pro
Enter your choice (number): 1

Generating outputs with different parameter combinations...
This may take a minute...

Results Summary:
[Table of results with different parameter combinations]

Detailed Results:
[Detailed outputs for each parameter combination]

Results saved to tesla_model_3_results.json and tesla_model_3_results.csv

Reflection on Parameter Effects:
[Reflection on how different parameters affected the outputs]
```

### Prompt Injection Simulator
```
$ python prompt_injection_simulator.py
Welcome to the Prompt Injection & Jailbreak Defense Simulator!
============================================================
[...]
```

### Context-Aware Chat
```
$ python gemini_chat.py
Welcome to Context-Aware Gemini Chat!
-----------------------------------
[...]
```
