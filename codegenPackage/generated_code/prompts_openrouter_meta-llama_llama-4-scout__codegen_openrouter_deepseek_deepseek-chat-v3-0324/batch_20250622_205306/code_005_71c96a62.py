"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a code snippet to calculate the environmental impact of packaging materials used for exporting fruits, considering factors like carbon footprint and recyclability."
Generated: DETERMINISTIC_71c96a62e4447689
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PackagingMaterial:
    """Represents a packaging material with environmental impact attributes."""
    
    def __init__(self, name: str, carbon_footprint: float, recyclability: float):
        """
        Initialize a packaging material.
        
        Args:
            name: Name of the material
            carbon_footprint: CO2 emissions per kg (in kg CO2/kg)
            recyclability: Percentage of material that can be recycled (0-1)
        """
        self.name = name
        self.carbon_footprint = carbon_footprint
        self.recyclability = recyclability

class FruitExport:
    """Calculates environmental impact of fruit exports based on packaging."""
    
    def __init__(self, materials: List[PackagingMaterial]):
        """
        Initialize with available packaging materials.
        
        Args:
            materials: List of PackagingMaterial objects
        """
        self.materials = {m.name: m for m in materials}
    
    def calculate_impact(
        self,
        material_name: str,
        weight_kg: float,
        distance_km: float,
        transport_carbon: float = 0.1  # default: kg CO2/km per kg
    ) -> Dict[str, Optional[float]]:
        """
        Calculate environmental impact for a shipment.
        
        Args:
            material_name: Name of packaging material
            weight_kg: Total weight of packaging in kg
            distance_km: Transport distance in km
            transport_carbon: Carbon footprint of transport per km per kg
            
        Returns:
            Dictionary with impact metrics or None if material not found
        """
        result = {
            'total_carbon': None,
            'transport_carbon': None,
            'packaging_carbon': None,
            'recyclability': None
        }
        
        if material_name not in self.materials:
            return result
            
        material = self.materials[material_name]
        
        # Calculate carbon components
        transport_carbon_total = distance_km * weight_kg * transport_carbon
        packaging_carbon_total = weight_kg * material.carbon_footprint
        
        result.update({
            'transport_carbon': transport_carbon_total,
            'packaging_carbon': packaging_carbon_total,
            'total_carbon': transport_carbon_total + packaging_carbon_total,
            'recyclability': material.recyclability
        })
        
        return result
    
    @classmethod
    def load_materials_from_json(cls, filepath: str) -> 'FruitExport':
        """
        Create FruitExport instance from JSON file of materials.
        
        Args:
            filepath: Path to JSON file containing material data
            
        Returns:
            FruitExport instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
            KeyError: If required fields are missing in JSON
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        materials = [
            PackagingMaterial(
                name=item['name'],
                carbon_footprint=item['carbon_footprint'],
                recyclability=item['recyclability']
            )
            for item in data['materials']
        ]
        
        return cls(materials)

# Example usage
if __name__ == "__main__":
    # Sample materials data
    sample_materials = [
        PackagingMaterial("Cardboard", 0.5, 0.9),
        PackagingMaterial("Plastic", 2.5, 0.3),
        PackagingMaterial("Wood", 1.2, 0.7)
    ]
    
    exporter = FruitExport(sample_materials)
    
    # Calculate impact for a shipment
    impact = exporter.calculate_impact(
        material_name="Cardboard",
        weight_kg=100,
        distance_km=500
    )
    
    print("Environmental Impact:")
    for key, value in impact.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```
