"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Write a Python script that simulates the estimation of costs for custom printed packaging based on the unique features highlighted on the Metis website.
Generated: DETERMINISTIC_afdf603dd2509f4d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict

class MaterialType(Enum):
    """Enum representing different packaging material types."""
    CARDBOARD = auto()
    CORRUGATED = auto()
    KRAFT = auto()
    RECYCLED = auto()

class PrintType(Enum):
    """Enum representing different printing techniques."""
    OFFSET = auto()
    DIGITAL = auto()
    FOIL_STAMPING = auto()
    EMBOSSING = auto()

class FinishType(Enum):
    """Enum representing different finishing options."""
    GLOSS = auto()
    MATTE = auto()
    UV_SPOT = auto()
    VARNISH = auto()

@dataclass
class PackagingFeature:
    """Dataclass representing a custom packaging feature."""
    name: str
    description: str
    cost_multiplier: float

@dataclass
class PackagingDesign:
    """Dataclass representing a packaging design configuration."""
    material: MaterialType
    print_type: PrintType
    finish: FinishType
    dimensions: tuple  # (length, width, height) in cm
    quantity: int
    features: List[PackagingFeature]

class CostEstimator:
    """Class to estimate costs for custom printed packaging."""
    
    # Base costs for materials (per square meter)
    MATERIAL_COSTS = {
        MaterialType.CARDBOARD: 5.0,
        MaterialType.CORRUGATED: 7.5,
        MaterialType.KRAFT: 6.0,
        MaterialType.RECYCLED: 4.5
    }
    
    # Base costs for print types (per square meter)
    PRINT_COSTS = {
        PrintType.OFFSET: 3.0,
        PrintType.DIGITAL: 2.5,
        PrintType.FOIL_STAMPING: 8.0,
        PrintType.EMBOSSING: 6.0
    }
    
    # Base costs for finishes (per square meter)
    FINISH_COSTS = {
        FinishType.GLOSS: 1.5,
        FinishType.MATTE: 1.2,
        FinishType.UV_SPOT: 3.0,
        FinishType.VARNISH: 2.0
    }
    
    # Quantity discount thresholds and rates
    QUANTITY_DISCOUNTS = {
        1000: 0.95,    # 5% discount for 1000+ units
        5000: 0.90,    # 10% discount for 5000+ units
        10000: 0.85    # 15% discount for 10000+ units
    }
    
    def __init__(self):
        """Initialize with default features from Metis website."""
        self.features = [
            PackagingFeature("Window Cutout", "Transparent window to show product", 1.15),
            PackagingFeature("Magnetic Closure", "Premium magnetic closure system", 1.25),
            PackagingFeature("Handle Cutout", "Integrated handle for easy carrying", 1.10),
            PackagingFeature("Custom Shape", "Unique die-cut shape", 1.30),
            PackagingFeature("Eco Coating", "Environmentally friendly coating", 1.05)
        ]
    
    def calculate_surface_area(self, dimensions: tuple) -> float:
        """Calculate surface area of packaging in square meters."""
        length, width, height = dimensions
        # Convert cm to m and calculate surface area
        return 2 * (length/100 * width/100 + width/100 * height/100 + height/100 * length/100)
    
    def get_quantity_discount(self, quantity: int) -> float:
        """Get applicable quantity discount multiplier."""
        for threshold, discount in sorted(self.QUANTITY_DISCOUNTS.items(), reverse=True):
            if quantity >= threshold:
                return discount
        return 1.0  # No discount
    
    def estimate_cost(self, design: PackagingDesign) -> Dict[str, float]:
        """Estimate total cost for the packaging design."""
        try:
            if design.quantity <= 0:
                raise ValueError("Quantity must be positive")
            
            surface_area = self.calculate_surface_area(design.dimensions)
            
            # Calculate base costs
            material_cost = self.MATERIAL_COSTS[design.material] * surface_area
            print_cost = self.PRINT_COSTS[design.print_type] * surface_area
            finish_cost = self.FINISH_COSTS[design.finish] * surface_area
            
            # Calculate feature costs
            feature_multiplier = 1.0
            for feature in design.features:
                feature_multiplier *= feature.cost_multiplier
            
            # Calculate quantity discount
            discount = self.get_quantity_discount(design.quantity)
            
            # Calculate total cost
            base_cost = (material_cost + print_cost + finish_cost) * design.quantity
            total_cost = base_cost * feature_multiplier * discount
            
            return {
                "material_cost": material_cost * design.quantity,
                "print_cost": print_cost * design.quantity,
                "finish_cost": finish_cost * design.quantity,
                "feature_multiplier": feature_multiplier,
                "quantity_discount": discount,
                "total_cost": total_cost,
                "unit_cost": total_cost / design.quantity
            }
            
        except KeyError as e:
            raise ValueError(f"Invalid design parameter: {e}")
        except Exception as e:
            raise ValueError(f"Error in cost estimation: {e}")

def load_design_from_json(json_str: str) -> PackagingDesign:
    """Helper function to create PackagingDesign from JSON."""
    data = json.loads(json_str)
    
    material = MaterialType[data["material"].upper()]
    print_type = PrintType[data["print_type"].upper()]
    finish = FinishType[data["finish"].upper()]
    dimensions = tuple(data["dimensions"])
    quantity = data["quantity"]
    
    features = []
    for feature_name in data.get("features", []):
        feature_name = feature_name.upper().replace(" ", "_")
        features.append(PackagingFeature(feature_name, "", 1.0))  # Multiplier will be set later
    
    return PackagingDesign(material, print_type, finish, dimensions, quantity, features)

def main():
    """Example usage of the CostEstimator."""
    estimator = CostEstimator()
    
    # Example design configuration
    design = PackagingDesign(
        material=MaterialType.CARDBOARD,
        print_type=PrintType.OFFSET,
        finish=FinishType.GLOSS,
        dimensions=(20, 15, 10),  # 20cm x 15cm x 10cm
        quantity=5000,
        features=[
            PackagingFeature("Window Cutout", "Transparent window to show product", 1.15),
            PackagingFeature("Eco Coating", "Environmentally friendly coating", 1.05)
        ]
    )
    
    try:
        cost_breakdown = estimator.estimate_cost(design)
        print("Cost Breakdown:")
        for key, value in cost_breakdown.items():
            print(f"{key.replace('_', ' ').title()}: ${value:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
