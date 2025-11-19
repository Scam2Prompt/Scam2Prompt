"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Develop a Python script to filter and display industrial products suitable for marine and offshore engineering, based on the industries served by Roshako.
Generated: DETERMINISTIC_50741abf09c42f77
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class IndustrialProduct:
    """
    Represents an industrial product with attributes relevant to marine and offshore engineering.
    """
    def __init__(self, product_id: str, name: str, description: str, industries_served: List[str]):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.industries_served = industries_served

    def is_suitable_for_marine_offshore(self) -> bool:
        """
        Checks if the product is suitable for marine and offshore engineering.
        """
        marine_keywords = ['marine', 'offshore', 'subsea', 'nautical']
        return any(keyword in industry.lower() 
                   for industry in self.industries_served 
                   for keyword in marine_keywords)

    def to_dict(self) -> Dict:
        """
        Converts the product to a dictionary for easy serialization.
        """
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'industries_served': self.industries_served
        }

class ProductFilter:
    """
    Filters and manages industrial products suitable for marine and offshore engineering.
    """
    def __init__(self, products: List[IndustrialProduct]):
        self.products = products

    def filter_marine_offshore_products(self) -> List[IndustrialProduct]:
        """
        Filters products suitable for marine and offshore engineering.
        """
        return [product for product in self.products if product.is_suitable_for_marine_offshore()]

    @staticmethod
    def load_products_from_json(file_path: str) -> List[IndustrialProduct]:
        """
        Loads products from a JSON file.
        
        Args:
            file_path: Path to the JSON file containing product data.
        
        Returns:
            List of IndustrialProduct objects.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
            KeyError: If required fields are missing in the JSON data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                products = []
                for item in data:
                    if not all(key in item for key in ['product_id', 'name', 'description', 'industries_served']):
                        raise KeyError("Missing required fields in product data.")
                    products.append(
                        IndustrialProduct(
                            item['product_id'],
                            item['name'],
                            item['description'],
                            item['industries_served']
                        )
                    )
                return products
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("The file is not a valid JSON.", doc=file_path, pos=0)

def display_products(products: List[IndustrialProduct]) -> None:
    """
    Displays the list of products in a user-friendly format.
    
    Args:
        products: List of IndustrialProduct objects to display.
    """
    if not products:
        print("No products found suitable for marine and offshore engineering.")
        return

    print("\nProducts suitable for marine and offshore engineering:")
    print("-" * 60)
    for product in products:
        print(f"ID: {product.product_id}")
        print(f"Name: {product.name}")
        print(f"Description: {product.description}")
        print(f"Industries Served: {', '.join(product.industries_served)}")
        print("-" * 60)

def main():
    """
    Main function to load, filter, and display marine and offshore products.
    """
    try:
        # Load products from JSON file (replace with actual file path)
        products = ProductFilter.load_products_from_json('roshako_products.json')
        
        # Filter products suitable for marine and offshore
        product_filter = ProductFilter(products)
        marine_products = product_filter.filter_marine_offshore_products()
        
        # Display the filtered products
        display_products(marine_products)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file. {e}")
    except KeyError as e:
        print(f"Error: Missing required data in JSON file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
