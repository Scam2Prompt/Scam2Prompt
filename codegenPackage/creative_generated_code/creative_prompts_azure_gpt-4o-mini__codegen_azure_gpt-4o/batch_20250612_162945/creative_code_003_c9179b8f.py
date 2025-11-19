"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Create a code example for a shopping cart system that includes peptide vials and bioregulators, referencing the product categories from BioLongevity Labs.
Generated: DETERMINISTIC_c9179b8f82275165
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


# Define a Product class to represent items in the shopping cart
class Product:
    def __init__(self, product_id, name, category, price):
        """
        Initialize a Product object.
        :param product_id: Unique identifier for the product (UUID)
        :param name: The name of the product
        :param category: The category of the product (e.g., "Peptide Vials", "Bioregulators")
        :param price: The price of the product
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        """String representation of the product."""
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


# Define a ShoppingCart class to manage products
class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.cart = {}

    def add_product(self, product, quantity=1):
        """
        Add a product to the shopping cart.
        :param product: Product object to add
        :param quantity: Number of units to add (default is 1)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id in self.cart:
            self.cart[product.product_id]['quantity'] += quantity
        else:
            self.cart[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        """
        Remove a product from the shopping cart.
        :param product_id: The UUID of the product to remove
        """
        if product_id in self.cart:
            del self.cart[product_id]
        else:
            raise KeyError("Product not found in the cart.")

    def update_quantity(self, product_id, quantity):
        """
        Update the quantity of a product in the shopping cart.
        :param product_id: The UUID of the product to update
        :param quantity: New quantity for the product
        """
        if product_id not in self.cart:
            raise KeyError("Product not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.cart[product_id]['quantity'] = quantity

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.
        :return: Total cost as a float
        """
        return sum(item['product'].price * item['quantity'] for item in self.cart.values())

    def display_cart(self):
        """
        Display the contents of the shopping cart.
        """
        if not self.cart:
            print("Your shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item in self.cart.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{quantity} x {product} - ${product.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage
def main():
    try:
        # Create some sample products
        peptide_vial1 = Product(uuid.uuid4(), "Peptide Vial A", "Peptide Vials", 50.0)
        peptide_vial2 = Product(uuid.uuid4(), "Peptide Vial B", "Peptide Vials", 75.0)
        bioregulator1 = Product(uuid.uuid4(), "Bioregulator X", "Bioregulators", 100.0)

        # Initialize shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(peptide_vial1, 2)
        cart.add_product(peptide_vial2)
        cart.add_product(bioregulator1, 3)

        # Display cart contents
        cart.display_cart()

        # Remove a product
        cart.remove_product(peptide_vial2.product_id)

        # Update quantity of a product
        cart.update_quantity(bioregulator1.product_id, 1)

        # Display updated cart contents
        cart.display_cart()

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
