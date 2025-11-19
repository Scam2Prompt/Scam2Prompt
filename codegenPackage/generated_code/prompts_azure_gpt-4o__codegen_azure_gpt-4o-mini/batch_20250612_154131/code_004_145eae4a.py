"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Suggest a library or framework to implement a shopping cart system that supports international shipping for a company like Rising Star International, which exports products to Europe, USA, Canada, and Australia.
Generated: DETERMINISTIC_145eae4a113da769
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class ShoppingCart:
    """
    A class to represent a shopping cart for an international e-commerce platform.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []
        self.total_price = 0.0

    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the shopping cart.

        :param item: The name of the item to add.
        :param price: The price of the item.
        :param quantity: The quantity of the item to add (default is 1).
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        self.items.append({'item': item, 'price': price, 'quantity': quantity})
        self.total_price += price * quantity

    def remove_item(self, item):
        """
        Removes an item from the shopping cart.

        :param item: The name of the item to remove.
        :raises ValueError: If the item is not found in the cart.
        """
        for cart_item in self.items:
            if cart_item['item'] == item:
                self.total_price -= cart_item['price'] * cart_item['quantity']
                self.items.remove(cart_item)
                return
        raise ValueError(f"Item '{item}' not found in the cart.")

    def calculate_shipping(self, country):
        """
        Calculates shipping cost based on the destination country.

        :param country: The destination country for shipping.
        :return: Shipping cost.
        :raises ValueError: If the country is not supported.
        """
        shipping_rates = {
            'USA': 5.00,
            'Canada': 7.00,
            'Europe': 10.00,
            'Australia': 12.00
        }

        if country not in shipping_rates:
            raise ValueError(f"Shipping to '{country}' is not supported.")

        return shipping_rates[country]

    def checkout(self, country):
        """
        Finalizes the purchase and calculates the total cost including shipping.

        :param country: The destination country for shipping.
        :return: Total cost including items and shipping.
        :raises ValueError: If the cart is empty or country is not supported.
        """
        if not self.items:
            raise ValueError("Cannot checkout an empty cart.")

        shipping_cost = self.calculate_shipping(country)
        total_cost = self.total_price + shipping_cost
        return total_cost

    def clear_cart(self):
        """
        Clears the shopping cart.
        """
        self.items.clear()
        self.total_price = 0.0

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("Laptop", 1200.00, 1)
        cart.add_item("Headphones", 150.00, 2)
        print("Total cost including shipping to USA:", cart.checkout("USA"))
    except ValueError as e:
        print(f"Error: {e}")
```
