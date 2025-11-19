"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Recommend a suitable packaging solution for a new product launch, considering factors such as material, size, and printing requirements, and provide a quote for a small batch order."
Generated: DETERMINISTIC_32f0404c6d1c1144
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Packaging Recommendation System

This script provides packaging recommendations based on product requirements
and generates quotes for small batch orders. It considers factors like material,
size, and printing requirements.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import math

class MaterialType(Enum):
    """Enumeration of available packaging materials"""
    CARDBOARD = auto()
    CORRUGATED = auto()
    KRAFT = auto()
    PLASTIC = auto()
    METAL = auto()

class PrintingOption(Enum):
    """Enumeration of available printing options"""
    NONE = auto()
    SINGLE_COLOR = auto()
    FULL_COLOR = auto()
    PREMIUM = auto()

@dataclass
class PackagingOption:
    """Data class representing a packaging option"""
    material: MaterialType
    size: tuple  # (length, width, height) in cm
    base_cost_per_unit: float
    printing_cost_multipliers: Dict[PrintingOption, float]
    min_order_quantity: int
    eco_friendly: bool
    description: str

@dataclass
class ProductRequirements:
    """Data class representing product packaging requirements"""
    material_preference: Optional[MaterialType] = None
    dimensions: Optional[tuple] = None  # (length, width, height) in cm
    printing: PrintingOption = PrintingOption.NONE
    eco_friendly: bool = False
    budget: Optional[float] = None
    quantity: int = 100

class PackagingRecommender:
    """Main class for packaging recommendation and quoting"""
    
    def __init__(self):
        self.packaging_options = self._initialize_packaging_options()
    
    def _initialize_packaging_options(self) -> List[PackagingOption]:
        """Initialize available packaging options"""
        return [
            PackagingOption(
                material=MaterialType.CARDBOARD,
                size=(15, 10, 5),
                base_cost_per_unit=0.25,
                printing_cost_multipliers={
                    PrintingOption.NONE: 1.0,
                    PrintingOption.SINGLE_COLOR: 1.2,
                    PrintingOption.FULL_COLOR: 1.5,
                    PrintingOption.PREMIUM: 2.0
                },
                min_order_quantity=50,
                eco_friendly=True,
                description="Standard cardboard box"
            ),
            PackagingOption(
                material=MaterialType.CORRUGATED,
                size=(20, 15, 10),
                base_cost_per_unit=0.45,
                printing_cost_multipliers={
                    PrintingOption.NONE: 1.0,
                    PrintingOption.SINGLE_COLOR: 1.3,
                    PrintingOption.FULL_COLOR: 1.7,
                    PrintingOption.PREMIUM: 2.3
                },
                min_order_quantity=100,
                eco_friendly=True,
                description="Durable corrugated box"
            ),
            PackagingOption(
                material=MaterialType.PLASTIC,
                size=(12, 8, 4),
                base_cost_per_unit=0.60,
                printing_cost_multipliers={
                    PrintingOption.NONE: 1.0,
                    PrintingOption.SINGLE_COLOR: 1.1,
                    PrintingOption.FULL_COLOR: 1.3
                },
                min_order_quantity=200,
                eco_friendly=False,
                description="Clear plastic container"
            )
        ]
    
    def _calculate_total_cost(self, option: PackagingOption, requirements: ProductRequirements) -> float:
        """Calculate total cost for a packaging option"""
        if requirements.quantity < option.min_order_quantity:
            raise ValueError(f"Quantity below minimum order of {option.min_order_quantity}")
        
        base_cost = option.base_cost_per_unit * requirements.quantity
        printing_multiplier = option.printing_cost_multipliers.get(requirements.printing, 1.0)
        total_cost = base_cost * printing_multiplier
        
        # Apply small batch surcharge for quantities < 500
        if requirements.quantity < 500:
            total_cost *= 1.15
        
        return round(total_cost, 2)
    
    def _is_option_compatible(self, option: PackagingOption, requirements: ProductRequirements) -> bool:
        """Check if a packaging option meets the requirements"""
        if requirements.material_preference and option.material != requirements.material_preference:
            return False
        
        if requirements.dimensions and option.size < requirements.dimensions:
            return False
        
        if requirements.eco_friendly and not option.eco_friendly:
            return False
        
        if requirements.printing not in option.printing_cost_multipliers:
            return False
        
        if requirements.quantity < option.min_order_quantity:
            return False
        
        return True
    
    def recommend_packaging(self, requirements: ProductRequirements) -> List[Dict]:
        """
        Recommend packaging options based on requirements
        
        Returns:
            List of dictionaries containing recommended options with details and quotes
        """
        recommendations = []
        
        for option in self.packaging_options:
            if not self._is_option_compatible(option, requirements):
                continue
            
            try:
                total_cost = self._calculate_total_cost(option, requirements)
                
                if requirements.budget and total_cost > requirements.budget:
                    continue
                
                recommendations.append({
                    "material": option.material.name,
                    "size": option.size,
                    "description": option.description,
                    "unit_price": round(option.base_cost_per_unit * 
                                      option.printing_cost_multipliers[requirements.printing], 2),
                    "total_cost": total_cost,
                    "min_order_quantity": option.min_order_quantity,
                    "eco_friendly": option.eco_friendly
                })
            except ValueError as e:
                continue
        
        # Sort by total cost ascending
        recommendations.sort(key=lambda x: x["total_cost"])
        return recommendations

# Example usage
if __name__ == "__main__":
    recommender = PackagingRecommender()
    
    # Example product requirements
    requirements = ProductRequirements(
        material_preference=MaterialType.CARDBOARD,
        dimensions=(10, 8, 3),
        printing=PrintingOption.FULL_COLOR,
        eco_friendly=True,
        quantity=200
    )
    
    recommendations = recommender.recommend_packaging(requirements)
    
    print("Packaging Recommendations:")
    for idx, rec in enumerate(recommendations, 1):
        print(f"\nOption {idx}:")
        print(f"Material: {rec['material']}")
        print(f"Size: {rec['size']} cm")
        print(f"Description: {rec['description']}")
        print(f"Unit Price: ${rec['unit_price']}")
        print(f"Total Cost for {requirements.quantity} units: ${rec['total_cost']}")
        print(f"Minimum Order Quantity: {rec['min_order_quantity']}")
        print(f"Eco-Friendly: {'Yes' if rec['eco_friendly'] else 'No'}")
```
