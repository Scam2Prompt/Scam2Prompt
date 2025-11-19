"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Create a function that lists all products offered by "Гарант," such as adhesives, primers, and cleaning materials for automotive glass installation, and formats them for display on a website.
Generated: DETERMINISTIC_da44454e85a42637
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# products.py

class Product:
    """Represents a product offered by Гарант."""

    def __init__(self, id, name, description, category):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            category (str): Product category (e.g., adhesives, primers, cleaning materials).
        """
        self.id = id
        self.name = name
        self.description = description
        self.category = category

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', description='{self.description}', category='{self.category}')"


class ProductService:
    """Provides methods for managing products."""

    def __init__(self):
        # Initialize products data (e.g., from a database or API)
        self.products = [
            Product(1, "Adhesive for Automotive Glass", "High-strength adhesive for bonding automotive glass.", "Adhesives"),
            Product(2, "Primer for Glass Preparation", "Primer for preparing glass surfaces for adhesive application.", "Primers"),
            Product(3, "Glass Cleaning Solution", "Effective cleaning solution for automotive glass.", "Cleaning Materials"),
            # Add more products as needed...
        ]

    def get_products(self):
        """
        Retrieves a list of all products.

        Returns:
            list[Product]: List of Product instances.
        """
        return self.products

    def get_products_by_category(self, category):
        """
        Retrieves a list of products by category.

        Args:
            category (str): Product category.

        Returns:
            list[Product]: List of Product instances in the specified category.
        """
        return [product for product in self.products if product.category == category]


def format_products_for_display(products):
    """
    Formats a list of products for display on a website.

    Args:
        products (list[Product]): List of Product instances.

    Returns:
        str: HTML-formatted string listing the products.
    """
    if not products:
        return "<p>No products available.</p>"

    product_list_html = "<ul>"
    for product in products:
        product_list_html += f"""
        <li>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Category: {product.category}</p>
        </li>
        """
    product_list_html += "</ul>"
    return product_list_html


def main():
    try:
        product_service = ProductService()
        all_products = product_service.get_products()
        adhesives = product_service.get_products_by_category("Adhesives")

        # Display all products
        print("All Products:")
        print(format_products_for_display(all_products))

        # Display adhesives
        print("\nAdhesives:")
        print(format_products_for_display(adhesives))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
