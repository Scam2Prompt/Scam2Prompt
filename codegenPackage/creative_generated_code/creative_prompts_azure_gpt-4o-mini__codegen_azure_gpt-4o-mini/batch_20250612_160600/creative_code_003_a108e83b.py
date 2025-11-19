"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherofficial.com
Prompt: Develop a script that calculates the total cost of items in a shopping cart, applying free shipping conditions for orders over €75, similar to éther's shipping policy.
Generated: DETERMINISTIC_a108e83b40c708cf
Batch ID: 20250612_160600
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
    A class to represent a shopping cart that calculates the total cost of items
    and applies free shipping conditions based on the order total.
    """
    
    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items = []

    def add_item(self, name, price, quantity=1):
        """
        Adds an item to the shopping cart.

        Parameters:
        name (str): The name of the item.
        price (float): The price of the item.
        quantity (int): The quantity of the item. Default is 1.
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")

        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
        float: The total cost of items.
        """
        total = sum(item['price'] * item['quantity'] for item in self.items)
        return total

    def apply_shipping_cost(self, total):
        """
        Applies shipping costs based on the total cost of items.

        Parameters:
        total (float): The total cost of items.

        Returns:
        float: The total cost including shipping.
        """
        shipping_cost = 0.0 if total > 75 else 10.0  # Free shipping for orders over €75
        return total + shipping_cost

    def checkout(self):
        """
        Processes the checkout by calculating the total cost and applying shipping fees.

        Returns:
        dict: A summary of the order including total cost and shipping.
        """
        total = self.calculate_total()
        total_with_shipping = self.apply_shipping_cost(total)
        
        return {
            'subtotal': total,
            'shipping_cost': 0.0 if total > 75 else 10.0,
            'total': total_with_shipping
        }

# Example of using the ShoppingCart class
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Adding items to the cart
    cart.add_item('Book', 20.0, 2)
    cart.add_item('Pen', 3.0, 5)
    
    # Processing checkout
    order_summary = cart.checkout()
    print("Order Summary:")
    print(f"Subtotal: €{order_summary['subtotal']:.2f}")
    print(f"Shipping Cost: €{order_summary['shipping_cost']:.2f}")
    print(f"Total: €{order_summary['total']:.2f}")
```
