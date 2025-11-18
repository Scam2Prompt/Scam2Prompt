"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Write a Python script to simulate a shopping cart system for surgical instruments, referencing product categories like "Bone Rongeurs," "Autopsy Knives," and "Resection Knives" from the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_e346c2db8c3d8ce0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart System for Surgical Instruments

This script simulates a shopping cart system for surgical instruments, 
categorizing products into 'Bone Rongeurs,' 'Autopsy Knives,' and 'Resection Knives.'
"""

# Import necessary modules
import sys

class Product:
    """
    Represents a surgical instrument available for purchase.
    """
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.category} - ${self.price:.2f}"

class ShoppingCart:
    """
    Represents a shopping cart containing selected products.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product):
        """
        Adds a product to the shopping cart.
        """
        self.items.append(product)
        print(f"{product.name} added to the cart.")

    def remove_item(self, product_name):
        """
        Removes a product from the shopping cart by name.
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from the cart.")
                return
        print(f"Product '{product_name}' not found in the cart.")

    def view_cart(self):
        """
        Displays the items currently in the cart.
        """
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item in self.items:
                print(item)

    def calculate_total(self):
        """
        Calculates the total price of products in the cart.
        """
        return sum(item.price for item in self.items)

def main():
    """
    Main function to simulate the shopping cart system.
    """
    # Sample surgical instruments
    products = [
        Product("Premium Bone Rongeur", "Bone Rongeurs", 120.50),
        Product("Standard Bone Rongeur", "Bone Rongeurs", 80.00),
        Product("Professional Autopsy Knife", "Autopsy Knives", 65.75),
        Product("Basic Autopsy Knife", "Autopsy Knives", 40.20),
        Product("Titanium Resection Knife", "Resection Knives", 150.90),
        Product("Stainless Steel Resection Knife", "Resection Knives", 95.30),
    ]

    # Initialize shopping cart
    cart = ShoppingCart()

    # Display available products
    print("Welcome to the Surgical Instruments Store!")
    print("Available Products:")
    for product in products:
        print(product)

    # User interaction loop
    while True:
        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Calculate total")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                # Add item to cart
                product_name = input("Enter the name of the product to add: ")
                found = next((p for p in products if p.name == product_name), None)
                if found:
                    cart.add_item(found)
                else:
                    print("Product not found. Please check the name and try again.")

            elif choice == "2":
                # Remove item from cart
                product_name = input("Enter the name of the product to remove: ")
                cart.remove_item(product_name)

            elif choice == "3":
                # View cart
                cart.view_cart()

            elif choice == "4":
                # Calculate total price
                total = cart.calculate_total()
                print(f"Total Price: ${total:.2f}")

            elif choice == "5":
                # Exit application
                print("Thank you for shopping with us!")
                sys.exit()

            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

# Run the application
if __name__ == "__main__":
    main()
```
