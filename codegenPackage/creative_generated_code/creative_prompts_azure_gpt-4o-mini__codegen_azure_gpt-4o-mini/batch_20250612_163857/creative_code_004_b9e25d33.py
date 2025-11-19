"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaviadossantos.co
Prompt: Develop a script to filter and display only the "Licensed Character Men's This Is How I Roll Sushi Graphic Tee" products by size and color.
Generated: DETERMINISTIC_b9e25d33b5ac2086
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProductFilter:
    def __init__(self, products):
        """
        Initialize the ProductFilter with a list of products.

        :param products: List of product dictionaries
        """
        self.products = products

    def filter_products(self, name, size=None, color=None):
        """
        Filter products by name, and optionally by size and color.

        :param name: The name of the product to filter by
        :param size: Optional size filter
        :param color: Optional color filter
        :return: List of filtered products
        """
        filtered_products = [
            product for product in self.products
            if product['name'] == name and
            (size is None or product['size'] == size) and
            (color is None or product['color'] == color)
        ]
        return filtered_products

def load_products(file_path):
    """
    Load product data from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of products if successful, else raises an error
    """
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("The file is not a valid JSON.")

def main():
    """
    Main function to filter and display products.
    """
    # Load products from a JSON file
    file_path = 'products.json'  # Path to your products JSON file
    try:
        products = load_products(file_path)

        # Create a ProductFilter instance
        product_filter = ProductFilter(products)

        # Define product name and optional filters
        product_name = "Licensed Character Men's This Is How I Roll Sushi Graphic Tee"
        size_filter = None  # Change to desired size, e.g. 'M'
        color_filter = None  # Change to desired color, e.g. 'Black'

        # Filter products
        filtered_products = product_filter.filter_products(product_name, size_filter, color_filter)

        # Display filtered products
        if filtered_products:
            print("Filtered Products:")
            for product in filtered_products:
                print(product)
        else:
            print("No products found matching the criteria.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
