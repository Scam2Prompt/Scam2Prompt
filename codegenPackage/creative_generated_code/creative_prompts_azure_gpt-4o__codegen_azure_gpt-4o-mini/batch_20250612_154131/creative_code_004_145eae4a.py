"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Suggest a library or framework to implement a shopping cart system that supports international shipping for a company like Rising Star International, which exports products to Europe, USA, Canada, and Australia.
Generated: DETERMINISTIC_145eae4a113da769
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class ShoppingCart:
    """
    A class to represent a shopping cart for an international e-commerce platform.
    This class supports adding items, calculating totals, and simulating an order.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []  # List to store items in the cart

    def add_item(self, product, quantity, price):
        """
        Adds an item to the shopping cart.

        :param product: str, the name of the product
        :param quantity: int, the quantity of the product
        :param price: float, the price of the product
        :raises ValueError: if quantity or price is non-positive
        """
        if quantity <= 0 or price < 0:
            raise ValueError("Quantity must be positive and price must be non-negative.")
        
        item = {
            'product': product,
            'quantity': quantity,
            'price': price
        }
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total price of all items in the cart.

        :return: float, total price
        """
        total = sum(item['quantity'] * item['price'] for item in self.items)
        return total

    def checkout(self, shipping_country):
        """
        Simulates the checkout process and provides shipping costs based on the country.

        :param shipping_country: str, the country to ship to
        :return: dict, summary of the order
        """
        total_amount = self.calculate_total()
        shipping_cost = self.calculate_shipping(shipping_country)
        
        order_summary = {
            'items': self.items,
            'total_amount': total_amount,
            'shipping_cost': shipping_cost,
            'grand_total': total_amount + shipping_cost
        }
        
        return order_summary

    def calculate_shipping(self, country):
        """
        Calculates shipping costs based on the destination country.

        :param country: str, the destination country
        :return: float, shipping cost
        """
        shipping_rates = {
            'USA': 10.0,
            'Canada': 15.0,
            'Europe': 20.0,
            'Australia': 25.0
        }

        # Get shipping cost from rates. Default to 30.0 for unsupported regions.
        return shipping_rates.get(country, 30.0)


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("Laptop", 1, 1200.00)
        cart.add_item("Wireless Mouse", 2, 25.00)
        
        order_summary = cart.checkout("USA")
        print("Order Summary:", order_summary)
    except ValueError as e:
        print("Error:", e)
```
