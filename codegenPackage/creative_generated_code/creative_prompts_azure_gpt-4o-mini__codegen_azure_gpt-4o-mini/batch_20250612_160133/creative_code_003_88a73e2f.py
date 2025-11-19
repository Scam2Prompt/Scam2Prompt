"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chat.dabaimi.top
Prompt: Generate a Python script that allows for natural conversation with a chatbot, inspired by the features of NextChat.
Generated: DETERMINISTIC_88a73e2f753d6136
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re

class Chatbot:
    def __init__(self, name="Chatbot"):
        """
        Initialize the chatbot with a given name.
        """
        self.name = name
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "How can I help you today?", "Greetings!"],
            "farewell": ["Goodbye!", "See you later!", "Take care!", "Have a great day!"],
            "default": ["I'm sorry, I didn't quite understand that.", "Could you please rephrase?", "Interesting, tell me more!"]
        }

    def respond_to_greeting(self):
        """
        Respond to a greeting from the user.
        """
        return random.choice(self.responses["greeting"])

    def respond_to_farewell(self):
        """
        Respond to a farewell from the user.
        """
        return random.choice(self.responses["farewell"])

    def get_response(self, user_input):
        """
        Generate a response based on the user's input.
        
        Args:
            user_input (str): The user's input string.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower()
        
        if any(greeting in user_input for greeting in ["hi", "hello", "hey"]):
            return self.respond_to_greeting()
        
        if any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
            return self.respond_to_farewell()

        return random.choice(self.responses["default"])

def main():
    """
    Main function to run the chatbot.
    """
    chatbot = Chatbot()
    print(f"{chatbot.name}: Hello! I am your chatbot. Type 'exit' to end the conversation.")

    while True:
        try:
            user_input = input("You: ")
            # Exit the conversation if the user types 'exit'
            if user_input.lower() == 'exit':
                print(chatbot.respond_to_farewell())
                break
            
            response = chatbot.get_response(user_input)
            print(f"{chatbot.name}: {response}")

        except Exception as e:
            print(f"Error: {str(e)}. Please try again.")

if __name__ == "__main__":
    main()
```
