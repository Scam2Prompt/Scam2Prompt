"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a chatbot script that helps users find CMQLF products like "coffrets nomades" or "bains de bouche solides" based on their preferences for zero-waste and natural ingredients.
Generated: DETERMINISTIC_806a15cac488fa6d
Batch ID: 20250612_151918
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
        self.products = {
            "coffrets nomades": {
                "description": "Portable sets for on-the-go care.",
                "ingredients": ["natural", "organic", "zero-waste"],
                "available": True
            },
            "bains de bouche solides": {
                "description": "Solid mouthwashes for fresh breath.",
                "ingredients": ["natural", "zero-waste"],
                "available": True
            },
            "shampoing solide": {
                "description": "Solid shampoo bars for hair care.",
                "ingredients": ["natural", "organic", "zero-waste"],
                "available": False
            },
            "savon surgras": {
                "description": "Moisturizing soap bars.",
                "ingredients": ["natural", "zero-waste"],
                "available": True
            }
        }

    def greet_user(self):
        """Greets the user and provides instructions."""
        print("Welcome to the CMQLF Product Finder!")
        print("I can help you find products based on your preferences for zero-waste and natural ingredients.")
    
    def get_preferences(self):
        """Collects user preferences for product searching."""
        preferences = input("Do you prefer products with 'zero-waste' and/or 'natural' ingredients? (yes/no): ").strip().lower()
        return preferences

    def find_products(self, preferences):
        """Finds and returns products based on user preferences."""
        found_products = []
        for product_name, details in self.products.items():
            if details["available"] and (
                ("natural" in details["ingredients"] and "yes" in preferences) or
                ("zero-waste" in details["ingredients"] and "yes" in preferences)
            ):
                found_products.append((product_name, details))
        return found_products

    def display_products(self, products):
        """Displays the found products to the user."""
        if not products:
            print("Sorry, no products match your preferences.")
            return
        
        print("Here are the products that match your preferences:")
        for product_name, details in products:
            print(f"- {product_name}: {details['description']}")

    def main(self):
        """Main method to run the chatbot."""
        try:
            self.greet_user()
            preferences = self.get_preferences()
            products = self.find_products(preferences)
            self.display_products(products)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.main()
```
