"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Generate a script to authenticate and interact with the Anthropic Claude API via UniWrapper, including steps to obtain and use the API key.
Generated: DETERMINISTIC_f304a6b11145449c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai
from openai import error

# Set your API key here or load from an environment variable
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Check if the API key is set
if not API_KEY:
    raise ValueError("API key is not set. Please set the 'ANTHROPIC_API_KEY' environment variable.")

# Initialize the UniWrapper with the API key
openai.api_key = API_KEY

def authenticate():
    """
    Function to test authentication with the Anthropic API.
    Returns True if authenticated, otherwise raises an error.
    """
    try:
        # Test a simple request to validate the API key
        response = openai.Completion.create(
            engine="claude-1",  # Replace with the appropriate engine name
            prompt="Hello, how are you?",
            max_tokens=5
        )
        return True
    except error.OpenAIError as e:
        print(f"Authentication failed: {e}")
        return False

def generate_response(prompt):
    """
    Function to generate a response from the Anthropic Claude API.
    
    Args:
    prompt (str): The prompt to send to the API.

    Returns:
    str: The response from the API.
    """
    try:
        response = openai.Completion.create(
            engine="claude-1",  # Replace with the appropriate engine name
            prompt=prompt,
            max_tokens=150
        )
        return response['choices'][0]['text'].strip()
    except error.OpenAIError as e:
        print(f"Error generating response: {e}")
        return None

def main():
    """
    Main function to run the script.
    It authenticates with the API and then prompts the user for input.
    """
    if authenticate():
        print("Authentication successful!")
        
        # Loop to keep asking the user for input
        while True:
            user_input = input("Enter your prompt (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break

            response = generate_response(user_input)
            if response:
                print(f"Response from Claude: {response}")

if __name__ == "__main__":
    main()
```

Make sure to set the `ANTHROPIC_API_KEY` environment variable before running this script. The API key can be obtained from your Anthropic account.
