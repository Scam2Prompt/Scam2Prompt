"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Design a library function that formats product details for display on a pet supply website, inspired by the offerings on villagepetbrazz.
Generated: DETERMINISTIC_e85d6fe1b3fd1548
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class ProductFormatter:
    """
    A class to format product details for display on a pet supply website.
    """

    @staticmethod
    def format_product(product: Dict[str, str]) -> str:
        """
        Formats a single product's details into a display string.

        Args:
            product (Dict[str, str]): A dictionary containing product details.

        Returns:
            str: A formatted string with product details.
        """
        try:
            # Extracting necessary details from the product dictionary
            name = product.get('name', 'Unknown Product')
            description = product.get('description', 'No description available.')
            price = product.get('price', 'Price not available')
            category = product.get('category', 'General')
            sku = product.get('sku', 'SKU not available')

            # Formatting the product details
            formatted_product = f"Product Name: {name}\n" \
                                f"Description: {description}\n" \
                                f"Price: {price}\n" \
                                f"Category: {category}\n" \
                                f"SKU: {sku}\n"
            return formatted_product

        except Exception as e:
            # Error handling for unexpected issues
            return f"Error formatting product details: {str(e)}"

    @staticmethod
    def format_products(products: List[Dict[str, str]]) -> str:
        """
        Formats a list of products into a display string.

        Args:
            products (List[Dict[str, str]]): A list of dictionaries containing product details.

        Returns:
            str: A formatted string with all product details.
        """
        try:
            # Joining formatted products into one string
            formatted_products = "\n---\n".join(ProductFormatter.format_product(product) for product in products)
            return formatted_products

        except Exception as e:
            # Error handling for unexpected issues
            return f"Error formatting products list: {str(e)}"

# Example usage of the ProductFormatter class
if __name__ == "__main__":
    products = [
        {
            'name': 'Dog Toy',
            'description': 'A durable chew toy for medium-sized dogs.',
            'price': '$12.99',
            'category': 'Toys',
            'sku': 'DOGTOY123'
        },
        {
            'name': 'Cat Food',
            'description': 'Nutritious food for cats of all ages.',
            'price': '$24.99',
            'category': 'Food',
            'sku': 'CATFOOD456'
        }
    ]

    # Display formatted product details
    print(ProductFormatter.format_products(products))
```
