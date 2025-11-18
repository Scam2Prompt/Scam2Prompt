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
from typing import List, Dict

class Product:
    """
    A class to represent a product in an online course platform.
    
    Attributes
    ----------
    id : int
        Unique identifier for the product.
    name : str
        Name of the product.
    keywords : List[str]
        Keywords associated with the product for search and sorting purposes.
    """

    def __init__(self, id: int, name: str, keywords: List[str]):
        self.id = id
        self.name = name
        self.keywords = keywords

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', keywords={self.keywords})"


def sort_products(products: List[Product], keyword: str) -> List[Product]:
    """
    Sorts the given list of products based on the presence of a keyword.

    Parameters
    ----------
    products : List[Product]
        The list of products to be sorted.
    keyword : str
        The keyword to search and sort products by.

    Returns
    -------
    List[Product]
        A list of products sorted based on keyword presence.
    
    Raises
    ------
    ValueError
        If the keyword is an empty string.
    """

    if not keyword:
        raise ValueError("Keyword must not be an empty string.")

    # Sort products based on whether the keyword is in their keywords list
    sorted_products = sorted(
        products,
        key=lambda product: keyword in product.keywords,
        reverse=True
    )

    return sorted_products


def main():
    # Example product list
    products = [
        Product(1, "Python Course", ["import_export", "programming", "python"]),
        Product(2, "Data Science with R", ["data", "science", "r"]),
        Product(3, "JavaScript Basics", ["web", "development", "javascript"]),
        Product(4, "Advanced Python", ["import_export", "advanced", "python"]),
        Product(5, "HTML & CSS", ["web", "design"]),
    ]

    keyword = "import_export"
    
    try:
        # Sort products by the specified keyword
        sorted_products = sort_products(products, keyword)
        print("Sorted Products:")
        for product in sorted_products:
            print(product)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
