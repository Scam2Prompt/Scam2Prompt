"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Write code to simulate a pharmacy inventory management system tailored for independent pharmacies, incorporating features like purchasing power optimization and flexible operational systems as described by PharmaChoice Canada.
Generated: DETERMINISTIC_ccb4c82fc84f8eeb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Medication:
    """Class to represent a medication in the pharmacy inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.name} (Qty: {self.quantity}, Price: ${self.price:.2f})"

class PharmacyInventory:
    """Class to manage the pharmacy inventory."""
    
    def __init__(self):
        self.inventory: Dict[str, Medication] = {}

    def add_medication(self, name: str, quantity: int, price: float) -> None:
        """Add a new medication to the inventory."""
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = Medication(name, quantity, price)

    def remove_medication(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of medication from the inventory."""
        if name in self.inventory:
            if self.inventory[name].quantity >= quantity:
                self.inventory[name].quantity -= quantity
                if self.inventory[name].quantity == 0:
                    del self.inventory[name]
            else:
                raise ValueError("Not enough medication in inventory to remove.")
        else:
            raise KeyError("Medication not found in inventory.")

    def get_inventory(self) -> List[Medication]:
        """Return a list of all medications in the inventory."""
        return list(self.inventory.values())

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({name: med.__dict__ for name, med in self.inventory.items()}, file)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, med_data in data.items():
                    self.inventory[name] = Medication(**med_data)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

    def optimize_purchasing_power(self) -> List[Medication]:
        """Optimize purchasing power by suggesting medications based on quantity and price."""
        # This is a placeholder for a more complex purchasing power optimization algorithm.
        return sorted(self.inventory.values(), key=lambda med: (med.price / med.quantity))

def main():
    """Main function to run the pharmacy inventory management system."""
    inventory = PharmacyInventory()

    # Load existing inventory if available
    inventory.load_inventory('inventory.json')

    # Example operations
    try:
        inventory.add_medication("Aspirin", 100, 0.10)
        inventory.add_medication("Ibuprofen", 50, 0.15)
        inventory.remove_medication("Aspirin", 20)

        print("Current Inventory:")
        for med in inventory.get_inventory():
            print(med)

        print("\nOptimized Purchasing Power:")
        for med in inventory.optimize_purchasing_power():
            print(med)

        # Save the updated inventory
        inventory.save_inventory('inventory.json')

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
