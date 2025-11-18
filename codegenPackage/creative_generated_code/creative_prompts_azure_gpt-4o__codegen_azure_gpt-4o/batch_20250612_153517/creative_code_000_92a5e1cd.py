"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Write Python code to simulate a shopping cart system for an online store that sells gardening tools, irrigation accessories, and household items, referencing categories like "Motocoasa," "Pompa Apa," and "Drujbe."
Generated: DETERMINISTIC_92a5e1cd12fdc0b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart System for an Online Store
Categories: Gardening Tools, Irrigation Accessories, Household Items
    - Gardening Tools: "Motocoasa" (brush cutter)
    - Irrigation Accessories: "Pompa Apa" (water pump)
    - Household Items: "Drujbe" (chainsaw)
"""

class Product:
    """
    Class to represent a product in the store.
    Attributes:
        name (str): Name of the product.
        category (str): Category of the product.
        price (float): Price of the product.
    """
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class ShoppingCart:
    """
    Class to represent the shopping cart system.
    Attributes:
        items (list): List of products added to the cart.
    Methods:
        add_to_cart(product): Add a product to the cart.
        remove_from_cart(product_name): Remove a product from the cart by name.
        calculate_total(): Calculate the total price of items in the cart.
        display_cart(): Display all items in the cart.
    """
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        """
        Add a product to the cart.
        Args:
            product (Product): The product to be added.
        """
        self.items.append(product)
        print(f'Added "{product.name}" to your cart.')

    def remove_from_cart(self, product_name):
        """
        Remove a product from the cart by name.
        Args:
            product_name (str): Name of the product to remove.
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f'Removed "{product_name}" from your cart.')
                return
        print(f'Product "{product_name}" not found in the cart.')

    def calculate_total(self):
        """
        Calculate the total price of items in the cart.
        Returns:
            float: Total price of all items.
        """
        return sum(item.price for item in self.items)

    def display_cart(self):
        """
        Display all items in the cart.
        """
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(f"- {item.name} ({item.category}) - ${item.price:.2f}")
            print(f"Total: ${self.calculate_total():.2f}")

def main():
    """
    Main function to simulate the shopping cart system.
    """
    # Sample products in the store
    products = [
        Product("Motocoasa GX45", "Gardening Tools", 150.00),
        Product("Pompa Apa PX90", "Irrigation Accessories", 75.50),
        Product("Drujbe XT200", "Household Items", 200.00),
    ]

    # Initialize a shopping cart
    cart = ShoppingCart()

    # Simulate adding products to the cart
    cart.add_to_cart(products[0])  # Add Motocoasa
    cart.add_to_cart(products[1])  # Add Pompa Apa
    
    # Display the cart contents
    cart.display_cart()

    # Simulate removing a product
    cart.remove_from_cart("Pompa Apa")
    
    # Display the cart contents again
    cart.display_cart()

    # Simulate adding another product
    cart.add_to_cart(products[2])  # Add Drujbe
    
    # Display final cart contents
    cart.display_cart()

# Run the program
if __name__ == "__main__":
    main()
```
