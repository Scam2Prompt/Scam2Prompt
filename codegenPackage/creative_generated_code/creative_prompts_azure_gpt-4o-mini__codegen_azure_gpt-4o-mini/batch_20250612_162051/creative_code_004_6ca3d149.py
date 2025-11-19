"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubephanoi.vn
Prompt: Illustrate how to implement a shopping cart feature for Ecoplast products, ensuring it can handle multiple item types like "Kệ Tivi" and "Tủ Quần Áo," referencing the structure on tubephanoi.vn.
Generated: DETERMINISTIC_6ca3d149817c0697
Batch ID: 20250612_162051
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
    """Represents a product in the shopping cart."""
    
    def __init__(self, product_id, name, price, quantity=1):
        """
        Initializes a new product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product to add to the cart
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Calculates total price for this product based on quantity."""
        return self.price * self.quantity


class ShoppingCart:
    """Represents a shopping cart for multiple products."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}  # Dictionary to hold products by product_id

    def add_product(self, product):
        """
        Adds a product to the shopping cart.
        
        If the product already exists, it updates the quantity.

        :param product: Product instance to add to the cart
        :raises ValueError: If the provided product is not an instance of Product
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        
        if product.product_id in self.items:
            self.items[product.product_id].quantity += product.quantity
        else:
            self.items[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart by product_id.

        :param product_id: Unique identifier of the product to remove
        """
        if product_id in self.items:
            del self.items[product_id]

    def get_total(self):
        """Calculates the total price of all items in the cart."""
        return sum(item.total_price() for item in self.items.values())

    def list_items(self):
        """Returns a list of items in the cart."""
        return [(item.name, item.quantity, item.total_price()) for item in self.items.values()]

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()


# Example usage:
if __name__ == "__main__":
    # Create a shopping cart instance
    cart = ShoppingCart()

    # Create sample products
    product1 = Product(product_id=1, name="Kệ Tivi", price=1500000, quantity=1)
    product2 = Product(product_id=2, name="Tủ Quần Áo", price=3000000, quantity=2)

    # Add products to the cart
    cart.add_product(product1)
    cart.add_product(product2)

    # Display cart items and total
    print("Cart Items:")
    for item in cart.list_items():
        print(f"Product: {item[0]}, Quantity: {item[1]}, Total Price: {item[2]}")

    print(f"Total Cart Price: {cart.get_total()}")
    
    # Remove a product
    cart.remove_product(1)  # Remove "Kệ Tivi"
    print("Cart after removing Kệ Tivi:")
    print(cart.list_items())

    # Clear the cart
    cart.clear_cart()
    print(f"Cart after clearing: {cart.list_items()}")
```
