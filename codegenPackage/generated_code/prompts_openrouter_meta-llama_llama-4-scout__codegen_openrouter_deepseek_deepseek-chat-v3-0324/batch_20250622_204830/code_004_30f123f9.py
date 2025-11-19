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
    """
    A class to represent a pizza order with customizable toppings and size.
    Calculates the total cost based on selections.
    """
    
    # Pricing configuration
    BASE_PRICES = {
        'small': 10.00,
        'medium': 12.00,
        'large': 14.00,
        'extra-large': 16.00
    }
    
    TOPPING_PRICES = {
        'pepperoni': 1.50,
        'mushrooms': 1.00,
        'onions': 0.75,
        'sausage': 1.75,
        'bacon': 2.00,
        'extra cheese': 1.25,
        'black olives': 0.80,
        'green peppers': 0.75
    }
    
    def __init__(self, size='medium'):
        """
        Initialize a pizza order with default size 'medium' and no toppings.
        """
        self.size = size.lower()
        self.toppings = []
        
    def add_topping(self, topping):
        """
        Add a topping to the pizza if it's available.
        """
        topping = topping.lower()
        if topping in self.TOPPING_PRICES:
            self.toppings.append(topping)
        else:
            raise ValueError(f"Invalid topping: {topping}. Available toppings: {list(self.TOPPING_PRICES.keys())}")
    
    def remove_topping(self, topping):
        """
        Remove a topping from the pizza if it exists.
        """
        topping = topping.lower()
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            raise ValueError(f"Topping {topping} not found in current order.")
    
    def set_size(self, size):
        """
        Set the pizza size if it's available.
        """
        size = size.lower()
        if size in self.BASE_PRICES:
            self.size = size
        else:
            raise ValueError(f"Invalid size: {size}. Available sizes: {list(self.BASE_PRICES.keys())}")
    
    def calculate_total(self):
        """
        Calculate the total cost of the pizza order.
        """
        try:
            base_price = self.BASE_PRICES[self.size]
            toppings_cost = sum(self.TOPPING_PRICES[topping] for topping in self.toppings)
            return base_price + toppings_cost
        except KeyError as e:
            raise ValueError(f"Invalid configuration: {str(e)}")
    
    def __str__(self):
        """
        Return a human-readable representation of the order.
        """
        toppings_str = ', '.join(self.toppings) if self.toppings else 'no toppings'
        return f"{self.size.capitalize()} pizza with {toppings_str}. Total: ${self.calculate_total():.2f}"


# Example usage
if __name__ == "__main__":
    try:
        order = PizzaOrder('large')
        order.add_topping('pepperoni')
        order.add_topping('mushrooms')
        order.add_topping('extra cheese')
        print(order)
        
        order.remove_topping('mushrooms')
        order.set_size('extra-large')
        print(order)
        
    except ValueError as e:
        print(f"Error: {e}")
```
