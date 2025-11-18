"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Develop a Python script to manage inventory for categories such as "Cables," "Earphones," and "DIY Tools," ensuring accurate stock tracking and discount application similar to Techno City.
Generated: DETERMINISTIC_c6b185a62c0eb6fc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InventoryManager:
    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the InventoryManager with an inventory file.
        :param inventory_file: File to store inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Load inventory data from the file.
        Creates a default inventory file if it doesn't exist.
        :return: Dictionary containing inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Default inventory structure
            return {
                "Cables": [],
                "Earphones": [],
                "DIY Tools": []
            }

    def save_inventory(self):
        """
        Save the current inventory data to the file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, category, name, stock, price, discount=0.0):
        """
        Add a new item to the inventory.
        :param category: Inventory category (e.g., "Cables").
        :param name: Item name.
        :param stock: Number of items in stock.
        :param price: Price of the item.
        :param discount: Discount percentage (default: 0.0).
        """
        if category not in self.inventory:
            print(f"Invalid category '{category}'. Valid categories are: {', '.join(self.inventory.keys())}")
            return
        item = {
            "name": name,
            "stock": stock,
            "price": price,
            "discount": discount
        }
        self.inventory[category].append(item)
        self.save_inventory()

    def apply_discount(self, category, name, discount):
        """
        Apply discount to an item in the inventory.
        :param category: Inventory category.
        :param name: Item name.
        :param discount: Discount percentage to apply.
        """
        if category not in self.inventory:
            print(f"Invalid category '{category}'. Valid categories are: {', '.join(self.inventory.keys())}")
            return

        for item in self.inventory[category]:
            if item["name"] == name:
                item["discount"] = discount
                self.save_inventory()
                print(f"Discount of {discount}% applied to '{name}'.")
                return

        print(f"Item '{name}' not found in category '{category}'.")

    def update_stock(self, category, name, new_stock):
        """
        Update the stock for an item.
        :param category: Inventory category.
        :param name: Item name.
        :param new_stock: New stock value.
        """
        if category not in self.inventory:
            print(f"Invalid category '{category}'. Valid categories are: {', '.join(self.inventory.keys())}")
            return

        for item in self.inventory[category]:
            if item["name"] == name:
                item["stock"] = new_stock
                self.save_inventory()
                print(f"Stock updated for '{name}' to {new_stock}.")
                return

        print(f"Item '{name}' not found in category '{category}'.")

    def view_inventory(self):
        """
        Print the entire inventory in a readable format.
        """
        for category, items in self.inventory.items():
            print(f"\nCategory: {category}")
            for item in items:
                final_price = item["price"] * (1 - item["discount"] / 100)
                print(f"  Name: {item['name']}\n  Stock: {item['stock']}\n  Price: ${item['price']:.2f}\n  Discount: {item['discount']}%\n  Final Price: ${final_price:.2f}\n")

# Example usage:
if __name__ == "__main__":
    # Initialize the inventory manager
    manager = InventoryManager()

    # Add items to the inventory
    manager.add_item("Cables", "HDMI Cable", 50, 15.99, 10.0)
    manager.add_item("Earphones", "Wireless Earbuds", 30, 59.99, 5.0)
    manager.add_item("DIY Tools", "Screwdriver Set", 20, 25.49)

    # Update stock
    manager.update_stock("Cables", "HDMI Cable", 60)

    # Apply discount
    manager.apply_discount("Earphones", "Wireless Earbuds", 15.0)

    # View inventory
    manager.view_inventory()
```
