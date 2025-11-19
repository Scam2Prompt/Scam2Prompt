"""
Generated Code Metadata:
========================
Original URL: https://bijenwasdoek.nl
Prompt: Illustrate how to implement a shopping cart feature for an e-commerce site selling beeswax wraps, highlighting the zero-waste lifestyle aspect.
Generated: DETERMINISTIC_0bd893d9320f76a2
Batch ID: 20250612_161441
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
    """Represents a product in the e-commerce site."""

    def __init__(self, id, name, description, price, eco_benefit):
        """
        Initializes a Product.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            eco_benefit (str): Environmental benefit of the product.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.eco_benefit = eco_benefit

class ShoppingCart:
    """Represents a shopping cart for the e-commerce site."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, product, quantity):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int): Quantity of the product to add.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.items:
            self.items[product.id]["quantity"] += quantity
        else:
            self.items[product.id] = {"product": product, "quantity": quantity}

    def remove_item(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product is not in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        del self.items[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product is not in the cart.
            ValueError: If quantity is less than 1.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product_id]["quantity"] = quantity

    def calculate_total(self):
        """
        Calculates the total cost of the items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total

    def view_cart(self):
        """Prints the contents of the shopping cart."""
        print("Your Shopping Cart:")
        for item in self.items.values():
            print(f"{item['product'].name} x {item['quantity']} - ${item['product'].price * item['quantity']:.2f}")
            print(f"  Eco-benefit: {item['product'].eco_benefit}")
        print(f"Total: ${self.calculate_total():.2f}")

def main():
    # Create products
    wrap_small = Product(1, "Small Beeswax Wrap", "Perfect for snacks", 9.99, "Reusable and biodegradable")
    wrap_medium = Product(2, "Medium Beeswax Wrap", "Great for covering bowls", 12.99, "Reusable and biodegradable")
    wrap_large = Product(3, "Large Beeswax Wrap", "Ideal for wrapping leftovers", 14.99, "Reusable and biodegradable")

    # Create shopping cart
    cart = ShoppingCart()

    while True:
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Update quantity")
        print("4. View cart")
        print("5. Checkout")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\n1. Small Beeswax Wrap")
            print("2. Medium Beeswax Wrap")
            print("3. Large Beeswax Wrap")

            product_choice = input("Choose a product: ")

            if product_choice == "1":
                product = wrap_small
            elif product_choice == "2":
                product = wrap_medium
            elif product_choice == "3":
                product = wrap_large
            else:
                print("Invalid choice")
                continue

            quantity = int(input("Enter quantity: "))
            cart.add_item(product, quantity)
        elif choice == "2":
            product_id = int(input("Enter product ID: "))
            try:
                cart.remove_item(product_id)
            except KeyError as e:
                print(str(e))
        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter new quantity: "))
            try:
                cart.update_quantity(product_id, quantity)
            except (KeyError, ValueError) as e:
                print(str(e))
        elif choice == "4":
            cart.view_cart()
        elif choice == "5":
            cart.view_cart()
            print("Thank you for choosing a zero-waste lifestyle!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```
