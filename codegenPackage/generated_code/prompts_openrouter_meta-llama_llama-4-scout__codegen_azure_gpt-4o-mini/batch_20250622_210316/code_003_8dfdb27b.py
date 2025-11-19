"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: "Design a product catalog system using a programming language of your choice, inspired by Fotopoint's product categories and subcategories."
Generated: DETERMINISTIC_8dfdb27bfcd73d9e
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a product in the catalog.
    """

    def __init__(self, product_id, name, description, price, category):
        """
        Initializes a new product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param description: Description of the product
        :param price: Price of the product
        :param category: Category of the product
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class Category:
    """
    Represents a category in the product catalog.
    """

    def __init__(self, name):
        """
        Initializes a new category.

        :param name: Name of the category
        """
        self.name = name
        self.subcategories = []
        self.products = []

    def add_subcategory(self, subcategory):
        """
        Adds a subcategory to the category.

        :param subcategory: Subcategory to be added
        """
        self.subcategories.append(subcategory)

    def add_product(self, product):
        """
        Adds a product to the category.

        :param product: Product to be added
        """
        self.products.append(product)

    def __str__(self):
        return f"Category: {self.name}, Products: {len(self.products)}"


class Catalog:
    """
    Represents the product catalog.
    """

    def __init__(self):
        """
        Initializes a new product catalog.
        """
        self.categories = {}

    def add_category(self, category):
        """
        Adds a category to the catalog.

        :param category: Category to be added
        """
        self.categories[category.name] = category

    def get_category(self, category_name):
        """
        Retrieves a category by name.

        :param category_name: Name of the category to retrieve
        :return: Category object or None if not found
        """
        return self.categories.get(category_name)

    def list_products(self):
        """
        Lists all products in the catalog.
        """
        for category in self.categories.values():
            print(f"Category: {category.name}")
            for product in category.products:
                print(f"  - {product}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a catalog
        catalog = Catalog()

        # Create categories
        electronics = Category("Electronics")
        clothing = Category("Clothing")

        # Add categories to the catalog
        catalog.add_category(electronics)
        catalog.add_category(clothing)

        # Create products
        phone = Product(1, "Smartphone", "Latest model smartphone", 699.99, "Electronics")
        laptop = Product(2, "Laptop", "High-performance laptop", 1299.99, "Electronics")
        tshirt = Product(3, "T-Shirt", "Cotton t-shirt", 19.99, "Clothing")

        # Add products to categories
        electronics.add_product(phone)
        electronics.add_product(laptop)
        clothing.add_product(tshirt)

        # List all products in the catalog
        catalog.list_products()

    except Exception as e:
        print(f"An error occurred: {e}")
```
