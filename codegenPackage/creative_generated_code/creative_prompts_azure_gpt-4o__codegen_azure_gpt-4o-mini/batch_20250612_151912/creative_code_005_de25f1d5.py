"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bettermost.net
Prompt: Develop a chatbot using OpenAI's GPT API that can answer questions about discussions from the "Chez Tremblay" section of the BetterMost forum.
Generated: DETERMINISTIC_de25f1d5014243e3
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load API keys and configurations
def load_api_key(filepath):
    """Load OpenAI API key from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            config = json.load(file)
            return config['openai_api_key']
    except (FileNotFoundError, KeyError) as e:
        logging.error(f"Error loading API key: {e}")
        raise

# Initialize OpenAI API
def initialize_openai(api_key):
    """Set up OpenAI API with the provided key."""
    openai.api_key = api_key

# Function to query the GPT model
def query_gpt(prompt):
    """Send a prompt to the OpenAI API and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Error querying GPT model: {e}")
        return "I'm sorry, but I couldn't process your request."

# Main chatbot function
def chatbot():
    """Run the chatbot for user interactions."""
    print("Welcome to the Chez Tremblay Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Query the GPT API with the user's question
        response = query_gpt(f"Answer the following question about the 'Chez Tremblay' section of the BetterMost forum: {user_input}")
        print(f"Bot: {response}")

if __name__ == "__main__":
    try:
        api_key = load_api_key("config.json")  # Path to your JSON config file
        initialize_openai(api_key)
        chatbot()
    except Exception as e:
        logging.critical(f"Failed to start the chatbot: {e}")
```

**Note**: Ensure you create a `config.json` file with your OpenAI API key in the following format:

```json
{
    "openai_api_key": "your_api_key_here"
}
```
