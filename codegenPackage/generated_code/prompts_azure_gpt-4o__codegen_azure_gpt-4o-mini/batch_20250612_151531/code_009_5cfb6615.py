"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: Write a script to simulate customer interactions for placing orders of thermal paper rolls, including customization options and bulk pricing, inspired by Apos Chile's offerings.
Generated: DETERMINISTIC_5cfb6615a1cd6365
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ThermalPaperRoll:
    """Class to represent a thermal paper roll with customization options."""
    
    def __init__(self, width: float, length: float, color: str, price_per_roll: float):
        """
        Initialize a ThermalPaperRoll instance.

        :param width: Width of the paper roll in mm.
        :param length: Length of the paper roll in meters.
        :param color: Color of the thermal paper.
        :param price_per_roll: Price of a single roll.
        """
        self.width = width
        self.length = length
        self.color = color
        self.price_per_roll = price_per_roll

    def get_price(self, quantity: int) -> float:
        """
        Calculate the total price for a given quantity of rolls.

        :param quantity: Number of rolls to purchase.
        :return: Total price after applying bulk pricing.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        # Apply bulk pricing
        if quantity >= 100:
            discount = 0.2  # 20% discount for bulk orders
        elif quantity >= 50:
            discount = 0.1  # 10% discount for orders of 50 or more
        else:
            discount = 0.0
        
        total_price = quantity * self.price_per_roll * (1 - discount)
        return total_price


class Order:
    """Class to represent a customer order for thermal paper rolls."""
    
    def __init__(self, customer_name: str):
        """
        Initialize an Order instance.

        :param customer_name: Name of the customer placing the order.
        """
        self.customer_name = customer_name
        self.items = []

    def add_item(self, roll: ThermalPaperRoll, quantity: int):
        """
        Add a thermal paper roll to the order.

        :param roll: The ThermalPaperRoll object to add.
        :param quantity: Number of rolls to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.items.append((roll, quantity))

    def calculate_total(self) -> float:
        """
        Calculate the total price of the order.

        :return: Total price of the order.
        """
        total = 0.0
        for roll, quantity in self.items:
            total += roll.get_price(quantity)
        return total

    def generate_invoice(self) -> dict:
        """
        Generate an invoice for the order.

        :return: A dictionary representing the invoice.
        """
        invoice = {
            "customer_name": self.customer_name,
            "items": [],
            "total": self.calculate_total()
        }
        for roll, quantity in self.items:
            invoice["items"].append({
                "width": roll.width,
                "length": roll.length,
                "color": roll.color,
                "quantity": quantity,
                "price_per_roll": roll.price_per_roll,
                "total_price": roll.get_price(quantity)
            })
        return invoice


def main():
    """Main function to simulate customer interactions."""
    try:
        # Create a new order for a customer
        customer_name = input("Enter customer name: ")
        order = Order(customer_name)

        # Simulate adding items to the order
        while True:
            width = float(input("Enter roll width (mm): "))
            length = float(input("Enter roll length (m): "))
            color = input("Enter roll color: ")
            price_per_roll = float(input("Enter price per roll: "))
            quantity = int(input("Enter quantity: "))

            # Create a thermal paper roll and add it to the order
            roll = ThermalPaperRoll(width, length, color, price_per_roll)
            order.add_item(roll, quantity)

            more_items = input("Add more items? (yes/no): ").strip().lower()
            if more_items != 'yes':
                break

        # Generate and print the invoice
        invoice = order.generate_invoice()
        print(json.dumps(invoice, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
