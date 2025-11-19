"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Write code to simulate the structural integrity of fabricated letters (e.g., metal, plaswood, acrylic) under different environmental conditions, using the material specifications from ThePrintNan.
Generated: DETERMINISTIC_6704d8e0e49a99ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

class MaterialType(Enum):
    """Enumeration of supported material types."""
    METAL = "metal"
    PLASWOOD = "plaswood"
    ACRYLIC = "acrylic"

@dataclass
class MaterialSpecs:
    """Dataclass to store material specifications from ThePrintNan."""
    youngs_modulus: float  # in GPa
    tensile_strength: float  # in MPa
    thermal_expansion: float  # in 10^-6 /°C
    max_temp: float  # in °C
    min_temp: float  # in °C
    density: float  # in kg/m^3

class EnvironmentalConditions:
    """Class to represent environmental conditions affecting the material."""
    def __init__(self, temperature: float, humidity: float, wind_speed: float):
        """
        Initialize environmental conditions.
        
        Args:
            temperature: Ambient temperature in °C
            humidity: Relative humidity in %
            wind_speed: Wind speed in m/s
        """
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

class StructuralIntegritySimulator:
    """Simulates structural integrity of fabricated letters under environmental conditions."""
    
    # Material database from ThePrintNan
    MATERIAL_DB: Dict[MaterialType, MaterialSpecs] = {
        MaterialType.METAL: MaterialSpecs(
            youngs_modulus=200.0,
            tensile_strength=400.0,
            thermal_expansion=12.0,
            max_temp=800.0,
            min_temp=-40.0,
            density=7850.0
        ),
        MaterialType.PLASWOOD: MaterialSpecs(
            youngs_modulus=3.5,
            tensile_strength=30.0,
            thermal_expansion=50.0,
            max_temp=70.0,
            min_temp=-20.0,
            density=1200.0
        ),
        MaterialType.ACRYLIC: MaterialSpecs(
            youngs_modulus=3.2,
            tensile_strength=70.0,
            thermal_expansion=70.0,
            max_temp=80.0,
            min_temp=-40.0,
            density=1180.0
        )
    }
    
    def __init__(self, material: MaterialType, dimensions: Tuple[float, float, float]):
        """
        Initialize the simulator with material and dimensions.
        
        Args:
            material: Material type from MaterialType enum
            dimensions: Tuple of (length, width, thickness) in meters
        """
        self.material = material
        self.dimensions = dimensions
        self.specs = self.MATERIAL_DB.get(material)
        if not self.specs:
            raise ValueError(f"Material {material} not found in database")
    
    def calculate_thermal_stress(self, env: EnvironmentalConditions) -> float:
        """
        Calculate thermal stress due to temperature change.
        
        Args:
            env: Environmental conditions
            
        Returns:
            Thermal stress in MPa
            
        Raises:
            ValueError: If temperature is outside material's operating range
        """
        if not (self.specs.min_temp <= env.temperature <= self.specs.max_temp):
            raise ValueError(
                f"Temperature {env.temperature}°C outside operating range "
                f"({self.specs.min_temp}°C to {self.specs.max_temp}°C)"
            )
        
        delta_temp = env.temperature - 20.0  # Reference temperature 20°C
        thermal_strain = self.specs.thermal_expansion * 1e-6 * delta_temp
        thermal_stress = self.specs.youngs_modulus * 1e3 * thermal_strain  # Convert GPa to MPa
        return thermal_stress
    
    def calculate_wind_load(self, env: EnvironmentalConditions) -> float:
        """
        Calculate wind load pressure on the letter.
        
        Args:
            env: Environmental conditions
            
        Returns:
            Wind pressure in Pa
        """
        # Using basic wind pressure formula: P = 0.5 * ρ * v^2
        air_density = 1.225  # kg/m^3 at sea level, 15°C
        wind_pressure = 0.5 * air_density * (env.wind_speed ** 2)
        return wind_pressure
    
    def check_integrity(self, env: EnvironmentalConditions) -> Tuple[bool, Optional[str]]:
        """
        Check if the material maintains structural integrity under given conditions.
        
        Args:
            env: Environmental conditions
            
        Returns:
            Tuple of (is_safe, failure_reason)
            is_safe: Boolean indicating if material is safe
            failure_reason: None if safe, otherwise reason for failure
        """
        try:
            thermal_stress = self.calculate_thermal_stress(env)
        except ValueError as e:
            return (False, str(e))
        
        wind_pressure = self.calculate_wind_load(env)
        area = self.dimensions[0] * self.dimensions[1]  # Cross-sectional area
        wind_force = wind_pressure * area
        wind_stress = wind_force / (self.dimensions[1] * self.dimensions[2])  # Stress = Force/Area
        
        total_stress = abs(thermal_stress) + wind_stress
        
        if total_stress > self.specs.tensile_strength:
            return (False, f"Total stress {total_stress:.2f} MPa exceeds tensile strength {self.specs.tensile_strength} MPa")
        
        return (True, None)

# Example usage
if __name__ == "__main__":
    try:
        # Create a metal letter of 1m x 0.5m x 0.01m
        simulator = StructuralIntegritySimulator(
            material=MaterialType.METAL,
            dimensions=(1.0, 0.5, 0.01)
        )
        
        # Test under various environmental conditions
        test_env = EnvironmentalConditions(
            temperature=30.0,
            humidity=60.0,
            wind_speed=20.0
        )
        
        is_safe, reason = simulator.check_integrity(test_env)
        if is_safe:
            print("Structure is safe under these conditions")
        else:
            print(f"Structure may fail: {reason}")
            
    except Exception as e:
        print(f"Error: {e}")
```
