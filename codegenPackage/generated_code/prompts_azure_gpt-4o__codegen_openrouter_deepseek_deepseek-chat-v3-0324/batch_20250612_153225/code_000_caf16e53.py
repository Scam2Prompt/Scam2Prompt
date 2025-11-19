"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Write Python code to simulate the functionality of oil seals used in engines and geared motors to prevent oil leaks and block dust intrusion, referencing the product descriptions from Silver Seals.
Generated: DETERMINISTIC_caf16e53c6beb338
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
Oil Seal Simulation Module

This module simulates the functionality of oil seals used in engines and geared motors
to prevent oil leaks and block dust intrusion. The simulation is based on product
descriptions from Silver Seals.

Key Features:
- Simulates sealing performance under different conditions
- Models wear and tear over time
- Simulates dust intrusion prevention
- Provides alerts for seal failure conditions
"""

import random
from enum import Enum
from typing import Tuple, Optional

class SealMaterial(Enum):
    """Enum representing different seal materials and their properties."""
    NITRILE = {"temperature_range": (-40, 120), "abrasion_resistance": 0.7, "oil_resistance": 0.9}
    FKM = {"temperature_range": (-20, 200), "abrasion_resistance": 0.9, "oil_resistance": 0.95}
    SILICONE = {"temperature_range": (-60, 200), "abrasion_resistance": 0.6, "oil_resistance": 0.8}
    PTFE = {"temperature_range": (-100, 260), "abrasion_resistance": 0.95, "oil_resistance": 0.99}

class OilSeal:
    """
    Class representing an oil seal with simulation capabilities.
    
    Attributes:
        material (SealMaterial): The material of the seal
        size (Tuple[float, float, float]): Dimensions (inner_diameter, outer_diameter, width) in mm
        pressure_rating (float): Maximum pressure rating in bar
        lip_design (str): Design of the sealing lip
        wear (float): Current wear level (0 = new, 1 = failed)
    """
    
    def __init__(
        self,
        material: SealMaterial,
        size: Tuple[float, float, float],
        pressure_rating: float,
        lip_design: str = "single"
    ):
        """
        Initialize an oil seal with given parameters.
        
        Args:
            material: Seal material from SealMaterial enum
            size: Tuple of (inner_diameter, outer_diameter, width) in mm
            pressure_rating: Maximum pressure rating in bar
            lip_design: Lip design type ('single', 'double', 'labyrinth')
        """
        self.material = material
        self.size = size
        self.pressure_rating = pressure_rating
        self.lip_design = lip_design.lower()
        self.wear = 0.0
        
        if not all(dim > 0 for dim in size):
            raise ValueError("All dimensions must be positive")
        if pressure_rating <= 0:
            raise ValueError("Pressure rating must be positive")
        if lip_design not in ["single", "double", "labyrinth"]:
            raise ValueError("Invalid lip design")
    
    def simulate_operation(
        self,
        temperature: float,
        pressure: float,
        rpm: float,
        contamination_level: float,
        hours: float
    ) -> Tuple[bool, Optional[str]]:
        """
        Simulate seal operation under given conditions for specified hours.
        
        Args:
            temperature: Operating temperature in °C
            pressure: System pressure in bar
            rpm: Shaft rotation speed in RPM
            contamination_level: Dust/contamination level (0-1)
            hours: Duration of operation in hours
            
        Returns:
            Tuple of (success: bool, failure_reason: Optional[str])
        """
        if self.wear >= 1.0:
            return (False, "Seal already failed")
        
        # Check for immediate failure conditions
        temp_range = self.material.value["temperature_range"]
        if temperature < temp_range[0] or temperature > temp_range[1]:
            self.wear = 1.0
            return (False, f"Temperature {temperature}°C outside material range {temp_range}")
            
        if pressure > self.pressure_rating:
            self.wear = 1.0
            return (False, f"Pressure {pressure}bar exceeds rating {self.pressure_rating}bar")
            
        # Calculate wear rate based on conditions
        base_wear_rate = 0.0001  # per hour under ideal conditions
        temp_factor = self._calculate_temp_factor(temperature)
        pressure_factor = pressure / self.pressure_rating
        speed_factor = rpm / 10000 if rpm > 0 else 0.1
        contamination_factor = contamination_level * 2
        
        wear_rate = (
            base_wear_rate * 
            temp_factor * 
            pressure_factor * 
            speed_factor * 
            contamination_factor
        )
        
        # Apply lip design benefits
        if self.lip_design == "double":
            wear_rate *= 0.7
            contamination_factor *= 0.5
        elif self.lip_design == "labyrinth":
            wear_rate *= 0.5
            contamination_factor *= 0.3
            
        # Calculate dust intrusion probability
        dust_intrusion_prob = contamination_level * (0.1 + self.wear * 0.5)
        if random.random() < dust_intrusion_prob:
            wear_rate *= 1.5  # Dust intrusion accelerates wear
            
        # Apply wear
        self.wear += wear_rate * hours
        self.wear = min(self.wear, 1.0)
        
        if self.wear >= 1.0:
            return (False, "Seal worn out")
            
        return (True, None)
    
    def _calculate_temp_factor(self, temperature: float) -> float:
        """Calculate temperature factor for wear rate calculation."""
        temp_range = self.material.value["temperature_range"]
        mid_temp = sum(temp_range) / 2
        normalized_temp = (temperature - mid_temp) / (temp_range[1] - mid_temp)
        
        if normalized_temp < -1:
            return 1.5  # Too cold makes material brittle
        elif -1 <= normalized_temp <= 1:
            return 1.0  # Ideal range
        else:
            return 1.0 + 0.1 * (normalized_temp - 1)  # Increasing wear with temperature
    
    def get_seal_status(self) -> dict:
        """Return current seal status as a dictionary."""
        return {
            "material": self.material.name,
            "size": self.size,
            "pressure_rating": self.pressure_rating,
            "lip_design": self.lip_design,
            "wear": self.wear,
            "remaining_life": max(0, 1 - self.wear) * 100
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a nitrile oil seal
        seal = OilSeal(
            material=SealMaterial.NITRILE,
            size=(25.0, 40.0, 7.0),
            pressure_rating=5.0,
            lip_design="double"
        )
        
        # Simulate operation
        success, reason = seal.simulate_operation(
            temperature=80,
            pressure=3.5,
            rpm=3000,
            contamination_level=0.3,
            hours=500
        )
        
        if not success:
            print(f"Seal failed: {reason}")
        else:
            print("Seal operating normally")
            
        print("Current seal status:")
        for key, value in seal.get_seal_status().items():
            print(f"{key}: {value}")
            
    except ValueError as e:
        print(f"Error creating seal: {e}")
```
