"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Develop a chatbot that uses AI to assist customers in choosing printing services and calculating costs for items like self-inking stamps, die-cut stickers, and product labels, based on ThePrintNan's offerings.
Generated: DETERMINISTIC_a4f88840b6f90b9c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import json

# Load API Key from environment variable or secure storage
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API key. Please set the OPENAI_API_KEY environment variable.")

# Configure the OpenAI API client
openai.api_key = OPENAI_API_KEY

class PrintNanChatbot:
    """
    A chatbot that assists customers with choosing printing services and calculating costs.
    """

    def __init__(self):
        # Initialize product catalog and pricing information
        self.products = {
            "self-inking stamps": {
                "description": "Custom self-inking stamps available in various sizes.",
                "price_per_unit": 15.00,
            },
            "die-cut stickers": {
                "description": "High-quality, weather-resistant die-cut stickers.",
                "price_per_unit": 0.50,  # Price per sticker
            },
            "product labels": {
                "description": "Custom labels for products, available in different shapes and sizes.",
                "price_per_unit": 0.80,  # Price per label
            }
        }

    def get_product_info(self, product_name):
        """
        Fetch product details from the catalog.

        :param product_name: Name of the product
        :return: Product details (description and price) or None
        """
        return self.products.get(product_name.lower())

    def calculate_cost(self, product_name, quantity):
        """
        Calculate the total cost for a given product and quantity.

        :param product_name: Name of the product
        :param quantity: Quantity to order
        :return: Total cost (float) or None if product not found
        """
        product = self.get_product_info(product_name)
        if product:
            return round(product["price_per_unit"] * quantity, 2)
        return None

    def generate_response(self, user_input):
        """
        Generate AI-powered responses using OpenAI's GPT model.

        :param user_input: Customer's input message
        :return: AI-generated response
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use a specific GPT model
                prompt=f"The customer said: {user_input}\n"
                       f"Respond as a helpful assistant for printing services offering self-inking stamps, die-cut stickers, and product labels. Provide product details, pricing, or cost estimation if relevant.",
                max_tokens=150,
                temperature=0.5
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"An error occurred while generating a response: {str(e)}"

    def chat(self):
        """
        Main chatbot loop for interacting with customers.
        """
        print("Welcome to ThePrintNan Chatbot!")
        print("How can I assist you today? Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Thank you for chatting with ThePrintNan Chatbot. Goodbye!")
                break

            # Check if the user is asking about product information or cost calculation
            if "price" in user_input.lower() or "cost" in user_input.lower():
                # Extract product name and quantity (basic parsing for demo purposes)
                words = user_input.lower().split()
                for product_name in self.products.keys():
                    if product_name in words:
                        # Try to find the quantity mentioned (e.g., "10 stamps")
                        quantity = 1  # Default to 1 if no quantity is found
                        for word in words:
                            if word.isdigit():
                                quantity = int(word)
                                break

                        cost = self.calculate_cost(product_name, quantity)
                        if cost is not None:
                            print(f"The total cost for {quantity} {product_name} is ${cost:.2f}.")
                        else:
                            print(f"I couldn't find pricing for {product_name}. Please check the product name.")
                        break
                else:
                    print("Could you clarify which product you're asking about?")
            else:
                # Generate a general AI response
                ai_response = self.generate_response(user_input)
                print(f"Chatbot: {ai_response}")


# Entry point for the chatbot application
if __name__ == "__main__":
    chatbot = PrintNanChatbot()
    chatbot.chat()
```
