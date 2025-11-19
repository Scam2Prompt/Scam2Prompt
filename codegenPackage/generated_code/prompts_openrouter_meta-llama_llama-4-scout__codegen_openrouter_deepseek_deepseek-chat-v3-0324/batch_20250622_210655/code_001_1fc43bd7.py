"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Write a Python code snippet to manage an inventory of customized pens, including tracking product codes, colors, and quantities, similar to the ones offered by Dom Brindes."
Generated: DETERMINISTIC_1fc43bd717a10095
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

class PenInventory:
    """
    A class to manage inventory of customized pens.
    Tracks product codes, colors, and quantities.
    """
    
    def __init__(self, inventory_file: str = "pen_inventory.json"):
        """
        Initialize the inventory with a JSON file for storage.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = self._load_inventory()
    
    def _load_inventory(self) -> Dict[str, Dict]:
        """
        Load inventory data from JSON file.
        Creates file if it doesn't exist.
        
        Returns:
            Dictionary containing inventory data.
        """
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            return {}
    
    def _save_inventory(self) -> None:
        """
        Save current inventory to JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")
    
    def add_pen(self, product_code: str, color: str, quantity: int) -> bool:
        """
        Add a new pen type or update existing pen quantity.
        
        Args:
            product_code: Unique identifier for the pen product.
            color: Color of the pen.
            quantity: Number of pens to add (positive) or remove (negative).
            
        Returns:
            True if operation succeeded, False otherwise.
        """
        if not product_code or not color:
            print("Product code and color cannot be empty.")
            return False
        
        if quantity == 0:
            print("Quantity must be non-zero.")
            return False
        
        if product_code in self.inventory:
            if self.inventory[product_code]['color'] != color:
                print(f"Color mismatch for product {product_code}.")
                return False
            new_quantity = self.inventory[product_code]['quantity'] + quantity
            if new_quantity < 0:
                print("Cannot have negative inventory.")
                return False
            self.inventory[product_code]['quantity'] = new_quantity
        else:
            if quantity <= 0:
                print("Cannot add new product with zero or negative quantity.")
                return False
            self.inventory[product_code] = {
                'color': color,
                'quantity': quantity
            }
        
        self._save_inventory()
        return True
    
    def remove_pen(self, product_code: str, quantity: int = 1) -> bool:
        """
        Remove pens from inventory.
        
        Args:
            product_code: Product to remove.
            quantity: Number to remove (default 1).
            
        Returns:
            True if operation succeeded, False otherwise.
        """
        return self.add_pen(product_code, '', -quantity)
    
    def get_inventory(self) -> Dict[str, Dict]:
        """
        Get current inventory snapshot.
        
        Returns:
            Dictionary of all products and their details.
        """
        return self.inventory.copy()
    
    def get_pen_details(self, product_code: str) -> Optional[Dict]:
        """
        Get details for a specific pen product.
        
        Args:
            product_code: Product to look up.
            
        Returns:
            Dictionary with product details if found, None otherwise.
        """
        return self.inventory.get(product_code)
    
    def search_by_color(self, color: str) -> List[Dict]:
        """
        Search for all pens matching a specific color.
        
        Args:
            color: Color to search for.
            
        Returns:
            List of matching products with their details.
        """
        return [
            {'product_code': code, **details} 
            for code, details in self.inventory.items() 
            if details['color'].lower() == color.lower()
        ]

# Example usage
if __name__ == "__main__":
    inventory = PenInventory()
    
    # Add some pens
    inventory.add_pen("PEN001", "Blue", 50)
    inventory.add_pen("PEN002", "Red", 30)
    inventory.add_pen("PEN003", "Black", 20)
    
    # Update quantities
    inventory.add_pen("PEN001", "Blue", 10)  # Add 10 more blue pens
    inventory.remove_pen("PEN002", 5)        # Remove 5 red pens
    
    # Get inventory
    print("Current inventory:")
    for code, details in inventory.get_inventory().items():
        print(f"{code}: {details['color']} - {details['quantity']} units")
    
    # Search by color
    print("\nRed pens:")
    for pen in inventory.search_by_color("Red"):
        print(f"{pen['product_code']}: {pen['quantity']} units")
```
