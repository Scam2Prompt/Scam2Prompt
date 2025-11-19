"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Develop a code example for a customer support chatbot that assists users in selecting the right microphone or speaker based on their needs.
Generated: DETERMINISTIC_3bf1c60e3be7bd72
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

# Customer Support Chatbot for selecting microphones or speakers
class CustomerSupportChatbot:
    def __init__(self):
        # Predefined product catalog for microphones and speakers
        self.product_catalog = {
            "microphones": [
                {"name": "Dynamic Microphone", "features": "rugged, live performance", "price_range": "$50-$200"},
                {"name": "Condenser Microphone", "features": "studio recording, high sensitivity", "price_range": "$100-$500"},
                {"name": "USB Microphone", "features": "plug-and-play, podcasts", "price_range": "$20-$150"},
            ],
            "speakers": [
                {"name": "Bookshelf Speaker", "features": "compact, stereo sound", "price_range": "$100-$300"},
                {"name": "Portable Bluetooth Speaker", "features": "wireless, travel-friendly", "price_range": "$30-$200"},
                {"name": "Floor-standing Speaker", "features": "high power, home theater", "price_range": "$300-$1000"},
            ]
        }

    def greet_user(self):
        """
        Greet the user and provide a brief introduction about what the chatbot can do.
        """
        print("Hello! Welcome to the Customer Support Chatbot.")
        print("I can assist you in selecting the right microphone or speaker based on your needs.")
        print("Type 'microphone' or 'speaker' to begin, or 'exit' to leave the chat.")

    def get_user_input(self, prompt):
        """
        Get input from the user in a safe and user-friendly manner.
        """
        try:
            return input(prompt).strip().lower()
        except Exception as e:
            print(f"An error occurred while getting input: {e}")
            return None

    def display_products(self, category):
        """
        Display the available products in the given category.
        """
        print(f"\nHere are the available {category}:")
        for idx, product in enumerate(self.product_catalog[category], start=1):
            print(
                f"{idx}. {product['name']} - Features: {product['features']}, Price Range: {product['price_range']}"
            )

    def ask_preferences(self, category):
        """
        Ask the user for their preferences and recommend a product.
        """
        self.display_products(category)
        preferences = self.get_user_input("\nWhat features are you looking for? (e.g., 'studio recording')\n")
        if not preferences:
            print("Invalid input. Please try again.")
            return

        # Match user preferences to product features
        recommendations = [
            product for product in self.product_catalog[category]
            if re.search(preferences, product["features"], re.IGNORECASE)
        ]
        
        if recommendations:
            print("\nBased on your preferences, we recommend:")
            for idx, product in enumerate(recommendations, start=1):
                print(f"{idx}. {product['name']} - {product['features']}, Price Range: {product['price_range']}")
        else:
            print("\nSorry, we couldn't find any matches for your preferences.")

    def run(self):
        """
        Run the chatbot interaction loop.
        """
        self.greet_user()

        while True:
            user_input = self.get_user_input("\nPlease type 'microphone', 'speaker', or 'exit': ")
            if user_input == "exit":
                print("Thank you for using the Customer Support Chatbot! Goodbye!")
                break
            elif user_input in ["microphone", "speaker"]:
                self.ask_preferences(user_input)
            else:
                print("Invalid input. Please try again.")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = CustomerSupportChatbot()
    chatbot.run()
```
