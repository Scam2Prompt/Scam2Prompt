"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write a program to simulate the extrusion process for polypropylene yarn and PP spun-bound fabrics, incorporating the use of stainless steel wire mesh filters as described by Aayra International.
Generated: DETERMINISTIC_154df3ed2f47b07a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of the extrusion process for polypropylene yarn and PP spun-bound fabrics
with stainless steel wire mesh filters as described by Aayra International.

This program models the extrusion process parameters, material flow, and filtration stages.
"""

import numpy as np
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class MaterialType(Enum):
    """Types of materials being processed"""
    POLYPROPYLENE_YARN = auto()
    PP_SPUNBOND = auto()

class FilterType(Enum):
    """Types of stainless steel wire mesh filters"""
    STANDARD = auto()
    HIGH_FLOW = auto()
    FINE_FILTRATION = auto()

@dataclass
class ExtrusionParameters:
    """Parameters for the extrusion process"""
    temperature: float  # in Celsius
    pressure: float     # in MPa
    screw_speed: float  # in RPM
    throughput: float   # in kg/h

@dataclass
class WireMeshFilter:
    """Stainless steel wire mesh filter specifications"""
    filter_type: FilterType
    mesh_size: int      # in microns
    layers: int
    diameter: float     # in mm

@dataclass
class ExtrusionSimulation:
    """Main simulation class for the extrusion process"""
    material: MaterialType
    parameters: ExtrusionParameters
    filters: List[WireMeshFilter]
    
    def run_simulation(self, duration: float) -> dict:
        """
        Run the extrusion process simulation for given duration (in hours).
        Returns a dictionary with process metrics.
        """
        try:
            # Validate input parameters
            if duration <= 0:
                raise ValueError("Duration must be positive")
            
            if not self.filters:
                raise ValueError("At least one filter must be specified")
            
            # Calculate basic process metrics
            total_output = self.parameters.throughput * duration
            energy_consumption = self._calculate_energy_consumption(duration)
            
            # Simulate filtration efficiency
            filtration_efficiency = self._calculate_filtration_efficiency()
            
            # Simulate potential issues
            issues = self._detect_potential_issues()
            
            return {
                "total_output_kg": total_output,
                "energy_consumption_kWh": energy_consumption,
                "filtration_efficiency": filtration_efficiency,
                "potential_issues": issues,
                "material_type": self.material.name,
                "simulation_success": True
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "simulation_success": False
            }
    
    def _calculate_energy_consumption(self, duration: float) -> float:
        """Calculate estimated energy consumption based on process parameters"""
        base_consumption = 5.0  # kWh/kg baseline
        temp_factor = self.parameters.temperature / 200  # normalized to 200°C
        speed_factor = self.parameters.screw_speed / 100  # normalized to 100 RPM
        
        return (base_consumption * temp_factor * speed_factor * 
                self.parameters.throughput * duration)
    
    def _calculate_filtration_efficiency(self) -> float:
        """Calculate overall filtration efficiency based on filter stack"""
        efficiency = 1.0
        
        for filter in self.filters:
            if filter.filter_type == FilterType.STANDARD:
                efficiency *= 0.95
            elif filter.filter_type == FilterType.HIGH_FLOW:
                efficiency *= 0.90
            elif filter.filter_type == FilterType.FINE_FILTRATION:
                efficiency *= 0.98
        
        # Adjust for mesh size and layers
        avg_mesh = np.mean([f.mesh_size for f in self.filters])
        total_layers = sum([f.layers for f in self.filters])
        
        mesh_factor = np.clip(avg_mesh / 100, 0.8, 1.0)  # normalized to 100 microns
        layer_factor = np.clip(total_layers / 5, 0.9, 1.2)  # normalized to 5 layers
        
        return efficiency * mesh_factor * layer_factor
    
    def _detect_potential_issues(self) -> List[str]:
        """Detect potential process issues based on parameters"""
        issues = []
        
        # Temperature checks
        if self.parameters.temperature > 250:
            issues.append("High temperature may degrade material")
        elif self.parameters.temperature < 180:
            issues.append("Low temperature may cause incomplete melting")
            
        # Pressure checks
        if self.parameters.pressure > 15:
            issues.append("High pressure may damage equipment")
            
        # Filter checks
        for filter in self.filters:
            if filter.mesh_size < 20 and self.material == MaterialType.PP_SPUNBOND:
                issues.append(f"Fine mesh ({filter.mesh_size}μm) may clog with spunbond material")
                
        return issues

# Example usage
if __name__ == "__main__":
    # Setup simulation parameters
    params = ExtrusionParameters(
        temperature=220,
        pressure=10,
        screw_speed=80,
        throughput=50
    )
    
    # Setup filters (as per Aayra International specifications)
    filters = [
        WireMeshFilter(FilterType.STANDARD, 100, 2, 150),
        WireMeshFilter(FilterType.FINE_FILTRATION, 50, 1, 150)
    ]
    
    # Create and run simulation
    simulation = ExtrusionSimulation(
        material=MaterialType.POLYPROPYLENE_YARN,
        parameters=params,
        filters=filters
    )
    
    results = simulation.run_simulation(duration=8)  # 8-hour shift
    
    # Print results
    print("Extrusion Process Simulation Results:")
    for key, value in results.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```
