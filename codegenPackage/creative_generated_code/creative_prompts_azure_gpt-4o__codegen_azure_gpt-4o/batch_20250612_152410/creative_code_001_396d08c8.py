"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Recommend an API or library to manage inventory for products like "Karma Dolap 8'li Soyunma Dolabı" and "Karma 3MT 25 Çekmeceli Çalışma Tezgahı," including features for tracking stock levels and generating purchase orders.
Generated: DETERMINISTIC_396d08c814934446
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

import json
import logging
from typing import List, Dict

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class InventoryManager:
    """
    A simple inventory management system to track stock levels and generate purchase orders.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_id: str, product_name: str, initial_stock: int = 0):
        """
        Adds a new product to the inventory.

        :param product_id: Unique identifier of the product.
        :param product_name: Name of the product.
        :param initial_stock: Initial stock level of the product.
        """
        if product_id in self.inventory:
            logging.error(f"Product ID '{product_id}' already exists.")
            raise ValueError("Product ID already exists.")
        
        self.inventory[product_id] = {
            "name": product_name,
            "stock": initial_stock
        }
        logging.info(f"Added product '{product_name}' with ID '{product_id}' to inventory.")

    def update_stock(self, product_id: str, quantity: int):
        """
        Updates the stock level for a specific product.

        :param product_id: Unique identifier of the product.
        :param quantity: Quantity to add or subtract from the current stock.
                         Positive for addition, negative for subtraction.
        """
        if product_id not in self.inventory:
            logging.error(f"Product ID '{product_id}' not found.")
            raise ValueError("Product ID not found.")
        
        self.inventory[product_id]["stock"] += quantity
        logging.info(f"Updated stock for product ID '{product_id}'. Current stock: {self.inventory[product_id]['stock']}")

    def check_stock(self, product_id: str) -> int:
        """
        Checks the stock level of a specific product.

        :param product_id: Unique identifier of the product.
        :return: Current stock level of the product.
        """
        if product_id not in self.inventory:
            logging.error(f"Product ID '{product_id}' not found.")
            raise ValueError("Product ID not found.")
        
        return self.inventory[product_id]["stock"]

    def generate_purchase_order(self, minimum_stock: int) -> List[Dict[str, str]]:
        """
        Generates a purchase order for products with stock levels below the minimum threshold.

        :param minimum_stock: Minimum stock level to consider for generating purchase orders.
        :return: List of products to restock.
        """
        purchase_order = []
        for product_id, details in self.inventory.items():
            if details["stock"] < minimum_stock:
                purchase_order.append({
                    "product_id": product_id,
                    "product_name": details["name"],
                    "current_stock": details["stock"],
                    "minimum_stock": minimum_stock
                })
        
        if purchase_order:
            logging.info("Generated purchase order for low-stock items.")
        else:
            logging.info("No products need restocking.")
        
        return purchase_order

    def save_inventory_to_file(self, filename: str):
        """
        Saves the current inventory state to a JSON file.

        :param filename: Name of the file to save the inventory.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.inventory, file, indent=4)
            logging.info(f"Inventory saved to file '{filename}'.")
        except Exception as e:
            logging.error(f"Failed to save inventory to file '{filename}': {e}")
            raise

    def load_inventory_from_file(self, filename: str):
        """
        Loads inventory data from a JSON file.

        :param filename: Name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            logging.info(f"Inventory loaded from file '{filename}'.")
        except Exception as e:
            logging.error(f"Failed to load inventory from file '{filename}': {e}")
            raise

# Example usage (can be removed for production deployments)
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add products
    manager.add_product("KD08", "Karma Dolap 8'li Soyunma Dolabı", initial_stock=10)
    manager.add_product("K3MT", "Karma 3MT 25 Çekmeceli Çalışma Tezgahı", initial_stock=5)

    # Update stock levels
    manager.update_stock("KD08", -3)
    manager.update_stock("K3MT", 2)

    # Check stock levels
    print(f"Stock for KD08: {manager.check_stock('KD08')}")
    print(f"Stock for K3MT: {manager.check_stock('K3MT')}")

    # Generate purchase order
    purchase_order = manager.generate_purchase_order(minimum_stock=6)
    print("Purchase Order:", purchase_order)

    # Save and load inventory
    manager.save_inventory_to_file("inventory.json")
    manager.load_inventory_from_file("inventory.json")
```

This code provides a basic inventory management system, including features for adding products, updating stock levels, checking stock, generating purchase orders, and saving/loading inventory to/from a file.
