"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from the "Venta de Garage" section of the Ortopedic website, including discounts on items like "Silla de ruedas Premium Full Equipada" and "Jeringas desechables."
Generated: DETERMINISTIC_6e75c2c046d85dee
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# garage_sale_calculator.py

class GarageSaleItem:
    """Represents an item from the Venta de Garage section."""

    def __init__(self, name, price, discount=0):
        """
        Initializes a GarageSaleItem.

        Args:
            name (str): The item name.
            price (float): The item price.
            discount (float, optional): The discount percentage. Defaults to 0.
        """
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_price(self):
        """
        Calculates the price with discount.

        Returns:
            float: The price with discount applied.
        """
        return self.price * (1 - self.discount / 100)


class GarageSaleCalculator:
    """Calculates the total cost of purchasing multiple items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the calculator.

        Args:
            item (GarageSaleItem): The item to add.
        """
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total cost of all items.

        Returns:
            float: The total cost.
        """
        return sum(item.calculate_price() for item in self.items)


def main():
    try:
        calculator = GarageSaleCalculator()

        # Define items with discounts
        silla_de_ruedas = GarageSaleItem(
            "Silla de ruedas Premium Full Equipada", 1000, discount=20
        )
        jeringas_desechables = GarageSaleItem("Jeringas desechables", 50, discount=10)

        # Add items to the calculator
        calculator.add_item(silla_de_ruedas)
        calculator.add_item(jeringas_desechables)

        # Calculate and print the total cost
        total_cost = calculator.calculate_total()
        print(f"Total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
