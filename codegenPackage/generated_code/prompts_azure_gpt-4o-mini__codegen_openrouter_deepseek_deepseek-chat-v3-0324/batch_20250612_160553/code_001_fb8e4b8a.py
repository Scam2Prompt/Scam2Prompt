"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: How can I implement a filtering system for furniture products based on price and relevance, as seen on the Móveis Campo Largo site?
Generated: DETERMINISTIC_fb8e4b8a25b4a871
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SortOrder(Enum):
    """Enum for sorting options"""
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"
    RELEVANCE = "relevance"

class FurnitureProduct:
    """Class representing a furniture product"""
    def __init__(self, id: int, name: str, price: float, relevance_score: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.relevance_score = relevance_score
        self.category = category

    def __repr__(self):
        return f"FurnitureProduct(id={self.id}, name='{self.name}', price={self.price})"

class ProductFilter:
    """Class for filtering and sorting furniture products"""
    def __init__(self, products: List[FurnitureProduct]):
        self.products = products

    def filter_by_price_range(self, min_price: Optional[float] = None, max_price: Optional[float] = None) -> List[FurnitureProduct]:
        """
        Filter products by price range
        Args:
            min_price: Minimum price threshold
            max_price: Maximum price threshold
        Returns:
            List of filtered products
        """
        try:
            filtered = self.products
            
            if min_price is not None:
                filtered = [p for p in filtered if p.price >= min_price]
            
            if max_price is not None:
                filtered = [p for p in filtered if p.price <= max_price]
                
            return filtered
        except Exception as e:
            logger.error(f"Error filtering by price range: {e}")
            return []

    def filter_by_category(self, category: str) -> List[FurnitureProduct]:
        """
        Filter products by category
        Args:
            category: Category to filter by
        Returns:
            List of filtered products
        """
        try:
            return [p for p in self.products if p.category.lower() == category.lower()]
        except Exception as e:
            logger.error(f"Error filtering by category: {e}")
            return []

    def sort_products(self, products: List[FurnitureProduct], sort_order: SortOrder) -> List[FurnitureProduct]:
        """
        Sort products based on specified order
        Args:
            products: List of products to sort
            sort_order: Sorting order (price_asc, price_desc, relevance)
        Returns:
            Sorted list of products
        """
        try:
            if sort_order == SortOrder.PRICE_ASC:
                return sorted(products, key=lambda p: p.price)
            elif sort_order == SortOrder.PRICE_DESC:
                return sorted(products, key=lambda p: p.price, reverse=True)
            elif sort_order == SortOrder.RELEVANCE:
                return sorted(products, key=lambda p: p.relevance_score, reverse=True)
            else:
                return products
        except Exception as e:
            logger.error(f"Error sorting products: {e}")
            return products

    def get_filtered_products(
        self,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        category: Optional[str] = None,
        sort_order: SortOrder = SortOrder.RELEVANCE
    ) -> List[FurnitureProduct]:
        """
        Apply all filters and sorting to products
        Args:
            min_price: Minimum price threshold
            max_price: Maximum price threshold
            category: Category to filter by
            sort_order: Sorting order
        Returns:
            Filtered and sorted list of products
        """
        try:
            filtered = self.products
            
            if min_price is not None or max_price is not None:
                filtered = self.filter_by_price_range(min_price, max_price)
                
            if category is not None:
                filtered = self.filter_by_category(category)
                
            return self.sort_products(filtered, sort_order)
        except Exception as e:
            logger.error(f"Error in get_filtered_products: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample products
    products = [
        FurnitureProduct(1, "Wooden Chair", 199.99, 0.8, "chairs"),
        FurnitureProduct(2, "Leather Sofa", 899.99, 0.9, "sofas"),
        FurnitureProduct(3, "Coffee Table", 249.99, 0.7, "tables"),
        FurnitureProduct(4, "Bookshelf", 179.99, 0.6, "shelves"),
        FurnitureProduct(5, "Dining Table", 599.99, 0.85, "tables"),
    ]
    
    filter_system = ProductFilter(products)
    
    # Filter by price range and sort by price ascending
    filtered_products = filter_system.get_filtered_products(
        min_price=150,
        max_price=600,
        sort_order=SortOrder.PRICE_ASC
    )
    
    print("Filtered Products:")
    for product in filtered_products:
        print(product)
```
