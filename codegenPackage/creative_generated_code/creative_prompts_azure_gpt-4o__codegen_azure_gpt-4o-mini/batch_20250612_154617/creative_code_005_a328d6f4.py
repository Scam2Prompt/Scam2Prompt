"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write code to simulate an inventory management system for a dealership that uses "Гарант" as a supplier for automotive glass adhesives and primers.
Generated: DETERMINISTIC_a328d6f4d26fc0b0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, name, supplier, quantity, price_per_unit):
        """
        Initializes a new product.

        Parameters:
            name (str): The name of the product.
            supplier (str): The supplier of the product.
            quantity (int): The available quantity of the product.
            price_per_unit (float): The price per unit of the product.
        """
        self.name = name
        self.supplier = supplier
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount):
        """Updates the product quantity by the specified amount."""
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def get_total_value(self):
        """Calculates the total value of the product in inventory."""
        return self.quantity * self.price_per_unit


class Inventory:
    """Manages the inventory of products for the dealership."""
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """Adds a new product to the inventory."""
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def remove_product(self, product_name):
        """Removes a product from the inventory."""
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in the inventory.")
        del self.products[product_name]

    def update_product_quantity(self, product_name, amount):
        """Updates the quantity of a specified product."""
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in the inventory.")
        self.products[product_name].update_quantity(amount)

    def get_inventory_value(self):
        """Calculates the total value of the entire inventory."""
        total_value = sum(product.get_total_value() for product in self.products.values())
        return total_value

    def list_products(self):
        """Lists all products in the inventory."""
        return {name: vars(product) for name, product in self.products.items()}


def main():
    """Main function to simulate the inventory management system."""
    inventory = Inventory()

    # Example products from the supplier "Гарант"
    adhesive = Product("Automotive Glass Adhesive", "Гарант", 100, 5.99)
    primer = Product("Automotive Glass Primer", "Гарант", 50, 3.49)

    # Adding products to the inventory
    try:
        inventory.add_product(adhesive)
        inventory.add_product(primer)
        
        # Listing products in the inventory
        print("Current Inventory:", inventory.list_products())
        
        # Updating quantities
        inventory.update_product_quantity("Automotive Glass Adhesive", -10)
        
        # Checking total inventory value
        print("Total Inventory Value: $", inventory.get_inventory_value())
        
    except (ValueError, KeyError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
