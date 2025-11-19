"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: "Generate a Python code snippet for an e-commerce product filter that categorizes hair care products by type (e.g., shampoo, styling cream, hair powder) and price range, inspired by the product offerings on Matin Shop."
Generated: DETERMINISTIC_1b5a907bf89f116f
Batch ID: 20250622_210655
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

class Product:
    """Represents a hair care product with its attributes."""
    
    def __init__(self, name: str, product_type: str, price: float):
        """
        Initialize a Product instance.
        
        Args:
            name (str): Name of the product
            product_type (str): Type of product (e.g., 'shampoo', 'styling cream')
            price (float): Price of the product
        """
        self.name = name
        self.type = product_type
        self.price = price
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary format."""
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price
        }

class ProductFilter:
    """Filters hair care products by type and price range."""
    
    def __init__(self, products: List[Product]):
        """
        Initialize ProductFilter with a list of products.
        
        Args:
            products (List[Product]): List of Product objects to filter
        """
        self.products = products
    
    def filter_by_type(self, product_type: str) -> List[Product]:
        """
        Filter products by product type.
        
        Args:
            product_type (str): Type to filter by (e.g., 'shampoo')
            
        Returns:
            List[Product]: Filtered list of products
        """
        return [product for product in self.products if product.type.lower() == product_type.lower()]
    
    def filter_by_price_range(self, min_price: Optional[float] = None, max_price: Optional[float] = None) -> List[Product]:
        """
        Filter products by price range.
        
        Args:
            min_price (float, optional): Minimum price threshold
            max_price (float, optional): Maximum price threshold
            
        Returns:
            List[Product]: Filtered list of products
            
        Raises:
            ValueError: If min_price is greater than max_price
        """
        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("min_price cannot be greater than max_price")
            
        filtered = []
        for product in self.products:
            if min_price is not None and product.price < min_price:
                continue
            if max_price is not None and product.price > max_price:
                continue
            filtered.append(product)
        return filtered
    
    def filter(self, product_type: Optional[str] = None, 
               min_price: Optional[float] = None, 
               max_price: Optional[float] = None) -> List[Product]:
        """
        Combined filter by type and price range.
        
        Args:
            product_type (str, optional): Type to filter by
            min_price (float, optional): Minimum price threshold
            max_price (float, optional): Maximum price threshold
            
        Returns:
            List[Product]: Filtered list of products
        """
        filtered_products = self.products
        
        if product_type:
            filtered_products = self.filter_by_type(product_type)
        
        if min_price is not None or max_price is not None:
            filtered_products = self.filter_by_price_range(min_price, max_price)
        
        return filtered_products
    
    def save_to_json(self, filename: str, products: List[Product]):
        """
        Save filtered products to a JSON file.
        
        Args:
            filename (str): Name of the output file
            products (List[Product]): List of products to save
        """
        with open(filename, 'w') as f:
            json.dump([product.to_dict() for product in products], f, indent=4)

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        Product("Moisturizing Shampoo", "shampoo", 12.99),
        Product("Volumizing Shampoo", "shampoo", 14.99),
        Product("Styling Cream", "styling cream", 18.50),
        Product("Hair Powder", "hair powder", 22.00),
        Product("Deep Conditioner", "conditioner", 15.75)
    ]
    
    # Initialize filter
    product_filter = ProductFilter(products)
    
    # Filter by type
    shampoos = product_filter.filter_by_type("shampoo")
    print("Shampoos:")
    for product in shampoos:
        print(f"- {product.name}: ${product.price:.2f}")
    
    # Filter by price range
    affordable_products = product_filter.filter_by_price_range(max_price=20.00)
    print("\nAffordable Products (under $20):")
    for product in affordable_products:
        print(f"- {product.name}: ${product.price:.2f}")
    
    # Combined filter
    filtered = product_filter.filter(product_type="shampoo", min_price=13.00)
    print("\nPremium Shampoos:")
    for product in filtered:
        print(f"- {product.name}: ${product.price:.2f}")
    
    # Save to JSON
    product_filter.save_to_json("filtered_products.json", filtered)
```
