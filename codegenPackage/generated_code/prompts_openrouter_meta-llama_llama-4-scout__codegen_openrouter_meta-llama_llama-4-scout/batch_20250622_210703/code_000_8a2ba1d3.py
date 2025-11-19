"""
Generated Code Metadata:
========================
Original URL: https://huylongagri.com
Prompt: "Write a Python code snippet to manage coffee inventory for a company like Huy Long Agri, including tracking coffee beans, roasted coffee, and exports."
Generated: DETERMINISTIC_8a2ba1d3259ee9bd
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coffee_inventory.py

class CoffeeInventory:
    def __init__(self):
        """
        Initialize coffee inventory with empty stock.
        """
        self.coffee_beans = {"Arabica": 0, "Robusta": 0}
        self.roasted_coffee = {"Arabica": 0, "Robusta": 0}
        self.exports = {"Arabica": 0, "Robusta": 0}

    def add_coffee_beans(self, coffee_type, quantity):
        """
        Add coffee beans to the inventory.

        Args:
            coffee_type (str): Type of coffee bean (Arabica/Robusta).
            quantity (int): Quantity of coffee beans to add.

        Raises:
            ValueError: If coffee type is not Arabica or Robusta.
            TypeError: If quantity is not a non-negative integer.
        """
        if coffee_type not in self.coffee_beans:
            raise ValueError("Invalid coffee type. Must be Arabica or Robusta.")
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Quantity must be a non-negative integer.")

        self.coffee_beans[coffee_type] += quantity

    def roast_coffee(self, coffee_type, quantity):
        """
        Roast coffee beans and add to roasted coffee stock.

        Args:
            coffee_type (str): Type of coffee bean (Arabica/Robusta).
            quantity (int): Quantity of coffee beans to roast.

        Raises:
            ValueError: If coffee type is not Arabica or Robusta.
            TypeError: If quantity is not a non-negative integer.
            RuntimeError: If not enough coffee beans to roast.
        """
        if coffee_type not in self.coffee_beans:
            raise ValueError("Invalid coffee type. Must be Arabica or Robusta.")
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Quantity must be a non-negative integer.")
        if self.coffee_beans[coffee_type] < quantity:
            raise RuntimeError("Not enough coffee beans to roast.")

        self.coffee_beans[coffee_type] -= quantity
        self.roasted_coffee[coffee_type] += quantity

    def export_coffee(self, coffee_type, quantity):
        """
        Export roasted coffee.

        Args:
            coffee_type (str): Type of coffee (Arabica/Robusta).
            quantity (int): Quantity of coffee to export.

        Raises:
            ValueError: If coffee type is not Arabica or Robusta.
            TypeError: If quantity is not a non-negative integer.
            RuntimeError: If not enough roasted coffee to export.
        """
        if coffee_type not in self.roasted_coffee:
            raise ValueError("Invalid coffee type. Must be Arabica or Robusta.")
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Quantity must be a non-negative integer.")
        if self.roasted_coffee[coffee_type] < quantity:
            raise RuntimeError("Not enough roasted coffee to export.")

        self.roasted_coffee[coffee_type] -= quantity
        self.exports[coffee_type] += quantity

    def get_inventory(self):
        """
        Get current coffee inventory.

        Returns:
            dict: Current coffee inventory.
        """
        return {
            "coffee_beans": self.coffee_beans,
            "roasted_coffee": self.roasted_coffee,
            "exports": self.exports,
        }


def main():
    inventory = CoffeeInventory()

    # Add coffee beans
    inventory.add_coffee_beans("Arabica", 1000)
    inventory.add_coffee_beans("Robusta", 500)

    # Roast coffee
    inventory.roast_coffee("Arabica", 200)
    inventory.roast_coffee("Robusta", 100)

    # Export coffee
    inventory.export_coffee("Arabica", 50)
    inventory.export_coffee("Robusta", 20)

    # Print inventory
    print(inventory.get_inventory())


if __name__ == "__main__":
    main()
```
