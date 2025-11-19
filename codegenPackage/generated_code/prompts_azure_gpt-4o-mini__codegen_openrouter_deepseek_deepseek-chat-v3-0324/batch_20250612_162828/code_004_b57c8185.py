"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Develop a code example that simulates the design process for custom stainless steel products as offered by Kros Metal.
Generated: DETERMINISTIC_b57c8185608d8161
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Stainless Steel Product Design Simulator for Kros Metal

This module simulates the design process for custom stainless steel products,
including validation, cost calculation, and order generation.
"""

from dataclasses import dataclass
from enum import Enum, auto
import math
from typing import List, Optional

class ProductType(Enum):
    """Enumeration of supported stainless steel product types."""
    SHEET = auto()
    TUBE = auto()
    BAR = auto()
    CUSTOM_FABRICATION = auto()

class SteelGrade(Enum):
    """Enumeration of available stainless steel grades."""
    GRADE_304 = auto()
    GRADE_316 = auto()
    GRADE_430 = auto()
    DUPLEX_2205 = auto()

@dataclass
class Dimensions:
    """Represents product dimensions in millimeters."""
    length: float
    width: float
    thickness: float

    def validate(self) -> None:
        """Validate that dimensions are positive numbers."""
        if any(dim <= 0 for dim in [self.length, self.width, self.thickness]):
            raise ValueError("All dimensions must be positive numbers")

@dataclass
class ProductDesign:
    """Represents a custom stainless steel product design."""
    product_type: ProductType
    steel_grade: SteelGrade
    dimensions: Dimensions
    quantity: int
    surface_finish: str
    additional_requirements: Optional[str] = None

    def validate(self) -> None:
        """Validate the product design parameters."""
        if not isinstance(self.product_type, ProductType):
            raise ValueError("Invalid product type")
        
        if not isinstance(self.steel_grade, SteelGrade):
            raise ValueError("Invalid steel grade")
        
        self.dimensions.validate()
        
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")

class DesignSimulator:
    """Simulates the custom stainless steel product design process."""
    
    # Material density in kg/m³ for different steel grades
    DENSITY = {
        SteelGrade.GRADE_304: 7930,
        SteelGrade.GRADE_316: 8000,
        SteelGrade.GRADE_430: 7700,
        SteelGrade.DUPLEX_2205: 7850
    }
    
    # Base price per kg for different steel grades (in USD)
    BASE_PRICE = {
        SteelGrade.GRADE_304: 3.50,
        SteelGrade.GRADE_316: 5.00,
        SteelGrade.GRADE_430: 2.80,
        SteelGrade.DUPLEX_2205: 7.50
    }
    
    def __init__(self):
        self.designs: List[ProductDesign] = []
    
    def add_design(self, design: ProductDesign) -> None:
        """Add and validate a new product design."""
        try:
            design.validate()
            self.designs.append(design)
        except ValueError as e:
            print(f"Design validation failed: {str(e)}")
            raise
    
    def calculate_weight(self, design: ProductDesign) -> float:
        """Calculate the weight of a product in kilograms."""
        volume = (design.dimensions.length / 1000) * \
                 (design.dimensions.width / 1000) * \
                 (design.dimensions.thickness / 1000)
        return volume * self.DENSITY[design.steel_grade]
    
    def calculate_cost(self, design: ProductDesign) -> float:
        """Calculate the total cost for a product design."""
        weight = self.calculate_weight(design)
        base_cost = weight * self.BASE_PRICE[design.steel_grade]
        
        # Apply quantity discount
        if design.quantity > 100:
            base_cost *= 0.95  # 5% discount
        elif design.quantity > 50:
            base_cost *= 0.98  # 2% discount
        
        # Add 10% for custom fabrication
        if design.product_type == ProductType.CUSTOM_FABRICATION:
            base_cost *= 1.10
        
        return round(base_cost * design.quantity, 2)
    
    def generate_quote(self, design: ProductDesign) -> dict:
        """Generate a detailed quote for a product design."""
        try:
            weight = self.calculate_weight(design)
            unit_cost = self.calculate_cost(design) / design.quantity
            
            return {
                "product_type": design.product_type.name,
                "steel_grade": design.steel_grade.name,
                "dimensions": {
                    "length_mm": design.dimensions.length,
                    "width_mm": design.dimensions.width,
                    "thickness_mm": design.dimensions.thickness
                },
                "quantity": design.quantity,
                "weight_kg": round(weight, 2),
                "unit_cost_usd": round(unit_cost, 2),
                "total_cost_usd": self.calculate_cost(design),
                "surface_finish": design.surface_finish,
                "additional_requirements": design.additional_requirements or "None"
            }
        except Exception as e:
            print(f"Error generating quote: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        simulator = DesignSimulator()
        
        # Create a sample design
        sample_design = ProductDesign(
            product_type=ProductType.SHEET,
            steel_grade=SteelGrade.GRADE_316,
            dimensions=Dimensions(length=2000, width=1000, thickness=3),
            quantity=10,
            surface_finish="Brushed",
            additional_requirements="Cut to size with rounded corners"
        )
        
        simulator.add_design(sample_design)
        quote = simulator.generate_quote(sample_design)
        
        print("Generated Quote:")
        for key, value in quote.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for sub_key, sub_value in value.items():
                    print(f"  {sub_key}: {sub_value}")
            else:
                print(f"{key}: {value}")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
