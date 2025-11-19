"""
Generated Code Metadata:
========================
Original URL: https://spmepl.com
Prompt: Generate code to calculate the load capacity of heavy-duty pipeline rollers, incorporating parameters like PU coating and multidirectional movement as mentioned on the SPM Equipment site.
Generated: DETERMINISTIC_330fe8d5fff6e391
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
from enum import Enum
from typing import Optional, Tuple

class RollerDirection(Enum):
    """Enumeration for roller movement direction."""
    UNIDIRECTIONAL = 1
    MULTIDIRECTIONAL = 2

class RollerMaterial(Enum):
    """Enumeration for roller coating material."""
    STEEL = 1
    PU_COATED = 2

class PipelineRoller:
    """
    A class to calculate the load capacity of heavy-duty pipeline rollers.
    
    Attributes:
        diameter (float): Roller diameter in millimeters
        length (float): Roller length in millimeters
        material (RollerMaterial): Roller material type
        direction (RollerDirection): Roller movement direction
        temperature (float): Operating temperature in Celsius (optional)
        speed (float): Operating speed in meters per second (optional)
    """
    
    # Material constants (load factors)
    MATERIAL_FACTORS = {
        RollerMaterial.STEEL: 1.0,
        RollerMaterial.PU_COATED: 0.85  # PU coating reduces load capacity
    }
    
    # Direction constants
    DIRECTION_FACTORS = {
        RollerDirection.UNIDIRECTIONAL: 1.0,
        RollerDirection.MULTIDIRECTIONAL: 0.7  # Multidirectional reduces capacity
    }
    
    # Temperature adjustment factors (for temperatures > 50°C)
    TEMPERATURE_FACTORS = {
        50: 1.0,
        60: 0.95,
        70: 0.9,
        80: 0.85,
        90: 0.8,
        100: 0.75
    }
    
    def __init__(
        self,
        diameter: float,
        length: float,
        material: RollerMaterial,
        direction: RollerDirection,
        temperature: Optional[float] = None,
        speed: Optional[float] = None
    ):
        """
        Initialize the pipeline roller with required parameters.
        
        Args:
            diameter: Roller diameter in mm
            length: Roller length in mm
            material: Roller material type
            direction: Movement direction type
            temperature: Operating temperature in °C (optional)
            speed: Operating speed in m/s (optional)
        """
        self.diameter = diameter
        self.length = length
        self.material = material
        self.direction = direction
        self.temperature = temperature
        self.speed = speed
        
        # Validate inputs
        if diameter <= 0 or length <= 0:
            raise ValueError("Diameter and length must be positive values")
        if temperature is not None and temperature < -20:
            raise ValueError("Temperature below -20°C is not supported")
        if speed is not None and speed < 0:
            raise ValueError("Speed cannot be negative")

    def _get_temperature_factor(self) -> float:
        """Calculate temperature adjustment factor."""
        if self.temperature is None or self.temperature <= 50:
            return 1.0
        
        # Find the closest temperature bracket
        temps = sorted(self.TEMPERATURE_FACTORS.keys())
        for temp in temps:
            if self.temperature <= temp:
                return self.TEMPERATURE_FACTORS[temp]
        
        # For temperatures above maximum in table
        return self.TEMPERATURE_FACTORS[temps[-1]] * 0.95 ** ((self.temperature - temps[-1]) / 10)

    def _get_speed_factor(self) -> float:
        """Calculate speed adjustment factor."""
        if self.speed is None or self.speed <= 1.0:
            return 1.0
        
        # Speed reduction factor (1% per 0.1 m/s above 1 m/s)
        return max(0.7, 1.0 - (self.speed - 1.0) * 0.01)

    def calculate_load_capacity(self) -> Tuple[float, str]:
        """
        Calculate the dynamic load capacity of the roller in kilograms.
        
        Returns:
            Tuple containing:
                - load_capacity (float): Calculated load capacity in kg
                - warning (str): Any warnings about calculation parameters
        """
        warning = ""
        
        # Base load capacity formula (simplified for demonstration)
        base_capacity = (math.pi * (self.diameter ** 2) * self.length) / 10000
        
        # Apply material factor
        material_factor = self.MATERIAL_FACTORS.get(self.material, 1.0)
        capacity = base_capacity * material_factor
        
        # Apply direction factor
        direction_factor = self.DIRECTION_FACTORS.get(self.direction, 1.0)
        capacity *= direction_factor
        
        # Apply temperature factor if provided
        if self.temperature is not None:
            temp_factor = self._get_temperature_factor()
            capacity *= temp_factor
            if self.temperature > 50:
                warning += f"Warning: High temperature ({self.temperature}°C) reduces capacity. "
        
        # Apply speed factor if provided
        if self.speed is not None:
            speed_factor = self._get_speed_factor()
            capacity *= speed_factor
            if self.speed > 1.0:
                warning += f"Warning: High speed ({self.speed}m/s) reduces capacity. "
        
        return round(capacity, 2), warning.strip()

# Example usage
if __name__ == "__main__":
    try:
        # Create a PU-coated multidirectional roller
        roller = PipelineRoller(
            diameter=150.0,
            length=300.0,
            material=RollerMaterial.PU_COATED,
            direction=RollerDirection.MULTIDIRECTIONAL,
            temperature=65.0,
            speed=1.5
        )
        
        capacity, warnings = roller.calculate_load_capacity()
        print(f"Calculated load capacity: {capacity} kg")
        if warnings:
            print(warnings)
            
    except ValueError as e:
        print(f"Error: {e}")
```
