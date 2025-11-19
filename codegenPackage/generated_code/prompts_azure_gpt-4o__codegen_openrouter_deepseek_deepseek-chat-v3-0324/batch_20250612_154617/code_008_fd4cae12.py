"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Write a script to categorize "Гарант's" products based on vehicle types (e.g., passenger cars, trucks, buses) and display them in a user-friendly format.
Generated: DETERMINISTIC_fd4cae12ae751da0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ProductCategorizer:
    """
    A class to categorize products based on vehicle types.
    """

    def __init__(self, data_source: str = "products.json"):
        """
        Initialize the categorizer with a data source.
        
        Args:
            data_source (str): Path to the JSON file containing product data.
        """
        self.data_source = data_source
        self.products = self._load_products()

    def _load_products(self) -> List[Dict[str, Any]]:
        """
        Load products from the JSON data source.
        
        Returns:
            List[Dict[str, Any]]: List of product dictionaries.
            
        Raises:
            FileNotFoundError: If the data source file is not found.
            json.JSONDecodeError: If the data source is not valid JSON.
        """
        try:
            with open(self.data_source, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data source file '{self.data_source}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in data source file '{self.data_source}'.", doc="", pos=0)

    def categorize_by_vehicle_type(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorize products by vehicle type.
        
        Returns:
            Dict[str, List[Dict[str, Any]]]: Dictionary with vehicle types as keys
            and lists of products as values.
        """
        categories = {
            "passenger_cars": [],
            "trucks": [],
            "buses": [],
            "other": []
        }
        
        for product in self.products:
            vehicle_type = product.get("vehicle_type", "").lower()
            
            if "passenger" in vehicle_type or "car" in vehicle_type:
                categories["passenger_cars"].append(product)
            elif "truck" in vehicle_type:
                categories["trucks"].append(product)
            elif "bus" in vehicle_type:
                categories["buses"].append(product)
            else:
                categories["other"].append(product)
                
        return categories

    def display_categories(self, categories: Dict[str, List[Dict[str, Any]]]) -> None:
        """
        Display categorized products in a user-friendly format.
        
        Args:
            categories (Dict[str, List[Dict[str, Any]]]): Categorized products.
        """
        for category, products in categories.items():
            print(f"\n{category.replace('_', ' ').title()} ({len(products)} products):")
            print("-" * 50)
            
            if not products:
                print("No products in this category.")
                continue
                
            for product in products:
                print(f"Name: {product.get('name', 'N/A')}")
                print(f"ID: {product.get('id', 'N/A')}")
                print(f"Price: {product.get('price', 'N/A')}")
                print(f"Vehicle Type: {product.get('vehicle_type', 'N/A')}")
                print("-" * 30)

def main():
    """
    Main function to run the product categorization script.
    """
    try:
        categorizer = ProductCategorizer()
        categories = categorizer.categorize_by_vehicle_type()
        categorizer.display_categories(categories)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
