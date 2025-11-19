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

class StudioEquipment:
    """Class to represent a piece of studio equipment."""
    
    def __init__(self, name, price):
        """
        Initialize the equipment with a name and price.

        Args:
            name (str): The name of the equipment.
            price (float): The price of the equipment.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the equipment."""
        return f"{self.name}: ${self.price:.2f}"


class HomeStudio:
    """Class to represent a home studio setup."""
    
    def __init__(self):
        """Initialize an empty list of equipment."""
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Add a piece of equipment to the studio.

        Args:
            equipment (StudioEquipment): The equipment to add.
        """
        if not isinstance(equipment, StudioEquipment):
            raise ValueError("Equipment must be an instance of StudioEquipment.")
        self.equipment_list.append(equipment)

    def total_cost(self):
        """Calculate the total cost of the studio equipment."""
        return sum(equipment.price for equipment in self.equipment_list)

    def display_equipment(self):
        """Display all equipment in the studio."""
        for equipment in self.equipment_list:
            print(equipment)


def main():
    """Main function to calculate the cost of building a home studio."""
    # Prices of equipment (in USD)
    equipment_prices = {
        "Cad E100s Microphone": 299.00,
        "SSL 2 Audio Interface": 199.00,
        # Add more equipment as needed
    }

    # Create a home studio instance
    home_studio = HomeStudio()

    # Add equipment to the studio
    for name, price in equipment_prices.items():
        try:
            equipment = StudioEquipment(name, price)
            home_studio.add_equipment(equipment)
        except ValueError as e:
            print(f"Error adding equipment: {e}")

    # Display the equipment and total cost
    print("Home Studio Equipment:")
    home_studio.display_equipment()
    print(f"\nTotal Cost: ${home_studio.total_cost():.2f}")

if __name__ == "__main__":
    main()
```
