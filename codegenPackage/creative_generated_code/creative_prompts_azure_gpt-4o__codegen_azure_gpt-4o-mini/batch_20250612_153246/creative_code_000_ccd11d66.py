"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Write Python code to simulate a shopping cart system that includes categories like "Gaming Accessories," "DIY Tools," and "Solar Panels," as described on the Techno City website. Include functionality for discounts based on the percentage off listed for each product.
Generated: DETERMINISTIC_ccd11d663e97c4ad
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Represents a product in the shopping cart with a name, category, price, and discount."""

    def __init__(self, name: str, category: str, price: float, discount: float = 0.0):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount

    def get_final_price(self) -> float:
        """Calculate the final price after applying the discount."""
        if self.discount < 0 or self.discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
        final_price = self.price * (1 - self.discount / 100)
        return round(final_price, 2)


class ShoppingCart:
    """Represents a shopping cart that holds multiple products."""

    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        """Add a product to the shopping cart."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the cart.")
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """Remove a product from the shopping cart by name."""
        self.products = [product for product in self.products if product.name != product_name]

    def calculate_total(self) -> float:
        """Calculate the total price of all products in the cart."""
        total = sum(product.get_final_price() for product in self.products)
        return round(total, 2)

    def list_products(self) -> None:
        """List all products in the shopping cart."""
        for product in self.products:
            print(f"{product.name} - Category: {product.category}, Price: ${product.price}, Discount: {product.discount}% - Final Price: ${product.get_final_price()}")


# Example usage
if __name__ == "__main__":
    # Create some products
    gaming_accessory = Product("Gaming Mouse", "Gaming Accessories", 49.99, 10)
    diy_tool = Product("Cordless Drill", "DIY Tools", 89.99, 15)
    solar_panel = Product("200W Solar Panel", "Solar Panels", 199.99, 20)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(gaming_accessory)
    cart.add_product(diy_tool)
    cart.add_product(solar_panel)

    # List products in the cart
    print("Products in Cart:")
    cart.list_products()

    # Calculate total price
    total_price = cart.calculate_total()
    print(f"\nTotal Price: ${total_price}")
    
    # Remove a product from the cart
    cart.remove_product("Gaming Mouse")
    print("\nProducts in Cart after removing Gaming Mouse:")
    cart.list_products()
    
    # Calculate total price again
    new_total_price = cart.calculate_total()
    print(f"\nNew Total Price: ${new_total_price}")
```
