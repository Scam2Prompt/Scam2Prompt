"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Develop a script that sorts products by price and popularity, mimicking the sorting functionality found on the T-Shirt Store's product listing page.
Generated: DETERMINISTIC_0d7615ad4fd902de
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Product:
    """A class to represent a product in the store."""

    def __init__(self, name: str, price: float, popularity: int):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, popularity={self.popularity})"


def load_products(file_path: str) -> List[Product]:
    """Load products from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing product data.

    Returns:
        List[Product]: A list of products.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(**product) for product in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError("Error: The file content is not valid JSON.") from e


def sort_products(products: List[Product], sort_by: str = 'price', ascending: bool = True) -> List[Product]:
    """Sort the list of products by specified criteria.

    Args:
        products (List[Product]): The list of products to sort.
        sort_by (str): The criteria to sort by ('price' or 'popularity').
        ascending (bool): If True, sort in ascending order; otherwise, sort in descending order.

    Returns:
        List[Product]: The sorted list of products.

    Raises:
        ValueError: If an invalid sorting criteria is provided.
    """
    if sort_by not in ['price', 'popularity']:
        raise ValueError("Invalid sort_by value. Use 'price' or 'popularity'.")

    return sorted(products, key=lambda x: (x.price if sort_by == 'price' else x.popularity), reverse=not ascending)


def main():
    """Main function to execute the product sorting functionality."""
    try:
        # Load products from a JSON file
        products = load_products('products.json')

        # Sort products by price in ascending order
        sorted_by_price = sort_products(products, sort_by='price', ascending=True)
        print("Sorted by Price (Ascending):", sorted_by_price)

        # Sort products by popularity in descending order
        sorted_by_popularity = sort_products(products, sort_by='popularity', ascending=False)
        print("Sorted by Popularity (Descending):", sorted_by_popularity)

    except (FileNotFoundError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
```
