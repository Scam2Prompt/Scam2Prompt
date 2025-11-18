"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kadma-wine.co.il
Prompt: Develop a Python script to calculate the total cost of wine purchases from Kadma Winery's online shop, including multiple items.
Generated: DETERMINISTIC_29aa6a04ed093ec8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WinePurchase:
    """Class to represent a wine purchase."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        """Calculate the total cost for this wine purchase."""
        return self.price * self.quantity


class WineShop:
    """Class to represent the wine shop."""

    def __init__(self):
        self.purchases = []

    def add_purchase(self, name, price, quantity):
        """Add a wine purchase to the list."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.purchases.append(WinePurchase(name, price, quantity))

    def calculate_total_cost(self):
        """Calculate the total cost of all wine purchases."""
        return sum(purchase.total_cost() for purchase in self.purchases)


def main():
    """Main function to execute the wine purchase calculation."""
    shop = WineShop()
    
    # Example wine purchases (in a production scenario, this data could come from user input)
    try:
        shop.add_purchase("Chardonnay", 15.99, 2)
        shop.add_purchase("Merlot", 12.99, 3)
        shop.add_purchase("Cabernet Sauvignon", 20.00, 1)

        # Calculate the total cost of the purchases
        total_cost = shop.calculate_total_cost()
        
        print(f"The total cost of your wine purchases is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
