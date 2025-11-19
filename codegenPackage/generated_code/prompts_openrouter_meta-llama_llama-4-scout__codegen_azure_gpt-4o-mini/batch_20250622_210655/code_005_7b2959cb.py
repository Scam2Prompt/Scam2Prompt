"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Create a simple chatbot script that responds to customer inquiries about Chat 'N' Chill's events, menu, and booking policies.
Generated: DETERMINISTIC_7b2959cb474bef8c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ChatNChillBot:
    def __init__(self):
        # Predefined responses for various inquiries
        self.responses = {
            "events": "We host a variety of events including live music, trivia nights, and themed parties. Check our website for the latest schedule!",
            "menu": "Our menu features a selection of appetizers, main courses, and desserts, along with a variety of beverages. Visit our menu page for more details.",
            "booking": "To book a table, please visit our booking page or call us at (123) 456-7890. We recommend booking in advance, especially on weekends.",
            "default": "I'm sorry, I didn't understand that. Can you please ask about our events, menu, or booking policies?"
        }

    def get_response(self, user_input):
        """
        Get a response based on user input.
        
        Args:
            user_input (str): The user's inquiry.
        
        Returns:
            str: The bot's response.
        """
        # Normalize user input to lower case for easier matching
        user_input = user_input.lower()

        # Check for keywords in user input and return appropriate response
        if re.search(r'\bevents?\b', user_input):
            return self.responses["events"]
        elif re.search(r'\bmenu\b', user_input):
            return self.responses["menu"]
        elif re.search(r'\bbooking\b', user_input):
            return self.responses["booking"]
        else:
            return self.responses["default"]

    def run(self):
        """
        Run the chatbot in a loop to continuously accept user input.
        """
        print("Welcome to Chat 'N' Chill Bot! How can I assist you today?")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print("Chat 'N' Chill Bot: Thank you for chatting! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chat 'N' Chill Bot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of the chatbot and run it
    bot = ChatNChillBot()
    bot.run()
```
