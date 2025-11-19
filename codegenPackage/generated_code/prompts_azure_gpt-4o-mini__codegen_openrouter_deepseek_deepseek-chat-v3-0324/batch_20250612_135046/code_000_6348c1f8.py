"""
Generated Code Metadata:
========================
Original URL: https://metmask.com
Prompt: Generate a Python script to manage and store fishing bait, including options for natural baits like bloodworm and casters, as mentioned on metmask.com.
Generated: DETERMINISTIC_6348c1f8d64e3c2e
Batch ID: 20250612_135046
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

class BaitManager:
    """A class to manage and store fishing bait inventory."""
    
    def __init__(self, storage_file: str = "bait_inventory.json"):
        """Initialize the BaitManager with a storage file.
        
        Args:
            storage_file: Path to the JSON file storing bait data.
        """
        self.storage_file = storage_file
        self.inventory: Dict[str, Dict[str, int]] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load bait inventory from the storage file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as file:
                    self.inventory = json.load(file)
            else:
                self.inventory = {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            self.inventory = {}
    
    def _save_inventory(self) -> None:
        """Save bait inventory to the storage file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")
    
    def add_bait(self, bait_type: str, bait_name: str, quantity: int) -> None:
        """Add bait to the inventory.
        
        Args:
            bait_type: Type of bait (e.g., 'natural', 'artificial').
            bait_name: Name of the bait (e.g., 'bloodworm', 'casters').
            quantity: Quantity to add.
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        
        if bait_type not in self.inventory:
            self.inventory[bait_type] = {}
        
        if bait_name in self.inventory[bait_type]:
            self.inventory[bait_type][bait_name] += quantity
        else:
            self.inventory[bait_type][bait_name] = quantity
        
        self._save_inventory()
    
    def remove_bait(self, bait_type: str, bait_name: str, quantity: int) -> None:
        """Remove bait from the inventory.
        
        Args:
            bait_type: Type of bait.
            bait_name: Name of the bait.
            quantity: Quantity to remove.
        """
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        
        if (bait_type in self.inventory and 
            bait_name in self.inventory[bait_type]):
            if self.inventory[bait_type][bait_name] >= quantity:
                self.inventory[bait_type][bait_name] -= quantity
                if self.inventory[bait_type][bait_name] == 0:
                    del self.inventory[bait_type][bait_name]
                    if not self.inventory[bait_type]:
                        del self.inventory[bait_type]
                self._save_inventory()
            else:
                print(f"Not enough {bait_name} in inventory.")
        else:
            print(f"{bait_name} not found in {bait_type} inventory.")
    
    def get_bait_quantity(self, bait_type: str, bait_name: str) -> int:
        """Get the quantity of a specific bait.
        
        Args:
            bait_type: Type of bait.
            bait_name: Name of the bait.
            
        Returns:
            Quantity of the bait, or 0 if not found.
        """
        return self.inventory.get(bait_type, {}).get(bait_name, 0)
    
    def list_bait_types(self) -> List[str]:
        """List all bait types in inventory.
        
        Returns:
            List of bait types.
        """
        return list(self.inventory.keys())
    
    def list_bait_by_type(self, bait_type: str) -> Dict[str, int]:
        """List all baits of a specific type.
        
        Args:
            bait_type: Type of bait.
            
        Returns:
            Dictionary of bait names and quantities.
        """
        return self.inventory.get(bait_type, {})
    
    def print_inventory(self) -> None:
        """Print the entire inventory."""
        for bait_type, baits in self.inventory.items():
            print(f"\n{bait_type.upper()}:")
            for bait_name, quantity in baits.items():
                print(f"  {bait_name}: {quantity}")

def main():
    """Example usage of the BaitManager."""
    manager = BaitManager()
    
    while True:
        print("\nFishing Bait Management System")
        print("1. Add Bait")
        print("2. Remove Bait")
        print("3. Check Bait Quantity")
        print("4. List All Bait Types")
        print("5. List Baits by Type")
        print("6. Print Full Inventory")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            bait_type = input("Enter bait type (e.g., natural, artificial): ").strip().lower()
            bait_name = input("Enter bait name (e.g., bloodworm, casters): ").strip().lower()
            try:
                quantity = int(input("Enter quantity to add: "))
                manager.add_bait(bait_type, bait_name, quantity)
                print(f"Added {quantity} of {bait_name} to {bait_type} inventory.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == "2":
            bait_type = input("Enter bait type: ").strip().lower()
            bait_name = input("Enter bait name: ").strip().lower()
            try:
                quantity = int(input("Enter quantity to remove: "))
                manager.remove_bait(bait_type, bait_name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == "3":
            bait_type = input("Enter bait type: ").strip().lower()
            bait_name = input("Enter bait name: ").strip().lower()
            quantity = manager.get_bait_quantity(bait_type, bait_name)
            print(f"Quantity of {bait_name} in {bait_type}: {quantity}")
        
        elif choice == "4":
            bait_types = manager.list_bait_types()
            print("\nBait Types:")
            for bt in bait_types:
                print(f"  - {bt}")
        
        elif choice == "5":
            bait_type = input("Enter bait type: ").strip().lower()
            baits = manager.list_bait_by_type(bait_type)
            if baits:
                print(f"\n{bait_type.upper()}:")
                for name, qty in baits.items():
                    print(f"  {name}: {qty}")
            else:
                print(f"No baits found for type: {bait_type}")
        
        elif choice == "6":
            manager.print_inventory()
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
