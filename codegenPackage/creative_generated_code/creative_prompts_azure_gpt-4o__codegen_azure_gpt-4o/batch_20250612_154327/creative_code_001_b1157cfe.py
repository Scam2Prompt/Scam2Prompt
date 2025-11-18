"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Generate code to create a product catalog for automotive accessories, including sound systems, dashboard mats, and decorative stickers, using the examples provided on paxosrew.com.
Generated: DETERMINISTIC_b1157cfe7afeb4e6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProductCatalog:
    """
    Class to manage a product catalog for automotive accessories.
    Includes sound systems, dashboard mats, and decorative stickers.
    """

    def __init__(self):
        # Initialize the catalog as an empty dictionary
        self.catalog = {}

    def add_product(self, category, product_id, name, price, description):
        """
        Add a product to the catalog.
        
        :param category: Category of the product (e.g., 'Sound Systems', 'Dashboard Mats', 'Decorative Stickers')
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param description: Description of the product
        """
        if category not in self.catalog:
            # Create a new category if it doesn't exist
            self.catalog[category] = {}

        if product_id in self.catalog[category]:
            raise ValueError(f"Product ID {product_id} already exists in category '{category}'.")

        # Add the product to the specified category
        self.catalog[category][product_id] = {
            "name": name,
            "price": price,
            "description": description
        }

    def remove_product(self, category, product_id):
        """
        Remove a product from the catalog.

        :param category: Category of the product
        :param product_id: Unique identifier of the product
        """
        if category not in self.catalog or product_id not in self.catalog[category]:
            raise KeyError(f"Product ID {product_id} not found in category '{category}'.")

        # Remove the product
        del self.catalog[category][product_id]

    def list_products(self, category=None):
        """
        List all products in the catalog or within a specific category.

        :param category: Category name to filter products (optional)
        :return: Dictionary of products
        """
        if category:
            if category not in self.catalog:
                raise KeyError(f"Category '{category}' not found.")
            return self.catalog[category]

        # Return all products across all categories
        return self.catalog

    def save_to_file(self, file_path):
        """
        Save the catalog to a JSON file.

        :param file_path: Path to the file where the catalog will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.catalog, file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while saving to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the catalog from a JSON file.

        :param file_path: Path to the file containing the catalog
        """
        try:
            with open(file_path, 'r') as file:
                self.catalog = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"An error occurred while loading from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a catalog instance
    catalog = ProductCatalog()

    try:
        # Add products
        catalog.add_product(
            category="Sound Systems",
            product_id="SS123",
            name="Premium Audio System",
            price=499.99,
            description="High-quality sound system with surround sound."
        )
        catalog.add_product(
            category="Dashboard Mats",
            product_id="DM456",
            name="Anti-Slip Dashboard Mat",
            price=29.99,
            description="Durable and anti-slip mat for your dashboard."
        )
        catalog.add_product(
            category="Decorative Stickers",
            product_id="DS789",
            name="Flame Decal Sticker",
            price=14.99,
            description="Stylish flame design stickers for car exteriors."
        )

        # List products in a category
        print("Sound Systems:", catalog.list_products("Sound Systems"))

        # List all products
        print("All Products:", catalog.list_products())

        # Save catalog to a file
        catalog.save_to_file("catalog.json")

        # Load catalog from a file
        catalog.load_from_file("catalog.json")
        print("Loaded Catalog:", catalog.list_products())

    except Exception as e:
        print(f"Error: {e}")
```
