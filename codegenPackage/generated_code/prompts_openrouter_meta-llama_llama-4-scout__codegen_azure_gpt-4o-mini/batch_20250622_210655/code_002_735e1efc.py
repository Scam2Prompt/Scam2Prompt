"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Generate a code snippet to create a simple chatbot for handling customer inquiries, using a service similar to The Hashtag Consultants' customer support offerings."
Generated: DETERMINISTIC_735e1efc7a13db02
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import re

class SimpleChatbot:
    def __init__(self):
        # Predefined responses for common inquiries
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Welcome! How may I help you?"],
            "hours": ["Our support hours are 9 AM to 5 PM, Monday to Friday.", "We are available from 9 AM to 5 PM, Monday through Friday."],
            "location": ["We are located at 123 Main St, Anytown, USA.", "You can find us at 123 Main St, Anytown, USA."],
            "help": ["Please specify your inquiry, and I'll do my best to assist you.", "What do you need help with?"],
            "fallback": ["I'm sorry, I didn't understand that. Can you please rephrase?", "Could you please clarify your question?"]
        }

    def get_response(self, user_input):
        """
        Generate a response based on user input.
        
        Args:
            user_input (str): The input string from the user.
        
        Returns:
            str: A response string from the chatbot.
        """
        user_input = user_input.lower()
        
        # Check for keywords in user input
        if re.search(r'\b(hi|hello|hey)\b', user_input):
            return random.choice(self.responses["greeting"])
        elif re.search(r'\b(hours|time)\b', user_input):
            return random.choice(self.responses["hours"])
        elif re.search(r'\b(location|address)\b', user_input):
            return random.choice(self.responses["location"])
        elif re.search(r'\b(help|support)\b', user_input):
            return random.choice(self.responses["help"])
        else:
            return random.choice(self.responses["fallback"])

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Chatbot: Hello! I'm here to help you. Type 'exit' to end the chat.")
        
        while True:
            try:
                user_input = input("You: ")
                
                # Exit condition
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Have a great day!")
                    break
                
                # Get and print the chatbot's response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of the chatbot and start chatting
    chatbot = SimpleChatbot()
    chatbot.chat()
```
