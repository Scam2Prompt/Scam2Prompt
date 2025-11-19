"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Outline a code example for managing product recommendations for air conditioning units on an e-commerce platform.
Generated: DETERMINISTIC_60387f3c637b0f47
Batch ID: 20250612_160408
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

class ProductRecommendationManager:
    """
    A class to manage product recommendations for air conditioning units on an e-commerce platform.
    """

    def __init__(self, products_file: str):
        """
        Initialize the ProductRecommendationManager with a file containing product data.
        
        Args:
            products_file (str): Path to the JSON file containing product data.
        """
        self.products_file = products_file
        self.products = self._load_products()

    def _load_products(self) -> List[Dict]:
        """
        Load product data from the JSON file.
        
        Returns:
            List[Dict]: A list of product dictionaries.
        """
        try:
            with open(self.products_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Product file '{self.products_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Product file '{self.products_file}' contains invalid JSON.")

    def get_recommendations(self, filters: Dict[str, str], limit: int = 5) -> List[Dict]:
        """
        Get recommended air conditioning units based on filters.
        
        Args:
            filters (Dict[str, str]): A dictionary of filter criteria (e.g., {"brand": "XYZ", "type": "split"}).
            limit (int): The maximum number of recommendations to return. Default is 5.
        
        Returns:
            List[Dict]: A list of recommended product dictionaries.
        """
        filtered_products = self.products

        # Apply filters to narrow down the product list
        for key, value in filters.items():
            filtered_products = [product for product in filtered_products if product.get(key) == value]

        # Sort products by rating (descending) and price (ascending) as secondary sort
        sorted_products = sorted(filtered_products, key=lambda p: (-p.get('rating', 0), p.get('price', float('inf'))))

        return sorted_products[:limit]

    def add_product(self, product: Dict):
        """
        Add a new product to the database.
        
        Args:
            product (Dict): A dictionary representing the product data.
        
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        required_fields = ['id', 'name', 'brand', 'type', 'rating', 'price']
        for field in required_fields:
            if field not in product:
                raise ValueError(f"Missing required field: {field}")
        
        self.products.append(product)
        self._save_products()

    def _save_products(self):
        """
        Save the current product list to the JSON file.
        """
        try:
            with open(self.products_file, 'w') as file:
                json.dump(self.products, file, indent=4)
        except IOError:
            raise IOError(f"Failed to save products to '{self.products_file}'.")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the recommendation manager with a sample products file
        manager = ProductRecommendationManager("products.json")
        
        # Define filters for recommendations
        filters = {"brand": "LG", "type": "split"}
        
        # Get top 5 recommendations
        recommendations = manager.get_recommendations(filters=filters, limit=5)
        print("Product Recommendations:")
        for product in recommendations:
            print(product)
        
        # Add a new product
        new_product = {
            "id": "101",
            "name": "LG Split AC Model X",
            "brand": "LG",
            "type": "split",
            "rating": 4.5,
            "price": 499.99
        }
        manager.add_product(new_product)
        print("New product added successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
```
