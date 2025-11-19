"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Develop a code snippet that integrates a product catalog for Himalayan salt items, focusing on unique offerings like salt massage stones and inhalers from Craftimus.
Generated: DETERMINISTIC_b153b3a1bd9acf49
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Optional
from dataclasses import dataclass
import json

@dataclass
class HimalayanSaltProduct:
    """Data class representing a Himalayan salt product."""
    id: str
    name: str
    description: str
    price: float
    category: str
    in_stock: bool
    weight_grams: Optional[int] = None
    dimensions: Optional[str] = None

class ProductCatalog:
    """Class to manage Himalayan salt products from Craftimus."""
    
    def __init__(self):
        """Initialize the product catalog with an empty list of products."""
        self.products: List[HimalayanSaltProduct] = []
    
    def add_product(self, product: HimalayanSaltProduct) -> None:
        """Add a product to the catalog.
        
        Args:
            product: HimalayanSaltProduct to be added
        """
        self.products.append(product)
    
    def get_product_by_id(self, product_id: str) -> Optional[HimalayanSaltProduct]:
        """Retrieve a product by its ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            HimalayanSaltProduct if found, None otherwise
        """
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def get_products_by_category(self, category: str) -> List[HimalayanSaltProduct]:
        """Retrieve all products in a specific category.
        
        Args:
            category: Category to filter products by
            
        Returns:
            List of HimalayanSaltProduct objects in the category
        """
        return [product for product in self.products if product.category.lower() == category.lower()]
    
    def load_from_json(self, file_path: str) -> None:
        """Load products from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
            KeyError: If required fields are missing in the JSON
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    product = HimalayanSaltProduct(
                        id=item['id'],
                        name=item['name'],
                        description=item['description'],
                        price=item['price'],
                        category=item['category'],
                        in_stock=item['in_stock'],
                        weight_grams=item.get('weight_grams'),
                        dimensions=item.get('dimensions')
                    )
                    self.add_product(product)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format", file_path, 0)
        except KeyError as e:
            raise KeyError(f"Missing required field in JSON: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize catalog
    catalog = ProductCatalog()
    
    # Add some sample products
    massage_stone = HimalayanSaltProduct(
        id="MS001",
        name="Salt Massage Stone",
        description="Hand-carved Himalayan salt stone for massage therapy",
        price=29.99,
        category="Massage",
        in_stock=True,
        weight_grams=500,
        dimensions="10x5x3 cm"
    )
    
    inhaler = HimalayanSaltProduct(
        id="INH002",
        name="Salt Inhaler",
        description="Portable Himalayan salt inhaler for respiratory health",
        price=19.99,
        category="Respiratory",
        in_stock=True,
        weight_grams=200
    )
    
    catalog.add_product(massage_stone)
    catalog.add_product(inhaler)
    
    # Example queries
    print("Massage products:")
    for product in catalog.get_products_by_category("Massage"):
        print(f"- {product.name}: ${product.price}")
    
    found_product = catalog.get_product_by_id("INH002")
    if found_product:
        print(f"\nFound product: {found_product.name}")
```
