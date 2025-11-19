"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Generate a Python script to simulate an ice cream truck inventory management system for a snow cone truck.
Generated: DETERMINISTIC_d5396b59319004f0
Batch ID: 20250612_162050
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

class SnowConeInventory:
    """
    A class to manage inventory for a snow cone truck.
    Handles adding, removing, and tracking stock of snow cone flavors and supplies.
    """
    
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the inventory system.
        
        Args:
            inventory_file: Path to JSON file storing inventory data
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict[str, int]] = {
            "flavors": {},
            "supplies": {}
        }
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory data from JSON file or create new file if it doesn't exist."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    self.inventory = json.load(f)
            else:
                self._save_inventory()
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            self._save_inventory()  # Create fresh inventory if file is corrupted
    
    def _save_inventory(self) -> None:
        """Save current inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")
    
    def add_flavor(self, name: str, quantity: int) -> None:
        """
        Add a snow cone flavor to inventory.
        
        Args:
            name: Name of the flavor
            quantity: Initial quantity to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        self.inventory["flavors"][name] = self.inventory["flavors"].get(name, 0) + quantity
        self._save_inventory()
    
    def remove_flavor(self, name: str, quantity: int) -> None:
        """
        Remove a snow cone flavor from inventory.
        
        Args:
            name: Name of the flavor
            quantity: Quantity to remove
            
        Raises:
            ValueError: If flavor doesn't exist or insufficient quantity
        """
        if name not in self.inventory["flavors"]:
            raise ValueError(f"Flavor '{name}' not in inventory")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if self.inventory["flavors"][name] < quantity:
            raise ValueError(f"Insufficient quantity of '{name}'")
            
        self.inventory["flavors"][name] -= quantity
        if self.inventory["flavors"][name] == 0:
            del self.inventory["flavors"][name]
        self._save_inventory()
    
    def add_supply(self, name: str, quantity: int) -> None:
        """
        Add a supply item to inventory.
        
        Args:
            name: Name of the supply (e.g., 'cones', 'napkins')
            quantity: Initial quantity to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        self.inventory["supplies"][name] = self.inventory["supplies"].get(name, 0) + quantity
        self._save_inventory()
    
    def remove_supply(self, name: str, quantity: int) -> None:
        """
        Remove a supply item from inventory.
        
        Args:
            name: Name of the supply
            quantity: Quantity to remove
            
        Raises:
            ValueError: If supply doesn't exist or insufficient quantity
        """
        if name not in self.inventory["supplies"]:
            raise ValueError(f"Supply '{name}' not in inventory")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if self.inventory["supplies"][name] < quantity:
            raise ValueError(f"Insufficient quantity of '{name}'")
            
        self.inventory["supplies"][name] -= quantity
        if self.inventory["supplies"][name] == 0:
            del self.inventory["supplies"][name]
        self._save_inventory()
    
    def get_flavor_quantity(self, name: str) -> int:
        """
        Get current quantity of a flavor.
        
        Args:
            name: Name of the flavor
            
        Returns:
            Current quantity (0 if not in inventory)
        """
        return self.inventory["flavors"].get(name, 0)
    
    def get_supply_quantity(self, name: str) -> int:
        """
        Get current quantity of a supply.
        
        Args:
            name: Name of the supply
            
        Returns:
            Current quantity (0 if not in inventory)
        """
        return self.inventory["supplies"].get(name, 0)
    
    def list_flavors(self) -> List[str]:
        """Return list of all available flavors."""
        return list(self.inventory["flavors"].keys())
    
    def list_supplies(self) -> List[str]:
        """Return list of all available supplies."""
        return list(self.inventory["supplies"].keys())
    
    def make_snow_cone(self, flavor: str, supplies_used: Dict[str, int]) -> bool:
        """
        Record the making of a snow cone by deducting from inventory.
        
        Args:
            flavor: Flavor used
            supplies_used: Dictionary of supplies and quantities used
            
        Returns:
            True if successful, False if insufficient inventory
            
        Raises:
            ValueError: If flavor doesn't exist
        """
        if flavor not in self.inventory["flavors"]:
            raise ValueError(f"Flavor '{flavor}' not in inventory")
        
        # Check if we have enough of everything
        if self.inventory["flavors"][flavor] < 1:
            return False
            
        for supply, quantity in supplies_used.items():
            if self.get_supply_quantity(supply) < quantity:
                return False
        
        # Deduct from inventory
        try:
            self.remove_flavor(flavor, 1)
            for supply, quantity in supplies_used.items():
                self.remove_supply(supply, quantity)
            return True
        except ValueError:
            return False


def main():
    """Example usage of the SnowConeInventory class."""
    inventory = SnowConeInventory()
    
    # Add some initial inventory
    inventory.add_flavor("Cherry", 50)
    inventory.add_flavor("Blue Raspberry", 50)
    inventory.add_flavor("Lemon", 30)
    
    inventory.add_supply("cones", 100)
    inventory.add_supply("napkins", 200)
    inventory.add_supply("spoons", 150)
    
    # Make some snow cones
    supplies_per_cone = {"cones": 1, "napkins": 2}
    if inventory.make_snow_cone("Cherry", supplies_per_cone):
        print("Made a cherry snow cone!")
    else:
        print("Failed to make cherry snow cone - insufficient inventory")
    
    # Display current inventory
    print("\nCurrent Inventory:")
    print("Flavors:")
    for flavor in inventory.list_flavors():
        print(f"  {flavor}: {inventory.get_flavor_quantity(flavor)}")
    
    print("\nSupplies:")
    for supply in inventory.list_supplies():
        print(f"  {supply}: {inventory.get_supply_quantity(supply)}")


if __name__ == "__main__":
    main()
```
