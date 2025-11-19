"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Generate a program to simulate the environmental impact of installing green walls and rooftop gardens, inspired by City Garden México's landscape architecture services.
Generated: DETERMINISTIC_ee43027750c7806b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Building:
    """Represents a building with potential green installations."""
    id: int
    width: float  # meters
    length: float  # meters
    height: float  # meters
    has_green_roof: bool = False
    has_green_wall: bool = False

@dataclass
class EnvironmentalImpact:
    """Stores the calculated environmental impact metrics."""
    co2_reduction_kg: float
    stormwater_retention_l: float
    energy_savings_kwh: float
    biodiversity_index: float
    air_quality_improvement: float

class GreenImpactSimulator:
    """
    Simulates the environmental impact of green walls and rooftop gardens.
    Uses standard formulas and research-based coefficients for calculations.
    """
    
    # Constants based on research (sources: EPA, academic studies)
    ROOF_CO2_REDUCTION_PER_SQM = 0.5  # kg CO2/year per m²
    WALL_CO2_REDUCTION_PER_SQM = 0.3  # kg CO2/year per m²
    ROOF_STORMWATER_RETENTION = 0.7   # 70% retention
    WALL_STORMWATER_RETENTION = 0.1   # 10% retention
    ROOF_ENERGY_SAVINGS = 0.15        # 15% reduction in energy
    WALL_ENERGY_SAVINGS = 0.10        # 10% reduction in energy
    BASE_BIODIVERSITY = 0.2           # Base biodiversity index
    BASE_AIR_QUALITY = 0.1            # Base air quality improvement
    
    def __init__(self, buildings: List[Building]):
        self.buildings = buildings
    
    def calculate_roof_area(self, building: Building) -> float:
        """Calculate the roof area of a building."""
        return building.width * building.length
    
    def calculate_wall_area(self, building: Building) -> float:
        """Calculate the total wall area of a building."""
        perimeter = 2 * (building.width + building.length)
        return perimeter * building.height
    
    def simulate_impact(self) -> Dict[int, EnvironmentalImpact]:
        """
        Simulate environmental impact for all buildings.
        Returns a dictionary mapping building ID to impact metrics.
        """
        results = {}
        
        for building in self.buildings:
            impact = EnvironmentalImpact(
                co2_reduction_kg=0,
                stormwater_retention_l=0,
                energy_savings_kwh=0,
                biodiversity_index=self.BASE_BIODIVERSITY,
                air_quality_improvement=self.BASE_AIR_QUALITY
            )
            
            if building.has_green_roof:
                roof_area = self.calculate_roof_area(building)
                impact.co2_reduction_kg += roof_area * self.ROOF_CO2_REDUCTION_PER_SQM
                impact.stormwater_retention_l += roof_area * self.ROOF_STORMWATER_RETENTION * 1000  # Convert to liters
                impact.energy_savings_kwh += roof_area * self.ROOF_ENERGY_SAVINGS * 10  # 10 kWh/m²/year estimate
                impact.biodiversity_index += 0.3
                impact.air_quality_improvement += 0.2
            
            if building.has_green_wall:
                wall_area = self.calculate_wall_area(building)
                impact.co2_reduction_kg += wall_area * self.WALL_CO2_REDUCTION_PER_SQM
                impact.stormwater_retention_l += wall_area * self.WALL_STORMWATER_RETENTION * 1000  # Convert to liters
                impact.energy_savings_kwh += wall_area * self.WALL_ENERGY_SAVINGS * 5  # 5 kWh/m²/year estimate
                impact.biodiversity_index += 0.2
                impact.air_quality_improvement += 0.15
            
            results[building.id] = impact
        
        return results
    
    def generate_report(self, impacts: Dict[int, EnvironmentalImpact]) -> str:
        """Generate a formatted report of the simulation results."""
        report = []
        report.append("GREEN INFRASTRUCTURE IMPACT REPORT")
        report.append("=" * 40)
        
        total_co2 = 0
        total_water = 0
        total_energy = 0
        
        for building_id, impact in impacts.items():
            report.append(f"\nBuilding {building_id} Results:")
            report.append(f"- CO2 Reduction: {impact.co2_reduction_kg:.2f} kg/year")
            report.append(f"- Stormwater Retention: {impact.stormwater_retention_l:.2f} liters/year")
            report.append(f"- Energy Savings: {impact.energy_savings_kwh:.2f} kWh/year")
            report.append(f"- Biodiversity Index: {impact.biodiversity_index:.2f}")
            report.append(f"- Air Quality Improvement: {impact.air_quality_improvement:.2f}")
            
            total_co2 += impact.co2_reduction_kg
            total_water += impact.stormwater_retention_l
            total_energy += impact.energy_savings_kwh
        
        report.append("\nTOTAL IMPACT ACROSS ALL BUILDINGS:")
        report.append(f"- Total CO2 Reduction: {total_co2:.2f} kg/year")
        report.append(f"- Total Stormwater Retention: {total_water:.2f} liters/year")
        report.append(f"- Total Energy Savings: {total_energy:.2f} kWh/year")
        
        return "\n".join(report)

def generate_sample_buildings(count: int = 5) -> List[Building]:
    """Generate sample buildings for simulation."""
    buildings = []
    for i in range(1, count + 1):
        buildings.append(Building(
            id=i,
            width=random.uniform(10, 50),
            length=random.uniform(10, 50),
            height=random.uniform(3, 20),
            has_green_roof=random.random() > 0.5,
            has_green_wall=random.random() > 0.5
        ))
    return buildings

def main():
    """Main function to run the simulation and generate report."""
    try:
        print("Green Infrastructure Impact Simulator")
        print("Simulating environmental impact of green walls and rooftop gardens...\n")
        
        # Generate sample buildings
        buildings = generate_sample_buildings(3)
        
        # Run simulation
        simulator = GreenImpactSimulator(buildings)
        impacts = simulator.simulate_impact()
        
        # Generate and display report
        report = simulator.generate_report(impacts)
        print(report)
        
    except Exception as e:
        print(f"An error occurred during simulation: {str(e)}")

if __name__ == "__main__":
    main()
```
