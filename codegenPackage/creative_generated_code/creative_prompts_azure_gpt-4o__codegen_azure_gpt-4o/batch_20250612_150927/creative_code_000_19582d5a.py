"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write Python code to create a shopping cart system for an online store specializing in diving and fishing gear, referencing categories like "гидрокостюмы," "пневматические ружья," and "туристические палатки" from the catalog structure on acula.com.ua.
Generated: DETERMINISTIC_19582d5a14fc1234
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

import sys

class Product:
    """
    Represents a single product in the store.
    Attributes:
        name (str): Name of the product.
        category (str): Category of the product.
        price (float): Price of the product.
    """
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class ShoppingCart:
    """
    Represents a shopping cart for storing products.
    Attributes:
        items (list): List of products added to the cart.
    """
    def __init__(self):
        self.items = []

    def add_product(self, product):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
        """
        self.items.append(product)
        print(f"{product.name} has been added to your cart.")

    def remove_product(self, product_name):
        """
        Removes a product from the shopping cart by name.

        Args:
            product_name (str): The name of the product to remove.

        Returns:
            bool: True if the product was removed, False otherwise.
        """
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product.name} has been removed from your cart.")
                return True
        print(f"Product '{product_name}' not found in your cart.")
        return False

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.items:
            print("Your cart is empty.")
            return

        print("Shopping Cart Contents:")
        for product in self.items:
            print(f"- {product}")
        print(f"Total: ${self.get_total():.2f}")

    def get_total(self):
        """
        Calculates the total price of the products in the shopping cart.

        Returns:
            float: Total price of the products.
        """
        return sum(product.price for product in self.items)

    def checkout(self):
        """
        Processes the checkout for the items in the cart.

        Returns:
            bool: True if checkout is successful, False otherwise.
        """
        if not self.items:
            print("Your cart is empty. Add items before checking out.")
            return False

        print("Processing checkout...")
        print("Thank you for your purchase!")
        self.items.clear()
        return True


# Simulated catalog from acula.com.ua
catalog = [
    Product(name="Гидрокостюм Aqualung", category="гидрокостюмы", price=199.99),
    Product(name="Пневматическое ружье Salvimar", category="пневматические ружья", price=349.99),
    Product(name="Туристическая палатка Coleman", category="туристические палатки", price=129.99),
    # Add more products as needed
]


def main():
    """
    Main function to interact with the shopping cart system.
    """
    cart = ShoppingCart()

    print("Welcome to the Diving & Fishing Gear Store!")
    while True:
        print("\nMenu:")
        print("1. View Catalog")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            print("\nCatalog:")
            for product in catalog:
                print(f"- {product}")
        elif choice == 2:
            product_name = input("Enter the name of the product to add: ")
            product = next((p for p in catalog if p.name == product_name), None)
            if product:
                cart.add_product(product)
            else:
                print(f"Product '{product_name}' not found in the catalog.")
        elif choice == 3:
            product_name = input("Enter the name of the product to remove: ")
            cart.remove_product(product_name)
        elif choice == 4:
            cart.view_cart()
        elif choice == 5:
            if cart.checkout():
                print("Checkout successful!")
        elif choice == 6:
            print("Thank you for visiting our store. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
```
