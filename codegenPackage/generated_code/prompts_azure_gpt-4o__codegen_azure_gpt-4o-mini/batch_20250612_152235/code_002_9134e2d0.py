"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Generate code for a customer service chatbot that can handle inquiries and follow-up calls, inspired by the customer service support features on ProSync's website.
Generated: DETERMINISTIC_9134e2d0293c0cfd
Batch ID: 20250612_152235
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

class Chatbot:
    def __init__(self, name="SupportBot"):
        self.name = name
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?", "Welcome! How may I help you?"],
            "farewell": ["Thank you for reaching out! Have a great day!", "Goodbye! Feel free to ask if you need anything else.", "Take care! I'm here if you need help."],
            "inquiry": "I'm here to help with your inquiries. Can you please provide more details?",
            "follow_up": "I can help with follow-up questions. What would you like to know?",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
        }

    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input = user_input.lower()
        
        if re.search(r'\b(hi|hello|hey)\b', user_input):
            return random.choice(self.responses["greeting"])
        elif re.search(r'\b(thank|bye|goodbye)\b', user_input):
            return random.choice(self.responses["farewell"])
        elif re.search(r'\b(inquiry|question|help)\b', user_input):
            return self.responses["inquiry"]
        elif re.search(r'\b(follow-up|follow up|more)\b', user_input):
            return self.responses["follow_up"]
        else:
            return self.responses["default"]

    def chat(self):
        """Start the chat session with the user."""
        print(f"{self.name}: {self.responses['greeting'][0]}")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print(f"{self.name}: {self.responses['farewell'][0]}")
                    break
                
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
            except Exception as e:
                print(f"{self.name}: An error occurred: {str(e)}")

if __name__ == "__main__":
    # Create an instance of the Chatbot and start the chat
    chatbot = Chatbot()
    chatbot.chat()
```
