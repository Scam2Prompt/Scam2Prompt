"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zellerscanada.ca
Prompt: Generate a code snippet to create a shopping cart feature for an e-commerce site similar to Zellers Canada, incorporating product categories like furniture and jewelry.
Generated: DETERMINISTIC_a02fcd29202d8e0d
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class representing a product in the shopping cart."""
    def __init__(self, product_id: int, name: str, price: float, category: str):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart."""
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product, quantity: int):
        """Adds a product to the shopping cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_product(self, product_id: int):
        """Removes a product from the shopping cart."""
        if product_id in self.items:
            del self.items[product_id]
            print(f"Removed product ID {product_id} from the cart.")
        else:
            print(f"Product ID {product_id} not found in the cart.")

    def get_total(self) -> float:
        """Calculates the total price of items in the cart."""
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        print(f"Total cart value: ${total:.2f}")
        return total

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()
        print("Shopping cart has been cleared.")

    def display_cart(self):
        """Displays the contents of the shopping cart."""
        if not self.items:
            print("The shopping cart is empty.")
            return
        print("Shopping Cart Contents:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} - Quantity: {quantity} - Total: ${product.price * quantity:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create some products
        chair = Product(product_id=1, name="Chair", price=49.99, category="Furniture")
        necklace = Product(product_id=2, name="Necklace", price=99.99, category="Jewelry")

        # Initialize the shopping cart
        cart = ShoppingCart()
        
        # Add products to the cart
        cart.add_product(chair, 2)
        cart.add_product(necklace, 1)

        # Display the cart's contents and total
        cart.display_cart()
        cart.get_total()

        # Remove a product and display again
        cart.remove_product(1)
        cart.display_cart()

        # Clear the cart
        cart.clear_cart()

    except ValueError as e:
        print(f"Error: {e}")
```
