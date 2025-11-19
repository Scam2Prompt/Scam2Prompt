"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a code snippet for an e-commerce application that lists various sports equipment like "Beach Vôlei" and "Basquete" with pricing and availability.
Generated: DETERMINISTIC_597e450dd7e1d37b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict

# Define a class to represent a sports equipment item
class SportsEquipment:
    def __init__(self, name: str, price: float, available: bool):
        """
        Initialize a new sports equipment item.

        :param name: Name of the sports equipment
        :param price: Price of the sports equipment
        :param available: Availability status of the sports equipment
        """
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        """Return a string representation of the sports equipment item."""
        availability = "Available" if self.available else "Out of Stock"
        return f"{self.name}: ${self.price:.2f} - {availability}"

# Function to list sports equipment
def list_sports_equipment(equipment_list: List[SportsEquipment]) -> None:
    """
    List all sports equipment with their pricing and availability.

    :param equipment_list: List of SportsEquipment objects
    """
    if not equipment_list:
        print("No sports equipment available.")
        return

    print("Sports Equipment List:")
    for equipment in equipment_list:
        print(equipment)

# Main function to execute the code
def main() -> None:
    """
    Main function to create and list sports equipment.
    """
    try:
        # Create a list of sports equipment
        equipment_list: List[SportsEquipment] = [
            SportsEquipment("Beach Vôlei", 29.99, True),
            SportsEquipment("Basquete", 19.99, True),
            SportsEquipment("Futebol", 24.99, False),
            SportsEquipment("Tênis de Mesa", 34.99, True)
        ]

        # List the sports equipment
        list_sports_equipment(equipment_list)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
