"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Write a Python script to track and manage inventory of Elisa Kits, such as AFP, AMH, and ANA, with their respective ratings and prices.
Generated: DETERMINISTIC_eb5888fd9f66adc6
Batch ID: 20250622_210650
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

class ElisaKitInventory:
    """
    A class to manage inventory of Elisa Kits with their ratings and prices.
    """
    
    def __init__(self, inventory_file: str = "elisa_inventory.json"):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = self._load_inventory()
    
    def _load_inventory(self) -> Dict[str, Dict]:
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
                with open(self.inventory_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in inventory file: {e}", e.doc, e.pos)
    
    def _save_inventory(self) -> None:
        """
        Save inventory data to JSON file.
        
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory: {e}")
    
    def add_kit(self, kit_name: str, quantity: int, price: float, rating: float) -> None:
        """
        Add a new Elisa kit to inventory or update existing one.
        
        Args:
            kit_name: Name of the kit (e.g., "AFP", "AMH", "ANA").
            quantity: Number of units in stock.
            price: Price per unit.
            rating: Quality rating (0-5).
            
        Raises:
            ValueError: If quantity, price or rating are invalid.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price <= 0:
            raise ValueError("Price must be positive")
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
            
        self.inventory[kit_name] = {
            'quantity': quantity,
            'price': price,
            'rating': rating
        }
        self._save_inventory()
    
    def remove_kit(self, kit_name: str) -> None:
        """
        Remove a kit from inventory.
        
        Args:
            kit_name: Name of the kit to remove.
            
        Raises:
            KeyError: If kit doesn't exist in inventory.
        """
        if kit_name not in self.inventory:
            raise KeyError(f"Kit '{kit_name}' not found in inventory")
            
        del self.inventory[kit_name]
        self._save_inventory()
    
    def update_quantity(self, kit_name: str, delta: int) -> None:
        """
        Update the quantity of a kit in inventory.
        
        Args:
            kit_name: Name of the kit to update.
            delta: Change in quantity (positive to add, negative to remove).
            
        Raises:
            KeyError: If kit doesn't exist in inventory.
            ValueError: If resulting quantity would be negative.
        """
        if kit_name not in self.inventory:
            raise KeyError(f"Kit '{kit_name}' not found in inventory")
            
        new_quantity = self.inventory[kit_name]['quantity'] + delta
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
            
        self.inventory[kit_name]['quantity'] = new_quantity
        self._save_inventory()
    
    def get_kit_info(self, kit_name: str) -> Optional[Dict]:
        """
        Get information about a specific kit.
        
        Args:
            kit_name: Name of the kit to retrieve.
            
        Returns:
            Dictionary with kit info or None if not found.
        """
        return self.inventory.get(kit_name)
    
    def list_kits(self) -> List[Dict]:
        """
        Get a list of all kits in inventory.
        
        Returns:
            List of dictionaries containing kit information.
        """
        return [
            {'name': name, **info} 
            for name, info in self.inventory.items()
        ]
    
    def search_kits(self, min_rating: float = 0, max_price: float = float('inf')) -> List[Dict]:
        """
        Search kits by rating and price.
        
        Args:
            min_rating: Minimum rating to include (default 0).
            max_price: Maximum price to include (default no limit).
            
        Returns:
            List of matching kits with their info.
        """
        return [
            {'name': name, **info}
            for name, info in self.inventory.items()
            if info['rating'] >= min_rating and info['price'] <= max_price
        ]


# Example usage
if __name__ == "__main__":
    try:
        inventory = ElisaKitInventory()
        
        # Add some kits
        inventory.add_kit("AFP", 50, 125.99, 4.2)
        inventory.add_kit("AMH", 30, 89.50, 4.5)
        inventory.add_kit("ANA", 20, 110.00, 3.8)
        
        # Update quantity
        inventory.update_quantity("AFP", -10)  # Remove 10 units
        
        # List all kits
        print("Current inventory:")
        for kit in inventory.list_kits():
            print(f"{kit['name']}: {kit['quantity']} units, ${kit['price']:.2f}, rating {kit['rating']}")
        
        # Search for kits
        print("\nKits with rating >= 4.0 and price <= $100:")
        for kit in inventory.search_kits(min_rating=4.0, max_price=100):
            print(f"{kit['name']}: {kit['quantity']} units, ${kit['price']:.2f}, rating {kit['rating']}")
            
    except Exception as e:
        print(f"Error: {e}")
```
