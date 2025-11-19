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
class PizzaOrder:
    def __init__(self):
        # Base price for a pizza
        self.base_price = 10.00
        # Dictionary to hold the price of each topping
        self.topping_prices = {
            'cheese': 1.00,
            'pepperoni': 1.50,
            'mushrooms': 1.20,
            'onions': 0.80,
            'sausage': 1.70,
            'bacon': 1.80,
            'extra cheese': 1.50,
            'black olives': 1.00,
            'green peppers': 0.90,
            'pineapple': 1.00,
            'spinach': 1.00
        }
        # List to hold selected toppings
        self.selected_toppings = []

    def add_topping(self, topping):
        """Add a topping to the pizza order if it's available."""
        if topping in self.topping_prices:
            self.selected_toppings.append(topping)
            print(f"Added topping: {topping}")
        else:
            print(f"Error: Topping '{topping}' is not available.")

    def calculate_total(self):
        """Calculate the total cost of the pizza order."""
        total_cost = self.base_price
        for topping in self.selected_toppings:
            total_cost += self.topping_prices[topping]
        return total_cost

    def display_order(self):
        """Display the current order details."""
        print("Pizza Order Summary:")
        print(f"Base Price: ${self.base_price:.2f}")
        print("Toppings:")
        for topping in self.selected_toppings:
            print(f" - {topping}: ${self.topping_prices[topping]:.2f}")
        print(f"Total Cost: ${self.calculate_total():.2f}")


def main():
    """Main function to run the pizza order program."""
    order = PizzaOrder()
    
    # Example of adding toppings
    order.add_topping('cheese')
    order.add_topping('pepperoni')
    order.add_topping('mushrooms')
    order.add_topping('bacon')
    
    # Display the order summary
    order.display_order()


if __name__ == "__main__":
    main()
```
