"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Generate code to simulate the ordering process for stainless steel screws and bolts from APN Hardware, including product selection, quantity input, and order confirmation.
Generated: DETERMINISTIC_2d1dfe8c65d6bca5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class to represent a product in the inventory."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Order:
    """Class to represent an order containing products and quantities."""
    
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        """Add a product to the order with the specified quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def calculate_total(self):
        """Calculate the total cost of the order."""
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total

    def confirm_order(self):
        """Display the order summary and total cost."""
        print("Order Summary:")
        for product, quantity in self.items.items():
            print(f"{product} x {quantity}")
        print(f"Total Cost: ${self.calculate_total():.2f}")


class Inventory:
    """Class to represent the inventory of APN Hardware."""
    
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a product to the inventory."""
        self.products.append(product)

    def display_products(self):
        """Display the available products for selection."""
        print("Available Products:")
        for idx, product in enumerate(self.products):
            print(f"{idx + 1}. {product}")


def main():
    """Main function to simulate the ordering process."""
    # Create inventory and add products
    inventory = Inventory()
    inventory.add_product(Product("Stainless Steel Screw", 0.10))
    inventory.add_product(Product("Stainless Steel Bolt", 0.25))

    # Display products
    inventory.display_products()

    # Create an order object
    order = Order()
    
    # Process user input for product selection and quantity
    try:
        product_index = int(input("Select a product by number: ")) - 1
        quantity = int(input("Enter quantity: "))
        
        if product_index < 0 or product_index >= len(inventory.products):
            raise IndexError("Selected product does not exist.")

        selected_product = inventory.products[product_index]
        order.add_product(selected_product, quantity)

        # Confirm the order
        order.confirm_order()
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except IndexError as ie:
        print(f"Selection Error: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
