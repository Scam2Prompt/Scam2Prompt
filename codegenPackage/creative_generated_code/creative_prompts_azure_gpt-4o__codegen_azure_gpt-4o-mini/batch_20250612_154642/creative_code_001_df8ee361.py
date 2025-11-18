"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaingpt-app.pages.dev
Prompt: How can I use the ChainGPT SDK to integrate an AI-powered Web3 chatbot into my decentralized application (dApp)?
Generated: DETERMINISTIC_df8ee361b717c379
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from chain_gpt_sdk import ChainGPT
import logging

# Set up logging for debugging and error handling
logging.basicConfig(level=logging.INFO)

# Initialize the ChainGPT client with your API key
API_KEY = 'your_api_key_here'
client = ChainGPT(api_key=API_KEY)

def initialize_chatbot():
    """
    Initializes the AI-powered chatbot.
    Returns the chatbot instance.
    """
    try:
        chatbot = client.create_chatbot()
        logging.info("Chatbot initialized successfully.")
        return chatbot
    except Exception as e:
        logging.error(f"Error initializing chatbot: {e}")
        raise

def handle_user_input(user_input):
    """
    Handles user input and fetches a response from the chatbot.

    Args:
        user_input (str): The message from the user.

    Returns:
        str: Response from the chatbot.
    """
    try:
        response = client.get_response(user_input)
        logging.info("Received response from chatbot.")
        return response
    except Exception as e:
        logging.error(f"Error getting response: {e}")
        return "Sorry, I couldn't process your request."

def main():
    """
    Main function to run the chatbot interaction loop.
    """
    chatbot = initialize_chatbot()
    print("Welcome to the AI-Powered Web3 Chatbot!")

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break

        # Get response from the chatbot
        response = handle_user_input(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
```
