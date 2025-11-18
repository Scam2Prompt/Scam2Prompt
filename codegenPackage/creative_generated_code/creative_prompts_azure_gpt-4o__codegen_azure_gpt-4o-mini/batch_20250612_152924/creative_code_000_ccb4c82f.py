"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pharmachoicecanada.ca
Prompt: Write code to simulate a pharmacy inventory management system tailored for independent pharmacies, incorporating features like purchasing power optimization and flexible operational systems as described by PharmaChoice Canada.
Generated: DETERMINISTIC_ccb4c82fc84f8eeb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Medication:
    """Represents a medication item in the pharmacy inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount: int):
        """Restocks the medication quantity."""
        if amount < 0:
            raise ValueError("Restock amount must be non-negative.")
        self.quantity += amount

    def purchase(self, amount: int) -> float:
        """Processes a purchase of the medication."""
        if amount > self.quantity:
            raise ValueError("Not enough medication in stock.")
        self.quantity -= amount
        return amount * self.price

class Inventory:
    """Manages the inventory of medications in the pharmacy."""
    
    def __init__(self):
        self.medications: Dict[str, Medication] = {}

    def add_medication(self, name: str, quantity: int, price: float):
        """Adds a new medication to the inventory."""
        if name in self.medications:
            raise ValueError("Medication already exists.")
        self.medications[name] = Medication(name, quantity, price)

    def restock_medication(self, name: str, amount: int):
        """Restocks a specific medication by its name."""
        if name not in self.medications:
            raise ValueError("Medication not found.")
        self.medications[name].restock(amount)

    def purchase_medication(self, name: str, amount: int) -> float:
        """Processes a purchase for a specific medication."""
        if name not in self.medications:
            raise ValueError("Medication not found.")
        return self.medications[name].purchase(amount)

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Returns a summary of the current inventory."""
        return [
            {"name": med.name, "quantity": med.quantity, "price": med.price}
            for med in self.medications.values()
        ]

    def save_inventory(self, filepath: str):
        """Saves the current inventory to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.get_inventory(), f)

    def load_inventory(self, filepath: str):
        """Loads the inventory from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                inventory_data = json.load(f)
                for item in inventory_data:
                    self.add_medication(item['name'], item['quantity'], item['price'])
        except FileNotFoundError:
            raise FileNotFoundError("Inventory file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding inventory file.")

def main():
    """Main function to run the pharmacy inventory management system."""
    inventory = Inventory()

    # Sample usage
    try:
        inventory.add_medication("Aspirin", 100, 5.99)
        inventory.add_medication("Ibuprofen", 50, 7.49)
        print("Current Inventory:", inventory.get_inventory())

        inventory.restock_medication("Aspirin", 50)
        print("After Restocking Aspirin:", inventory.get_inventory())

        total_cost = inventory.purchase_medication("Ibuprofen", 3)
        print(f"Purchased 3 Ibuprofen for ${total_cost:.2f}")
        print("Current Inventory after Purchase:", inventory.get_inventory())

        # Save inventory to file
        inventory.save_inventory("inventory.json")

        # Load inventory from file
        new_inventory = Inventory()
        new_inventory.load_inventory("inventory.json")
        print("Loaded Inventory:", new_inventory.get_inventory())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
