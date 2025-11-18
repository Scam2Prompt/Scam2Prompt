"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Write Python code to create a shopping cart system that includes product categories like "잔디깍기," "예초기," and "체인톱" from 심바공구, allowing users to add items with unique product IDs and calculate total prices.
Generated: DETERMINISTIC_ae6c61f702b8d9d5
Batch ID: 20250612_154958
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
    
    def __init__(self, product_id: str, name: str, price: float, category: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, Price: {self.price}, Category: {self.category})"


class ShoppingCart:
    """Represents a shopping cart that holds products."""
    
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        """Adds a product to the shopping cart."""
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Must be an instance of Product.")
        self.items.append(product)

    def calculate_total(self) -> float:
        """Calculates the total price of all items in the cart."""
        total = sum(item.price for item in self.items)
        return round(total, 2)

    def list_products(self):
        """Lists all products in the shopping cart."""
        if not self.items:
            print("The cart is empty.")
        else:
            for item in self.items:
                print(item)

    def clear_cart(self):
        """Removes all items from the shopping cart."""
        self.items.clear()
        print("All items have been removed from the cart.")


# Example usage
if __name__ == "__main__":
    # Create some products
    lawn_mower = Product("001", "잔디깍기", 250.00, "Lawn Care")
    trimmer = Product("002", "예초기", 150.00, "Lawn Care")
    chainsaw = Product("003", "체인톱", 350.00, "Power Tools")

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    try:
        cart.add_product(lawn_mower)
        cart.add_product(trimmer)
        cart.add_product(chainsaw)

        # List products in the cart
        print("Products in cart:")
        cart.list_products()

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price: {total_price} 원")

        # Clear the cart
        cart.clear_cart()
        cart.list_products()  # Show empty cart
    except Exception as e:
        print(f"An error occurred: {e}")
```
