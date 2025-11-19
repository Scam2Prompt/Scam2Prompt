"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Generate a code snippet for an online ordering system that offers discounts, similar to the 50% OFF promotion mentioned on utterlybaked.com.
Generated: DETERMINISTIC_20eb447371df3cb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class OnlineOrderingSystem:
    def __init__(self):
        # Initialize the system with an empty list of orders and a default discount
        self.orders = []
        self.discount_percentage = 50  # Default discount percentage (e.g., 50% OFF)

    def calculate_discounted_price(self, original_price):
        """
        Calculate the discounted price based on the current discount percentage.
        :param original_price: float - The original price of the item.
        :return: float - The price after applying the discount.
        """
        if original_price < 0:
            raise ValueError("Original price cannot be negative.")
        discount = (self.discount_percentage / 100) * original_price
        return round(original_price - discount, 2)

    def place_order(self, customer_name, item_name, original_price):
        """
        Place an order and apply the discount to the item's price.
        :param customer_name: str - Name of the customer.
        :param item_name: str - Name of the item being ordered.
        :param original_price: float - Original price of the item.
        :return: dict - Details of the placed order.
        """
        try:
            discounted_price = self.calculate_discounted_price(original_price)
            order = {
                "customer_name": customer_name,
                "item_name": item_name,
                "original_price": original_price,
                "discounted_price": discounted_price,
                "order_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.orders.append(order)
            return order
        except ValueError as e:
            print(f"Error placing order: {e}")
            return None

    def get_all_orders(self):
        """
        Retrieve all orders placed in the system.
        :return: list - List of all orders.
        """
        return self.orders


# Example usage
if __name__ == "__main__":
    # Create an instance of the ordering system
    system = OnlineOrderingSystem()

    # Place some orders
    order1 = system.place_order("Alice", "Chocolate Cake", 20.0)
    order2 = system.place_order("Bob", "Vanilla Cupcake", 15.0)

    # Print the orders
    if order1:
        print("Order 1:", order1)
    if order2:
        print("Order 2:", order2)

    # Retrieve and print all orders
    print("\nAll Orders:")
    for order in system.get_all_orders():
        print(order)
```
