"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Outline a library recommendation for managing product catalogs for a business like Maderas Elaboradas that deals with various wood products, including furniture and tool handles.
Generated: DETERMINISTIC_5af837d4ee979eec
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog Management Library for Maderas Elaboradas

This library provides functionality to manage a catalog of wood products,
including furniture and tool handles, with CRUD operations, search, and inventory tracking.
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import os
from enum import Enum

class ProductCategory(Enum):
    """Enum representing product categories."""
    FURNITURE = "furniture"
    TOOL_HANDLE = "tool_handle"
    OTHER = "other"

@dataclass
class Product:
    """Data class representing a product in the catalog."""
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    stock_quantity: int
    dimensions: Optional[Dict[str, float]] = None
    weight: Optional[float] = None

class ProductCatalog:
    """Class to manage product catalog operations."""
    
    def __init__(self, catalog_file: str = "product_catalog.json"):
        """
        Initialize the catalog.
        
        Args:
            catalog_file: Path to the JSON file storing catalog data.
        """
        self.catalog_file = catalog_file
        self.products: Dict[str, Product] = {}
        self._load_catalog()

    def _load_catalog(self) -> None:
        """Load catalog data from the JSON file."""
        try:
            if os.path.exists(self.catalog_file):
                with open(self.catalog_file, 'r') as file:
                    data = json.load(file)
                    for product_id, product_data in data.items():
                        product_data['category'] = ProductCategory(product_data['category'])
                        self.products[product_id] = Product(**product_data)
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load catalog: {e}")

    def _save_catalog(self) -> None:
        """Save catalog data to the JSON file."""
        try:
            with open(self.catalog_file, 'w') as file:
                data = {
                    product_id: {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'category': product.category.value,
                        'price': product.price,
                        'stock_quantity': product.stock_quantity,
                        'dimensions': product.dimensions,
                        'weight': product.weight
                    }
                    for product_id, product in self.products.items()
                }
                json.dump(data, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save catalog: {e}")

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the catalog.
        
        Args:
            product: Product to add.
        
        Raises:
            ValueError: If product ID already exists.
        """
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        self._save_catalog()

    def get_product(self, product_id: str) -> Optional[Product]:
        """
        Retrieve a product by ID.
        
        Args:
            product_id: ID of the product to retrieve.
        
        Returns:
            Product if found, None otherwise.
        """
        return self.products.get(product_id)

    def update_product(self, product_id: str, **kwargs) -> None:
        """
        Update product attributes.
        
        Args:
            product_id: ID of the product to update.
            **kwargs: Attributes to update (e.g., name="New Name").
        
        Raises:
            ValueError: If product ID doesn't exist or invalid attributes provided.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if key == 'category' and isinstance(value, str):
                value = ProductCategory(value)
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")
        self._save_catalog()

    def delete_product(self, product_id: str) -> None:
        """
        Delete a product from the catalog.
        
        Args:
            product_id: ID of the product to delete.
        
        Raises:
            ValueError: If product ID doesn't exist.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self._save_catalog()

    def search_products(self, name: Optional[str] = None, category: Optional[ProductCategory] = None) -> List[Product]:
        """
        Search products by name and/or category.
        
        Args:
            name: Name substring to search for.
            category: Product category to filter by.
        
        Returns:
            List of matching products.
        """
        results = []
        for product in self.products.values():
            if name and name.lower() not in product.name.lower():
                continue
            if category and product.category != category:
                continue
            results.append(product)
        return results

    def update_stock(self, product_id: str, quantity_change: int) -> None:
        """
        Update product stock quantity.
        
        Args:
            product_id: ID of the product to update.
            quantity_change: Amount to add (positive) or subtract (negative).
        
        Raises:
            ValueError: If product ID doesn't exist or stock would go negative.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        new_quantity = self.products[product_id].stock_quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
        
        self.products[product_id].stock_quantity = new_quantity
        self._save_catalog()
```
