"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Provide a Python library recommendation for managing product categories and inventory in an e-commerce platform, specifically for items like customized gifts and home decor.
Generated: DETERMINISTIC_829f07ecb5259754
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
inventory_manager.py

This module provides a class that manages product categories and inventory
for an e-commerce platform focused on customized gifts and home decor.
"""

class InventoryManager:
    def __init__(self):
        # Initialize an empty dictionary to store categories and their products
        self.categories = {}

    def add_category(self, category_name):
        """Add a new product category if it doesn't already exist."""
        if category_name in self.categories:
            raise ValueError(f"Category '{category_name}' already exists.")
        self.categories[category_name] = []
        print(f"Category '{category_name}' added successfully.")

    def remove_category(self, category_name):
        """Remove a category and all its products."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        del self.categories[category_name]
        print(f"Category '{category_name}' removed successfully.")

    def add_product(self, category_name, product):
        """Add a new product to a specified category."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        self.categories[category_name].append(product)
        print(f"Product '{product}' added to category '{category_name}'.")

    def remove_product(self, category_name, product):
        """Remove a product from a specified category."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        try:
            self.categories[category_name].remove(product)
            print(f"Product '{product}' removed from category '{category_name}'.")
        except ValueError:
            raise ValueError(f"Product '{product}' not found in category '{category_name}'.")

    def list_categories(self):
        """Return a list of all product categories."""
        return list(self.categories.keys())

    def list_products(self, category_name):
        """Return a list of products in the specified category."""
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")
        return self.categories[category_name]

if __name__ == "__main__":
    # Example usage
    try:
        inventory = InventoryManager()
        inventory.add_category("Customized Gifts")
        inventory.add_category("Home Decor")
        inventory.add_product("Customized Gifts", "Personalized Mug")
        inventory.add_product("Home Decor", "Wall Art")
        print(inventory.list_categories())
        print(inventory.list_products("Customized Gifts"))
        inventory.remove_product("Home Decor", "Wall Art")
        inventory.remove_category("Customized Gifts")
    except Exception as e:
        print(f"Error: {e}")
```
