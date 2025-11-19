"""
Generated Code Metadata:
========================
Original URL: https://khalom.in
Prompt: Generate a code snippet to create a shopping cart feature for an online clothing store, similar to the one described on Khalomclothing, including functions for adding items, viewing the cart, and checking out.
Generated: DETERMINISTIC_f0e0cef4231590dd
Batch ID: 20250612_160720
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
    """Represents a product in the online clothing store."""

    def __init__(self, product_id, name, price):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price


class ShoppingCart:
    """Represents a shopping cart for an online clothing store."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.cart = {}

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add to the cart.
            quantity (int, optional): Quantity of the product to add. Defaults to 1.

        Raises:
            ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.product_id in self.cart:
            self.cart[product.product_id]["quantity"] += quantity
        else:
            self.cart[product.product_id] = {"product": product, "quantity": quantity}

    def view_cart(self):
        """Prints the contents of the shopping cart."""
        if not self.cart:
            print("Your cart is empty.")
            return

        print("Your Shopping Cart:")
        for product_id, item in self.cart.items():
            print(f"{item['product'].name} x {item['quantity']} = ${item['product'].price * item['quantity']:.2f}")

    def checkout(self):
        """Calculates the total cost of the items in the shopping cart."""
        if not self.cart:
            print("Your cart is empty.")
            return

        total_cost = sum(item["product"].price * item["quantity"] for item in self.cart.values())
        print(f"Total: ${total_cost:.2f}")
        self.cart.clear()
        print("Thank you for shopping with us!")


def main():
    # Create some products
    products = [
        Product(1, "T-Shirt", 19.99),
        Product(2, "Jeans", 49.99),
        Product(3, "Hoodie", 29.99),
    ]

    # Create a shopping cart
    cart = ShoppingCart()

    while True:
        print("\n1. View products")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable products:")
            for product in products:
                print(f"{product.product_id}. {product.name} - ${product.price:.2f}")
        elif choice == "2":
            product_id = int(input("Enter the product ID: "))
            quantity = int(input("Enter the quantity: "))
            product = next((p for p in products if p.product_id == product_id), None)
            if product:
                try:
                    cart.add_item(product, quantity)
                except ValueError as e:
                    print(str(e))
            else:
                print("Product not found.")
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            cart.checkout()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
