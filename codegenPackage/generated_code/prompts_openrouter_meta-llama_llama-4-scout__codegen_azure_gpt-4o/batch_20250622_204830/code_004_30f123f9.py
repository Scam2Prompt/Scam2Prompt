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
# Python program to calculate the total cost of a pizza order with different toppings

# Define a class to represent a Pizza Order
class PizzaOrder:
    def __init__(self, base_price):
        """
        Initialize the PizzaOrder with a base price.
        :param base_price: The base price of the pizza (e.g., plain cheese pizza).
        """
        self.base_price = base_price
        self.toppings = {}
    
    def add_topping(self, topping_name, topping_price):
        """
        Add a topping to the pizza order.
        :param topping_name: Name of the topping (e.g., "Pepperoni").
        :param topping_price: Price of the topping.
        """
        if topping_name in self.toppings:
            raise ValueError(f"Topping '{topping_name}' is already added.")
        self.toppings[topping_name] = topping_price
    
    def calculate_total(self):
        """
        Calculate the total cost of the pizza order.
        :return: Total cost as a float.
        """
        total = self.base_price + sum(self.toppings.values())
        return total
    
    def display_order(self):
        """
        Display the details of the pizza order.
        """
        print("Pizza Order:")
        print(f"  Base Price: ${self.base_price:.2f}")
        if self.toppings:
            print("  Toppings:")
            for topping, price in self.toppings.items():
                print(f"    {topping}: ${price:.2f}")
        else:
            print("  No toppings added.")
        print(f"  Total Cost: ${self.calculate_total():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a pizza order with a base price of $10.00
        order = PizzaOrder(base_price=10.00)
        
        # Add toppings
        order.add_topping("Pepperoni", 2.50)
        order.add_topping("Mushrooms", 1.75)
        order.add_topping("Olives", 1.25)
        
        # Display the order details
        order.display_order()
    except ValueError as e:
        # Handle errors such as duplicate toppings
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
```
