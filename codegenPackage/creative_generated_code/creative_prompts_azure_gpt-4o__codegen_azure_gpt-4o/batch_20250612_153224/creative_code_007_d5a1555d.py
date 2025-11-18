"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Generate code to implement a shopping cart system for Bollé's e-commerce site, including support for adding discounted products like the CHRONOSHIELD TITANIUM MATTE.
Generated: DETERMINISTIC_d5a1555dfefe0d07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart System for Bollé's E-commerce Site

Features:
- Add products to the cart
- Handle discounted products
- Calculate total price with discounts applied
- Display cart contents
"""

class Product:
    """
    Represents a product in the store.
    Attributes:
        name (str): Name of the product.
        price (float): Price of the product.
        discount (float): Discount percentage (0-100).
    """
    def __init__(self, name: str, price: float, discount: float = 0.0):
        if price < 0 or discount < 0 or discount > 100:
            raise ValueError("Invalid price or discount value.")
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self) -> float:
        """
        Calculate the price after applying the discount.
        Returns:
            float: Discounted price.
        """
        return self.price * (1 - self.discount / 100)


class ShoppingCart:
    """
    Represents a shopping cart.
    Attributes:
        cart (list[Product]): List of products in the cart.
    """
    def __init__(self):
        self.cart = []

    def add_product(self, product: Product):
        """
        Add a product to the cart.
        Args:
            product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise TypeError("Invalid product type. Must be a Product instance.")
        self.cart.append(product)

    def remove_product(self, product_name: str):
        """
        Remove a product by name from the cart.
        Args:
            product_name (str): Name of the product to remove.
        """
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                return
        raise ValueError(f"Product '{product_name}' not found in cart.")

    def calculate_total(self) -> float:
        """
        Calculate the total price of all products in the cart.
        Returns:
            float: Total price after discounts.
        """
        return sum(product.get_discounted_price() for product in self.cart)

    def display_cart(self):
        """
        Display the contents of the cart.
        """
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Shopping Cart Contents:")
        for product in self.cart:
            print(f"- {product.name}: ${product.get_discounted_price():.2f} (Original: ${product.price:.2f}, Discount: {product.discount}%)")
        print(f"Total Price: ${self.calculate_total():.2f}")


# Example Usage:
if __name__ == "__main__":
    try:
        # Create some products
        chronoshield = Product(name="CHRONOSHIELD TITANIUM MATTE", price=199.99, discount=15)
        sunglasses = Product(name="Bollé Sunglasses", price=99.99)
        
        # Initialize shopping cart
        cart = ShoppingCart()
        
        # Add products to cart
        cart.add_product(chronoshield)
        cart.add_product(sunglasses)
        
        # Display cart contents
        cart.display_cart()
        
        # Remove a product and display cart again
        cart.remove_product("Bollé Sunglasses")
        cart.display_cart()
        
    except Exception as e:
        print(f"Error: {e}")
```
