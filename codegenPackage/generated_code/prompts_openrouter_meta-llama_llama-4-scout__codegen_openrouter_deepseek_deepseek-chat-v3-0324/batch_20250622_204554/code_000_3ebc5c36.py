"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: "Generate a Python code snippet to create a catalog system for ITACA CERAMIC's tile products, including slab tiles, vitrified tiles, and wall tiles with their respective sizes and features."
Generated: DETERMINISTIC_3ebc5c3660777e82
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ITACA CERAMIC Tile Catalog System
This module provides a catalog system for managing tile products including slab tiles,
vitrified tiles, and wall tiles with their respective sizes and features.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict


class TileType(Enum):
    """Enum representing different types of tiles."""
    SLAB = auto()
    VITRIFIED = auto()
    WALL = auto()


@dataclass
class TileFeature:
    """Class representing features of a tile."""
    name: str
    description: str


@dataclass
class TileSize:
    """Class representing dimensions of a tile."""
    length: float  # in cm
    width: float   # in cm
    thickness: Optional[float] = None  # in mm


@dataclass
class TileProduct:
    """Class representing a tile product in the catalog."""
    product_id: str
    name: str
    tile_type: TileType
    size: TileSize
    features: List[TileFeature]
    price: float
    stock: int = 0
    description: Optional[str] = None


class TileCatalog:
    """Main catalog system for managing tile products."""
    
    def __init__(self):
        self.products: Dict[str, TileProduct] = {}
    
    def add_product(self, product: TileProduct) -> None:
        """Add a new product to the catalog.
        
        Args:
            product: TileProduct to be added
            
        Raises:
            ValueError: If product with same ID already exists
        """
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
    
    def get_product(self, product_id: str) -> Optional[TileProduct]:
        """Retrieve a product by its ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            TileProduct if found, None otherwise
        """
        return self.products.get(product_id)
    
    def update_product_stock(self, product_id: str, quantity: int) -> bool:
        """Update the stock quantity of a product.
        
        Args:
            product_id: ID of the product to update
            quantity: New stock quantity (must be >= 0)
            
        Returns:
            True if update was successful, False if product not found
            
        Raises:
            ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
        
        product = self.get_product(product_id)
        if product:
            product.stock = quantity
            return True
        return False
    
    def search_products(
        self,
        tile_type: Optional[TileType] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        in_stock: bool = False
    ) -> List[TileProduct]:
        """Search products based on various criteria.
        
        Args:
            tile_type: Filter by tile type
            min_price: Minimum price filter
            max_price: Maximum price filter
            in_stock: Only include products with stock > 0
            
        Returns:
            List of matching TileProduct objects
        """
        results = []
        
        for product in self.products.values():
            if tile_type and product.tile_type != tile_type:
                continue
            if min_price is not None and product.price < min_price:
                continue
            if max_price is not None and product.price > max_price:
                continue
            if in_stock and product.stock <= 0:
                continue
            results.append(product)
        
        return results
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from the catalog.
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            True if product was found and removed, False otherwise
        """
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False


# Example usage
if __name__ == "__main__":
    catalog = TileCatalog()
    
    # Create some sample products
    slab_tile = TileProduct(
        product_id="SLAB-001",
        name="Premium Marble Slab",
        tile_type=TileType.SLAB,
        size=TileSize(length=120, width=60, thickness=10),
        price=45.99,
        stock=50,
        description="High-quality marble slab tile with natural veining",
        features=[
            TileFeature("Scratch Resistant", "Highly resistant to scratches"),
            TileFeature("Stain Proof", "Resistant to stains and spills")
        ]
    )
    
    vitrified_tile = TileProduct(
        product_id="VIT-002",
        name="Glossy Vitrified Floor Tile",
        tile_type=TileType.VITRIFIED,
        size=TileSize(length=80, width=80, thickness=8),
        price=32.50,
        stock=120,
        features=[
            TileFeature("Slip Resistant", "Safe for wet areas"),
            TileFeature("High Shine", "Maintains glossy finish for years")
        ]
    )
    
    wall_tile = TileProduct(
        product_id="WALL-003",
        name="Subway Wall Tile",
        tile_type=TileType.WALL,
        size=TileSize(length=30, width=10, thickness=5),
        price=12.75,
        stock=200,
        features=[
            TileFeature("Easy Clean", "Simple to maintain and clean"),
            TileFeature("Classic Design", "Timeless subway tile pattern")
        ]
    )
    
    # Add products to catalog
    catalog.add_product(slab_tile)
    catalog.add_product(vitrified_tile)
    catalog.add_product(wall_tile)
    
    # Search example
    print("All slab tiles:")
    for product in catalog.search_products(tile_type=TileType.SLAB):
        print(f"- {product.name} (ID: {product.product_id})")
    
    print("\nAll products under $40:")
    for product in catalog.search_products(max_price=40):
        print(f"- {product.name} (${product.price})")
```
