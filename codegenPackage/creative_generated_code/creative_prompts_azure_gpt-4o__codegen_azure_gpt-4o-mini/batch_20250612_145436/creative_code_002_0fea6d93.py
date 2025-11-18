"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Generate code to create a shopping cart feature for an e-commerce site that sells farming machinery such as water pumps and lawnmowers, inspired by Dotcom Machinery's product categories.
Generated: DETERMINISTIC_0fea6d935e447c5d
Batch ID: 20250612_145436
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
    """Represents a product in the catalogue."""
    
    def __init__(self, product_id, name, price):
        """
        Initializes a new product.

        Args:
            product_id (str): The unique identifier for the product.
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} (ID: {self.product_id}, Price: ${self.price:.2f})"


class ShoppingCart:
    """Represents a shopping cart for an e-commerce site."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_product(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id, quantity=1):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (str): The ID of the product to remove.
            quantity (int): The quantity of the product to remove.
        """
        if product_id not in self.items:
            raise KeyError(f"Product ID '{product_id}' not found in the cart.")

        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        if self.items[product_id]['quantity'] <= quantity:
            del self.items[product_id]  # Remove product completely if quantity drops to zero
        else:
            self.items[product_id]['quantity'] -= quantity

    def view_cart(self):
        """Returns a summary of the shopping cart contents."""
        if not self.items:
            return "Shopping cart is empty."
        return {product_id: {'product': details['product'], 'quantity': details['quantity']} 
                for product_id, details in self.items.items()}

    def total_price(self):
        """Calculates the total price of all items in the cart."""
        return sum(details['product'].price * details['quantity'] for details in self.items.values())

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()


# Example usage
if __name__ == "__main__":
    # Create some product instances
    pump = Product("P001", "Water Pump", 150.00)
    mower = Product("M001", "Lawnmower", 300.00)

    # Create a shopping cart instance
    cart = ShoppingCart()

    # Add products to the cart with quantity
    cart.add_product(pump, 2)  # Adding 2 water pumps
    cart.add_product(mower, 1)  # Adding 1 lawnmower

    # View cart contents
    print("Cart contents:", cart.view_cart())

    # Total price calculation
    print("Total price:", cart.total_price())

    # Remove a product
    cart.remove_product("P001", 1)  # Remove 1 water pump
    print("Cart contents after removal:", cart.view_cart())

    # Clear the cart
    cart.clear_cart()
    print("Cart contents after clearing:", cart.view_cart())
```
