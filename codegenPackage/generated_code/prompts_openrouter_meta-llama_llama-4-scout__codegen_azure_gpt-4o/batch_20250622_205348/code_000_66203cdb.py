"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: "Write a Python code snippet to manage inventory for a meat product company like Holambra Alimentos, including tracking products for consumer and industrial use."
Generated: DETERMINISTIC_66203cdb0f751b3e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid

class Product:
    """
    Represents a product in the inventory.
    """
    def __init__(self, name, category, quantity, price_per_unit):
        """
        Initialize a product with its details.

        :param name: Name of the product
        :param category: Category of the product ('consumer' or 'industrial')
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the product
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __str__(self):
        """
        String representation of the product.
        """
        return f"Product(ID: {self.id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Price/Unit: ${self.price_per_unit:.2f})"


class Inventory:
    """
    Manages the inventory of products.
    """
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        :param product: Product object to be added
        """
        if product.id in self.products:
            raise ValueError("Product with this ID already exists in the inventory.")
        self.products[product.id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        :param product_id: ID of the product to be removed
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        del self.products[product_id]

    def update_product_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product in the inventory.

        :param product_id: ID of the product to be updated
        :param new_quantity: New quantity of the product
        """
        if product_id not in self.products:
            raise ValueError("Product ID not found in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def list_products(self, category=None):
        """
        List all products in the inventory, optionally filtered by category.

        :param category: Category to filter products ('consumer' or 'industrial')
        :return: List of products
        """
        if category:
            return [product for product in self.products.values() if product.category == category]
        return list(self.products.values())

    def __str__(self):
        """
        String representation of the inventory.
        """
        return "\n".join(str(product) for product in self.products.values())


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory
        inventory = Inventory()

        # Add products
        product1 = Product(name="Chicken Breast", category="consumer", quantity=100, price_per_unit=5.99)
        product2 = Product(name="Ground Beef", category="industrial", quantity=500, price_per_unit=3.49)
        inventory.add_product(product1)
        inventory.add_product(product2)

        # List all products
        print("All Products:")
        print(inventory)

        # List consumer products
        print("\nConsumer Products:")
        for product in inventory.list_products(category="consumer"):
            print(product)

        # Update product quantity
        inventory.update_product_quantity(product1.id, 120)

        # Remove a product
        inventory.remove_product(product2.id)

        # List all products after updates
        print("\nUpdated Inventory:")
        print(inventory)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
