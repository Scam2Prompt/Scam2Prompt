"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pasionxlascasacas.com.uy
Prompt: Illustrate how to implement a shopping cart feature using the Pasión X Las Casacas product data, ensuring it includes options for custom engraving on jerseys.
Generated: DETERMINISTIC_09d078984597eb72
Batch ID: 20250612_161616
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
    """Class representing a product in the store."""
    
    def __init__(self, id, name, price):
        """
        Initialize the product with an ID, name, and price.
        
        :param id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        """
        self.id = id
        self.name = name
        self.price = price


class CartItem:
    """Class representing an item in the shopping cart."""
    
    def __init__(self, product, quantity, engraving=None):
        """
        Initialize the cart item with a product, quantity, and optional engraving.
        
        :param product: Instance of Product
        :param quantity: Quantity of the product
        :param engraving: Custom engraving text (optional)
        """
        self.product = product
        self.quantity = quantity
        self.engraving = engraving

    def total_price(self):
        """Calculate the total price for this cart item."""
        return self.product.price * self.quantity


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity, engraving=None):
        """
        Add an item to the cart.
        
        :param product: Instance of Product to add
        :param quantity: Quantity of the product to add
        :param engraving: Custom engraving text (optional)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        # Check if the item already exists in the cart
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                if engraving:
                    item.engraving = engraving
                return
        
        # If the product is not already in the cart, add a new item
        self.items.append(CartItem(product, quantity, engraving))

    def remove_item(self, product_id):
        """
        Remove an item from the cart by product ID.
        
        :param product_id: Unique identifier of the product to remove
        """
        self.items = [item for item in self.items if item.product.id != product_id]

    def total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(item.total_price() for item in self.items)

    def display_cart(self):
        """Display the contents of the cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for item in self.items:
            engraving_text = f" (Engraving: {item.engraving})" if item.engraving else ""
            print(f"{item.product.name} - Qty: {item.quantity}, Price: ${item.total_price():.2f}{engraving_text}")
        print(f"Total Price: ${self.total_price():.2f}")


# Example Usage
if __name__ == "__main__":
    # Sample product data for Pasión X Las Casacas
    products = [
        Product(1, "Pasión Jersey #1", 49.99),
        Product(2, "Pasión Jersey #2", 59.99),
    ]

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add items to the cart with custom engraving
    try:
        cart.add_item(products[0], 1, "John Doe")
        cart.add_item(products[1], 2)
        cart.add_item(products[0], 1)  # Add more of the same item

        # Display the cart
        cart.display_cart()

        # Remove an item by product ID
        cart.remove_item(1)

        # Display the cart again
        cart.display_cart()
    except ValueError as e:
        print(f"Error: {e}")
```
