"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Generate a code snippet for a web application that helps users design rural potable water systems, incorporating best practices from AJP Ingenieros' expertise in sanitary infrastructure.
Generated: DETERMINISTIC_eb839667d83f03cf
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# water_system_designer.py

from typing import Dict, List
import math

class WaterSource:
    """Represents a water source in the rural potable water system."""
    
    def __init__(self, name: str, flow_rate: float, quality: str):
        """
        Initializes a WaterSource object.

        Args:
        - name (str): The name of the water source.
        - flow_rate (float): The flow rate of the water source in liters per second.
        - quality (str): The quality of the water source (e.g., "good", "fair", "poor").
        """
        self.name = name
        self.flow_rate = flow_rate
        self.quality = quality

class Pipe:
    """Represents a pipe in the rural potable water system."""
    
    def __init__(self, diameter: float, length: float, material: str):
        """
        Initializes a Pipe object.

        Args:
        - diameter (float): The diameter of the pipe in meters.
        - length (float): The length of the pipe in meters.
        - material (str): The material of the pipe (e.g., "PVC", "HDPE", "cast iron").
        """
        self.diameter = diameter
        self.length = length
        self.material = material

    def calculate_friction_factor(self) -> float:
        """Calculates the friction factor for the pipe."""
        # Using the Hazen-Williams equation for friction factor
        if self.material == "PVC":
            return 0.013
        elif self.material == "HDPE":
            return 0.012
        else:
            return 0.015

class WaterSystem:
    """Represents a rural potable water system."""
    
    def __init__(self, water_sources: List[WaterSource], pipes: List[Pipe]):
        """
        Initializes a WaterSystem object.

        Args:
        - water_sources (List[WaterSource]): A list of water sources in the system.
        - pipes (List[Pipe]): A list of pipes in the system.
        """
        self.water_sources = water_sources
        self.pipes = pipes

    def calculate_total_flow_rate(self) -> float:
        """Calculates the total flow rate of the water sources."""
        return sum(source.flow_rate for source in self.water_sources)

    def calculate_pressure_drop(self, pipe: Pipe, flow_rate: float) -> float:
        """
        Calculates the pressure drop across a pipe.

        Args:
        - pipe (Pipe): The pipe to calculate the pressure drop for.
        - flow_rate (float): The flow rate through the pipe.

        Returns:
        - The pressure drop across the pipe in meters of head.
        """
        friction_factor = pipe.calculate_friction_factor()
        diameter = pipe.diameter
        length = pipe.length
        # Using the Darcy-Weisbach equation for pressure drop
        pressure_drop = (friction_factor * length * (flow_rate ** 2)) / (diameter * 2 * 9.81)
        return pressure_drop

    def design_system(self) -> Dict:
        """
        Designs the rural potable water system.

        Returns:
        - A dictionary containing the system design parameters.
        """
        total_flow_rate = self.calculate_total_flow_rate()
        system_design = {
            "total_flow_rate": total_flow_rate,
            "pipes": []
        }
        for pipe in self.pipes:
            pressure_drop = self.calculate_pressure_drop(pipe, total_flow_rate)
            system_design["pipes"].append({
                "diameter": pipe.diameter,
                "length": pipe.length,
                "material": pipe.material,
                "pressure_drop": pressure_drop
            })
        return system_design

def main():
    try:
        # Create water sources
        water_source1 = WaterSource("Well 1", 0.05, "good")
        water_source2 = WaterSource("Well 2", 0.03, "fair")

        # Create pipes
        pipe1 = Pipe(0.1, 100, "PVC")
        pipe2 = Pipe(0.15, 50, "HDPE")

        # Create water system
        water_system = WaterSystem([water_source1, water_source2], [pipe1, pipe2])

        # Design the system
        system_design = water_system.design_system()

        # Print the system design
        print("System Design:")
        print(f"Total Flow Rate: {system_design['total_flow_rate']} L/s")
        for i, pipe_design in enumerate(system_design["pipes"]):
            print(f"Pipe {i+1}:")
            print(f"  Diameter: {pipe_design['diameter']} m")
            print(f"  Length: {pipe_design['length']} m")
            print(f"  Material: {pipe_design['material']}")
            print(f"  Pressure Drop: {pipe_design['pressure_drop']} m")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
