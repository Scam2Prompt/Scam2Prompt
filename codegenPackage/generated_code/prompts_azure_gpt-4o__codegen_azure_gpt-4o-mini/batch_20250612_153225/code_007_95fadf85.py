"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Create a chatbot script to handle customer inquiries about uniform customization, pricing, and delivery timelines, inspired by Real Garment's customer service approach.
Generated: DETERMINISTIC_95fadf859bca991f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import random

class Chatbot:
    def __init__(self):
        # Predefined responses for various inquiries
        self.responses = {
            "customization": [
                "We offer a variety of customization options including embroidery, screen printing, and color choices.",
                "You can customize your uniforms with logos, names, and other designs. What specific customization are you interested in?",
                "Our customization process is simple! Just provide us with your design, and we will take care of the rest."
            ],
            "pricing": [
                "Pricing varies based on the type of uniform and customization options. Can you provide more details?",
                "Our prices start at $20 per uniform, but it can vary based on your requirements.",
                "For bulk orders, we offer discounts. How many uniforms are you looking to order?"
            ],
            "delivery": [
                "Standard delivery takes 5-7 business days. Expedited options are available for an additional fee.",
                "Once your order is confirmed, we will provide you with a tracking number. Delivery typically takes 5-10 business days.",
                "We aim to deliver your customized uniforms within 7-10 business days after finalizing your order."
            ],
            "default": [
                "I'm sorry, I didn't quite understand that. Can you please rephrase your question?",
                "Could you please provide more details about your inquiry?",
                "I'm here to help! Please ask me anything about uniform customization, pricing, or delivery."
            ]
        }

    def get_response(self, user_input):
        """
        Determine the appropriate response based on user input.
        
        Args:
            user_input (str): The user's inquiry.
        
        Returns:
            str: A response from the chatbot.
        """
        user_input = user_input.lower()
        
        if re.search(r'customization|customize|design', user_input):
            return random.choice(self.responses["customization"])
        elif re.search(r'price|pricing|cost', user_input):
            return random.choice(self.responses["pricing"])
        elif re.search(r'delivery|shipping|timeline', user_input):
            return random.choice(self.responses["delivery"])
        else:
            return random.choice(self.responses["default"])

    def chat(self):
        """
        Start the chatbot conversation loop.
        """
        print("Welcome to Real Garment's Chatbot! How can I assist you today?")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("Chatbot: Thank you for chatting with us! Have a great day!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"Chatbot: Oops! Something went wrong. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()
```
