"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiomartdigital.com
Prompt: Create a chatbot script that helps customers navigate Jiomart Digital's product categories, such as home appliances and personal care, and assists with financing options.
Generated: DETERMINISTIC_d5a50cc11c421454
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class Chatbot:
    def __init__(self):
        """Initializes the chatbot with predefined product categories and financing options."""
        self.categories = {
            "home_appliances": ["Refrigerator", "Washing Machine", "Microwave Oven"],
            "personal_care": ["Shampoo", "Face Wash", "Toothpaste"],
        }
        self.financing_options = [
            "Pay in 3 installments",
            "Zero-interest financing for 6 months",
            "10% discount on upfront payment"
        ]
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Welcome! What would you like to know?"
        ]

    def greet_user(self):
        """Greets the user with a random greeting."""
        return random.choice(self.greetings)

    def get_categories(self):
        """Returns the available product categories."""
        return list(self.categories.keys())

    def get_products(self, category):
        """Returns products for the specified category if it exists.

        Args:
            category (str): The category to retrieve products from.

        Returns:
            list: List of products in the specified category.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found.")
        return self.categories[category]

    def get_financing_options(self):
        """Returns available financing options."""
        return self.financing_options

    def run_bot(self):
        """Runs the main interaction loop for the chatbot."""
        print(self.greet_user())
        while True:
            user_input = input("You: ").strip().lower()

            if user_input == "exit":
                print("Chatbot: Thank you for chatting! Goodbye!")
                break

            elif user_input == "categories":
                categories = self.get_categories()
                print(f"Chatbot: We have the following categories: {', '.join(categories)}.")

            elif user_input.startswith("products in "):
                category = user_input.split("products in ")[-1]
                try:
                    products = self.get_products(category)
                    print(f"Chatbot: In the '{category}' category, we have: {', '.join(products)}.")
                except ValueError as e:
                    print(f"Chatbot: {e}")

            elif user_input == "financing options":
                options = self.get_financing_options()
                print(f"Chatbot: Here are the financing options: {', '.join(options)}.")

            else:
                print("Chatbot: I'm sorry, I didn't understand that. Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    # Create an instance of the Chatbot and run it
    bot = Chatbot()
    bot.run_bot()
```
