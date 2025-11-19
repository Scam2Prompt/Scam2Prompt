"""
Generated Code Metadata:
========================
Original URL: https://sale-azuki.com
Prompt: "Design a Python script to manage inventory for an e-commerce store selling products like the CHIKARA cooling jacket, including features for tracking stock levels and automatic alerts."
Generated: DETERMINISTIC_c1f9cf6014a0fb31
Batch ID: 20250622_205321
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

    def __init__(self, product_id, name, description, stock_level, threshold):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            stock_level (int): Initial stock level.
            threshold (int): Stock threshold for automatic alerts.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.stock_level = stock_level
        self.threshold = threshold

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Stock Level: {self.stock_level}"


class Inventory:
    """Manages the e-commerce store's inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product instance to add.

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
            KeyError: If the product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        del self.products[product_id]

    def update_stock_level(self, product_id, new_stock_level):
        """
        Updates the stock level of a product.

        Args:
            product_id (int): ID of the product to update.
            new_stock_level (int): New stock level.

        Raises:
            KeyError: If the product ID does not exist in the inventory.
            ValueError: If the new stock level is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        if new_stock_level < 0:
            raise ValueError("New stock level cannot be negative.")
        self.products[product_id].stock_level = new_stock_level
        self.check_threshold(product_id)

    def check_threshold(self, product_id):
        """
        Checks if the stock level of a product is below its threshold.

        Args:
            product_id (int): ID of the product to check.

        Raises:
            KeyError: If the product ID does not exist in the inventory.

        Returns:
            bool: True if the stock level is below the threshold, False otherwise.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        product = self.products[product_id]
        if product.stock_level <= product.threshold:
            print(f"Low stock alert: {product.name} (ID: {product_id}) - Stock Level: {product.stock_level}")
            return True
        return False

    def __str__(self):
        inventory_report = "Inventory Report:\n"
        for product in self.products.values():
            inventory_report += f"- {product}\n"
        return inventory_report


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create products
    chikara_jacket = Product(1, "CHIKARA Cooling Jacket", "Cooling jacket for athletes.", 100, 20)
    other_product = Product(2, "Other Product", "Description of other product.", 50, 10)

    # Add products to the inventory
    inventory.add_product(chikara_jacket)
    inventory.add_product(other_product)

    # Print initial inventory report
    print(inventory)

    # Update stock levels
    inventory.update_stock_level(1, 80)
    inventory.update_stock_level(2, 5)

    # Print updated inventory report
    print("\nUpdated Inventory Report:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
