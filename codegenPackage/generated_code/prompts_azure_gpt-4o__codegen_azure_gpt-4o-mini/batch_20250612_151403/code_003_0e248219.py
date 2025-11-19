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
class Order:
    """
    A class to represent a customer order for personalized reusable bags.
    """

    def __init__(self, customer_name, design_preferences, quantity):
        """
        Initializes a new order with customer details.

        :param customer_name: str - Name of the customer placing the order
        :param design_preferences: str - Design preferences for the bags
        :param quantity: int - Number of bags ordered
        """
        self.customer_name = customer_name
        self.design_preferences = design_preferences
        self.quantity = quantity

    def validate_order(self):
        """
        Validates the order details.

        :raises ValueError: If quantity is not a positive integer
        :raises ValueError: If customer name or design preferences are empty
        """
        if not self.customer_name or not self.design_preferences:
            raise ValueError("Customer name and design preferences cannot be empty.")
        if not isinstance(self.quantity, int) or self.quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

    def calculate_total_price(self, price_per_bag):
        """
        Calculates the total price of the order.

        :param price_per_bag: float - Price of a single reusable bag
        :return: float - Total price for the order
        """
        return self.quantity * price_per_bag

    def __str__(self):
        """
        Returns a string representation of the order details.
        """
        return (f"Order for {self.customer_name}:\n"
                f"Design Preferences: {self.design_preferences}\n"
                f"Quantity: {self.quantity}")


def main():
    """
    Main function to simulate the order process.
    """
    try:
        # Sample input for the order
        customer_name = input("Enter your name: ")
        design_preferences = input("Enter design preferences: ")
        quantity = int(input("Enter quantity of bags: "))

        # Create an order instance
        order = Order(customer_name, design_preferences, quantity)

        # Validate the order
        order.validate_order()

        # Define price per bag
        price_per_bag = 10.0  # Example price

        # Calculate total price
        total_price = order.calculate_total_price(price_per_bag)

        # Display order details
        print(order)
        print(f"Total Price: ${total_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
