"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: Develop a chatbot using Python that can answer customer queries about Akash Infotech's computer products and services.
Generated: DETERMINISTIC_da57748bcec37b48
Batch ID: 20250612_154115
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
    def __init__(self):
        # Predefined responses for common queries
        self.responses = {
            "products": [
                "We offer a variety of computer products including laptops, desktops, and accessories.",
                "Our product range includes high-performance laptops, budget-friendly desktops, and gaming accessories."
            ],
            "services": [
                "We provide repair services, software installation, and technical support.",
                "Our services include system upgrades, virus removal, and custom builds."
            ],
            "pricing": [
                "Our pricing varies based on the product and specifications. Please visit our website for detailed pricing.",
                "For specific pricing information, you can contact our sales team or check our online store."
            ],
            "support": [
                "You can reach our support team via email at support@akashinfotech.com or call us at 1-800-555-0199.",
                "For support, please visit our help center on our website."
            ],
            "greeting": [
                "Hello! How can I assist you today?",
                "Hi there! What questions do you have about our products and services?"
            ],
            "fallback": [
                "I'm sorry, I didn't understand that. Can you please rephrase your question?",
                "Could you please provide more details? I'm here to help!"
            ]
        }

    def get_response(self, user_input):
        """
        Generate a response based on user input.
        
        Args:
            user_input (str): The input query from the user.
        
        Returns:
            str: A response from the chatbot.
        """
        user_input = user_input.lower()
        
        # Check for keywords in user input
        if re.search(r'\b(products?|items?)\b', user_input):
            return random.choice(self.responses["products"])
        elif re.search(r'\b(services?)\b', user_input):
            return random.choice(self.responses["services"])
        elif re.search(r'\b(pricing|cost)\b', user_input):
            return random.choice(self.responses["pricing"])
        elif re.search(r'\b(support|help)\b', user_input):
            return random.choice(self.responses["support"])
        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            return random.choice(self.responses["greeting"])
        else:
            return random.choice(self.responses["fallback"])

    def chat(self):
        """
        Start the chatbot conversation loop.
        """
        print("Welcome to Akash Infotech Chatbot! Type 'exit' to end the chat.")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting with us! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of the Chatbot and start the chat
    chatbot = Chatbot()
    chatbot.chat()
```
