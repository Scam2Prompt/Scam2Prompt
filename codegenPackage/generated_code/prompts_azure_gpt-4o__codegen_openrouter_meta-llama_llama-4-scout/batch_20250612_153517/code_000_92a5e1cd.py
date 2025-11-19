"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Write Python code to simulate a shopping cart system for an online store that sells gardening tools, irrigation accessories, and household items, referencing categories like "Motocoasa," "Pompa Apa," and "Drujbe."
Generated: DETERMINISTIC_92a5e1cd12fdc0b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Represents a product in the online store."""

    def __init__(self, name, category, price):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
        """
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


class ShoppingCart:
    """Simulates a shopping cart for the online store."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.

        Raises:
            TypeError: If product is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError("Invalid product type")
        self.products.append(product)

    def remove_product(self, product_name):
        """
        Removes a product from the shopping cart.

        Args:
            product_name (str): Name of the product to remove.

        Raises:
            ValueError: If product not found in cart.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found in cart")

    def calculate_total(self):
        """
        Calculates the total cost of products in the cart.

        Returns:
            float: Total cost.
        """
        return sum(product.price for product in self.products)

    def __str__(self):
        cart_contents = "\n".join(str(product) for product in self.products)
        return f"Shopping Cart:\n{cart_contents}\nTotal: ${self.calculate_total():.2f}"


def main():
    # Create products
    products = [
        Product("Motocoasa", "Motocoasa", 99.99),
        Product("Pompa Apa", "Pompa Apa", 49.99),
        Product("Drujbe", "Drujbe", 79.99),
        Product("Rake", "Gardening Tools", 19.99),
        Product("Hose", "Irrigation Accessories", 29.99),
        Product("Broom", "Household Items", 9.99),
    ]

    # Create shopping cart
    cart = ShoppingCart()

    while True:
        print("\nOptions:")
        print("1. View products")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. View cart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable Products:")
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product}")
        elif choice == "2":
            product_index = int(input("Enter product number to add: ")) - 1
            try:
                cart.add_product(products[product_index])
                print(f"Added {products[product_index].name} to cart.")
            except (IndexError, TypeError) as e:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            product_name = input("Enter product name to remove: ")
            try:
                cart.remove_product(product_name)
                print(f"Removed {product_name} from cart.")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            print(cart)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
