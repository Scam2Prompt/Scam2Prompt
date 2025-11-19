"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Write a Python program to simulate a customer order for personalized reusable bags from Grupo ProBolsa, including fields for design preferences and quantity.
Generated: DETERMINISTIC_0e248219f5d271b4
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

class DesignPreferences:
    """Represents design preferences for a reusable bag."""

    def __init__(self, color, material, size, logo=None, text=None):
        """
        Initializes a DesignPreferences object.

        Args:
            color (str): The color of the bag.
            material (str): The material of the bag.
            size (str): The size of the bag.
            logo (str, optional): The logo to be printed on the bag. Defaults to None.
            text (str, optional): The text to be printed on the bag. Defaults to None.
        """
        self.color = color
        self.material = material
        self.size = size
        self.logo = logo
        self.text = text


class CustomerOrder:
    """Represents a customer order for personalized reusable bags."""

    def __init__(self, customer_name, design_preferences, quantity):
        """
        Initializes a CustomerOrder object.

        Args:
            customer_name (str): The name of the customer.
            design_preferences (DesignPreferences): The design preferences for the bags.
            quantity (int): The number of bags ordered.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.customer_name = customer_name
        self.design_preferences = design_preferences
        self.quantity = quantity

    def __str__(self):
        return f"Customer: {self.customer_name}\nDesign Preferences: {self.design_preferences.__dict__}\nQuantity: {self.quantity}"


class GrupoProBolsaOrderSystem:
    """Simulates the Grupo ProBolsa order system."""

    def __init__(self):
        self.orders = []

    def place_order(self, customer_order):
        """
        Places a customer order.

        Args:
            customer_order (CustomerOrder): The customer order to be placed.

        Raises:
            TypeError: If customer_order is not a CustomerOrder object.
        """
        if not isinstance(customer_order, CustomerOrder):
            raise TypeError("Invalid order type.")

        self.orders.append(customer_order)
        print("Order placed successfully!")
        print(customer_order)

    def view_orders(self):
        """Displays all placed orders."""
        if not self.orders:
            print("No orders placed.")
            return

        for i, order in enumerate(self.orders, start=1):
            print(f"Order {i}:")
            print(order)
            print("------------------------")


def main():
    try:
        # Get customer information
        customer_name = input("Enter customer name: ")

        # Get design preferences
        color = input("Enter bag color: ")
        material = input("Enter bag material: ")
        size = input("Enter bag size: ")
        logo = input("Enter logo (optional): ")
        text = input("Enter text (optional): ")

        design_preferences = DesignPreferences(color, material, size, logo or None, text or None)

        # Get quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")

        # Create customer order
        customer_order = CustomerOrder(customer_name, design_preferences, quantity)

        # Place order
        order_system = GrupoProBolsaOrderSystem()
        order_system.place_order(customer_order)

        # View orders
        order_system.view_orders()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
