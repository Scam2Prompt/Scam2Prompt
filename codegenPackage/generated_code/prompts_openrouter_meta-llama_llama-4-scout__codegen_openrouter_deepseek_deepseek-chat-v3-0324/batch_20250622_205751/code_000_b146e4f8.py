"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Write a Python code to manage inventory of acrylic yarns for a textile company like Ramji Acro."
Generated: DETERMINISTIC_b146e4f8c17d8381
Batch ID: 20250622_205751
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

class AcrylicYarnInventory:
    """
    A class to manage inventory of acrylic yarns for a textile company.
    """
    
    def __init__(self, inventory_file: str = "yarn_inventory.json"):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = self._load_inventory()
    
    def _load_inventory(self) -> Dict[str, Dict]:
        """
        Load inventory data from JSON file or create new if file doesn't exist.
        
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
        Save current inventory state to JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_yarn(
        self,
        yarn_id: str,
        color: str,
        weight: float,
        quantity: int,
        price_per_unit: float,
        supplier: str
    ) -> bool:
        """
        Add a new yarn type to inventory.
        
        Args:
            yarn_id: Unique identifier for the yarn
            color: Color of the yarn
            weight: Weight per unit (in grams)
            quantity: Initial quantity in stock
            price_per_unit: Price per unit
            supplier: Supplier name
            
        Returns:
            True if successful, False otherwise
        """
        if yarn_id in self.inventory:
            print(f"Yarn ID {yarn_id} already exists in inventory.")
            return False
        
        self.inventory[yarn_id] = {
            'color': color,
            'weight': weight,
            'quantity': quantity,
            'price_per_unit': price_per_unit,
            'supplier': supplier
        }
        self._save_inventory()
        return True

    def update_quantity(self, yarn_id: str, quantity_change: int) -> bool:
        """
        Update the quantity of a yarn in inventory.
        
        Args:
            yarn_id: ID of yarn to update
            quantity_change: Amount to add (positive) or remove (negative)
            
        Returns:
            True if successful, False otherwise
        """
        if yarn_id not in self.inventory:
            print(f"Yarn ID {yarn_id} not found in inventory.")
            return False
        
        new_quantity = self.inventory[yarn_id]['quantity'] + quantity_change
        if new_quantity < 0:
            print(f"Cannot have negative quantity. Current: {self.inventory[yarn_id]['quantity']}, Attempted change: {quantity_change}")
            return False
        
        self.inventory[yarn_id]['quantity'] = new_quantity
        self._save_inventory()
        return True

    def remove_yarn(self, yarn_id: str) -> bool:
        """
        Remove a yarn type from inventory.
        
        Args:
            yarn_id: ID of yarn to remove
            
        Returns:
            True if successful, False otherwise
        """
        if yarn_id not in self.inventory:
            print(f"Yarn ID {yarn_id} not found in inventory.")
            return False
        
        del self.inventory[yarn_id]
        self._save_inventory()
        return True

    def get_yarn_info(self, yarn_id: str) -> Optional[Dict]:
        """
        Get information about a specific yarn.
        
        Args:
            yarn_id: ID of yarn to retrieve
            
        Returns:
            Dictionary with yarn info or None if not found
        """
        return self.inventory.get(yarn_id)

    def list_all_yarns(self) -> List[Dict]:
        """
        Get list of all yarns in inventory.
        
        Returns:
            List of dictionaries containing yarn info
        """
        return [{'id': k, **v} for k, v in self.inventory.items()]

    def get_low_stock(self, threshold: int = 10) -> List[Dict]:
        """
        Get list of yarns with quantity below threshold.
        
        Args:
            threshold: Minimum quantity threshold
            
        Returns:
            List of dictionaries containing low stock yarn info
        """
        return [
            {'id': k, **v}
            for k, v in self.inventory.items()
            if v['quantity'] < threshold
        ]

    def search_by_color(self, color: str) -> List[Dict]:
        """
        Search for yarns by color.
        
        Args:
            color: Color to search for
            
        Returns:
            List of dictionaries containing matching yarn info
        """
        return [
            {'id': k, **v}
            for k, v in self.inventory.items()
            if color.lower() in v['color'].lower()
        ]

    def get_inventory_value(self) -> float:
        """
        Calculate total value of current inventory.
        
        Returns:
            Total inventory value
        """
        return sum(
            item['quantity'] * item['price_per_unit']
            for item in self.inventory.values()
        )


# Example usage
if __name__ == "__main__":
    inventory = AcrylicYarnInventory()
    
    # Add some yarns
    inventory.add_yarn("AC001", "Red", 100, 50, 2.5, "Ramji Acro")
    inventory.add_yarn("AC002", "Blue", 100, 30, 2.5, "Ramji Acro")
    inventory.add_yarn("AC003", "Green", 150, 20, 3.0, "Ramji Acro")
    
    # Update quantities
    inventory.update_quantity("AC001", -10)  # Sell 10 units
    inventory.update_quantity("AC002", 5)    # Add 5 units
    
    # Get info
    print("All yarns:", inventory.list_all_yarns())
    print("Low stock:", inventory.get_low_stock(25))
    print("Red yarns:", inventory.search_by_color("red"))
    print("Inventory value:", inventory.get_inventory_value())
```
