"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Create a Python script to simulate product SKUs and inventory management for a direct-to-consumer (DTC) brand like skyMD.
Generated: DETERMINISTIC_b679226634467b60
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_sku_inventory.py

class Product:
    """Represents a product with a unique SKU."""

    def __init__(self, sku, name, description, price):
        """
        Initializes a Product instance.

        Args:
        - sku (str): Unique Stock Keeping Unit (SKU) identifier.
        - name (str): Product name.
        - description (str): Product description.
        - price (float): Product price.
        """
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(sku='{self.sku}', name='{self.name}', description='{self.description}', price={self.price})"


class Inventory:
    """Manages product inventory for a DTC brand."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product, quantity):
        """
        Adds a product to the inventory.

        Args:
        - product (Product): Product instance to add.
        - quantity (int): Initial quantity of the product.

        Raises:
        - ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.products[product.sku] = {"product": product, "quantity": quantity}

    def remove_product(self, sku):
        """
        Removes a product from the inventory.

        Args:
        - sku (str): SKU of the product to remove.

        Raises:
        - KeyError: If the product is not found in the inventory.
        """
        if sku not in self.products:
            raise KeyError(f"Product with SKU '{sku}' not found")

        del self.products[sku]

    def update_quantity(self, sku, quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
        - sku (str): SKU of the product to update.
        - quantity (int): New quantity of the product.

        Raises:
        - KeyError: If the product is not found in the inventory.
        - ValueError: If quantity is negative.
        """
        if sku not in self.products:
            raise KeyError(f"Product with SKU '{sku}' not found")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.products[sku]["quantity"] = quantity

    def get_product_info(self, sku):
        """
        Retrieves product information and quantity.

        Args:
        - sku (str): SKU of the product to retrieve.

        Returns:
        - dict: Product information and quantity.

        Raises:
        - KeyError: If the product is not found in the inventory.
        """
        if sku not in self.products:
            raise KeyError(f"Product with SKU '{sku}' not found")

        return {
            "sku": self.products[sku]["product"].sku,
            "name": self.products[sku]["product"].name,
            "description": self.products[sku]["product"].description,
            "price": self.products[sku]["product"].price,
            "quantity": self.products[sku]["quantity"],
        }

    def __repr__(self):
        return f"Inventory(products={list(self.products.keys())})"


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create product instances
    product1 = Product("ABC123", "Product A", "This is product A", 19.99)
    product2 = Product("DEF456", "Product B", "This is product B", 29.99)

    # Add products to the inventory
    inventory.add_product(product1, 100)
    inventory.add_product(product2, 50)

    # Print product information
    print(inventory.get_product_info("ABC123"))
    print(inventory.get_product_info("DEF456"))

    # Update quantity
    inventory.update_quantity("ABC123", 80)
    print(inventory.get_product_info("ABC123"))

    # Remove product
    inventory.remove_product("DEF456")
    try:
        print(inventory.get_product_info("DEF456"))
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()
```
