"""
Generated Code Metadata:
========================
Original URL: https://www.techno-city.co.za
Prompt: Create a script to implement a product search feature for categories like "Gaming Accessories" and "DIY Tools" with filters for price and discount percentage, inspired by the Techno City website.
Generated: DETERMINISTIC_37c697b3e6149507
Batch ID: 20250612_153246
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

class ProductSearch:
    """
    A class to handle product search functionality with filters for price and discount.
    Inspired by Techno City website's product search feature.
    """
    
    def __init__(self, products_data: List[Dict]):
        """
        Initialize the ProductSearch with product data.
        
        Args:
            products_data (List[Dict]): List of product dictionaries containing product details.
        """
        self.products = products_data
    
    def search_by_category(self, category: str) -> List[Dict]:
        """
        Search products by category.
        
        Args:
            category (str): Category to filter products by (e.g., "Gaming Accessories", "DIY Tools").
            
        Returns:
            List[Dict]: List of products in the specified category.
        """
        return [product for product in self.products if product.get('category') == category]
    
    def apply_price_filter(self, products: List[Dict], min_price: Optional[float] = None, max_price: Optional[float] = None) -> List[Dict]:
        """
        Apply price range filter to products.
        
        Args:
            products (List[Dict]): List of products to filter.
            min_price (Optional[float]): Minimum price threshold.
            max_price (Optional[float]): Maximum price threshold.
            
        Returns:
            List[Dict]: Filtered list of products within the price range.
        """
        filtered_products = products
        
        if min_price is not None:
            filtered_products = [p for p in filtered_products if p.get('price', 0) >= min_price]
        
        if max_price is not None:
            filtered_products = [p for p in filtered_products if p.get('price', float('inf')) <= max_price]
            
        return filtered_products
    
    def apply_discount_filter(self, products: List[Dict], min_discount: Optional[float] = None) -> List[Dict]:
        """
        Apply discount percentage filter to products.
        
        Args:
            products (List[Dict]): List of products to filter.
            min_discount (Optional[float]): Minimum discount percentage threshold.
            
        Returns:
            List[Dict]: Filtered list of products with at least the specified discount.
        """
        if min_discount is None:
            return products
            
        return [p for p in products if p.get('discount_percentage', 0) >= min_discount]
    
    def search(
        self,
        category: str,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_discount: Optional[float] = None
    ) -> List[Dict]:
        """
        Perform a comprehensive product search with all filters applied.
        
        Args:
            category (str): Product category to search.
            min_price (Optional[float]): Minimum price threshold.
            max_price (Optional[float]): Maximum price threshold.
            min_discount (Optional[float]): Minimum discount percentage threshold.
            
        Returns:
            List[Dict]: Filtered list of products matching all criteria.
        """
        try:
            # Step 1: Filter by category
            category_products = self.search_by_category(category)
            
            # Step 2: Apply price filters
            price_filtered = self.apply_price_filter(category_products, min_price, max_price)
            
            # Step 3: Apply discount filter
            final_products = self.apply_discount_filter(price_filtered, min_discount)
            
            return final_products
            
        except Exception as e:
            print(f"Error during product search: {e}")
            return []

def load_products_from_file(file_path: str) -> List[Dict]:
    """
    Load product data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing product data.
        
    Returns:
        List[Dict]: List of product dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return []
    except Exception as e:
        print(f"Error loading products: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Load sample product data
    products = load_products_from_file("products.json")
    
    if products:
        # Initialize search system
        search_system = ProductSearch(products)
        
        # Perform a sample search
        results = search_system.search(
            category="Gaming Accessories",
            min_price=20.0,
            max_price=100.0,
            min_discount=10.0
        )
        
        print(f"Found {len(results)} products:")
        for product in results:
            print(f"- {product.get('name')} (${product.get('price')}, {product.get('discount_percentage')}% off)")
```
