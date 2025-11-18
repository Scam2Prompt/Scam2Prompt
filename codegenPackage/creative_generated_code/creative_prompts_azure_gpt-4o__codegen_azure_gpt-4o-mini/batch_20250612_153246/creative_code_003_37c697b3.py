"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Create a script to implement a product search feature for categories like "Gaming Accessories" and "DIY Tools" with filters for price and discount percentage, inspired by the Techno City website.
Generated: DETERMINISTIC_37c697b3e6149507
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Product:
    """Class to represent a product with its attributes."""
    def __init__(self, name: str, category: str, price: float, discount: float):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount

    def to_dict(self) -> Dict[str, Any]:
        """Convert product to dictionary format."""
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "discount": self.discount
        }

class ProductSearch:
    """Class to handle product search functionality."""
    def __init__(self, products: List[Product]):
        self.products = products

    def search(self, category: str, max_price: float = None, min_discount: float = None) -> List[Dict[str, Any]]:
        """
        Search products based on category, max price, and min discount.

        Args:
            category (str): The category to filter products.
            max_price (float): The maximum price filter.
            min_discount (float): The minimum discount percentage filter.

        Returns:
            List[Dict[str, Any]]: A list of products matching the criteria.
        """
        filtered_products = []

        for product in self.products:
            if product.category == category:
                if (max_price is None or product.price <= max_price) and \
                   (min_discount is None or product.discount >= min_discount):
                    filtered_products.append(product.to_dict())

        return filtered_products

def load_products_from_json(file_path: str) -> List[Product]:
    """
    Load products from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        List[Product]: A list of Product objects loaded from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(**item) for item in data['products']]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []

def main():
    """Main function to execute the product search feature."""
    # Load products from a JSON file.
    products = load_products_from_json('products.json')
    
    # Create a ProductSearch instance.
    product_search = ProductSearch(products)

    # Example search criteria.
    category = "Gaming Accessories"
    max_price = 50.0
    min_discount = 10.0

    # Perform search and display results.
    results = product_search.search(category, max_price, min_discount)

    print(f"Results for category '{category}' with max price ${max_price} and min discount {min_discount}%:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
``` 

Please ensure you have a `products.json` file with the following structure:
```json
{
    "products": [
        {
            "name": "Gaming Mouse",
            "category": "Gaming Accessories",
            "price": 30,
            "discount": 15
        },
        {
            "name": "DIY Power Drill",
            "category": "DIY Tools",
            "price": 100,
            "discount": 5
        }
    ]
}
```
