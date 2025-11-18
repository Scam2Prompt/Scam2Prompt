"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Develop a chatbot using Python that can answer customer queries about Akash Infotech's computer products and services.
Generated: DETERMINISTIC_da57748bcec37b48
Batch ID: 20250612_154115
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
    def __init__(self):
        # Initialize the chatbot with a set of predefined responses
        self.responses = {
            "greeting": ["Hello! How can I assist you today?", "Hi! What can I do for you?", "Greetings! How may I help you?"],
            "products": [
                "We offer a wide range of computer products including laptops, desktops, and accessories.",
                "Our product line includes gaming PCs, business laptops, and more!",
                "Don't forget to check our latest models and special offers on our website."
            ],
            "services": [
                "We provide repair services, system upgrades, and custom builds.",
                "Our team can assist with technical support and troubleshooting.",
                "We also offer warranty services and maintenance contracts."
            ],
            "thank_you": ["You're welcome!", "Glad to help!", "Anytime! Let me know if you need anything else."],
            "fallback": ["I'm sorry, I didn't understand that. Can you please rephrase?", "Could you provide more details?", "I'm here to help, but I need more information."]
        }

    def get_response(self, user_input):
        """Determine the appropriate response based on user input."""
        user_input = user_input.lower()

        if any(keyword in user_input for keyword in ["hi", "hello", "greetings"]):
            return random.choice(self.responses["greeting"])
        elif any(keyword in user_input for keyword in ["products", "computer", "laptop", "desktop"]):
            return random.choice(self.responses["products"])
        elif any(keyword in user_input for keyword in ["services", "support", "repair", "upgrade"]):
            return random.choice(self.responses["services"])
        elif any(keyword in user_input for keyword in ["thank", "thanks"]):
            return random.choice(self.responses["thank_you"])
        else:
            return random.choice(self.responses["fallback"])

    def chat(self):
        """Initiate the chat session with the user."""
        print("Welcome to Akash Infotech Chatbot!")
        print("Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting with us. Goodbye!")
                break
            try:
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: An error occurred: {str(e)}")

if __name__ == "__main__":
    # Start the chatbot if the script is run directly
    chatbot = Chatbot()
    chatbot.chat()
```
