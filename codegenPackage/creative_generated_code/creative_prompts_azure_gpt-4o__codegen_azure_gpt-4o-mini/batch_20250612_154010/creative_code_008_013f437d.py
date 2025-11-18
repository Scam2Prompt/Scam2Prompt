"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgsends.top
Prompt: Create a Python function to filter products by UCI approval status, allowing users to search for items like "UCI Approved Track Wheels."
Generated: DETERMINISTIC_013f437dd30c046d
Batch ID: 20250612_154010
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
    A class to represent a product with a name and its UCI approval status.
    """

    def __init__(self, name: str, uci_approved: bool):
        """
        Initializes a new product instance.

        :param name: The name of the product.
        :param uci_approved: A boolean indicating if the product is UCI approved.
        """
        self.name = name
        self.uci_approved = uci_approved

    def __repr__(self):
        return f"Product(name={self.name}, uci_approved={self.uci_approved})"


def filter_products_by_uci_approval(products: List[Product], search_term: str) -> List[Product]:
    """
    Filters a list of products by their UCI approval status and a search term.

    :param products: A list of Product instances to filter.
    :param search_term: A string to search for in product names.
    :return: A list of UCI approved products matching the search term.
    :raises ValueError: If the products list is empty.
    """
    if not products:
        raise ValueError("The products list is empty.")

    # Convert search term to lower case for case-insensitive matching
    search_term = search_term.lower()

    # Filter products based on UCI approval and the search term
    filtered_products = [
        product for product in products 
        if product.uci_approved and search_term in product.name.lower()
    ]

    return filtered_products


# Example usage
if __name__ == "__main__":
    # Sample product list
    product_list = [
        Product(name="UCI Approved Track Wheels", uci_approved=True),
        Product(name="Non-UCI Approved Track Wheels", uci_approved=False),
        Product(name="UCI Approved Road Tires", uci_approved=True),
        Product(name="Regular Track Wheels", uci_approved=False),
    ]

    try:
        # Filter for UCI approved track wheels
        approved_products = filter_products_by_uci_approval(product_list, "UCI Approved Track Wheels")
        print("Filtered Products:", approved_products)
    except ValueError as e:
        print("Error:", e)
```
