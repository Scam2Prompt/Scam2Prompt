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
# Shopping Cart System for Replica Wrestling Championship Belts

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, id, name, price, category):
        """
        Initialize a new product.

        :param id: Unique identifier for the product.
        :param name: Name of the product.
        :param price: Price of the product.
        :param category: Category of the product (e.g., AEW, WWE, MLB).
        """
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} (${self.price:.2f}) - Category: {self.category}"


class ShoppingCart:
    """Represents a shopping cart that holds products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_product(self, product):
        """
        Add a product to the cart.

        :param product: Product instance to be added to the cart.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_product(self, product_id):
        """
        Remove a product from the cart by its ID.

        :param product_id: Unique identifier of the product to be removed.
        :raises ValueError: If the product ID does not exist in the cart.
        """
        for product in self.items:
            if product.id == product_id:
                self.items.remove(product)
                print(f"Removed {product.name} from the cart.")
                return
        raise ValueError("Product not found in the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("Shopping Cart Contents:")
        for product in self.items:
            print(f"- {product}")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        total = sum(product.price for product in self.items)
        print(f"Total Amount: ${total:.2f}")
        return total

# Example usage
def main():
    """Main function to demonstrate the shopping cart functionality."""
    # Create some products
    belt1 = Product(1, "AEW World Championship Belt", 299.99, "AEW Belts")
    belt2 = Product(2, "WWE Universal Championship Belt", 349.99, "WWE Belts")
    belt3 = Product(3, "MLB World Series Title Belt", 249.99, "MLB Title Belts")

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to cart
    try:
        cart.add_product(belt1)
        cart.add_product(belt2)
        cart.add_product(belt3)

        # View cart
        cart.view_cart()

        # Calculate total
        cart.calculate_total()

        # Remove a product
        cart.remove_product(2)  # Remove the WWE belt
        cart.view_cart()
        cart.calculate_total()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
