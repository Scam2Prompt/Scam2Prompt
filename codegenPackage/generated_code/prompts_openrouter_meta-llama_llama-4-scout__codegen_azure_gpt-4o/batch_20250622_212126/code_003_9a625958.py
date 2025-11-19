"""
Generated Code Metadata:
========================
Original URL: https://pin-ai.org
Prompt: How does AI impact human-computer interaction?
Generated: DETERMINISTIC_9a625958974af62a
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how AI impacts human-computer interaction (HCI) by simulating
a simple chatbot that uses natural language processing (NLP) to interact with users.
The chatbot leverages AI to understand user input and provide relevant responses.
"""

import random

def get_response(user_input):
    """
    Generate a response based on user input using a simple rule-based approach.
    In a production system, this could be replaced with a more advanced AI model.
    
    Args:
        user_input (str): The input provided by the user.
    
    Returns:
        str: The chatbot's response.
    """
    # Predefined responses for demonstration purposes
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a program, but I'm here to help you!",
        "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines.",
        "bye": "Goodbye! Have a great day!",
    }
    
    # Normalize user input to lowercase for matching
    normalized_input = user_input.lower()
    
    # Return a predefined response if available, otherwise a default response
    return responses.get(normalized_input, "I'm sorry, I didn't understand that. Can you rephrase?")

def main():
    """
    Main function to run the chatbot interaction loop.
    """
    print("Welcome to the AI Chatbot! Type 'bye' to exit.")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit the loop if the user types 'bye'
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye! Have a great day!")
                break
            
            # Generate and display the chatbot's response
            response = get_response(user_input)
            print(f"Chatbot: {response}")
        
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred: {e}")
            print("Chatbot: I'm sorry, something went wrong. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
