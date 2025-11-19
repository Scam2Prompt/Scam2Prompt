"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write a program to manage inventory and fiscalized goods using SIAF (Sistema Integrado de Administración Financiera), as taught in the "Gestión de Tesorería con el SIAF" course on AulaContable.
Generated: DETERMINISTIC_1782893db3e2aa0c
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm ready to provide the code. However, I need to clarify that I'll be using Python as the programming language. Please let me know if there's a specific language you'd like me to use.

```python
# inventory_management.py

class FiscalizedGood:
    """Represents a fiscalized good in the SIAF system."""

    def __init__(self, code, description, quantity, value):
        """
        Initializes a FiscalizedGood object.

        Args:
            code (str): Unique code for the good.
            description (str): Description of the good.
            quantity (int): Quantity of the good in stock.
            value (float): Value of the good.
        """
        self.code = code
        self.description = description
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"{self.code} - {self.description} ({self.quantity} units @ {self.value:.2f} each)"


class Inventory:
    """Manages inventory and fiscalized goods using SIAF."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.goods = {}

    def add_good(self, code, description, quantity, value):
        """
        Adds a fiscalized good to the inventory.

        Args:
            code (str): Unique code for the good.
            description (str): Description of the good.
            quantity (int): Quantity of the good in stock.
            value (float): Value of the good.

        Raises:
            ValueError: If the code already exists in the inventory.
        """
        if code in self.goods:
            raise ValueError(f"Good with code {code} already exists in the inventory.")
        self.goods[code] = FiscalizedGood(code, description, quantity, value)

    def remove_good(self, code):
        """
        Removes a fiscalized good from the inventory.

        Args:
            code (str): Unique code for the good.

        Raises:
            ValueError: If the code does not exist in the inventory.
        """
        if code not in self.goods:
            raise ValueError(f"Good with code {code} does not exist in the inventory.")
        del self.goods[code]

    def update_quantity(self, code, new_quantity):
        """
        Updates the quantity of a fiscalized good in the inventory.

        Args:
            code (str): Unique code for the good.
            new_quantity (int): New quantity of the good in stock.

        Raises:
            ValueError: If the code does not exist in the inventory.
        """
        if code not in self.goods:
            raise ValueError(f"Good with code {code} does not exist in the inventory.")
        self.goods[code].quantity = new_quantity

    def get_good(self, code):
        """
        Retrieves a fiscalized good from the inventory.

        Args:
            code (str): Unique code for the good.

        Returns:
            FiscalizedGood: The fiscalized good object.

        Raises:
            ValueError: If the code does not exist in the inventory.
        """
        if code not in self.goods:
            raise ValueError(f"Good with code {code} does not exist in the inventory.")
        return self.goods[code]

    def list_goods(self):
        """Returns a list of all fiscalized goods in the inventory."""
        return list(self.goods.values())


def main():
    # Create an instance of the Inventory class
    inventory = Inventory()

    while True:
        print("\nInventory Management Menu:")
        print("1. Add fiscalized good")
        print("2. Remove fiscalized good")
        print("3. Update quantity")
        print("4. Get fiscalized good")
        print("5. List all fiscalized goods")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                code = input("Enter good code: ")
                description = input("Enter good description: ")
                quantity = int(input("Enter quantity: "))
                value = float(input("Enter value: "))
                inventory.add_good(code, description, quantity, value)
            elif choice == "2":
                code = input("Enter good code: ")
                inventory.remove_good(code)
            elif choice == "3":
                code = input("Enter good code: ")
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(code, new_quantity)
            elif choice == "4":
                code = input("Enter good code: ")
                good = inventory.get_good(code)
                print(good)
            elif choice == "5":
                goods = inventory.list_goods()
                for good in goods:
                    print(good)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
