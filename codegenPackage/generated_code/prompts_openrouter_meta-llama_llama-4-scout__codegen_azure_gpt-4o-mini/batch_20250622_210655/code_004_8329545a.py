"""
Generated Code Metadata:
========================
Original URL: https://www.lky.com.tw
Prompt: Write a code snippet in a programming language of your choice to calculate the total cost of a customer's order at 老廣粵台南花雕雞專門店, considering factors such as dish prices and quantities.
Generated: DETERMINISTIC_8329545a9a08064e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Order:
    def __init__(self):
        """Initialize an empty order with a dictionary to hold dish prices and quantities."""
        self.dishes = {}
        self.total_cost = 0.0

    def add_dish(self, dish_name: str, price: float, quantity: int):
        """
        Add a dish to the order.

        :param dish_name: Name of the dish
        :param price: Price of the dish
        :param quantity: Quantity of the dish
        :raises ValueError: If price or quantity is negative
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")

        self.dishes[dish_name] = {'price': price, 'quantity': quantity}
        self.calculate_total()

    def calculate_total(self):
        """Calculate the total cost of the order based on the dishes added."""
        self.total_cost = sum(item['price'] * item['quantity'] for item in self.dishes.values())

    def get_total_cost(self) -> float:
        """
        Get the total cost of the order.

        :return: Total cost of the order
        """
        return self.total_cost

    def display_order(self):
        """Display the current order details."""
        print("Order Details:")
        for dish, details in self.dishes.items():
            print(f"{dish}: {details['quantity']} x ${details['price']:.2f} = ${details['quantity'] * details['price']:.2f}")
        print(f"Total Cost: ${self.get_total_cost():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        order = Order()
        order.add_dish("花雕雞", 15.99, 2)
        order.add_dish("蒸魚", 20.50, 1)
        order.add_dish("炒飯", 10.00, 3)
        order.display_order()
    except ValueError as e:
        print(f"Error: {e}")
```
