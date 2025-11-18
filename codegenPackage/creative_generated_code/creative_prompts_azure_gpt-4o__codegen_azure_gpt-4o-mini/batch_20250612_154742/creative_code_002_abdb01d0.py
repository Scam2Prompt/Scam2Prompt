"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom.gifts
Prompt: Generate code to simulate a daily updated "Item Shop" for Fortnite skins, including categories like Legendary, Epic, Rare, and Uncommon, with prices as described on Phantom's website.
Generated: DETERMINISTIC_abdb01d05e0bfa0a
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
import json

class Item:
    def __init__(self, name, category, price):
        """
        Initialize an Item with a name, category, and price.

        :param name: The name of the item.
        :param category: The category of the item (Legendary, Epic, Rare, Uncommon).
        :param price: The price of the item in V-Bucks.
        """
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self):
        """Convert the item to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

class ItemShop:
    def __init__(self):
        """
        Initialize the Item Shop with an empty item list and current date.
        """
        self.items = []
        self.current_date = datetime.now().date()

    def generate_items(self):
        """
        Generate a list of items for the shop based on predefined categories and prices.
        """
        categories = {
            'Legendary': 2000,
            'Epic': 1500,
            'Rare': 1000,
            'Uncommon': 500
        }

        item_names = [
            "Skin A", "Skin B", "Skin C", "Skin D", "Skin E",
            "Skin F", "Skin G", "Skin H", "Skin I", "Skin J"
        ]

        self.items = []
        for category, price in categories.items():
            # Randomly select an item name
            item_name = random.choice(item_names)
            item = Item(item_name, category, price)
            self.items.append(item)

    def update_shop(self):
        """
        Update the shop items daily.
        """
        if self.current_date < datetime.now().date():
            self.current_date = datetime.now().date()
            self.generate_items()

    def get_items(self):
        """
        Get the current list of items in the shop.

        :return: List of items in dictionary format.
        """
        return [item.to_dict() for item in self.items]

    def save_items_to_json(self, filename='item_shop.json'):
        """
        Save the current items to a JSON file.

        :param filename: The name of the file to save the items to.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.get_items(), json_file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving items to JSON: {e}")

def main():
    """
    Main function to simulate the item shop update and display items.
    """
    shop = ItemShop()
    shop.update_shop()  # Generate initial items
    shop.save_items_to_json()  # Save items to JSON

    # Display items to console
    for item in shop.get_items():
        print(f"{item['name']} ({item['category']}): {item['price']} V-Bucks")

if __name__ == "__main__":
    main()
```
