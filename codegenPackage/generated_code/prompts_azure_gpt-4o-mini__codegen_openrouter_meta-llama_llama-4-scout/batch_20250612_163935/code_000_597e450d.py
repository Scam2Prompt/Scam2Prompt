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
# sports_equipment.py

class SportsEquipment:
    """Represents a sports equipment item."""

    def __init__(self, name, price, quantity):
        """
        Initializes a SportsEquipment object.

        Args:
            name (str): The name of the sports equipment.
            price (float): The price of the sports equipment.
            quantity (int): The available quantity of the sports equipment.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Returns a string representation of the sports equipment."""
        availability = "In stock" if self.quantity > 0 else "Out of stock"
        return f"{self.name}: R${self.price:.2f} - {availability}"


class SportsEquipmentStore:
    """Represents an e-commerce store for sports equipment."""

    def __init__(self):
        """Initializes a SportsEquipmentStore object."""
        self.equipment = []

    def add_equipment(self, equipment):
        """
        Adds a sports equipment item to the store.

        Args:
            equipment (SportsEquipment): The sports equipment item to add.
        """
        self.equipment.append(equipment)

    def list_equipment(self):
        """Lists all sports equipment items in the store."""
        if not self.equipment:
            print("No sports equipment available.")
            return

        print("Sports Equipment:")
        for i, equipment in enumerate(self.equipment, start=1):
            print(f"{i}. {equipment}")


def main():
    try:
        store = SportsEquipmentStore()

        # Add sports equipment items
        store.add_equipment(SportsEquipment("Beach Vôlei", 99.99, 10))
        store.add_equipment(SportsEquipment("Basquete", 149.99, 5))
        store.add_equipment(SportsEquipment("Futebol", 79.99, 0))

        # List sports equipment items
        store.list_equipment()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
