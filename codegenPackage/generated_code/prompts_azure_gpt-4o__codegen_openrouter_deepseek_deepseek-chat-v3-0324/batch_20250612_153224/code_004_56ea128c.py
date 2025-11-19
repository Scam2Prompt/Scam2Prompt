"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Create a Python program to simulate the environmental impact of underground construction projects, incorporating geological and geotechnical factors similar to those handled by URANPRES.
Generated: DETERMINISTIC_56ea128cfcc734bd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from enum import Enum
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SoilType(Enum):
    """Enumeration of soil types with their properties."""
    CLAY = {'cohesion': 50, 'friction_angle': 20, 'density': 1800}
    SAND = {'cohesion': 0, 'friction_angle': 30, 'density': 1600}
    ROCK = {'cohesion': 200, 'friction_angle': 45, 'density': 2500}
    SILT = {'cohesion': 10, 'friction_angle': 25, 'density': 1700}

class ConstructionMethod(Enum):
    """Enumeration of construction methods with their impact factors."""
    TUNNEL_BORING_MACHINE = {'vibration': 0.2, 'noise': 0.3, 'dust': 0.1}
    DRILL_AND_BLAST = {'vibration': 0.8, 'noise': 0.9, 'dust': 0.7}
    CUT_AND_COVER = {'vibration': 0.5, 'noise': 0.6, 'dust': 0.4}

@dataclass
class GeologicalLayer:
    """Represents a geological layer with its properties."""
    soil_type: SoilType
    thickness: float  # in meters
    depth: float  # in meters
    groundwater_pressure: float  # in kPa

@dataclass
class ConstructionProject:
    """Represents an underground construction project."""
    name: str
    depth: float  # in meters
    length: float  # in meters
    diameter: float  # in meters
    method: ConstructionMethod
    geological_layers: List[GeologicalLayer]

class EnvironmentalImpactSimulator:
    """Simulates the environmental impact of underground construction projects."""
    
    def __init__(self, project: ConstructionProject):
        self.project = project
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate project inputs."""
        if self.project.depth <= 0 or self.project.length <= 0 or self.project.diameter <= 0:
            raise ValueError("Project dimensions must be positive values.")
        if not self.project.geological_layers:
            raise ValueError("At least one geological layer must be provided.")
    
    def calculate_ground_subsidence(self) -> float:
        """Calculate potential ground subsidence based on project parameters."""
        total_subsidence = 0.0
        for layer in self.project.geological_layers:
            if layer.depth <= self.project.depth:
                # Simplified subsidence calculation based on layer properties
                layer_subsidence = (
                    (self.project.diameter ** 2) * 
                    (1 - layer.soil_type.value['cohesion'] / 100) * 
                    (layer.thickness / 10)
                )
                total_subsidence += layer_subsidence
        
        # Normalize by project length
        normalized_subsidence = total_subsidence * (self.project.length / 1000)
        return normalized_subsidence
    
    def calculate_vibration_impact(self) -> float:
        """Calculate vibration impact based on construction method and soil type."""
        method_factor = self.project.method.value['vibration']
        avg_cohesion = np.mean([layer.soil_type.value['cohesion'] for layer in self.project.geological_layers])
        
        # Higher cohesion reduces vibration impact
        vibration_impact = method_factor * (1 - (avg_cohesion / 200))
        return vibration_impact
    
    def calculate_noise_pollution(self) -> float:
        """Calculate noise pollution based on construction method."""
        noise_factor = self.project.method.value['noise']
        depth_factor = 1 - (self.project.depth / 100)  # Deeper projects have less surface noise
        return noise_factor * depth_factor
    
    def calculate_dust_emission(self) -> float:
        """Calculate dust emission based on construction method and soil type."""
        method_factor = self.project.method.value['dust']
        avg_density = np.mean([layer.soil_type.value['density'] for layer in self.project.geological_layers])
        
        # Lower density soils produce more dust
        dust_emission = method_factor * (1 - (avg_density / 3000))
        return dust_emission
    
    def calculate_groundwater_impact(self) -> float:
        """Calculate potential groundwater impact."""
        total_impact = 0.0
        for layer in self.project.geological_layers:
            if layer.depth <= self.project.depth and layer.groundwater_pressure > 0:
                impact = (
                    (layer.groundwater_pressure / 100) * 
                    (layer.thickness / 10) * 
                    (1 - layer.soil_type.value['cohesion'] / 200)
                )
                total_impact += impact
        
        return total_impact
    
    def simulate_impacts(self) -> Dict[str, float]:
        """Run all impact simulations and return results."""
        try:
            results = {
                'ground_subsidence': self.calculate_ground_subsidence(),
                'vibration_impact': self.calculate_vibration_impact(),
                'noise_pollution': self.calculate_noise_pollution(),
                'dust_emission': self.calculate_dust_emission(),
                'groundwater_impact': self.calculate_groundwater_impact()
            }
            logger.info("Successfully simulated environmental impacts.")
            return results
        except Exception as e:
            logger.error(f"Error during simulation: {str(e)}")
            raise

def create_sample_project() -> ConstructionProject:
    """Create a sample construction project for demonstration."""
    layers = [
        GeologicalLayer(SoilType.CLAY, thickness=5, depth=0, groundwater_pressure=50),
        GeologicalLayer(SoilType.SAND, thickness=10, depth=5, groundwater_pressure=100),
        GeologicalLayer(SoilType.ROCK, thickness=15, depth=15, groundwater_pressure=0)
    ]
    
    project = ConstructionProject(
        name="Sample Tunnel Project",
        depth=20,
        length=500,
        diameter=10,
        method=ConstructionMethod.TUNNEL_BORING_MACHINE,
        geological_layers=layers
    )
    return project

def main():
    """Main function to demonstrate the simulation."""
    try:
        project = create_sample_project()
        simulator = EnvironmentalImpactSimulator(project)
        
        print(f"Simulating environmental impacts for: {project.name}")
        print(f"Construction Method: {project.method.name}")
        print(f"Project Depth: {project.depth}m, Length: {project.length}m")
        
        results = simulator.simulate_impacts()
        
        print("\nSimulation Results:")
        for impact, value in results.items():
            print(f"{impact.replace('_', ' ').title()}: {value:.4f}")
            
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
