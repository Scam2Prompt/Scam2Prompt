"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eclat.com.tr
Prompt: Generate a code snippet for an online shopping cart that includes features for nail art supplies, specifically for ECLAT's permanent nail polish and nail extension kits.
Generated: DETERMINISTIC_2c283794cd37229b
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, name, price, quantity=0):
        """
        Initializes a new product.

        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product in the cart
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        """Updates the product quantity in the cart."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity


class ShoppingCart:
    """Represents a shopping cart for nail art supplies."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """Adds a product to the shopping cart."""
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        
        # Check if the product is already in the cart
        for item in self.items:
            if item.name == product.name:
                item.update_quantity(item.quantity + product.quantity)
                return
        
        # If not, add the new product
        self.items.append(product)

    def remove_product(self, product_name):
        """Removes a product from the shopping cart by name."""
        self.items = [item for item in self.items if item.name != product_name]

    def calculate_total(self):
        """Calculates the total cost of the items in the shopping cart."""
        total = sum(item.price * item.quantity for item in self.items)
        return total

    def checkout(self):
        """Processes the checkout and returns the total amount."""
        if not self.items:
            raise Exception("Your cart is empty. Add products before checking out.")
        
        total_amount = self.calculate_total()
        self.items.clear()  # Clear the cart after successful checkout
        return total_amount


# Example usage
if __name__ == "__main__":
    try:
        # Create shopping cart instance
        cart = ShoppingCart()

        # Add ECLAT nail products
        nail_polish = Product("ECLAT Permanent Nail Polish", 12.99, 2)
        nail_extension_kit = Product("ECLAT Nail Extension Kit", 25.50, 1)

        cart.add_product(nail_polish)
        cart.add_product(nail_extension_kit)

        # Display total cost
        total_cost = cart.calculate_total()
        print(f"Total cost: ${total_cost:.2f}")

        # Checkout
        final_amount = cart.checkout()
        print(f"Checkout successful! Total amount charged: ${final_amount:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
