"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: "Write a Python script to manage inventory of plastic products, such as Tấm nhựa Ecoplast, Giường Nhựa Ecoplast, and Tủ Quần Áo Ecoplast."
Generated: DETERMINISTIC_eda2445c61361f66
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class InventoryManager:
    """A class to manage inventory of plastic products."""
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the InventoryManager with a JSON file for storage.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict[str, int]] = self._load_inventory()
        
    def _load_inventory(self) -> Dict[str, Dict[str, int]]:
        """
        Load inventory data from JSON file.
        
        Returns:
            Dictionary containing inventory data.
            
        Raises:
            FileNotFoundError: If the inventory file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as file:
                    return json.load(file)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in inventory file: {e}", e.doc, e.pos)
            
    def _save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)
            
    def add_product(self, product_name: str, initial_stock: int = 0) -> None:
        """
        Add a new product to inventory.
        
        Args:
            product_name: Name of the product to add.
            initial_stock: Initial stock quantity (default 0).
            
        Raises:
            ValueError: If product already exists or stock is negative.
        """
        if product_name in self.inventory:
            raise ValueError(f"Product '{product_name}' already exists in inventory.")
        if initial_stock < 0:
            raise ValueError("Stock quantity cannot be negative.")
            
        self.inventory[product_name] = {"stock": initial_stock}
        self._save_inventory()
        
    def update_stock(self, product_name: str, quantity: int) -> None:
        """
        Update stock quantity for a product.
        
        Args:
            product_name: Name of the product to update.
            quantity: Amount to add (positive) or remove (negative).
            
        Raises:
            ValueError: If product doesn't exist or resulting stock would be negative.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
            
        new_stock = self.inventory[product_name]["stock"] + quantity
        if new_stock < 0:
            raise ValueError("Insufficient stock for this operation.")
            
        self.inventory[product_name]["stock"] = new_stock
        self._save_inventory()
        
    def get_stock(self, product_name: str) -> int:
        """
        Get current stock for a product.
        
        Args:
            product_name: Name of the product to check.
            
        Returns:
            Current stock quantity.
            
        Raises:
            ValueError: If product doesn't exist.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
            
        return self.inventory[product_name]["stock"]
        
    def list_products(self) -> List[str]:
        """
        List all products in inventory.
        
        Returns:
            List of product names.
        """
        return list(self.inventory.keys())
        
    def remove_product(self, product_name: str) -> None:
        """
        Remove a product from inventory.
        
        Args:
            product_name: Name of the product to remove.
            
        Raises:
            ValueError: If product doesn't exist.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
            
        del self.inventory[product_name]
        self._save_inventory()


def main():
    """Command-line interface for inventory management."""
    manager = InventoryManager()
    
    while True:
        print("\nPlastic Product Inventory Management")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Check Stock")
        print("4. List Products")
        print("5. Remove Product")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        try:
            if choice == "1":
                product = input("Enter product name: ")
                stock = int(input("Enter initial stock quantity: "))
                manager.add_product(product, stock)
                print(f"Product '{product}' added with stock {stock}.")
                
            elif choice == "2":
                product = input("Enter product name: ")
                quantity = int(input("Enter quantity to add/remove (use - for removal): "))
                manager.update_stock(product, quantity)
                print(f"Stock updated for '{product}'. New stock: {manager.get_stock(product)}")
                
            elif choice == "3":
                product = input("Enter product name: ")
                stock = manager.get_stock(product)
                print(f"Current stock for '{product}': {stock}")
                
            elif choice == "4":
                products = manager.list_products()
                print("\nProducts in inventory:")
                for product in products:
                    print(f"- {product}: {manager.get_stock(product)} in stock")
                    
            elif choice == "5":
                product = input("Enter product name to remove: ")
                manager.remove_product(product)
                print(f"Product '{product}' removed from inventory.")
                
            elif choice == "6":
                print("Exiting inventory management system.")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
