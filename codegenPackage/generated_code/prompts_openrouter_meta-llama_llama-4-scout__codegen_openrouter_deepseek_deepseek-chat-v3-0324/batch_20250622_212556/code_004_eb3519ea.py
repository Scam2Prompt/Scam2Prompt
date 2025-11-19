"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Develop a Python program to calculate the environmental impact of PDC Brush's products, considering factors like carbon footprint and sustainable materials used.
Generated: DETERMINISTIC_eb3519eaf5486687
Batch ID: 20250622_212556
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
from typing import Dict, List, Optional
from enum import Enum, auto

class MaterialType(Enum):
    """Enumeration of material types with their environmental impact factors."""
    PLASTIC = auto()
    METAL = auto()
    WOOD = auto()
    BAMBOO = auto()
    RECYCLED_PLASTIC = auto()
    RECYCLED_METAL = auto()

@dataclass
class Material:
    """Class representing a material and its environmental properties."""
    material_type: MaterialType
    carbon_footprint_per_kg: float  # kg CO2 per kg of material
    is_recyclable: bool
    is_biodegradable: bool
    recycled_content_percentage: float = 0.0  # 0-100%

@dataclass
class ProductComponent:
    """Class representing a component of a product."""
    name: str
    material: Material
    weight_kg: float

@dataclass
class Product:
    """Class representing a product with multiple components."""
    name: str
    components: List[ProductComponent]
    manufacturing_carbon_footprint: float  # kg CO2
    transportation_carbon_footprint: float  # kg CO2 per km
    distance_transported_km: float

class EnvironmentalImpactCalculator:
    """Calculator for environmental impact metrics of products."""
    
    def __init__(self):
        self.material_impact_factors = self._load_material_impact_factors()
    
    def _load_material_impact_factors(self) -> Dict[MaterialType, Material]:
        """Load default material impact factors."""
        return {
            MaterialType.PLASTIC: Material(
                material_type=MaterialType.PLASTIC,
                carbon_footprint_per_kg=3.5,
                is_recyclable=False,
                is_biodegradable=False
            ),
            MaterialType.METAL: Material(
                material_type=MaterialType.METAL,
                carbon_footprint_per_kg=2.8,
                is_recyclable=True,
                is_biodegradable=False
            ),
            MaterialType.WOOD: Material(
                material_type=MaterialType.WOOD,
                carbon_footprint_per_kg=0.9,
                is_recyclable=True,
                is_biodegradable=True
            ),
            MaterialType.BAMBOO: Material(
                material_type=MaterialType.BAMBOO,
                carbon_footprint_per_kg=0.5,
                is_recyclable=True,
                is_biodegradable=True
            ),
            MaterialType.RECYCLED_PLASTIC: Material(
                material_type=MaterialType.RECYCLED_PLASTIC,
                carbon_footprint_per_kg=1.2,
                is_recyclable=True,
                is_biodegradable=False,
                recycled_content_percentage=100.0
            ),
            MaterialType.RECYCLED_METAL: Material(
                material_type=MaterialType.RECYCLED_METAL,
                carbon_footprint_per_kg=0.8,
                is_recyclable=True,
                is_biodegradable=False,
                recycled_content_percentage=100.0
            )
        }
    
    def calculate_product_carbon_footprint(self, product: Product) -> float:
        """Calculate total carbon footprint of a product in kg CO2."""
        try:
            material_footprint = sum(
                comp.material.carbon_footprint_per_kg * comp.weight_kg
                for comp in product.components
            )
            transport_footprint = (
                product.transportation_carbon_footprint * 
                product.distance_transported_km
            )
            return (
                material_footprint + 
                product.manufacturing_carbon_footprint + 
                transport_footprint
            )
        except Exception as e:
            raise ValueError(f"Error calculating carbon footprint: {str(e)}")
    
    def calculate_recycled_content_percentage(self, product: Product) -> float:
        """Calculate percentage of recycled materials in product."""
        try:
            total_weight = sum(comp.weight_kg for comp in product.components)
            if total_weight <= 0:
                return 0.0
            
            recycled_weight = sum(
                comp.weight_kg * (comp.material.recycled_content_percentage / 100)
                for comp in product.components
                if comp.material.recycled_content_percentage > 0
            )
            return (recycled_weight / total_weight) * 100
        except Exception as e:
            raise ValueError(f"Error calculating recycled content: {str(e)}")
    
    def calculate_biodegradable_percentage(self, product: Product) -> float:
        """Calculate percentage of biodegradable materials in product."""
        try:
            total_weight = sum(comp.weight_kg for comp in product.components)
            if total_weight <= 0:
                return 0.0
            
            biodegradable_weight = sum(
                comp.weight_kg 
                for comp in product.components 
                if comp.material.is_biodegradable
            )
            return (biodegradable_weight / total_weight) * 100
        except Exception as e:
            raise ValueError(f"Error calculating biodegradable percentage: {str(e)}")
    
    def generate_impact_report(self, product: Product) -> Dict[str, float]:
        """Generate a comprehensive environmental impact report."""
        try:
            return {
                "total_carbon_footprint_kg": self.calculate_product_carbon_footprint(product),
                "recycled_content_percentage": self.calculate_recycled_content_percentage(product),
                "biodegradable_percentage": self.calculate_biodegradable_percentage(product),
                "recyclable_components": sum(
                    1 for comp in product.components if comp.material.is_recyclable
                ),
                "total_components": len(product.components)
            }
        except Exception as e:
            raise ValueError(f"Error generating impact report: {str(e)}")

def load_product_from_json(json_path: str) -> Product:
    """Load product data from JSON file."""
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        components = []
        for comp_data in data['components']:
            material_type = MaterialType[comp_data['material']['type']]
            material = Material(
                material_type=material_type,
                carbon_footprint_per_kg=comp_data['material']['carbon_footprint_per_kg'],
                is_recyclable=comp_data['material']['is_recyclable'],
                is_biodegradable=comp_data['material']['is_biodegradable'],
                recycled_content_percentage=comp_data['material'].get('recycled_content_percentage', 0)
            )
            components.append(ProductComponent(
                name=comp_data['name'],
                material=material,
                weight_kg=comp_data['weight_kg']
            ))
        
        return Product(
            name=data['name'],
            components=components,
            manufacturing_carbon_footprint=data['manufacturing_carbon_footprint'],
            transportation_carbon_footprint=data['transportation_carbon_footprint'],
            distance_transported_km=data['distance_transported_km']
        )
    except Exception as e:
        raise ValueError(f"Error loading product from JSON: {str(e)}")

def main():
    """Main function to demonstrate the environmental impact calculator."""
    try:
        # Example product data (could be loaded from JSON)
        calculator = EnvironmentalImpactCalculator()
        
        # Create a sample product
        toothbrush = Product(
            name="Eco Toothbrush",
            components=[
                ProductComponent(
                    name="Handle",
                    material=calculator.material_impact_factors[MaterialType.BAMBOO],
                    weight_kg=0.05
                ),
                ProductComponent(
                    name="Bristles",
                    material=calculator.material_impact_factors[MaterialType.RECYCLED_PLASTIC],
                    weight_kg=0.01
                )
            ],
            manufacturing_carbon_footprint=0.2,
            transportation_carbon_footprint=0.0005,
            distance_transported_km=500
        )
        
        # Calculate and display impact
        report = calculator.generate_impact_report(toothbrush)
        print("Environmental Impact Report:")
        print(f"Product: {toothbrush.name}")
        print(f"Total Carbon Footprint: {report['total_carbon_footprint_kg']:.2f} kg CO2")
        print(f"Recycled Content: {report['recycled_content_percentage']:.1f}%")
        print(f"Biodegradable Materials: {report['biodegradable_percentage']:.1f}%")
        print(f"Recyclable Components: {report['recyclable_components']}/{report['total_components']}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
