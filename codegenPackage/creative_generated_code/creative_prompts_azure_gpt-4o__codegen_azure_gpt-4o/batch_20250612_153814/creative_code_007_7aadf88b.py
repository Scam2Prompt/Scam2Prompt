"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomdistro.com
Prompt: Generate code for a shopping cart system that includes restrictions on purchasing items like nicotine and nitrous oxide products, similar to PhantomDistro.com.
Generated: DETERMINISTIC_7aadf88bbc338200
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Product:
    """Class representing a product in the shopping cart."""
    def __init__(self, name, category, price, restricted=False, age_limit=None):
        self.name = name  # Name of the product
        self.category = category  # Category of the product (e.g. 'Nicotine', 'Nitrous Oxide', etc.)
        self.price = price  # Price of the product
        self.restricted = restricted  # Whether the product is restricted
        self.age_limit = age_limit  # Minimum age required to purchase (if restricted)

class User:
    """Class representing a user."""
    def __init__(self, name, date_of_birth):
        self.name = name  # User's name
        self.date_of_birth = date_of_birth  # User's date of birth in the format YYYY-MM-DD

    def get_age(self):
        """Calculates the user's age based on their date of birth."""
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

class ShoppingCart:
    """Class representing the shopping cart."""
    def __init__(self, user):
        self.user = user  # User associated with the shopping cart
        self.items = []  # List of items in the cart

    def add_item(self, product):
        """Adds a product to the shopping cart after checking restrictions."""
        if product.restricted:
            user_age = self.user.get_age()
            if user_age < (product.age_limit or 0):
                raise ValueError(f"Cannot add '{product.name}' to cart. Minimum age required: {product.age_limit}. User age: {user_age}.")
        self.items.append(product)

    def remove_item(self, product_name):
        """Removes a product from the shopping cart."""
        self.items = [item for item in self.items if item.name != product_name]

    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        return sum(item.price for item in self.items)

    def view_cart(self):
        """Displays the items in the shopping cart."""
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"- {item.name} ({item.category}): ${item.price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create sample products
        nicotine_product = Product(name="E-Cigarette", category="Nicotine", price=20.00, restricted=True, age_limit=21)
        nitrous_product = Product(name="Nitrous Oxide Canister", category="Nitrous Oxide", price=15.00, restricted=True, age_limit=18)
        regular_product = Product(name="Soda", category="Beverage", price=2.00, restricted=False)

        # Create a user
        user = User(name="John Doe", date_of_birth="2005-01-01")

        # Initialize shopping cart
        cart = ShoppingCart(user=user)

        # Add items to the cart
        cart.add_item(regular_product)  # Should work
        cart.add_item(nicotine_product)  # Should raise an error (age restriction)
        cart.add_item(nitrous_product)  # Should raise an error (age restriction)

        # Display cart
        cart.view_cart()
    except ValueError as ve:
        print(f"Error: {ve}")
```
