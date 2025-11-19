"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Create a simple chatbot script to handle customer inquiries about hair services and products, such as answering questions about hair care and providing recommendations.
Generated: DETERMINISTIC_fe5eece3e37d573f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HairCareChatbot:
    def __init__(self):
        # Predefined responses for common inquiries
        self.responses = {
            "services": "We offer haircuts, coloring, styling, and treatments. What service are you interested in?",
            "products": "We have shampoos, conditioners, hair masks, and styling products. What type of product are you looking for?",
            "recommendation": "Based on your hair type, I recommend using a sulfate-free shampoo and a hydrating conditioner. Would you like more details?",
            "hours": "Our salon is open from 9 AM to 7 PM, Monday through Saturday. Would you like to book an appointment?",
            "pricing": "Our pricing varies depending on the service. Haircuts start at $25, and coloring starts at $50. Would you like a detailed price list?",
            "default": "I'm sorry, I didn't quite understand that. Could you please rephrase your question?"
        }

    def get_response(self, user_input):
        """
        Generate a response based on user input.

        Args:
            user_input (str): The customer's inquiry.

        Returns:
            str: The chatbot's response.
        """
        # Normalize user input to lowercase for matching
        user_input = user_input.lower()

        # Match user input to predefined responses
        if "service" in user_input or "services" in user_input:
            return self.responses["services"]
        elif "product" in user_input or "products" in user_input:
            return self.responses["products"]
        elif "recommend" in user_input or "recommendation" in user_input:
            return self.responses["recommendation"]
        elif "hour" in user_input or "open" in user_input:
            return self.responses["hours"]
        elif "price" in user_input or "cost" in user_input:
            return self.responses["pricing"]
        else:
            return self.responses["default"]

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Welcome to the Hair Care Chatbot! How can I assist you today?")
        while True:
            try:
                # Get user input
                user_input = input("You: ")
                
                # Exit condition
                if user_input.lower() in ["exit", "quit"]:
                    print("Chatbot: Thank you for chatting with me! Have a great day!")
                    break
                
                # Generate and display response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Chatbot: I'm sorry, something went wrong. Please try again later. (Error: {e})")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = HairCareChatbot()
    chatbot.chat()
```
