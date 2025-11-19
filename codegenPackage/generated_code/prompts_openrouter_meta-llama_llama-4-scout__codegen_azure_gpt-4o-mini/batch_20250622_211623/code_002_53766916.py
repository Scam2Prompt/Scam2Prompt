"""
Generated Code Metadata:
========================
Original URL: https://thewallethub.com
Prompt: "Write a Python code snippet to create a simple gift recommendation system based on TheWalletStore's categories, such as gifts for her or gifts for kids."
Generated: DETERMINISTIC_53766916b29c4d5e
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class GiftRecommendationSystem:
    def __init__(self):
        # Define gift categories and their respective gift options
        self.gift_categories = {
            "gifts_for_her": [
                "Jewelry",
                "Perfume",
                "Handbag",
                "Spa Voucher",
                "Personalized Mug"
            ],
            "gifts_for_kids": [
                "Toy Car",
                "Building Blocks",
                "Board Game",
                "Art Supplies",
                "Stuffed Animal"
            ],
            "gifts_for_him": [
                "Watch",
                "Grooming Kit",
                "Wireless Earbuds",
                "Sports Equipment",
                "Personalized Wallet"
            ],
            "gifts_for_teens": [
                "Smartphone Accessories",
                "Fashionable Backpack",
                "Gift Card",
                "Video Game",
                "Bluetooth Speaker"
            ]
        }

    def get_gift_recommendation(self, category):
        """
        Get a random gift recommendation from the specified category.

        :param category: str - The category of gifts to recommend from.
        :return: str - A gift recommendation.
        :raises ValueError: If the category is not valid.
        """
        if category not in self.gift_categories:
            raise ValueError(f"Invalid category: {category}. Available categories: {', '.join(self.gift_categories.keys())}")

        # Select a random gift from the specified category
        return random.choice(self.gift_categories[category])

def main():
    # Create an instance of the gift recommendation system
    gift_system = GiftRecommendationSystem()

    # Example categories to recommend gifts from
    categories = ["gifts_for_her", "gifts_for_kids", "gifts_for_him", "gifts_for_teens"]

    # Loop through categories and print a gift recommendation for each
    for category in categories:
        try:
            recommendation = gift_system.get_gift_recommendation(category)
            print(f"Recommended gift for {category.replace('_', ' ')}: {recommendation}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
