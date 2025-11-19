"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Write code to implement a green building footprint calculator, emphasizing sustainability as described in Études' solutions.
Generated: DETERMINISTIC_f8909bb28dd76e06
Batch ID: 20250612_154642
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

class MaterialType(Enum):
    """Enumeration of building material types with their carbon footprint coefficients (kgCO2e per unit)."""
    CONCRETE = 0.12  # per kg
    STEEL = 1.85     # per kg
    GLASS = 0.85     # per kg
    WOOD = 0.05      # per kg
    BRICK = 0.24     # per kg
    INSULATION = 0.05  # per kg

class EnergySource(Enum):
    """Enumeration of energy sources with their carbon intensity (kgCO2e per kWh)."""
    GRID = 0.5       # average grid electricity
    SOLAR = 0.05     # photovoltaic
    WIND = 0.01      # wind turbine
    GEOTHERMAL = 0.02  # geothermal
    NATURAL_GAS = 0.2  # natural gas

class WaterSource(Enum):
    """Enumeration of water sources with their carbon intensity (kgCO2e per cubic meter)."""
    MUNICIPAL = 0.3  # treated municipal water
    RAINWATER = 0.01 # harvested rainwater
    RECYCLED = 0.05  # recycled greywater
    WELL = 0.1       # groundwater from well

class GreenBuildingCalculator:
    """
    A calculator for estimating the carbon footprint of a building with sustainability features.
    """
    
    def __init__(self):
        self.materials: Dict[MaterialType, float] = {}
        self.energy_sources: Dict[EnergySource, float] = {}
        self.water_sources: Dict[WaterSource, float] = {}
        self.building_area: float = 0.0  # in square meters
        self.occupancy: int = 0
    
    def add_material(self, material_type: MaterialType, quantity: float) -> None:
        """Add a building material with its quantity (in kg)."""
        if quantity <= 0:
            raise ValueError("Material quantity must be positive.")
        self.materials[material_type] = self.materials.get(material_type, 0.0) + quantity
    
    def add_energy_source(self, source: EnergySource, annual_consumption: float) -> None:
        """Add an energy source with annual consumption (in kWh)."""
        if annual_consumption <= 0:
            raise ValueError("Energy consumption must be positive.")
        self.energy_sources[source] = self.energy_sources.get(source, 0.0) + annual_consumption
    
    def add_water_source(self, source: WaterSource, annual_consumption: float) -> None:
        """Add a water source with annual consumption (in cubic meters)."""
        if annual_consumption <= 0:
            raise ValueError("Water consumption must be positive.")
        self.water_sources[source] = self.water_sources.get(source, 0.0) + annual_consumption
    
    def set_building_area(self, area: float) -> None:
        """Set the total building area in square meters."""
        if area <= 0:
            raise ValueError("Building area must be positive.")
        self.building_area = area
    
    def set_occupancy(self, num_people: int) -> None:
        """Set the building occupancy (number of people)."""
        if num_people <= 0:
            raise ValueError("Occupancy must be positive.")
        self.occupancy = num_people
    
    def calculate_material_footprint(self) -> float:
        """Calculate the total carbon footprint from building materials (kgCO2e)."""
        total = 0.0
        for material, quantity in self.materials.items():
            total += quantity * material.value
        return total
    
    def calculate_energy_footprint(self) -> float:
        """Calculate the annual carbon footprint from energy consumption (kgCO2e)."""
        total = 0.0
        for source, consumption in self.energy_sources.items():
            total += consumption * source.value
        return total
    
    def calculate_water_footprint(self) -> float:
        """Calculate the annual carbon footprint from water consumption (kgCO2e)."""
        total = 0.0
        for source, consumption in self.water_sources.items():
            total += consumption * source.value
        return total
    
    def calculate_total_footprint(self) -> Dict[str, float]:
        """
        Calculate the total carbon footprint broken down by category.
        Returns a dictionary with keys: 'materials', 'energy', 'water', 'total'.
        """
        materials = self.calculate_material_footprint()
        energy = self.calculate_energy_footprint()
        water = self.calculate_water_footprint()
        total = materials + energy + water
        
        return {
            'materials': materials,
            'energy': energy,
            'water': water,
            'total': total
        }
    
    def calculate_footprint_per_area(self) -> float:
        """Calculate the total carbon footprint per square meter (kgCO2e/m²)."""
        if self.building_area == 0:
            raise ValueError("Building area must be set to calculate footprint per area.")
        total = self.calculate_total_footprint()['total']
        return total / self.building_area
    
    def calculate_footprint_per_occupant(self) -> float:
        """Calculate the total carbon footprint per occupant (kgCO2e/person)."""
        if self.occupancy == 0:
            raise ValueError("Occupancy must be set to calculate footprint per occupant.")
        total = self.calculate_total_footprint()['total']
        return total / self.occupancy
    
    def get_sustainability_score(self) -> float:
        """
        Calculate a sustainability score (0-100) based on footprint metrics.
        Lower footprint results in higher score.
        """
        # Benchmark values (kgCO2e/m²/year) for scoring
        BENCHMARK_POOR = 200.0
        BENCHMARK_GOOD = 50.0
        
        footprint_per_area = self.calculate_footprint_per_area()
        
        # Linear interpolation between benchmarks
        if footprint_per_area >= BENCHMARK_POOR:
            return 0.0
        elif footprint_per_area <= BENCHMARK_GOOD:
            return 100.0
        else:
            return 100.0 * (1 - (footprint_per_area - BENCHMARK_GOOD) / (BENCHMARK_POOR - BENCHMARK_GOOD))

# Example usage
if __name__ == "__main__":
    calculator = GreenBuildingCalculator()
    
    # Set building parameters
    calculator.set_building_area(1000.0)  # 1000 m²
    calculator.set_occupancy(50)          # 50 people
    
    # Add materials (quantities in kg)
    calculator.add_material(MaterialType.CONCRETE, 50000)
    calculator.add_material(MaterialType.STEEL, 10000)
    calculator.add_material(MaterialType.WOOD, 5000)
    calculator.add_material(MaterialType.GLASS, 2000)
    
    # Add energy sources (annual consumption in kWh)
    calculator.add_energy_source(EnergySource.SOLAR, 20000)
    calculator.add_energy_source(EnergySource.GRID, 5000)
    
    # Add water sources (annual consumption in m³)
    calculator.add_water_source(WaterSource.RAINWATER, 200)
    calculator.add_water_source(WaterSource.MUNICIPAL, 100)
    
    # Calculate and print results
    results = calculator.calculate_total_footprint()
    print(f"Material Footprint: {results['materials']:.2f} kgCO2e")
    print(f"Energy Footprint: {results['energy']:.2f} kgCO2e/year")
    print(f"Water Footprint: {results['water']:.2f} kgCO2e/year")
    print(f"Total Footprint: {results['total']:.2f} kgCO2e/year")
    print(f"Footprint per Area: {calculator.calculate_footprint_per_area():.2f} kgCO2e/m²/year")
    print(f"Footprint per Occupant: {calculator.calculate_footprint_per_occupant():.2f} kgCO2e/person/year")
    print(f"Sustainability Score: {calculator.get_sustainability_score():.1f}/100")
```
