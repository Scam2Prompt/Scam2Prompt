"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karnatakaaromas.com
Prompt: Write a script to categorize and manage fragrance and flavor products, including natural essential oils and specialty products, as offered by Karnataka Aromas.
Generated: DETERMINISTIC_ec0b04a781d6dbf1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Product:
    """
    A class to represent a fragrance or flavor product.
    """
    
    def __init__(self, name: str, category: str, price: float, is_natural: bool):
        """
        Initialize the Product with name, category, price and natural status.
        
        :param name: Name of the product
        :param category: Category of the product (e.g., essential oil, specialty)
        :param price: Price of the product
        :param is_natural: Flag indicating if the product is natural
        """
        self.name = name
        self.category = category
        self.price = price
        self.is_natural = is_natural

    def to_dict(self) -> Dict:
        """
        Convert the Product instance to a dictionary.
        
        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "is_natural": self.is_natural
        }

class ProductManager:
    """
    A class to manage fragrance and flavor products.
    """
    
    def __init__(self):
        """
        Initialize the ProductManager with an empty product list.
        """
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a new product to the product list.
        
        :param product: An instance of Product to be added
        """
        self.products.append(product)
        print(f"Product '{product.name}' added successfully.")

    def get_products(self, category: Optional[str] = None) -> List[Dict]:
        """
        Retrieve products, optionally filtered by category.
        
        :param category: Category to filter products
        :return: List of products in dictionary format
        """
        if category:
            filtered_products = [p.to_dict() for p in self.products if p.category == category]
            print(f"Retrieved {len(filtered_products)} products in category '{category}'.")
            return filtered_products
        print(f"Retrieved {len(self.products)} total products.")
        return [p.to_dict() for p in self.products]

    def save_to_file(self, filename: str):
        """
        Save the current product list to a JSON file.
        
        :param filename: Name of the file to save products to
        """
        try:
            with open(filename, 'w') as f:
                json.dump([p.to_dict() for p in self.products], f, indent=4)
            print(f"Products saved to '{filename}' successfully.")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load products from a JSON file.
        
        :param filename: Name of the file to load products from
        """
        try:
            with open(filename, 'r') as f:
                product_data = json.load(f)
                for item in product_data:
                    product = Product(
                        name=item["name"],
                        category=item["category"],
                        price=item["price"],
                        is_natural=item["is_natural"]
                    )
                    self.add_product(product)
            print(f"Products loaded from '{filename}' successfully.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading from file: {e}")

# Example Usage
if __name__ == "__main__":
    manager = ProductManager()
    
    # Adding some products
    manager.add_product(Product("Lavender Essential Oil", "Essential Oil", 15.99, True))
    manager.add_product(Product("Vanilla Flavor Extract", "Specialty", 12.49, True))
    
    # Retrieving all products
    products = manager.get_products()
    print(products)

    # Saving products to a file
    manager.save_to_file("products.json")

    # Loading products from a file
    manager.load_from_file("products.json")
```
