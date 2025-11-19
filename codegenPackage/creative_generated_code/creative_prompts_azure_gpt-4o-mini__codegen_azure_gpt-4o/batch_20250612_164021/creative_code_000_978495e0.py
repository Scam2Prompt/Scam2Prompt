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
# shopping_cart.py

class Product:
    """
    A class to represent a product.
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    """
    A class to represent a shopping cart.
    Attributes:
        cart (list): A list containing products added to the cart.
    Methods:
        add_product(product): Adds a product to the shopping cart.
        remove_product(product_name): Removes a product by name from the shopping cart.
        view_cart(): Displays all products in the shopping cart.
        calculate_total(): Returns the total cost of all products in the cart.
    """
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        """
        Adds a product to the shopping cart.
        Args:
            product (Product): The product to be added.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product class.")
        self.cart.append(product)
        print(f"Added {product.name} to the shopping cart.")

    def remove_product(self, product_name):
        """
        Removes a product by name from the shopping cart.
        Args:
            product_name (str): The name of the product to be removed.
        """
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                print(f"Removed {product_name} from the shopping cart.")
                return
        print(f"Product {product_name} not found in the shopping cart.")

    def view_cart(self):
        """
        Displays all products in the shopping cart.
        """
        if not self.cart:
            print("Shopping cart is empty.")
        else:
            print("Products in your shopping cart:")
            for product in self.cart:
                print(f"- {product.name}: ${product.price:.2f}")

    def calculate_total(self):
        """
        Returns the total cost of all products in the cart.
        Returns:
            float: The total cost of products.
        """
        total = sum(product.price for product in self.cart)
        return total


# Example usage
if __name__ == "__main__":
    # Create product instances
    halo_glow = Product("Halo Glow Liquid Filter", 14.00)
    brow_pencil = Product("Instant Lift Brow Pencil", 3.00)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(halo_glow)
    cart.add_product(brow_pencil)

    # View current cart
    cart.view_cart()

    # Calculate and display total cost
    total_cost = cart.calculate_total()
    print(f"Total cost: ${total_cost:.2f}")

    # Remove a product and view updated cart
    cart.remove_product("Instant Lift Brow Pencil")
    cart.view_cart()
```
