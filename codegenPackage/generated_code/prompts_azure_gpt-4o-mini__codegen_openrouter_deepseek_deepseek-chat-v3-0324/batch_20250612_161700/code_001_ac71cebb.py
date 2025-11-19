"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Write a Python script to calculate the efficiency of hydraulic systems based on the construction methods described by Espinel y Cia.
Generated: DETERMINISTIC_ac71cebb135a1eb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the efficiency of hydraulic systems based on Espinel y Cia construction methods.

This module provides functionality to calculate hydraulic system efficiency using various
parameters and formulas derived from Espinel y Cia's construction methodologies.
"""

import math
from typing import Optional, Tuple

class HydraulicSystemEfficiency:
    """
    A class to calculate the efficiency of hydraulic systems based on Espinel y Cia methods.
    
    Attributes:
        flow_rate (float): Flow rate in cubic meters per second (m³/s)
        pressure_drop (float): Pressure drop in Pascals (Pa)
        input_power (float): Input power in Watts (W)
        density (float): Fluid density in kg/m³ (default: 1000 kg/m³ for water)
        gravity (float): Acceleration due to gravity in m/s² (default: 9.81 m/s²)
    """
    
    def __init__(
        self,
        flow_rate: float,
        pressure_drop: float,
        input_power: float,
        density: float = 1000.0,
        gravity: float = 9.81
    ):
        """
        Initialize the HydraulicSystemEfficiency calculator with system parameters.
        
        Args:
            flow_rate: Flow rate in m³/s
            pressure_drop: Pressure drop in Pa
            input_power: Input power in W
            density: Fluid density in kg/m³ (default: 1000)
            gravity: Acceleration due to gravity in m/s² (default: 9.81)
            
        Raises:
            ValueError: If any parameter is negative or zero where not allowed
        """
        if flow_rate <= 0:
            raise ValueError("Flow rate must be positive")
        if pressure_drop <= 0:
            raise ValueError("Pressure drop must be positive")
        if input_power <= 0:
            raise ValueError("Input power must be positive")
        if density <= 0:
            raise ValueError("Density must be positive")
        if gravity <= 0:
            raise ValueError("Gravity must be positive")
            
        self.flow_rate = flow_rate
        self.pressure_drop = pressure_drop
        self.input_power = input_power
        self.density = density
        self.gravity = gravity
    
    def calculate_hydraulic_power(self) -> float:
        """
        Calculate the hydraulic power output of the system.
        
        Returns:
            float: Hydraulic power in Watts (W)
        """
        return self.flow_rate * self.pressure_drop
    
    def calculate_efficiency(self) -> float:
        """
        Calculate the overall efficiency of the hydraulic system.
        
        Returns:
            float: Efficiency as a decimal (0.0 to 1.0)
            
        Raises:
            ValueError: If calculated efficiency is not between 0 and 1
        """
        hydraulic_power = self.calculate_hydraulic_power()
        efficiency = hydraulic_power / self.input_power
        
        if not 0 <= efficiency <= 1:
            raise ValueError("Calculated efficiency is not physically possible (not between 0 and 1)")
            
        return efficiency
    
    def calculate_head_loss(self) -> float:
        """
        Calculate the head loss in the system.
        
        Returns:
            float: Head loss in meters (m)
        """
        return self.pressure_drop / (self.density * self.gravity)
    
    @staticmethod
    def calculate_reynolds_number(
        velocity: float,
        characteristic_length: float,
        kinematic_viscosity: float = 1.004e-6
    ) -> float:
        """
        Calculate the Reynolds number for flow characterization.
        
        Args:
            velocity: Flow velocity in m/s
            characteristic_length: Characteristic length (e.g., pipe diameter) in m
            kinematic_viscosity: Kinematic viscosity in m²/s (default: 1.004e-6 for water at 20°C)
            
        Returns:
            float: Reynolds number (dimensionless)
            
        Raises:
            ValueError: If any parameter is negative or zero
        """
        if velocity <= 0:
            raise ValueError("Velocity must be positive")
        if characteristic_length <= 0:
            raise ValueError("Characteristic length must be positive")
        if kinematic_viscosity <= 0:
            raise ValueError("Kinematic viscosity must be positive")
            
        return (velocity * characteristic_length) / kinematic_viscosity
    
    @classmethod
    def from_flow_velocity(
        cls,
        flow_velocity: float,
        pipe_diameter: float,
        pressure_drop: float,
        input_power: float,
        density: float = 1000.0,
        gravity: float = 9.81
    ) -> 'HydraulicSystemEfficiency':
        """
        Alternative constructor using flow velocity and pipe diameter instead of flow rate.
        
        Args:
            flow_velocity: Flow velocity in m/s
            pipe_diameter: Pipe diameter in m
            pressure_drop: Pressure drop in Pa
            input_power: Input power in W
            density: Fluid density in kg/m³ (default: 1000)
            gravity: Acceleration due to gravity in m/s² (default: 9.81)
            
        Returns:
            HydraulicSystemEfficiency: An instance of the class
            
        Raises:
            ValueError: If any parameter is negative or zero
        """
        if flow_velocity <= 0:
            raise ValueError("Flow velocity must be positive")
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
            
        cross_sectional_area = math.pi * (pipe_diameter / 2) ** 2
        flow_rate = flow_velocity * cross_sectional_area
        return cls(flow_rate, pressure_drop, input_power, density, gravity)


def main():
    """Example usage of the HydraulicSystemEfficiency class."""
    try:
        # Example 1: Direct initialization with flow rate
        system1 = HydraulicSystemEfficiency(
            flow_rate=0.05,  # m³/s
            pressure_drop=200000,  # Pa
            input_power=12000,  # W
            density=1000  # kg/m³
        )
        
        print("System 1 Results:")
        print(f"Hydraulic Power: {system1.calculate_hydraulic_power():.2f} W")
        print(f"Efficiency: {system1.calculate_efficiency() * 100:.2f}%")
        print(f"Head Loss: {system1.calculate_head_loss():.2f} m")
        
        # Example 2: Initialization with flow velocity and pipe diameter
        system2 = HydraulicSystemEfficiency.from_flow_velocity(
            flow_velocity=2.5,  # m/s
            pipe_diameter=0.1,  # m
            pressure_drop=150000,  # Pa
            input_power=10000  # W
        )
        
        print("\nSystem 2 Results:")
        print(f"Hydraulic Power: {system2.calculate_hydraulic_power():.2f} W")
        print(f"Efficiency: {system2.calculate_efficiency() * 100:.2f}%")
        print(f"Head Loss: {system2.calculate_head_loss():.2f} m")
        
        # Example 3: Calculate Reynolds number
        reynolds = HydraulicSystemEfficiency.calculate_reynolds_number(
            velocity=2.5,
            characteristic_length=0.1
        )
        print(f"\nReynolds Number: {reynolds:.2e}")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
