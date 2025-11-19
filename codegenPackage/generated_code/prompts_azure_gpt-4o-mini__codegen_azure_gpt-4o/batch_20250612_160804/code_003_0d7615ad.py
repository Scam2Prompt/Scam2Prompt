"""
Generated Code Metadata:
========================
Original URL: https://demo-8g2.pages.dev
Prompt: Develop a script that sorts products by price and popularity, mimicking the sorting functionality found on the T-Shirt Store's product listing page.
Generated: DETERMINISTIC_0d7615ad4fd902de
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import operator

def sort_products(products, sort_by="price", order="asc"):
    """
    Sorts a list of products by price or popularity.

    Args:
        products (list): A list of dictionaries where each dictionary represents a product.
                         Each product should have 'price' and 'popularity' keys.
        sort_by (str): The attribute to sort by. Options are 'price' or 'popularity'.
        order (str): The sort order. Options are 'asc' for ascending or 'desc' for descending.

    Returns:
        list: A sorted list of products.
    """
    # Validate input
    if sort_by not in ["price", "popularity"]:
        raise ValueError("Invalid sort_by value. Must be 'price' or 'popularity'.")
    if order not in ["asc", "desc"]:
        raise ValueError("Invalid order value. Must be 'asc' or 'desc'.")

    # Determine the sort order
    reverse = True if order == "desc" else False

    # Sort the products
    try:
        sorted_products = sorted(products, key=operator.itemgetter(sort_by), reverse=reverse)
    except KeyError as e:
        raise KeyError(f"Missing key in product data: {e}")
    except TypeError as e:
        raise TypeError(f"Invalid data type encountered: {e}")

    return sorted_products


# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        {"name": "T-Shirt A", "price": 19.99, "popularity": 85},
        {"name": "T-Shirt B", "price": 25.99, "popularity": 90},
        {"name": "T-Shirt C", "price": 15.99, "popularity": 75},
        {"name": "T-Shirt D", "price": 22.99, "popularity": 80},
    ]

    # Sort by price in ascending order
    print("Sorted by price (asc):")
    print(sort_products(products, sort_by="price", order="asc"))

    # Sort by popularity in descending order
    print("\nSorted by popularity (desc):")
    print(sort_products(products, sort_by="popularity", order="desc"))
```
