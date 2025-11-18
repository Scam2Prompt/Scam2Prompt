"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Create a chatbot using Python that simulates Eximious Global's live chat service for recruitment and compliance inquiries.
Generated: DETERMINISTIC_48810a835cb0646b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    """A simple chatbot to simulate Eximious Global's live chat service for recruitment and compliance inquiries."""

    def __init__(self):
        # Define a list of predefined responses for common inquiries
        self.responses = {
            "hello": [
                "Hello! How can I assist you today?",
                "Hi there! What questions do you have for us?",
                "Greetings! How may I help you?"
            ],
            "recruitment": [
                "For recruitment inquiries, please visit our careers page.",
                "You can check our current job openings on our website.",
                "If you have questions about recruitment, let me know!"
            ],
            "compliance": [
                "For compliance questions, please refer to our compliance guidelines.",
                "Our compliance team is here to assist you with any inquiries.",
                "Feel free to ask if you have specific compliance questions!"
            ],
            "goodbye": [
                "Thank you for chatting with us! Have a great day!",
                "Goodbye! We look forward to assisting you again.",
                "Take care! If you have more questions, don't hesitate to reach out."
            ]
        }
        self.default_response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    def get_response(self, user_input):
        """Returns a chatbot response based on user input."""
        user_input = user_input.lower()  # Normalize user input to lowercase
        for keyword in self.responses:
            if keyword in user_input:
                return random.choice(self.responses[keyword])  # Return a random response from the matched category
        return self.default_response  # Return default response if no match found

    def start_chat(self):
        """Initiates the chat session with the user."""
        print("Welcome to Eximious Global's live chat! Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.start_chat()  # Start the chatbot session
    except Exception as e:
        print(f"An error occurred: {e}")  # General error handling
```
