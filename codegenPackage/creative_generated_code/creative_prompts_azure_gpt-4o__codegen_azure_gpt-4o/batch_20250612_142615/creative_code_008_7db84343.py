"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Develop a sorting algorithm for products on an online course platform, using keywords like "import_export" and "search."
Generated: DETERMINISTIC_7db8434331694932
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define a Product class to store details of each product
class Product:
    def __init__(self, name, description, tags):
        """
        Initialize a Product object.

        :param name: Name of the product (string)
        :param description: Description of the product (string)
        :param tags: List of tags/keywords associated with the product
        """
        self.name = name
        self.description = description
        self.tags = tags

# Define a sorting function for products based on keywords
def sort_products_by_keywords(products, keywords):
    """
    Sort a list of products based on their relevance to the given keywords.

    :param products: List of Product objects
    :param keywords: List of keywords to prioritize in sorting
    :return: List of Product objects sorted by relevance to keywords
    """
    def relevance_score(product):
        """
        Calculate the relevance score of a product based on the number of matching keywords.

        :param product: A Product object
        :return: Integer score for relevance
        """
        score = 0
        for keyword in keywords:
            # Prioritize matches in tags, followed by description and name
            if keyword.lower() in map(str.lower, product.tags):
                score += 3  # Highest weight for tags
            elif keyword.lower() in product.description.lower():
                score += 2  # Medium weight for description
            elif keyword.lower() in product.name.lower():
                score += 1  # Lowest weight for name
        return score

    # Sort products by relevance score (descending order)
    return sorted(products, key=relevance_score, reverse=True)

# Main function demonstrating sorting functionality
if __name__ == "__main__":
    try:
        # Example product list
        products = [
            Product("Python for Beginners", "Learn the basics of Python programming.", ["python", "beginner"]),
            Product("Advanced Data Analysis", "Master data analysis techniques using Python.", ["data", "analysis", "python"]),
            Product("Web Development Bootcamp", "Build modern web applications with Django and React.", ["web", "django", "react"]),
            Product("Import Export Essentials", "Understand the principles of importing and exporting goods.", ["import_export", "trade"]),
        ]

        # Keywords to prioritize
        keywords = ["import_export", "search", "python"]

        # Sort products based on keywords
        sorted_products = sort_products_by_keywords(products, keywords)

        # Display sorted products
        print("Sorted Products:")
        for product in sorted_products:
            print(f"Name: {product.name}, Description: {product.description}, Tags: {product.tags}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {str(e)}")
```
