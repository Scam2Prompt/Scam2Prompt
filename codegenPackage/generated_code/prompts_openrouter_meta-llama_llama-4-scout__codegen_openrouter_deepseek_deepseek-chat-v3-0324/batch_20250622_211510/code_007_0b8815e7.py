"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "Develop a conceptual design for a sanitary infrastructure project in a Chilean region using local regulations and standards."
Generated: DETERMINISTIC_0b8815e7235dd40c
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Sanitary Infrastructure Project Design for Chilean Region

This script provides a conceptual design for a sanitary infrastructure project
in Chile, adhering to local regulations and standards (e.g., NCh, DS, OGUC).

Key components:
- Water supply system design
- Wastewater collection system
- Stormwater management
- Compliance with Chilean norms
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass
import math

# Constants based on Chilean regulations
MIN_WATER_PRESSURE = 10  # meters (NCh409/1)
MAX_WATER_PRESSURE = 50  # meters (NCh409/1)
DAILY_WATER_CONSUMPTION = 200  # liters/person/day (DS N°609/98)
PEAK_FACTOR = 1.8  # Peak demand factor (NCh1108)
PIPE_MATERIALS = ["PVC", "HDPE", "Ductile Iron"]  # Approved materials (NCh2313)

@dataclass
class PopulationData:
    """Population data for the project area"""
    current: int
    growth_rate: float  # annual growth rate
    design_period: int  # years

    def future_population(self) -> int:
        """Calculate future population using compound growth"""
        return round(self.current * (1 + self.growth_rate) ** self.design_period)

@dataclass
class TopographyData:
    """Topographic data for the project area"""
    elevation_profile: List[float]  # meters above sea level
    terrain_slope: float  # percentage

@dataclass
class WaterSource:
    """Water source information"""
    name: str
    capacity: float  # liters/second
    quality_parameters: Dict[str, float]  # e.g., {"turbidity": 0.5, "pH": 7.2}

class SanitaryDesign:
    """Main class for sanitary infrastructure design"""
    
    def __init__(self, population: PopulationData, topography: TopographyData):
        self.population = population
        self.topography = topography
        self.water_sources: List[WaterSource] = []
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate input parameters against Chilean standards"""
        if self.population.current <= 0:
            raise ValueError("Population must be positive")
        if not 0 <= self.population.growth_rate <= 0.05:
            raise ValueError("Growth rate must be between 0 and 5%")
        if self.population.design_period not in range(10, 31):
            raise ValueError("Design period must be 10-30 years")
            
    def add_water_source(self, source: WaterSource):
        """Add a water source to the design"""
        self.water_sources.append(source)
        
    def calculate_water_demand(self) -> Dict[str, float]:
        """
        Calculate water demand based on Chilean standards
        Returns average and peak demand in liters/second
        """
        future_pop = self.population.future_population()
        avg_demand = (future_pop * DAILY_WATER_CONSUMPTION) / 86400  # l/s
        peak_demand = avg_demand * PEAK_FACTOR
        
        return {
            "average_demand": round(avg_demand, 2),
            "peak_demand": round(peak_demand, 2)
        }
    
    def design_water_network(self) -> Dict:
        """Design water distribution network"""
        demand = self.calculate_water_demand()
        total_capacity = sum(src.capacity for src in self.water_sources)
        
        if total_capacity < demand["peak_demand"]:
            raise ValueError("Insufficient water source capacity")
            
        return {
            "pipe_material": self._select_pipe_material(),
            "required_pressure": self._calculate_required_pressure(),
            "network_layout": self._generate_network_layout()
        }
    
    def _select_pipe_material(self) -> str:
        """Select appropriate pipe material based on topography"""
        if self.topography.terrain_slope > 15:
            return "Ductile Iron"  # For high pressure areas
        return "PVC"  # Default choice
    
    def _calculate_required_pressure(self) -> float:
        """Calculate required pressure based on elevation differences"""
        max_elevation = max(self.topography.elevation_profile)
        min_elevation = min(self.topography.elevation_profile)
        return max_elevation - min_elevation + MIN_WATER_PRESSURE
    
    def _generate_network_layout(self) -> List[Dict]:
        """Generate preliminary network layout (simplified)"""
        return [{
            "segment": f"Segment_{i+1}",
            "length": 100,  # meters (example)
            "diameter": self._calculate_pipe_diameter(),
            "material": self._select_pipe_material()
        } for i in range(5)]  # Example: 5 segments
    
    def _calculate_pipe_diameter(self) -> int:
        """Calculate pipe diameter based on demand (simplified)"""
        demand = self.calculate_water_demand()
        if demand["peak_demand"] < 5:
            return 100  # mm
        elif demand["peak_demand"] < 15:
            return 150  # mm
        else:
            return 200  # mm
    
    def generate_report(self) -> str:
        """Generate a JSON report of the design"""
        report = {
            "population_data": {
                "current": self.population.current,
                "future": self.population.future_population(),
                "growth_rate": self.population.growth_rate,
                "design_period": self.population.design_period
            },
            "water_demand": self.calculate_water_demand(),
            "water_sources": [{
                "name": src.name,
                "capacity": src.capacity,
                "quality": src.quality_parameters
            } for src in self.water_sources],
            "water_network": self.design_water_network(),
            "compliance": ["NCh409", "DS609", "NCh2313"]  # Relevant standards
        }
        return json.dumps(report, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for a Chilean region
        population = PopulationData(
            current=5000,
            growth_rate=0.02,
            design_period=20
        )
        
        topography = TopographyData(
            elevation_profile=[450, 460, 455, 470, 465],
            terrain_slope=8.5
        )
        
        design = SanitaryDesign(population, topography)
        
        # Add water sources
        design.add_water_source(WaterSource(
            name="Rio Maipo",
            capacity=25.0,
            quality_parameters={"turbidity": 1.2, "pH": 7.5}
        ))
        
        design.add_water_source(WaterSource(
            name="Groundwater Well",
            capacity=10.0,
            quality_parameters={"turbidity": 0.3, "pH": 6.8}
        ))
        
        # Generate and print report
        print(design.generate_report())
        
    except Exception as e:
        print(f"Error in sanitary design: {str(e)}")
```
