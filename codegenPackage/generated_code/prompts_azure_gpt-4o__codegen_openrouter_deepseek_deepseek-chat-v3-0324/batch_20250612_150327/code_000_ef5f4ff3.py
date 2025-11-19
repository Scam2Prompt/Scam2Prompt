"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a Python script to calculate the environmental impact of using FSC-certified materials in cleaning tool production, referencing PDC Brush's sustainability practices.
Generated: DETERMINISTIC_ef5f4ff3f164dd78
Batch ID: 20250612_150327
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
from typing import Optional, Dict, List

@dataclass
class MaterialImpact:
    """Data class to store environmental impact metrics for a material."""
    name: str
    co2_emissions_kg: float  # CO2 emissions per kg of material
    water_usage_liters: float  # Water usage per kg of material
    land_use_m2: float  # Land use per kg of material
    is_fsc_certified: bool

@dataclass
class CleaningTool:
    """Data class to represent a cleaning tool and its material composition."""
    name: str
    materials: Dict[str, float]  # Material name to weight in kg

class SustainabilityCalculator:
    """Calculator for environmental impact of cleaning tools using FSC-certified materials."""
    
    def __init__(self, material_data: List[MaterialImpact]):
        """
        Initialize calculator with material impact data.
        
        Args:
            material_data: List of MaterialImpact objects containing impact metrics.
        """
        self.materials = {m.name: m for m in material_data}
    
    def calculate_impact(self, tool: CleaningTool) -> Dict[str, float]:
        """
        Calculate environmental impact for a cleaning tool.
        
        Args:
            tool: CleaningTool object representing the product.
            
        Returns:
            Dictionary with total CO2 emissions, water usage, and land use.
            
        Raises:
            ValueError: If material in tool is not found in the database.
        """
        total_co2 = 0.0
        total_water = 0.0
        total_land = 0.0
        
        for material_name, weight in tool.materials.items():
            if material_name not in self.materials:
                raise ValueError(f"Material '{material_name}' not found in database")
            
            material = self.materials[material_name]
            total_co2 += weight * material.co2_emissions_kg
            total_water += weight * material.water_usage_liters
            total_land += weight * material.land_use_m2
        
        return {
            'total_co2_kg': total_co2,
            'total_water_liters': total_water,
            'total_land_m2': total_land,
            'fsc_percentage': self._calculate_fsc_percentage(tool)
        }
    
    def _calculate_fsc_percentage(self, tool: CleaningTool) -> float:
        """
        Calculate percentage of FSC-certified materials by weight.
        
        Args:
            tool: CleaningTool object to analyze.
            
        Returns:
            Percentage (0-100) of FSC-certified materials.
        """
        total_weight = sum(tool.materials.values())
        if total_weight == 0:
            return 0.0
            
        fsc_weight = 0.0
        for material_name, weight in tool.materials.items():
            if self.materials[material_name].is_fsc_certified:
                fsc_weight += weight
                
        return (fsc_weight / total_weight) * 100

def load_material_data(filepath: str) -> List[MaterialImpact]:
    """
    Load material impact data from JSON file.
    
    Args:
        filepath: Path to JSON file containing material data.
        
    Returns:
        List of MaterialImpact objects.
        
    Raises:
        FileNotFoundError: If file doesn't exist.
        json.JSONDecodeError: If file has invalid JSON.
        KeyError: If required fields are missing in JSON.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        materials = []
        for item in data['materials']:
            materials.append(MaterialImpact(
                name=item['name'],
                co2_emissions_kg=item['co2_emissions_kg'],
                water_usage_liters=item['water_usage_liters'],
                land_use_m2=item['land_use_m2'],
                is_fsc_certified=item['is_fsc_certified']
            ))
            
        return materials
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Material data file not found at {filepath}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in material data file", doc="", pos=0)
    except KeyError as e:
        raise KeyError(f"Missing required field in material data: {str(e)}")

def main():
    """Main function to demonstrate the sustainability calculator."""
    try:
        # Load material data (in a real application, this would be a proper database)
        materials = load_material_data('material_data.json')
        calculator = SustainabilityCalculator(materials)
        
        # Example cleaning tool (similar to PDC Brush products)
        brush = CleaningTool(
            name="Eco Cleaning Brush",
            materials={
                "FSC Wood": 0.5,    # 500g of FSC-certified wood
                "Recycled Plastic": 0.2,  # 200g of recycled plastic
                "Natural Bristles": 0.3   # 300g of natural bristles
            }
        )
        
        # Calculate impact
        impact = calculator.calculate_impact(brush)
        
        # Print results
        print(f"Environmental Impact for {brush.name}:")
        print(f"- CO2 Emissions: {impact['total_co2_kg']:.2f} kg")
        print(f"- Water Usage: {impact['total_water_liters']:.2f} liters")
        print(f"- Land Use: {impact['total_land_m2']:.2f} m²")
        print(f"- FSC Certified Materials: {impact['fsc_percentage']:.1f}%")
        
    except Exception as e:
        print(f"Error calculating environmental impact: {str(e)}")

if __name__ == "__main__":
    main()
```
