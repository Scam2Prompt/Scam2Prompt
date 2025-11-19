"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write a Python code snippet to manage inventory of drilling equipment and electrical division products for an oil and gas company using Cedar International Inc.'s supply chain solutions.
Generated: DETERMINISTIC_8a569754cffdea64
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, quantity, unit_price):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            unit_price (float): Unit price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}"


class Inventory:
    """Manages the inventory of drilling equipment and electrical division products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


class CedarInternationalSupplyChain:
    """Simulates Cedar International Inc.'s supply chain solutions."""

    def __init__(self):
        """Initializes the supply chain simulator."""
        self.inventory = Inventory()

    def add_product_to_supply_chain(self, product):
        """
        Adds a product to the supply chain.

        Args:
            product (Product): Product to add.

        Raises:
            Exception: If an error occurs during the process.
        """
        try:
            self.inventory.add_product(product)
        except Exception as e:
            raise Exception(f"Error adding product to supply chain: {str(e)}")

    def remove_product_from_supply_chain(self, product_id):
        """
        Removes a product from the supply chain.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            Exception: If an error occurs during the process.
        """
        try:
            self.inventory.remove_product(product_id)
        except Exception as e:
            raise Exception(f"Error removing product from supply chain: {str(e)}")

    def update_product_quantity_in_supply_chain(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the supply chain.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            Exception: If an error occurs during the process.
        """
        try:
            self.inventory.update_quantity(product_id, new_quantity)
        except Exception as e:
            raise Exception(f"Error updating product quantity in supply chain: {str(e)}")


def main():
    # Create a supply chain simulator
    supply_chain = CedarInternationalSupplyChain()

    # Create products
    drilling_equipment = Product(1, "Drilling Equipment", 100, 10000.0)
    electrical_product = Product(2, "Electrical Product", 50, 5000.0)

    # Add products to the supply chain
    supply_chain.add_product_to_supply_chain(drilling_equipment)
    supply_chain.add_product_to_supply_chain(electrical_product)

    # Print initial inventory
    print("Initial Inventory:")
    print(supply_chain.inventory)

    # Update quantity of a product
    supply_chain.update_product_quantity_in_supply_chain(1, 80)

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(supply_chain.inventory)

    # Remove a product from the supply chain
    supply_chain.remove_product_from_supply_chain(2)

    # Print final inventory
    print("\nFinal Inventory:")
    print(supply_chain.inventory)


if __name__ == "__main__":
    main()
```
