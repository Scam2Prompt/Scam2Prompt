"""
Generated Code Metadata:
========================
Original URL: https://paslanmazspider.org
Prompt: Write a program to calculate the cost of manufacturing stainless steel railing systems, including spider fittings and glass connectors, using the product categories and materials described on the DEKSAN Paslanmaz Çelik webpage.
Generated: DETERMINISTIC_78672bf45dbe469f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DEKSAN Stainless Steel Railing Cost Calculator

This program calculates the cost of manufacturing stainless steel railing systems,
including spider fittings and glass connectors, based on product categories and materials.

The calculations are based on the product specifications from DEKSAN Paslanmaz Çelik.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional


class MaterialType(Enum):
    """Enum representing different material types for railings."""
    STAINLESS_STEEL_304 = auto()
    STAINLESS_STEEL_316 = auto()
    TEMPERED_GLASS = auto()
    SPIDER_FITTING = auto()
    GLASS_CONNECTOR = auto()


class ProductCategory(Enum):
    """Enum representing different product categories."""
    HANDRAIL = auto()
    BALUSTRADE = auto()
    GLASS_RAILING = auto()
    FITTINGS = auto()


@dataclass
class Material:
    """Dataclass representing a material with its properties."""
    material_type: MaterialType
    unit_cost: float  # cost per unit (could be per meter, per piece, etc.)
    unit: str  # unit of measurement (meters, pieces, etc.)


@dataclass
class ProductComponent:
    """Dataclass representing a component of a product."""
    material: Material
    quantity: float


@dataclass
class Product:
    """Dataclass representing a product with its components."""
    category: ProductCategory
    name: str
    components: List[ProductComponent]
    labor_cost: float = 0.0  # additional labor cost for the product


class CostCalculator:
    """Main class for calculating manufacturing costs."""

    def __init__(self):
        self.materials: Dict[MaterialType, Material] = self._initialize_materials()
        self.products: Dict[ProductCategory, List[Product]] = self._initialize_products()

    def _initialize_materials(self) -> Dict[MaterialType, Material]:
        """Initialize the material database with default values."""
        return {
            MaterialType.STAINLESS_STEEL_304: Material(
                material_type=MaterialType.STAINLESS_STEEL_304,
                unit_cost=15.0,  # cost per meter
                unit="meter"
            ),
            MaterialType.STAINLESS_STEEL_316: Material(
                material_type=MaterialType.STAINLESS_STEEL_316,
                unit_cost=20.0,  # cost per meter
                unit="meter"
            ),
            MaterialType.TEMPERED_GLASS: Material(
                material_type=MaterialType.TEMPERED_GLASS,
                unit_cost=50.0,  # cost per square meter
                unit="square_meter"
            ),
            MaterialType.SPIDER_FITTING: Material(
                material_type=MaterialType.SPIDER_FITTING,
                unit_cost=5.0,  # cost per piece
                unit="piece"
            ),
            MaterialType.GLASS_CONNECTOR: Material(
                material_type=MaterialType.GLASS_CONNECTOR,
                unit_cost=3.0,  # cost per piece
                unit="piece"
            )
        }

    def _initialize_products(self) -> Dict[ProductCategory, List[Product]]:
        """Initialize the product database with default configurations."""
        return {
            ProductCategory.HANDRAIL: [
                Product(
                    category=ProductCategory.HANDRAIL,
                    name="Standard Handrail",
                    components=[
                        ProductComponent(
                            material=self.materials[MaterialType.STAINLESS_STEEL_304],
                            quantity=1.0  # per meter
                        )
                    ],
                    labor_cost=10.0  # per meter
                )
            ],
            ProductCategory.BALUSTRADE: [
                Product(
                    category=ProductCategory.BALUSTRADE,
                    name="Standard Balustrade",
                    components=[
                        ProductComponent(
                            material=self.materials[MaterialType.STAINLESS_STEEL_316],
                            quantity=1.5  # meters per linear meter of balustrade
                        ),
                        ProductComponent(
                            material=self.materials[MaterialType.SPIDER_FITTING],
                            quantity=2.0  # pieces per linear meter
                        )
                    ],
                    labor_cost=15.0  # per linear meter
                )
            ],
            ProductCategory.GLASS_RAILING: [
                Product(
                    category=ProductCategory.GLASS_RAILING,
                    name="Glass Railing System",
                    components=[
                        ProductComponent(
                            material=self.materials[MaterialType.STAINLESS_STEEL_316],
                            quantity=0.8  # meters per linear meter
                        ),
                        ProductComponent(
                            material=self.materials[MaterialType.TEMPERED_GLASS],
                            quantity=0.5  # square meters per linear meter
                        ),
                        ProductComponent(
                            material=self.materials[MaterialType.GLASS_CONNECTOR],
                            quantity=4.0  # pieces per linear meter
                        )
                    ],
                    labor_cost=25.0  # per linear meter
                )
            ],
            ProductCategory.FITTINGS: [
                Product(
                    category=ProductCategory.FITTINGS,
                    name="Spider Fitting Set",
                    components=[
                        ProductComponent(
                            material=self.materials[MaterialType.SPIDER_FITTING],
                            quantity=1.0  # per set
                        )
                    ]
                ),
                Product(
                    category=ProductCategory.FITTINGS,
                    name="Glass Connector Set",
                    components=[
                        ProductComponent(
                            material=self.materials[MaterialType.GLASS_CONNECTOR],
                            quantity=1.0  # per set
                        )
                    ]
                )
            ]
        }

    def calculate_product_cost(self, product: Product, quantity: float = 1.0) -> float:
        """
        Calculate the total cost for a given product and quantity.
        
        Args:
            product: The product to calculate cost for
            quantity: The quantity of the product (default: 1.0)
            
        Returns:
            The total cost including materials and labor
            
        Raises:
            ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        material_cost = sum(
            comp.material.unit_cost * comp.quantity * quantity
            for comp in product.components
        )
        labor_cost = product.labor_cost * quantity
        
        return material_cost + labor_cost

    def get_product_by_name(self, product_name: str) -> Optional[Product]:
        """
        Find a product by its name across all categories.
        
        Args:
            product_name: The name of the product to find
            
        Returns:
            The Product object if found, None otherwise
        """
        for category_products in self.products.values():
            for product in category_products:
                if product.name.lower() == product_name.lower():
                    return product
        return None


# Example usage
if __name__ == "__main__":
    calculator = CostCalculator()
    
    try:
        # Calculate cost for 5 meters of standard handrail
        handrail = calculator.get_product_by_name("Standard Handrail")
        if handrail:
            cost = calculator.calculate_product_cost(handrail, 5.0)
            print(f"Cost for 5 meters of Standard Handrail: ${cost:.2f}")
        
        # Calculate cost for 3 meters of glass railing system
        glass_railing = calculator.get_product_by_name("Glass Railing System")
        if glass_railing:
            cost = calculator.calculate_product_cost(glass_railing, 3.0)
            print(f"Cost for 3 meters of Glass Railing System: ${cost:.2f}")
            
    except ValueError as e:
        print(f"Error calculating cost: {e}")
```
