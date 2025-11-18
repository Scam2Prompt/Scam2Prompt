"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write a function to manage inventory for schools, including stock tracking and purchase records, inspired by Him Saral's Inventory module.
Generated: DETERMINISTIC_db5e6d5d66b30156
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Inventory:
    """
    A class to manage inventory for schools, including stock tracking and purchase records.
    """

    def __init__(self):
        """
        Initializes the inventory with an empty stock dictionary and an empty purchase records list.
        """
        self.stock = {}
        self.purchase_records = []

    def add_item(self, item_name: str, quantity: int, price_per_item: float):
        """
        Adds an item to the inventory or updates the quantity if it already exists.

        Parameters:
        - item_name (str): The name of the item.
        - quantity (int): The quantity of the item to add.
        - price_per_item (float): The price of the item.
        
        Raises:
        - ValueError: If quantity is not positive or if the price is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if price_per_item <= 0:
            raise ValueError("Price per item must be a positive float.")

        if item_name in self.stock:
            self.stock[item_name]['quantity'] += quantity
        else:
            self.stock[item_name] = {'quantity': quantity, 'price_per_item': price_per_item}

    def purchase_item(self, item_name: str, quantity: int):
        """
        Records a purchase of an item and updates the inventory.

        Parameters:
        - item_name (str): The name of the item to purchase.
        - quantity (int): The quantity of the item to purchase.

        Raises:
        - ValueError: If the item does not exist or if the quantity is not available.
        """
        if item_name not in self.stock:
            raise ValueError(f"Item '{item_name}' does not exist in inventory.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if self.stock[item_name]['quantity'] < quantity:
            raise ValueError("Insufficient quantity in stock.")

        # Update stock and record purchase
        self.stock[item_name]['quantity'] -= quantity
        total_cost = quantity * self.stock[item_name]['price_per_item']
        self.purchase_records.append({'item_name': item_name, 'quantity': quantity, 'total_cost': total_cost})

    def get_stock(self):
        """
        Returns the current stock of items in the inventory.

        Returns:
        dict: A dictionary containing item names and their stock details.
        """
        return self.stock

    def get_purchase_records(self):
        """
        Returns the purchase records.

        Returns:
        list: A list of purchase records.
        """
        return self.purchase_records

    def restock_item(self, item_name: str, quantity: int):
        """
        Restocks an item in the inventory.

        Parameters:
        - item_name (str): The name of the item to restock.
        - quantity (int): The quantity to add to the stock.

        Raises:
        - ValueError: If quantity is not positive or if the item does not exist.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if item_name not in self.stock:
            raise ValueError(f"Item '{item_name}' does not exist in inventory.")

        self.stock[item_name]['quantity'] += quantity

# Example usage
if __name__ == "__main__":
    # Create an inventory instance
    school_inventory = Inventory()

    # Adding items to the inventory
    school_inventory.add_item("Pencils", 100, 0.25)
    school_inventory.add_item("Notebooks", 50, 1.00)

    # Purchasing items
    school_inventory.purchase_item("Pencils", 20)

    # Displaying stock and purchase records
    print("Current Stock:", school_inventory.get_stock())
    print("Purchase Records:", school_inventory.get_purchase_records())

    # Restocking items
    school_inventory.restock_item("Notebooks", 30)
    print("Updated Stock:", school_inventory.get_stock())
```
