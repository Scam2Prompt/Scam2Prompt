"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Develop a script that handles the shopping cart functionality for an online cosmetics store, incorporating features seen on Galitska's site.
Generated: DETERMINISTIC_7f1b626ae6045486
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Product:
    """Represents a product in the cosmetics store."""
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock})"


class ShoppingCart:
    """Handles the shopping cart functionality for an online cosmetics store."""
    def __init__(self):
        self.cart = {}
        self.total_price = 0.0

    def add_product(self, product: Product, quantity: int):
        """Adds a product to the shopping cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if product.stock < quantity:
            raise ValueError(f"Insufficient stock for {product.name}. Available: {product.stock}")

        if product.id in self.cart:
            self.cart[product.id]['quantity'] += quantity
        else:
            self.cart[product.id] = {'product': product, 'quantity': quantity}

        product.stock -= quantity
        self.total_price += product.price * quantity
        print(f"Added {quantity} of {product.name} to the cart. Total price is now: ${self.total_price:.2f}")

    def remove_product(self, product_id: int):
        """Removes a product from the shopping cart."""
        if product_id in self.cart:
            product_info = self.cart[product_id]
            product_info['product'].stock += product_info['quantity']
            self.total_price -= product_info['product'].price * product_info['quantity']
            del self.cart[product_id]
            print(f"Removed product id {product_id} from the cart. Total price is now: ${self.total_price:.2f}")
        else:
            raise ValueError("Product not found in cart.")

    def view_cart(self):
        """Displays the current items in the shopping cart."""
        if not self.cart:
            print("Shopping cart is empty.")
            return

        print("Shopping Cart Contents:")
        for item in self.cart.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} - Quantity: {quantity}, Price: ${product.price} each, Total: ${product.price * quantity:.2f}")
        print(f"Total Price: ${self.total_price:.2f}")

    def checkout(self):
        """Finalizes the purchase and clears the cart."""
        if not self.cart:
            print("Cannot checkout, shopping cart is empty.")
            return

        print(f"Checking out. Your total is: ${self.total_price:.2f}")
        # Here, integrate with payment gateway and finalize the order
        self.cart.clear()
        self.total_price = 0.0
        print("Thank you for your purchase!")


# Example usage
if __name__ == "__main__":
    # Initializing products
    lipstick = Product(id=1, name="Lipstick", price=12.99, stock=50)
    foundation = Product(id=2, name="Foundation", price=29.99, stock=30)

    # Creating a shopping cart
    cart = ShoppingCart()

    # Adding products
    try:
        cart.add_product(lipstick, 2)
        cart.add_product(foundation, 1)
        cart.view_cart()

        # Removing a product
        cart.remove_product(1)
        cart.view_cart()

        # Proceeding to checkout
        cart.checkout()
    except ValueError as e:
        print(f"Error: {e}")
```
