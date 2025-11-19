"""
Generated Code Metadata:
========================
Original URL: https://meta-mask-co-wallet.blogspot.com
Prompt: Write a code in a programming language of your choice to calculate the total cost of a pizza order with different toppings, similar to how A Pizza da Mooca might calculate their orders.
Generated: DETERMINISTIC_30f123f9132075bb
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pizza_order.py

class Pizza:
    """Represents a pizza with a base price and toppings."""

    def __init__(self, base_price):
        """
        Initializes a Pizza object.

        Args:
            base_price (float): The base price of the pizza.
        """
        self.base_price = base_price
        self.toppings = {}

    def add_topping(self, name, price):
        """
        Adds a topping to the pizza.

        Args:
            name (str): The name of the topping.
            price (float): The price of the topping.
        """
        self.toppings[name] = price

    def remove_topping(self, name):
        """
        Removes a topping from the pizza.

        Args:
            name (str): The name of the topping.

        Raises:
            ValueError: If the topping is not found.
        """
        if name not in self.toppings:
            raise ValueError(f"Topping '{name}' not found.")
        del self.toppings[name]

    def calculate_total(self):
        """
        Calculates the total cost of the pizza.

        Returns:
            float: The total cost of the pizza.
        """
        total = self.base_price
        for price in self.toppings.values():
            total += price
        return total


class PizzaOrder:
    """Represents a pizza order with multiple pizzas."""

    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        """
        Adds a pizza to the order.

        Args:
            pizza (Pizza): The pizza to add.
        """
        self.pizzas.append(pizza)

    def remove_pizza(self, index):
        """
        Removes a pizza from the order.

        Args:
            index (int): The index of the pizza to remove.

        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.pizzas):
            raise IndexError("Index out of range.")
        del self.pizzas[index]

    def calculate_total(self):
        """
        Calculates the total cost of the order.

        Returns:
            float: The total cost of the order.
        """
        total = 0
        for pizza in self.pizzas:
            total += pizza.calculate_total()
        return total


def main():
    # Create a pizza order
    order = PizzaOrder()

    # Create pizzas
    pizza1 = Pizza(10.99)  # Base price
    pizza1.add_topping("Mozzarella", 1.50)
    pizza1.add_topping("Pepperoni", 2.00)

    pizza2 = Pizza(12.99)  # Base price
    pizza2.add_topping("Mozzarella", 1.50)
    pizza2.add_topping("Sausage", 2.50)

    # Add pizzas to the order
    order.add_pizza(pizza1)
    order.add_pizza(pizza2)

    # Calculate and print the total cost
    try:
        total_cost = order.calculate_total()
        print(f"Total cost: ${total_cost:.2f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
