"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Generate a Python script to create an online ordering system for sweets and bakery products similar to those offered by Govind Sweets, including categories like Mava Mithai and Namkeen.
Generated: DETERMINISTIC_6e990229ffc86a61
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define classes for the Online Ordering System
class Product:
    """
    Represents a product in the catalog.
    Each product has a name, category, price, and stock.
    """
    def __init__(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} | Category: {self.category} | Price: ₹{self.price} | Stock: {self.stock}"


class Catalog:
    """
    Represents the catalog of products.
    Provides methods to display and search for products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\nAvailable Products:")
        print("-" * 50)
        for product in self.products:
            print(product)

    def get_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


class Order:
    """
    Represents a customer's order.
    Tracks items in the order and calculates total cost.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
        else:
            print(f"Insufficient stock for {product.name}. Available: {product.stock}.")

    def display_order_summary(self):
        print("\nOrder Summary:")
        print("-" * 50)
        total_cost = 0
        for product, quantity in self.items:
            cost = product.price * quantity
            total_cost += cost
            print(f"{product.name} | Quantity: {quantity} | Price: ₹{cost}")
        print(f"\nTotal Cost: ₹{total_cost}")


# Error handling for user input
def safe_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")


# Main function to simulate the online ordering system
def main():
    print("Welcome to Govind Sweets Online Ordering System!")
    catalog = Catalog()

    # Pre-defined products in the catalog
    catalog.add_product(Product("Kaju Katli", "Mava Mithai", 450, 10))
    catalog.add_product(Product("Rasgulla", "Mava Mithai", 300, 15))
    catalog.add_product(Product("Bhujia", "Namkeen", 150, 20))
    catalog.add_product(Product("Moong Dal", "Namkeen", 180, 25))

    order = Order()

    while True:
        print("\nMenu:")
        print("1. View Products")
        print("2. Place Order")
        print("3. View Order Summary")
        print("4. Exit")

        choice = safe_input("Choose an option: ")
        if choice == 1:
            catalog.display_products()
        elif choice == 2:
            catalog.display_products()
            product_name = input("\nEnter the name of the product you want to order: ").strip()
            product = catalog.get_product_by_name(product_name)

            if product:
                quantity = safe_input(f"Enter quantity for {product.name} (Available: {product.stock}): ")
                if quantity > 0:
                    order.add_item(product, quantity)
                else:
                    print("Quantity must be greater than zero.")
            else:
                print("Product not found. Please try again.")
        elif choice == 3:
            order.display_order_summary()
        elif choice == 4:
            print("Thank you for using Govind Sweets Online Ordering System!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
