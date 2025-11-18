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
Library Name: ecommerce_inventory_manager

This Python library helps manage product categories and inventory for an e-commerce platform,
specifically targeting items like customized gifts and home decor.

Features:
- Add, update, and remove product categories
- Add, update, and remove products
- Track inventory levels
- Search products by category or keyword
"""

import logging

# Configure logging for the library
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class CategoryNotFoundError(Exception):
    """Custom exception for handling category-related errors."""
    pass

class ProductNotFoundError(Exception):
    """Custom exception for handling product-related errors."""
    pass


class EcommerceInventoryManager:
    def __init__(self):
        """
        Initializes the inventory manager with empty categories and products.
        """
        self.categories = {}  # Dictionary to store categories and associated products
        self.products = {}    # Dictionary to store product details
        logging.info("Inventory manager initialized.")

    def add_category(self, category_name):
        """
        Adds a new category to the inventory.

        :param category_name: Name of the category to be added
        """
        if category_name in self.categories:
            logging.warning(f"Category '{category_name}' already exists.")
        else:
            self.categories[category_name] = []
            logging.info(f"Category '{category_name}' added successfully.")

    def remove_category(self, category_name):
        """
        Removes a category from the inventory.

        :param category_name: Name of the category to be removed
        :raises CategoryNotFoundError: If the category does not exist
        """
        if category_name not in self.categories:
            raise CategoryNotFoundError(f"Category '{category_name}' does not exist.")
        del self.categories[category_name]
        logging.info(f"Category '{category_name}' removed successfully.")

    def add_product(self, product_id, product_name, category_name, stock_quantity):
        """
        Adds a new product to the inventory.

        :param product_id: Unique identifier for the product
        :param product_name: Name of the product
        :param category_name: Category under which the product falls
        :param stock_quantity: Initial stock quantity for the product
        :raises CategoryNotFoundError: If the category does not exist
        """
        if category_name not in self.categories:
            raise CategoryNotFoundError(f"Category '{category_name}' does not exist.")
        self.products[product_id] = {
            "name": product_name,
            "category": category_name,
            "stock": stock_quantity,
        }
        self.categories[category_name].append(product_id)
        logging.info(f"Product '{product_name}' added successfully under category '{category_name}'.")

    def update_stock(self, product_id, new_stock_quantity):
        """
        Updates the inventory stock level for a given product.

        :param product_id: Unique identifier for the product
        :param new_stock_quantity: New stock quantity to be updated
        :raises ProductNotFoundError: If the product does not exist
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with ID '{product_id}' does not exist.")
        self.products[product_id]["stock"] = new_stock_quantity
        logging.info(f"Stock for product ID '{product_id}' updated to {new_stock_quantity}.")

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        :param product_id: Unique identifier for the product to be removed
        :raises ProductNotFoundError: If the product does not exist
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with ID '{product_id}' does not exist.")
        category_name = self.products[product_id]["category"]
        self.categories[category_name].remove(product_id)
        del self.products[product_id]
        logging.info(f"Product with ID '{product_id}' removed successfully.")

    def search_products_by_category(self, category_name):
        """
        Searches and retrieves all products under a specific category.

        :param category_name: Name of the category to search
        :raises CategoryNotFoundError: If the category does not exist
        :return: List of products under the specified category
        """
        if category_name not in self.categories:
            raise CategoryNotFoundError(f"Category '{category_name}' does not exist.")
        products_in_category = [
            self.products[product_id]
            for product_id in self.categories[category_name]
        ]
        logging.info(f"Found {len(products_in_category)} products in category '{category_name}'.")
        return products_in_category

    def search_products_by_keyword(self, keyword):
        """
        Searches and retrieves products based on a keyword.

        :param keyword: Keyword to search in product names
        :return: List of products matching the keyword
        """
        matching_products = [
            product for product in self.products.values()
            if keyword.lower() in product["name"].lower()
        ]
        logging.info(f"Found {len(matching_products)} products matching keyword '{keyword}'.")
        return matching_products


if __name__ == "__main__":
    # Example usage
    inventory_manager = EcommerceInventoryManager()

    # Adding categories
    inventory_manager.add_category("Customized Gifts")
    inventory_manager.add_category("Home Decor")

    # Adding products
    inventory_manager.add_product(product_id=1, product_name="Personalized Mug", category_name="Customized Gifts", stock_quantity=100)
    inventory_manager.add_product(product_id=2, product_name="Wall Art Decor", category_name="Home Decor", stock_quantity=50)

    # Searching products
    customized_gifts = inventory_manager.search_products_by_category("Customized Gifts")
    decor_items = inventory_manager.search_products_by_keyword("Decor")

    # Updating stock
    inventory_manager.update_stock(product_id=1, new_stock_quantity=120)

    # Removing products and categories
    inventory_manager.remove_product(product_id=2)
    inventory_manager.remove_category("Home Decor")
```
