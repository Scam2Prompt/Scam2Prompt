"""
Generated Code Metadata:
========================
Original URL: https://lggraphics.com.br
Prompt: Create a product catalog for L&G Graphics' printing services, including sections for banners, posters, and folders.
Generated: DETERMINISTIC_56d702adbbd28170
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Class representing a product in the catalog."""
    
    def __init__(self, name, category, price, description):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param category: str - The category of the product (e.g., Banners, Posters, Folders)
        :param price: float - The price of the product
        :param description: str - A brief description of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.description = description

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category}): ${self.price:.2f} - {self.description}"


class ProductCatalog:
    """Class representing a product catalog for L&G Graphics' printing services."""
    
    def __init__(self):
        """Initialize an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        :param product: Product - The product to add
        :raises ValueError: If the product is not an instance of Product
        """
        if not isinstance(product, Product):
            raise ValueError("Only instances of Product can be added to the catalog.")
        self.products.append(product)

    def get_products_by_category(self, category):
        """
        Retrieve products by category.

        :param category: str - The category to filter products by
        :return: list - A list of products in the specified category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]

    def display_catalog(self):
        """Display all products in the catalog."""
        if not self.products:
            print("The catalog is currently empty.")
            return
        
        print("Product Catalog:")
        for product in self.products:
            print(product)


def main():
    """Main function to demonstrate the product catalog functionality."""
    catalog = ProductCatalog()

    # Adding products to the catalog
    try:
        catalog.add_product(Product("Vinyl Banner", "Banners", 29.99, "Durable vinyl banner for outdoor use."))
        catalog.add_product(Product("Event Poster", "Posters", 19.99, "High-quality poster for events."))
        catalog.add_product(Product("Presentation Folder", "Folders", 15.99, "Customizable presentation folder."))
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Display the entire catalog
    catalog.display_catalog()

    # Display products by category
    print("\nBanners:")
    banners = catalog.get_products_by_category("Banners")
    for banner in banners:
        print(banner)

    print("\nPosters:")
    posters = catalog.get_products_by_category("Posters")
    for poster in posters:
        print(poster)

    print("\nFolders:")
    folders = catalog.get_products_by_category("Folders")
    for folder in folders:
        print(folder)


if __name__ == "__main__":
    main()
```
