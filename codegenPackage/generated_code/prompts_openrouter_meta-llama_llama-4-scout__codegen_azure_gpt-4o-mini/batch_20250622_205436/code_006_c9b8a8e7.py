"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Generate a digital rate card for a sports business, including a value matrix for digital inventory to support partner discussions around value and intellectual property.
Generated: DETERMINISTIC_c9b8a8e70b1aabcd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class DigitalRateCard:
    """
    A class to represent a digital rate card for a sports business.
    It includes a value matrix for digital inventory to support partner discussions.
    """

    def __init__(self):
        """
        Initializes the DigitalRateCard with an empty inventory and pricing structure.
        """
        self.inventory = []
        self.pricing = {}

    def add_inventory_item(self, item_name, item_type, description):
        """
        Adds a digital inventory item to the rate card.

        Parameters:
        item_name (str): The name of the inventory item.
        item_type (str): The type of the inventory item (e.g., banner, video, social media).
        description (str): A brief description of the inventory item.
        """
        self.inventory.append({
            'item_name': item_name,
            'item_type': item_type,
            'description': description
        })

    def set_pricing(self, item_name, price):
        """
        Sets the pricing for a specific inventory item.

        Parameters:
        item_name (str): The name of the inventory item.
        price (float): The price for the inventory item.
        """
        if item_name not in [item['item_name'] for item in self.inventory]:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
        self.pricing[item_name] = price

    def generate_rate_card(self):
        """
        Generates a rate card as a Pandas DataFrame.

        Returns:
        pd.DataFrame: A DataFrame containing the inventory and pricing information.
        """
        if not self.inventory:
            raise ValueError("No inventory items found. Please add items before generating the rate card.")

        rate_card_data = []
        for item in self.inventory:
            item_name = item['item_name']
            price = self.pricing.get(item_name, 'N/A')  # Default to 'N/A' if no price is set
            rate_card_data.append({
                'Item Name': item_name,
                'Item Type': item['item_type'],
                'Description': item['description'],
                'Price': price
            })

        return pd.DataFrame(rate_card_data)

    def save_rate_card(self, file_name):
        """
        Saves the rate card to a CSV file.

        Parameters:
        file_name (str): The name of the file to save the rate card to.
        """
        try:
            rate_card_df = self.generate_rate_card()
            rate_card_df.to_csv(file_name, index=False)
            print(f"Rate card saved to {file_name}")
        except Exception as e:
            print(f"An error occurred while saving the rate card: {e}")

# Example usage
if __name__ == "__main__":
    try:
        rate_card = DigitalRateCard()
        rate_card.add_inventory_item("Homepage Banner", "Banner", "A banner displayed on the homepage.")
        rate_card.add_inventory_item("Social Media Post", "Social Media", "A post shared on social media platforms.")
        rate_card.set_pricing("Homepage Banner", 1500.00)
        rate_card.set_pricing("Social Media Post", 500.00)
        rate_card.save_rate_card("digital_rate_card.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
```
