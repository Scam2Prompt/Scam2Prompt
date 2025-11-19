"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Generate code to simulate the ordering process for stainless steel screws and bolts from APN Hardware, including product selection, quantity input, and order confirmation.
Generated: DETERMINISTIC_2d1dfe8c65d6bca5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Order:
    """Class to represent an order of products."""
    
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        """Add a product and its quantity to the order."""
        self.items.append((product, quantity))

    def total_cost(self):
        """Calculate the total cost of the order."""
        return sum(product.price * quantity for product, quantity in self.items)

    def confirm_order(self):
        """Display the order summary and total cost."""
        print("\nOrder Summary:")
        for product, quantity in self.items:
            print(f"{quantity} x {product}")
        print(f"Total Cost: ${self.total_cost():.2f}")


class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a product to the inventory."""
        self.products.append(product)

    def display_products(self):
        """Display all available products."""
        print("Available Products:")
        for index, product in enumerate(self.products):
            print(f"{index + 1}. {product}")


def main():
    """Main function to simulate the ordering process."""
    # Initialize inventory and add products
    inventory = Inventory()
    inventory.add_product(Product("Stainless Steel Screw", 0.10))
    inventory.add_product(Product("Stainless Steel Bolt", 0.15))

    # Display available products
    inventory.display_products()

    order = Order()

    while True:
        try:
            # User selects a product
            product_choice = int(input("Select a product by number (or 0 to finish): ")) - 1
            
            if product_choice == -1:
                break  # Exit the loop if the user is done

            if product_choice < 0 or product_choice >= len(inventory.products):
                print("Invalid selection. Please try again.")
                continue

            # User inputs quantity
            quantity = int(input(f"Enter quantity for {inventory.products[product_choice].name}: "))
            if quantity <= 0:
                print("Quantity must be a positive integer. Please try again.")
                continue

            # Add selected product and quantity to the order
            order.add_item(inventory.products[product_choice], quantity)

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Confirm the order
    order.confirm_order()


if __name__ == "__main__":
    main()
```
