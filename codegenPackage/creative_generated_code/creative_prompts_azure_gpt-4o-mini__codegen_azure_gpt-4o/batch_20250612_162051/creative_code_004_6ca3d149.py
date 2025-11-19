"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tubephanoi.vn
Prompt: Illustrate how to implement a shopping cart feature for Ecoplast products, ensuring it can handle multiple item types like "Kệ Tivi" and "Tủ Quần Áo," referencing the structure on tubephanoi.vn.
Generated: DETERMINISTIC_6ca3d149817c0697
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart Implementation for Ecoplast Products
Supports multiple item types like "Kệ Tivi" and "Tủ Quần Áo".
"""

from typing import List, Dict


class Product:
    """
    Represents a product in the shopping cart.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a Product object.
        :param name: Name of the product (e.g., "Kệ Tivi", "Tủ Quần Áo").
        :param price: Price of the product.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """
    Represents a shopping cart containing Ecoplast products.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.cart: Dict[str, int] = {}  # Key: Product name, Value: Quantity
        self.products: Dict[str, Product] = {}  # Key: Product name, Value: Product object

    def add_product(self, product: Product, quantity: int = 1):
        """
        Adds a product to the shopping cart.
        :param product: The product to add.
        :param quantity: The number of units to add (default is 1).
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if product.name not in self.products:
            self.products[product.name] = product

        if product.name in self.cart:
            self.cart[product.name] += quantity
        else:
            self.cart[product.name] = quantity

    def remove_product(self, product_name: str):
        """
        Removes a product from the shopping cart.
        :param product_name: Name of the product to remove.
        """
        if product_name in self.cart:
            del self.cart[product_name]
        else:
            raise KeyError(f"Product '{product_name}' not found in the cart.")

    def update_quantity(self, product_name: str, quantity: int):
        """
        Updates the quantity of a product in the shopping cart.
        :param product_name: Name of the product to update.
        :param quantity: The new quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if product_name in self.cart:
            self.cart[product_name] = quantity
        else:
            raise KeyError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the shopping cart.
        :return: The total price.
        """
        total = 0.0
        for product_name, quantity in self.cart.items():
            product = self.products.get(product_name)
            if product:
                total += product.price * quantity
        return total

    def list_cart_items(self) -> List[Dict[str, str]]:
        """
        Lists all items in the shopping cart.
        :return: A list of dictionaries representing cart items.
        """
        cart_items = []
        for product_name, quantity in self.cart.items():
            product = self.products.get(product_name)
            if product:
                cart_items.append({
                    "Product Name": product.name,
                    "Price": f"{product.price:.2f}",
                    "Quantity": quantity,
                    "Subtotal": f"{product.price * quantity:.2f}"
                })
        return cart_items


# Example usage
if __name__ == "__main__":
    try:
        # Create some products
        ke_tivi = Product(name="Kệ Tivi", price=200.0)
        tu_quan_ao = Product(name="Tủ Quần Áo", price=500.0)

        # Initialize shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(ke_tivi, 2)
        cart.add_product(tu_quan_ao, 1)

        # List cart items
        print("Cart Items:")
        for item in cart.list_cart_items():
            print(item)

        # Update quantity
        cart.update_quantity("Kệ Tivi", 3)

        # Calculate total
        print(f"\nTotal Price: {cart.calculate_total():.2f}")

        # Remove a product
        cart.remove_product("Tủ Quần Áo")
        print("\nCart Items After Removing 'Tủ Quần Áo':")
        for item in cart.list_cart_items():
            print(item)

    except Exception as e:
        print(f"Error: {e}")
```
