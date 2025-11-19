"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Generate Python code to calculate the environmental impact of construction projects, considering methods like brick construction commonly used in Argentina.
Generated: DETERMINISTIC_b7f50b6547e3aa7b
Batch ID: 20250612_150920
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
from typing import Dict, List, Optional, Tuple

class ConstructionType(Enum):
    BRICK = "brick"
    CONCRETE = "concrete"
    STEEL = "steel"
    WOOD = "wood"

class EnvironmentalImpactCalculator:
    """
    A calculator to estimate the environmental impact of construction projects.
    Focuses on common construction methods in Argentina, particularly brick construction.
    """
    
    # Emission factors (kg CO2 per kg of material)
    EMISSION_FACTORS = {
        ConstructionType.BRICK: 0.22,
        ConstructionType.CONCRETE: 0.12,
        ConstructionType.STEEL: 1.85,
        ConstructionType.WOOD: 0.04
    }
    
    # Water consumption factors (liters per kg of material)
    WATER_FACTORS = {
        ConstructionType.BRICK: 0.5,
        ConstructionType.CONCRETE: 1.2,
        ConstructionType.STEEL: 5.0,
        ConstructionType.WOOD: 0.1
    }
    
    # Energy consumption factors (kWh per kg of material)
    ENERGY_FACTORS = {
        ConstructionType.BRICK: 0.8,
        ConstructionType.CONCRETE: 0.5,
        ConstructionType.STEEL: 10.0,
        ConstructionType.WOOD: 0.3
    }
    
    def __init__(self):
        self.materials: Dict[ConstructionType, float] = {}
    
    def add_material(self, material_type: ConstructionType, quantity_kg: float) -> None:
        """
        Add a construction material to the calculation.
        
        Args:
            material_type: Type of construction material
            quantity_kg: Quantity in kilograms
        """
        if quantity_kg <= 0:
            raise ValueError("Quantity must be positive")
        self.materials[material_type] = self.materials.get(material_type, 0) + quantity_kg
    
    def calculate_co2_emissions(self) -> float:
        """
        Calculate total CO2 emissions in kg.
        
        Returns:
            Total CO2 emissions in kilograms
        """
        total = 0.0
        for material, quantity in self.materials.items():
            total += quantity * self.EMISSION_FACTORS[material]
        return total
    
    def calculate_water_consumption(self) -> float:
        """
        Calculate total water consumption in liters.
        
        Returns:
            Total water consumption in liters
        """
        total = 0.0
        for material, quantity in self.materials.items():
            total += quantity * self.WATER_FACTORS[material]
        return total
    
    def calculate_energy_consumption(self) -> float:
        """
        Calculate total energy consumption in kWh.
        
        Returns:
            Total energy consumption in kilowatt-hours
        """
        total = 0.0
        for material, quantity in self.materials.items():
            total += quantity * self.ENERGY_FACTORS[material]
        return total
    
    def calculate_all_impacts(self) -> Dict[str, float]:
        """
        Calculate all environmental impacts.
        
        Returns:
            Dictionary containing CO2 emissions, water consumption, and energy consumption
        """
        return {
            "co2_emissions_kg": self.calculate_co2_emissions(),
            "water_consumption_liters": self.calculate_water_consumption(),
            "energy_consumption_kwh": self.calculate_energy_consumption()
        }
    
    def generate_report(self) -> str:
        """
        Generate a human-readable environmental impact report.
        
        Returns:
            Formatted report string
        """
        impacts = self.calculate_all_impacts()
        report = []
        report.append("Environmental Impact Report")
        report.append("=" * 40)
        report.append(f"Materials used: {self.materials}")
        report.append("-" * 40)
        report.append(f"Total CO2 Emissions: {impacts['co2_emissions_kg']:.2f} kg")
        report.append(f"Total Water Consumption: {impacts['water_consumption_liters']:.2f} liters")
        report.append(f"Total Energy Consumption: {impacts['energy_consumption_kwh']:.2f} kWh")
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    try:
        calculator = EnvironmentalImpactCalculator()
        
        # Add materials for a typical brick construction in Argentina
        calculator.add_material(ConstructionType.BRICK, 5000)  # 5000 kg of bricks
        calculator.add_material(ConstructionType.CONCRETE, 3000)  # 3000 kg of concrete
        calculator.add_material(ConstructionType.STEEL, 500)  # 500 kg of steel
        
        # Generate and print the report
        print(calculator.generate_report())
        
    except ValueError as e:
        print(f"Error: {e}")
```
