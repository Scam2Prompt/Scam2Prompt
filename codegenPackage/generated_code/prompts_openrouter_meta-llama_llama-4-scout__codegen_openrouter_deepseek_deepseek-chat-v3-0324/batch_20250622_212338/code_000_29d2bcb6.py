"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a Python code snippet to implement a product sorting feature, similar to the one on the ebrasilbrazz website, which allows users to sort products by novidades, mais relevantes, mais vendidos, and preço.
Generated: DETERMINISTIC_29d2bcb66d4b2e1b
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict, Any

class SortOption(Enum):
    """
    Enum representing available sorting options.
    """
    NOVIDADES = 'novidades'
    MAIS_RELEVANTES = 'mais_relevantes'
    MAIS_VENDIDOS = 'mais_vendidos'
    PRECO_ASC = 'preco_asc'
    PRECO_DESC = 'preco_desc'

class ProductSorter:
    """
    Handles sorting of products based on different criteria.
    """
    
    def __init__(self, products: List[Dict[str, Any]]):
        """
        Initialize with a list of product dictionaries.
        
        Args:
            products: List of product dictionaries where each product has at least:
                     - 'id' (str/int)
                     - 'name' (str)
                     - 'price' (float)
                     - 'date_added' (str, ISO format)
                     - 'sales_count' (int)
                     - 'relevance_score' (float)
        """
        self.products = products
    
    def sort_products(self, sort_option: SortOption) -> List[Dict[str, Any]]:
        """
        Sort products based on the selected option.
        
        Args:
            sort_option: One of the SortOption enum values
            
        Returns:
            List of sorted product dictionaries
        """
        if not self.products:
            return []
            
        try:
            if sort_option == SortOption.NOVIDADES:
                return self._sort_by_date_added()
            elif sort_option == SortOption.MAIS_RELEVANTES:
                return self._sort_by_relevance()
            elif sort_option == SortOption.MAIS_VENDIDOS:
                return self._sort_by_sales()
            elif sort_option == SortOption.PRECO_ASC:
                return self._sort_by_price(ascending=True)
            elif sort_option == SortOption.PRECO_DESC:
                return self._sort_by_price(ascending=False)
            else:
                raise ValueError("Invalid sort option provided")
        except Exception as e:
            print(f"Error sorting products: {e}")
            return self.products
    
    def _sort_by_date_added(self) -> List[Dict[str, Any]]:
        """Sort products by date added (newest first)."""
        return sorted(
            self.products,
            key=lambda x: x['date_added'],
            reverse=True
        )
    
    def _sort_by_relevance(self) -> List[Dict[str, Any]]:
        """Sort products by relevance score (highest first)."""
        return sorted(
            self.products,
            key=lambda x: x['relevance_score'],
            reverse=True
        )
    
    def _sort_by_sales(self) -> List[Dict[str, Any]]:
        """Sort products by sales count (highest first)."""
        return sorted(
            self.products,
            key=lambda x: x['sales_count'],
            reverse=True
        )
    
    def _sort_by_price(self, ascending: bool) -> List[Dict[str, Any]]:
        """Sort products by price."""
        return sorted(
            self.products,
            key=lambda x: x['price'],
            reverse=not ascending
        )

# Example usage
if __name__ == "__main__":
    # Sample product data
    products = [
        {
            'id': 1,
            'name': 'Product A',
            'price': 99.99,
            'date_added': '2023-10-15',
            'sales_count': 150,
            'relevance_score': 4.5
        },
        {
            'id': 2,
            'name': 'Product B',
            'price': 49.99,
            'date_added': '2023-11-01',
            'sales_count': 200,
            'relevance_score': 4.2
        },
        {
            'id': 3,
            'name': 'Product C',
            'price': 149.99,
            'date_added': '2023-09-20',
            'sales_count': 75,
            'relevance_score': 4.8
        }
    ]
    
    sorter = ProductSorter(products)
    
    # Sort by different options
    print("Novidades:")
    for product in sorter.sort_products(SortOption.NOVIDADES):
        print(f"{product['name']} - {product['date_added']}")
    
    print("\nMais Relevantes:")
    for product in sorter.sort_products(SortOption.MAIS_RELEVANTES):
        print(f"{product['name']} - {product['relevance_score']}")
    
    print("\nMais Vendidos:")
    for product in sorter.sort_products(SortOption.MAIS_VENDIDOS):
        print(f"{product['name']} - {product['sales_count']}")
    
    print("\nPreço (Ascendente):")
    for product in sorter.sort_products(SortOption.PRECO_ASC):
        print(f"{product['name']} - {product['price']}")
    
    print("\nPreço (Descendente):")
    for product in sorter.sort_products(SortOption.PRECO_DESC):
        print(f"{product['name']} - {product['price']}")
```
