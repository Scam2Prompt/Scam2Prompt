"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate a code snippet to create a shopping cart functionality for an e-commerce site that includes categories like "Ambientes Perfumados" and "Móveis Decoração."
Generated: DETERMINISTIC_c25139d4a984b2b9
Batch ID: 20250612_162544
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
    """Class representing a product in the shopping cart."""
    
    def __init__(self, product_id, name, price, category):
        """
        Initialize a Product instance.
        
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param category: Category of the product
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category


class ShoppingCart:
    """Class representing a shopping cart for an e-commerce site."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.
        
        :param product: Instance of Product to add to the cart
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product_id):
        """
        Remove a product from the shopping cart by product_id.
        
        :param product_id: Unique identifier for the product to remove
        :raises ValueError: If the product is not found in the cart
        """
        for item in self.items:
            if item.product_id == product_id:
                self.items.remove(item)
                return
        raise ValueError(f"Product with ID {product_id} not found in the cart.")

    def calculate_total(self):
        """
        Calculate the total price of the items in the cart.
        
        :return: Total price as a float
        """
        return sum(item.price for item in self.items)

    def list_products(self):
        """
        List all products in the shopping cart.
        
        :return: List of product names and their prices
        """
        return [(item.name, item.price) for item in self.items]


# Example usage of the ShoppingCart functionality
if __name__ == "__main__":
    # Create some products
    product1 = Product(product_id=1, name="Ambiente Perfumado - Lavanda", price=29.99, category="Ambientes Perfumados")
    product2 = Product(product_id=2, name="Sofa Moderno", price=499.99, category="Móveis Decoração")

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to cart
    cart.add_product(product1)
    cart.add_product(product2)

    # List products in the cart
    products_in_cart = cart.list_products()
    print("Products in Cart:", products_in_cart)

    # Calculate total price
    total_price = cart.calculate_total()
    print("Total Price:", total_price)

    # Remove a product
    try:
        cart.remove_product(1)  # Attempt to remove product with ID 1
        print("Product with ID 1 removed successfully.")
    except ValueError as e:
        print(e)

    # Final product list and total price after removal
    print("Updated Products in Cart:", cart.list_products())
    print("Updated Total Price:", cart.calculate_total())
```
