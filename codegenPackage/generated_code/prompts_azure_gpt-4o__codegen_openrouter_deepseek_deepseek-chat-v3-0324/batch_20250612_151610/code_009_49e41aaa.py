"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Develop a tool to recommend the best packaging material (e.g., corrugated cardboard, stretch film, or adhesive tape) for specific product dimensions and weights, using the product attributes from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_49e41aaad183175e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Tuple, List

class PackagingMaterial(Enum):
    """Enumeration of available packaging materials."""
    CORRUGATED_CARDBOARD = "Corrugated Cardboard"
    STRETCH_FILM = "Stretch Film"
    ADHESIVE_TAPE = "Adhesive Tape"

@dataclass
class Product:
    """Data class representing a product to be packaged."""
    length: float  # in cm
    width: float   # in cm
    height: float  # in cm
    weight: float  # in kg
    fragile: bool = False

@dataclass
class PackagingRecommendation:
    """Data class representing a packaging recommendation."""
    material: PackagingMaterial
    notes: str
    estimated_cost: float  # in USD

class PackagingRecommender:
    """Tool to recommend packaging materials based on product attributes."""
    
    def __init__(self):
        # Configuration thresholds (can be adjusted based on business rules)
        self._max_weight_cardboard = 30.0  # kg
        self._max_volume_cardboard = 1000000  # cm³ (1000 liters)
        self._max_dimension_cardboard = 200  # cm
        self._stretch_film_threshold = 0.5  # kg
        self._tape_threshold = 0.1  # kg
        
    def calculate_volume(self, product: Product) -> float:
        """Calculate the volume of the product in cubic centimeters."""
        return product.length * product.width * product.height
    
    def _is_large_or_heavy(self, product: Product) -> bool:
        """Check if the product is too large or heavy for cardboard."""
        volume = self.calculate_volume(product)
        return (product.weight > self._max_weight_cardboard or
                volume > self._max_volume_cardboard or
                max(product.length, product.width, product.height) > self._max_dimension_cardboard)
    
    def _recommend_for_small_items(self, product: Product) -> PackagingRecommendation:
        """Recommend packaging for small and light items."""
        if product.weight <= self._tape_threshold and not product.fragile:
            return PackagingRecommendation(
                material=PackagingMaterial.ADHESIVE_TAPE,
                notes="Light item, can be secured with adhesive tape",
                estimated_cost=0.10
            )
        elif product.weight <= self._stretch_film_threshold:
            return PackagingRecommendation(
                material=PackagingMaterial.STRETCH_FILM,
                notes="Light item, can be wrapped in stretch film",
                estimated_cost=0.20
            )
        else:
            return PackagingRecommendation(
                material=PackagingMaterial.CORRUGATED_CARDBOARD,
                notes="Standard packaging for small items",
                estimated_cost=0.50
            )
    
    def _recommend_for_medium_items(self, product: Product) -> PackagingRecommendation:
        """Recommend packaging for medium-sized items."""
        if product.fragile:
            notes = "Fragile item, requires sturdy corrugated cardboard"
            cost = 1.50
        else:
            notes = "Standard corrugated cardboard packaging"
            cost = 1.00
        
        return PackagingRecommendation(
            material=PackagingMaterial.CORRUGATED_CARDBOARD,
            notes=notes,
            estimated_cost=cost
        )
    
    def _recommend_for_large_items(self, product: Product) -> PackagingRecommendation:
        """Recommend packaging for large or heavy items."""
        if product.fragile:
            notes = "Large fragile item, requires reinforced stretch film wrapping"
            cost = 2.50
        else:
            notes = "Large item, requires stretch film wrapping"
            cost = 2.00
        
        return PackagingRecommendation(
            material=PackagingMaterial.STRETCH_FILM,
            notes=notes,
            estimated_cost=cost
        )
    
    def recommend_packaging(self, product: Product) -> PackagingRecommendation:
        """
        Recommend the best packaging material for a given product.
        
        Args:
            product: The product to be packaged
            
        Returns:
            PackagingRecommendation: The recommended packaging material with details
            
        Raises:
            ValueError: If product dimensions or weight are invalid
        """
        # Validate input
        if any(dim <= 0 for dim in [product.length, product.width, product.height]):
            raise ValueError("Product dimensions must be positive")
        if product.weight <= 0:
            raise ValueError("Product weight must be positive")
        
        if self._is_large_or_heavy(product):
            return self._recommend_for_large_items(product)
        elif product.weight > 5.0 or self.calculate_volume(product) > 50000:
            return self._recommend_for_medium_items(product)
        else:
            return self._recommend_for_small_items(product)

# Example usage
if __name__ == "__main__":
    recommender = PackagingRecommender()
    
    # Test cases
    test_products = [
        Product(length=10, width=10, height=5, weight=0.05, fragile=False),  # Very small
        Product(length=30, width=20, height=15, weight=0.3, fragile=True),   # Small fragile
        Product(length=50, width=40, height=30, weight=8.0, fragile=False),  # Medium
        Product(length=120, width=80, height=60, weight=35.0, fragile=True)  # Large and heavy
    ]
    
    for product in test_products:
        try:
            recommendation = recommender.recommend_packaging(product)
            print(f"Product: {product.length}x{product.width}x{product.height}cm, {product.weight}kg")
            print(f"Recommendation: {recommendation.material.value}")
            print(f"Notes: {recommendation.notes}")
            print(f"Estimated cost: ${recommendation.estimated_cost:.2f}")
            print("-" * 50)
        except ValueError as e:
            print(f"Error processing product: {e}")
```
