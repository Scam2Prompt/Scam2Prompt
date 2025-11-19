"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to calculate the cost of building a home studio like Eric Navarro's, considering the prices of equipment such as the Cad E100s microphone and SSL 2 audio interface.
Generated: DETERMINISTIC_9dd6a6ec67d5654c
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
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class EquipmentItem:
    """Class to represent a single equipment item with its price."""
    name: str
    price: float
    quantity: int = 1

    def total_cost(self) -> float:
        """Calculate total cost for this item."""
        return self.price * self.quantity

class StudioCalculator:
    """Class to calculate the total cost of building a home studio."""
    
    def __init__(self):
        self.equipment: List[EquipmentItem] = []
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add an equipment item to the studio setup.
        
        Args:
            name: Name of the equipment
            price: Price per unit
            quantity: Number of units (default 1)
        """
        self.equipment.append(EquipmentItem(name, price, quantity))
    
    def remove_item(self, name: str) -> None:
        """Remove an equipment item by name.
        
        Args:
            name: Name of the equipment to remove
        """
        self.equipment = [item for item in self.equipment if item.name != name]
    
    def calculate_total(self) -> float:
        """Calculate the total cost of all equipment."""
        return sum(item.total_cost() for item in self.equipment)
    
    def get_equipment_list(self) -> List[Dict[str, float]]:
        """Get a list of all equipment with their individual costs.
        
        Returns:
            List of dictionaries with equipment details
        """
        return [
            {
                "name": item.name,
                "unit_price": item.price,
                "quantity": item.quantity,
                "total_cost": item.total_cost()
            }
            for item in self.equipment
        ]
    
    def save_to_file(self, filename: str) -> None:
        """Save the current equipment list to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_equipment_list(), f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load equipment list from a JSON file.
        
        Args:
            filename: Name of the file to load from
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.equipment = [
                    EquipmentItem(
                        name=item["name"],
                        price=item["unit_price"],
                        quantity=item["quantity"]
                    )
                    for item in data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading file: {e}")

def main():
    """Main function to demonstrate the studio calculator."""
    calculator = StudioCalculator()
    
    # Add Eric Navarro's studio equipment with approximate prices
    calculator.add_item("Cad E100s Microphone", 399.00)
    calculator.add_item("SSL 2 Audio Interface", 229.99)
    calculator.add_item("Studio Headphones", 99.99)
    calculator.add_item("MIDI Controller", 129.99)
    calculator.add_item("Studio Monitors", 299.99)
    calculator.add_item("XLR Cables", 19.99, 2)
    calculator.add_item("Mic Stand", 29.99)
    calculator.add_item("Pop Filter", 14.99)
    
    # Calculate and display total cost
    total_cost = calculator.calculate_total()
    print("Studio Equipment Breakdown:")
    for item in calculator.get_equipment_list():
        print(f"{item['name']} (x{item['quantity']}): ${item['total_cost']:.2f}")
    print(f"\nTotal Cost: ${total_cost:.2f}")
    
    # Save to file for future reference
    calculator.save_to_file("studio_equipment.json")

if __name__ == "__main__":
    main()
```
