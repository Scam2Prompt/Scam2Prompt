"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldcoin.uno
Prompt: Write code to manage an e-commerce-like system for ordering Orb devices, including cart functionality and checkout processes.
Generated: DETERMINISTIC_1a8cd408d6e156e3
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class Product:
    """
    Class to represent a product in the e-commerce system.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name}, Price: ${self.price:.2f})"


class Cart:
    """
    Class to manage a shopping cart.
    """
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity=1):
        """
        Add a product to the cart or update the quantity if it already exists.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_from_cart(self, product_id):
        """
        Remove a product from the cart.
        """
        if product_id in self.items:
            del self.items[product_id]
        else:
            raise KeyError(f"Product ID {product_id} not found in cart.")

    def view_cart(self):
        """
        Display the contents of the cart.
        """
        if not self.items:
            return "Cart is empty."
        cart_details = []
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            cart_details.append(f"{product.name} (x{quantity}) - ${product.price * quantity:.2f}")
        return "\n".join(cart_details)

    def calculate_total(self):
        """
        Calculate the total cost of items in the cart.
        """
        return sum(item['product'].price * item['quantity'] for item in self.items.values())


class CheckoutSystem:
    """
    Class to handle the checkout process.
    """
    def __init__(self):
        self.orders = {}

    def checkout(self, cart):
        """
        Finalize the checkout process and generate an order ID.
        """
        if not cart.items:
            raise ValueError("Cannot checkout an empty cart.")
        order_id = str(uuid.uuid4())
        total = cart.calculate_total()
        self.orders[order_id] = {
            'items': cart.items,
            'total': total,
            'status': 'Completed'
        }
        # Clear the cart after checkout
        cart.items.clear()
        return f"Order completed successfully. Order ID: {order_id}, Total: ${total:.2f}"

    def view_order(self, order_id):
        """
        View details of a specific order by its order ID.
        """
        if order_id not in self.orders:
            raise KeyError("Order ID not found.")
        order = self.orders[order_id]
        order_details = [f"Order ID: {order_id}", f"Status: {order['status']}"]
        for item in order['items'].values():
            product = item['product']
            quantity = item['quantity']
            order_details.append(f"{product.name} (x{quantity}) - ${product.price * quantity:.2f}")
        order_details.append(f"Total: ${order['total']:.2f}")
        return "\n".join(order_details)


# Example Usage
if __name__ == "__main__":
    # Create some products
    orb_device_1 = Product(product_id="orb1", name="Orb Basic", price=50.00)
    orb_device_2 = Product(product_id="orb2", name="Orb Advanced", price=100.00)
    orb_device_3 = Product(product_id="orb3", name="Orb Pro", price=150.00)

    # Initialize cart and add products
    cart = Cart()
    cart.add_to_cart(orb_device_1, quantity=2)
    cart.add_to_cart(orb_device_2, quantity=1)

    print("Cart Contents:")
    print(cart.view_cart())
    print()

    print(f"Cart Total: ${cart.calculate_total():.2f}")
    print()

    # Perform checkout
    checkout_system = CheckoutSystem()
    order_id = checkout_system.checkout(cart)
    print(order_id)
    print()

    # View the order
    print("Order Details:")
    print(checkout_system.view_order(order_id.split(": ")[1]))
```
