"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Write code to create a shopping cart system for a website selling replica wrestling championship belts, including categories like AEW Belts, WWE Belts, and MLB Title Belts.
Generated: DETERMINISTIC_01625f360ddfb1ef
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Dict, Union

# Define the Product class
class Product:
    """
    Represents a product in the shopping cart system.
    """
    def __init__(self, id: int, name: str, category: str, price: float):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - ${self.price:.2f}"

# Define the ShoppingCart class
class ShoppingCart:
    """
    Represents a shopping cart for storing products.
    """
    def __init__(self):
        self.cart: Dict[int, int] = {}  # Dictionary to store product ID and quantity
        self.products: Dict[int, Product] = {}  # Dictionary to store product details

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """
        Adds a product to the shopping cart.
        :param product: The product to add.
        :param quantity: The quantity of the product to add.
        """
        if product.id not in self.products:
            self.products[product.id] = product

        if product.id in self.cart:
            self.cart[product.id] += quantity
        else:
            self.cart[product.id] = quantity

    def remove_product(self, product_id: int) -> None:
        """
        Removes a product from the shopping cart by its ID.
        :param product_id: The ID of the product to remove.
        """
        if product_id in self.cart:
            del self.cart[product_id]
        else:
            raise ValueError(f"Product with ID {product_id} not found in the cart.")

    def update_quantity(self, product_id: int, quantity: int) -> None:
        """
        Updates the quantity of a product in the shopping cart.
        :param product_id: The ID of the product to update.
        :param quantity: The new quantity for the product.
        """
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id] = quantity
            else:
                self.remove_product(product_id)
        else:
            raise ValueError(f"Product with ID {product_id} not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart.
        :return: The total price.
        """
        total = 0.0
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            total += product.price * quantity
        return total

    def view_cart(self) -> List[str]:
        """
        Provides a summary of the shopping cart's contents.
        :return: A list of strings describing the items in the cart.
        """
        if not self.cart:
            return ["Your shopping cart is empty."]
        summary = []
        for product_id, quantity in self.cart.items():
            product = self.products[product_id]
            summary.append(f"{product.name} ({product.category}) - Quantity: {quantity}, Unit Price: ${product.price:.2f}, Subtotal: ${product.price * quantity:.2f}")
        return summary

    def clear_cart(self) -> None:
        """
        Clears all items from the shopping cart.
        """
        self.cart.clear()

# Products for the shopping cart
available_products = [
    Product(1, "AEW World Championship Belt", "AEW Belts", 299.99),
    Product(2, "WWE Universal Championship Belt", "WWE Belts", 249.99),
    Product(3, "MLB Replica Championship Belt", "MLB Title Belts", 199.99)
]

# Example usage (can be replaced with web framework or API integrations)
if __name__ == "__main__":
    # Initialize the shopping cart
    cart = ShoppingCart()
    
    # Add products to the cart
    cart.add_product(available_products[0], 2)  # Add 2 AEW belts
    cart.add_product(available_products[1])     # Add 1 WWE belt
    
    # View cart contents
    print("Cart Contents:")
    for item in cart.view_cart():
        print(item)

    # Update product quantity
    cart.update_quantity(1, 3)  # Update AEW belts to 3

    # Calculate total
    print(f"\nTotal Price: ${cart.calculate_total():.2f}")

    # Remove a product
    cart.remove_product(2)  # Remove WWE belt

    # View updated cart contents
    print("\nUpdated Cart Contents:")
    for item in cart.view_cart():
        print(item)

    # Clear the cart
    cart.clear_cart()
    print("\nCart Contents After Clearing:")
    print(cart.view_cart()[0])
```
