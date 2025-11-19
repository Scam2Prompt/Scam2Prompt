"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for auto parts, including product codes, names, and prices, similar to the one found on autopecasbrazz.
Generated: DETERMINISTIC_72c805eb833ca877
Batch ID: 20250622_205612
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
from dataclasses import dataclass, asdict

@dataclass
class AutoPart:
    """Represents an auto part product in the catalog."""
    product_code: str
    name: str
    price: float
    category: str
    brand: Optional[str] = None
    description: Optional[str] = None
    stock: int = 0

class AutoPartsCatalog:
    """Manages an e-commerce catalog of auto parts."""
    
    def __init__(self):
        self.products: Dict[str, AutoPart] = {}
    
    def add_product(self, product: AutoPart) -> None:
        """Adds a product to the catalog.
        
        Args:
            product: AutoPart object to be added.
            
        Raises:
            ValueError: If product code already exists.
        """
        if product.product_code in self.products:
            raise ValueError(f"Product with code {product.product_code} already exists")
        self.products[product.product_code] = product
    
    def get_product(self, product_code: str) -> Optional[AutoPart]:
        """Retrieves a product by its code.
        
        Args:
            product_code: The code of the product to retrieve.
            
        Returns:
            The AutoPart object if found, None otherwise.
        """
        return self.products.get(product_code)
    
    def update_product(self, product_code: str, **kwargs) -> None:
        """Updates product attributes.
        
        Args:
            product_code: Code of the product to update.
            **kwargs: Attributes to update with their new values.
            
        Raises:
            KeyError: If product code doesn't exist.
            ValueError: If trying to update product_code.
        """
        if product_code not in self.products:
            raise KeyError(f"Product with code {product_code} not found")
        
        if 'product_code' in kwargs:
            raise ValueError("Cannot update product_code")
            
        product = self.products[product_code]
        for key, value in kwargs.items():
            setattr(product, key, value)
    
    def remove_product(self, product_code: str) -> None:
        """Removes a product from the catalog.
        
        Args:
            product_code: Code of the product to remove.
            
        Raises:
            KeyError: If product code doesn't exist.
        """
        if product_code not in self.products:
            raise KeyError(f"Product with code {product_code} not found")
        del self.products[product_code]
    
    def search_products(self, query: str) -> List[AutoPart]:
        """Searches products by name or description.
        
        Args:
            query: Search term to look for in product names and descriptions.
            
        Returns:
            List of matching AutoPart objects.
        """
        query = query.lower()
        return [
            product for product in self.products.values()
            if query in product.name.lower() or 
               (product.description and query in product.description.lower())
        ]
    
    def filter_by_category(self, category: str) -> List[AutoPart]:
        """Filters products by category.
        
        Args:
            category: Category to filter by.
            
        Returns:
            List of AutoPart objects in the specified category.
        """
        return [
            product for product in self.products.values()
            if product.category.lower() == category.lower()
        ]
    
    def save_to_file(self, filename: str) -> None:
        """Saves catalog to a JSON file.
        
        Args:
            filename: Name of the file to save to.
        """
        with open(filename, 'w') as f:
            json.dump(
                [asdict(product) for product in self.products.values()],
                f,
                indent=2
            )
    
    def load_from_file(self, filename: str) -> None:
        """Loads catalog from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            ValueError: If file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = {
                    item['product_code']: AutoPart(**item)
                    for item in data
                }
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e
        except KeyError as e:
            raise ValueError("Missing required field in product data") from e

# Example usage
if __name__ == "__main__":
    catalog = AutoPartsCatalog()
    
    # Add sample products
    catalog.add_product(AutoPart(
        product_code="AP001",
        name="Brake Pads",
        price=45.99,
        category="Brakes",
        brand="Brembo",
        description="High-performance brake pads",
        stock=50
    ))
    
    catalog.add_product(AutoPart(
        product_code="AP002",
        name="Oil Filter",
        price=12.50,
        category="Engine",
        brand="Mann-Filter",
        description="Premium oil filter for all weather conditions",
        stock=100
    ))
    
    # Save catalog to file
    catalog.save_to_file("auto_parts_catalog.json")
```
