"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collect-pudgypenguins.pages.dev
Prompt: Write code to design a trading card inventory system for Pudgy Penguins collectibles, including features for tracking "GoldFeathers" items.
Generated: DETERMINISTIC_dd2c4bb92a338862
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TradingCardInventory:
    """
    A class to manage trading card inventory for Pudgy Penguins collectibles,
    including specific tracking for "GoldFeathers" items.
    """
    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.inventory = {}

    def add_card(self, card_name, card_type, quantity=1):
        """
        Adds a card to the inventory.
        :param card_name: The name of the card.
        :param card_type: The type of the card (e.g., 'GoldFeathers', 'Standard').
        :param quantity: The number of cards to add (default is 1).
        """
        if card_name in self.inventory:
            self.inventory[card_name]['quantity'] += quantity
        else:
            self.inventory[card_name] = {'type': card_type, 'quantity': quantity}

    def remove_card(self, card_name, quantity=1):
        """
        Removes a specified quantity of a card from the inventory.
        :param card_name: The name of the card to remove.
        :param quantity: The number of cards to remove (default is 1).
        :raises ValueError: If the card does not exist or if the quantity to remove exceeds available stock.
        """
        if card_name not in self.inventory:
            raise ValueError(f"Card '{card_name}' does not exist in inventory.")
        if self.inventory[card_name]['quantity'] < quantity:
            raise ValueError(f"Cannot remove {quantity} of '{card_name}' - only {self.inventory[card_name]['quantity']} available.")
        
        self.inventory[card_name]['quantity'] -= quantity
        if self.inventory[card_name]['quantity'] == 0:
            del self.inventory[card_name]

    def get_card_info(self, card_name):
        """
        Retrieves information about a specific card.
        :param card_name: The name of the card to retrieve information for.
        :return: A dictionary with card type and quantity.
        :raises ValueError: If the card does not exist in inventory.
        """
        if card_name not in self.inventory:
            raise ValueError(f"Card '{card_name}' does not exist in inventory.")
        return self.inventory[card_name]

    def list_gold_feathers(self):
        """
        Lists all "GoldFeathers" cards in the inventory.
        :return: A dictionary containing "GoldFeathers" cards and their quantities.
        """
        return {card: details for card, details in self.inventory.items() if details['type'] == 'GoldFeathers'}

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.
        :param file_path: The file path where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.
        :param file_path: The file path from which inventory will be loaded.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            print(f"Error reading inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data in file: {e}")


# Example usage:
if __name__ == "__main__":
    inventory = TradingCardInventory()

    # Add cards
    inventory.add_card("Penguin King", "GoldFeathers", 3)
    inventory.add_card("Snowy", "Standard", 5)

    # Remove a card
    try:
        inventory.remove_card("Penguin King", 1)
    except ValueError as e:
        print(e)

    # Get card information
    try:
        card_info = inventory.get_card_info("Penguin King")
        print(f"Penguin King Info: {card_info}")
    except ValueError as e:
        print(e)

    # List all GoldFeathers cards
    gold_feathers = inventory.list_gold_feathers()
    print(f"GoldFeathers Cards: {gold_feathers}")

    # Save inventory to a file
    inventory.save_inventory_to_file("inventory.json")

    # Load inventory from a file
    try:
        inventory.load_inventory_from_file("inventory.json")
        print("Inventory successfully loaded from file.")
    except ValueError as e:
        print(e)
```
