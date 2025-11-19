"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfcosmetics.com.ua
Prompt: Generate a code snippet for a shopping cart feature that allows users to add products like "Halo Glow Liquid Filter" and "Instant Lift Brow Pencil" from the ELF Cosmetics website.
Generated: DETERMINISTIC_978495e0f9ad2cb0
Batch ID: 20250612_164021
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
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Represents a shopping cart that holds products."""
    
    def __init__(self):
        self.items = []

    def add_product(self, product):
        """Adds a product to the shopping cart."""
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product.")
        self.items.append(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product_name):
        """Removes a product from the shopping cart by name."""
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {item} from the cart.")
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        total = sum(item.price for item in self.items)
        return total

    def display_cart(self):
        """Displays the current items in the shopping cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        print("Shopping Cart Items:")
        for item in self.items:
            print(f" - {item}")
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        halo_glow = Product("Halo Glow Liquid Filter", 14.00)
        brow_pencil = Product("Instant Lift Brow Pencil", 5.00)

        cart.add_product(halo_glow)
        cart.add_product(brow_pencil)
        cart.display_cart()

        cart.remove_product("Halo Glow Liquid Filter")
        cart.display_cart()

    except ValueError as e:
        print(f"Error: {e}")
```
