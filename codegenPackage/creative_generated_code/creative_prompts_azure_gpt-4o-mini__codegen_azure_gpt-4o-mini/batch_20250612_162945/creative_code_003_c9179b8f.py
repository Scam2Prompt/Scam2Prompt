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
# shopping_cart.py

class Product:
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, name, price, category):
        """
        Initializes a new product with the given name, price, and category.

        :param name: str - the name of the product
        :param price: float - the price of the product
        :param category: str - the category of the product
        """
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class ShoppingCart:
    """Class to represent a shopping cart containing products."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """
        Adds a product to the shopping cart.

        :param product: Product - the product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product):
        """
        Removes a product from the shopping cart.

        :param product: Product - the product to remove
        :raises ValueError: If the product is not in the cart
        """
        try:
            self.items.remove(product)
        except ValueError:
            print("Product not found in the cart.")

    def calculate_total(self):
        """
        Calculates the total price of the products in the cart.

        :return: float - the total price
        """
        return sum(item.price for item in self.items)

    def display_cart(self):
        """Displays the items in the shopping cart."""
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart Items:")
            for item in self.items:
                print(f"- {item}")

# Example usage
if __name__ == "__main__":
    # Sample products from BioLongevity Labs
    peptide_vial = Product("Peptide Vial A", 29.99, "Peptides")
    bioregulator = Product("Bioregulator B", 49.99, "Bioregulators")

    # Create a shopping cart instance
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(peptide_vial)
    cart.add_product(bioregulator)

    # Display the cart items
    cart.display_cart()

    # Calculate and print the total cost
    total_cost = cart.calculate_total()
    print(f"Total cost: ${total_cost:.2f}")

    # Remove a product and display the cart again
    cart.remove_product(peptide_vial)
    cart.display_cart()
```
