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
# environmental_impact_simulator.py

import numpy as np
from enum import Enum
from typing import Dict, List

class GeologyType(Enum):
    """Geology types"""
    CLAY = 1
    SILT = 2
    SAND = 3
    GRAVEL = 4
    ROCK = 5

class GeotechnicalProperties:
    """Geotechnical properties of soil or rock"""
    def __init__(self, cohesion: float, friction_angle: float, density: float):
        """
        Initialize geotechnical properties.

        Args:
        - cohesion (float): Cohesion of soil or rock in kPa.
        - friction_angle (float): Friction angle of soil or rock in degrees.
        - density (float): Density of soil or rock in kg/m^3.
        """
        self.cohesion = cohesion
        self.friction_angle = friction_angle
        self.density = density

class EnvironmentalImpactSimulator:
    """Simulator for environmental impact of underground construction projects"""
    def __init__(self, geology_type: GeologyType, geotechnical_properties: GeotechnicalProperties, tunnel_depth: float, tunnel_diameter: float):
        """
        Initialize simulator.

        Args:
        - geology_type (GeologyType): Type of geology.
        - geotechnical_properties (GeotechnicalProperties): Geotechnical properties of soil or rock.
        - tunnel_depth (float): Depth of tunnel in meters.
        - tunnel_diameter (float): Diameter of tunnel in meters.
        """
        self.geology_type = geology_type
        self.geotechnical_properties = geotechnical_properties
        self.tunnel_depth = tunnel_depth
        self.tunnel_diameter = tunnel_diameter

    def calculate_settlement(self) -> float:
        """
        Calculate settlement of soil or rock due to tunnel construction.

        Returns:
        - settlement (float): Settlement in meters.
        """
        try:
            # Calculate settlement using a simple empirical formula
            settlement = (self.tunnel_diameter ** 2) * self.geotechnical_properties.density / (self.tunnel_depth * self.geotechnical_properties.cohesion)
            return settlement
        except ZeroDivisionError:
            raise ValueError("Cohesion or tunnel depth cannot be zero")

    def calculate_groundwater_inflow(self) -> float:
        """
        Calculate groundwater inflow into tunnel.

        Returns:
        - groundwater_inflow (float): Groundwater inflow in m^3/day.
        """
        try:
            # Calculate groundwater inflow using a simple empirical formula
            groundwater_inflow = 1.366 * (self.tunnel_diameter ** 2) * self.tunnel_depth ** 0.5
            return groundwater_inflow
        except Exception as e:
            raise RuntimeError(f"Failed to calculate groundwater inflow: {str(e)}")

    def simulate_environmental_impact(self) -> Dict[str, float]:
        """
        Simulate environmental impact of underground construction project.

        Returns:
        - environmental_impact (Dict[str, float]): Dictionary containing settlement and groundwater inflow.
        """
        environmental_impact = {
            "settlement": self.calculate_settlement(),
            "groundwater_inflow": self.calculate_groundwater_inflow()
        }
        return environmental_impact

def main():
    geology_type = GeologyType.CLAY
    geotechnical_properties = GeotechnicalProperties(cohesion=20.0, friction_angle=25.0, density=1800.0)
    tunnel_depth = 20.0
    tunnel_diameter = 5.0

    simulator = EnvironmentalImpactSimulator(geology_type, geotechnical_properties, tunnel_depth, tunnel_diameter)
    environmental_impact = simulator.simulate_environmental_impact()

    print("Environmental Impact:")
    for impact, value in environmental_impact.items():
        print(f"- {impact.capitalize().replace('_', ' ')}: {value:.2f}")

if __name__ == "__main__":
    main()
```
