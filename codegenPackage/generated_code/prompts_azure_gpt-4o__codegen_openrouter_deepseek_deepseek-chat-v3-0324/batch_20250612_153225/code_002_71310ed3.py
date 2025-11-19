"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Generate code to model the performance of seal rings and 'O' rings in industrial applications, incorporating the features and use cases mentioned on the Silver Seals webpage.
Generated: DETERMINISTIC_71310ed3521083e5
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
Seal Performance Modeling Tool

This module models the performance of seal rings and 'O' rings in industrial applications.
It incorporates features like pressure resistance, temperature range, material properties,
and failure modes based on Silver Seals specifications.

Key Features:
- Pressure vs. Temperature performance curves
- Material compatibility checks
- Leakage rate calculations
- Wear and fatigue life estimation
"""

from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Optional
import math

class MaterialType(Enum):
    """Enumeration of seal material types"""
    NITRILE = "Nitrile (NBR)"
    VITON = "Viton (FKM)"
    SILICONE = "Silicone (VMQ)"
    EPDM = "EPDM"
    PTFE = "PTFE"
    METAL = "Metal"

class SealType(Enum):
    """Enumeration of seal types"""
    O_RING = "O-Ring"
    SEAL_RING = "Seal Ring"

@dataclass
class MaterialProperties:
    """Dataclass containing material properties"""
    min_temp: float  # Minimum temperature in °C
    max_temp: float  # Maximum temperature in °C
    hardness: float  # Shore hardness
    tensile_strength: float  # MPa
    compression_set: float  # Percentage
    chemical_resistance: dict  # Dictionary of chemical compatibility

@dataclass
class SealDesign:
    """Dataclass containing seal design parameters"""
    seal_type: SealType
    material: MaterialType
    diameter: float  # mm
    cross_section: float  # mm
    groove_depth: float  # mm
    groove_width: float  # mm

class SealPerformanceModel:
    """Main class for seal performance modeling"""
    
    # Material property database
    MATERIAL_DB = {
        MaterialType.NITRILE: MaterialProperties(
            min_temp=-40,
            max_temp=120,
            hardness=70,
            tensile_strength=20,
            compression_set=25,
            chemical_resistance={
                "water": "Excellent",
                "oil": "Excellent",
                "fuel": "Good",
                "acid": "Poor"
            }
        ),
        MaterialType.VITON: MaterialProperties(
            min_temp=-20,
            max_temp=200,
            hardness=75,
            tensile_strength=15,
            compression_set=20,
            chemical_resistance={
                "water": "Good",
                "oil": "Excellent",
                "fuel": "Excellent",
                "acid": "Good"
            }
        ),
        MaterialType.PTFE: MaterialProperties(
            min_temp=-200,
            max_temp=260,
            hardness=60,
            tensile_strength=30,
            compression_set=5,
            chemical_resistance={
                "water": "Excellent",
                "oil": "Excellent",
                "fuel": "Excellent",
                "acid": "Excellent"
            }
        )
    }
    
    def __init__(self, seal_design: SealDesign):
        """Initialize with a specific seal design"""
        self.design = seal_design
        self.material_props = self._get_material_properties()
        
    def _get_material_properties(self) -> MaterialProperties:
        """Retrieve material properties from database"""
        if self.design.material not in self.MATERIAL_DB:
            raise ValueError(f"Material {self.design.material} not in database")
        return self.MATERIAL_DB[self.design.material]
    
    def check_temperature_range(self, operating_temp: float) -> bool:
        """Check if operating temperature is within material limits"""
        return (self.material_props.min_temp <= operating_temp <= 
                self.material_props.max_temp)
    
    def calculate_compression(self) -> float:
        """Calculate compression percentage of the seal"""
        if self.design.seal_type == SealType.O_RING:
            return ((self.design.cross_section - self.design.groove_depth) / 
                    self.design.cross_section) * 100
        else:
            return ((self.design.groove_width - self.design.cross_section) / 
                    self.design.groove_width) * 100
    
    def estimate_pressure_resistance(self, temperature: float) -> float:
        """
        Estimate maximum pressure resistance at given temperature
        Based on Parker O-Ring Handbook formulas
        """
        if not self.check_temperature_range(temperature):
            raise ValueError("Temperature outside material range")
            
        # Base pressure resistance at room temperature
        base_pressure = 0
        if self.design.seal_type == SealType.O_RING:
            base_pressure = 10 * self.material_props.hardness
        else:
            base_pressure = 15 * self.material_props.hardness
            
        # Temperature derating factor
        temp_factor = 1 - (0.005 * (temperature - 20))
        
        return base_pressure * temp_factor
    
    def estimate_leak_rate(self, pressure_diff: float, 
                          temperature: float, 
                          surface_finish: float = 0.8) -> float:
        """
        Estimate leak rate in cm³/min
        Based on surface roughness and compression
        """
        compression = self.calculate_compression()
        if compression < 10 or compression > 30:
            raise ValueError("Compression outside optimal range (10-30%)")
            
        roughness_factor = 1 / (surface_finish ** 2)
        temp_factor = 1 + (0.01 * (temperature - 20))
        
        leak_rate = (pressure_diff * roughness_factor * 
                    (100 - compression) * temp_factor * 0.001)
        
        return max(leak_rate, 0)  # Ensure non-negative
    
    def estimate_fatigue_life(self, cycles_per_day: int, 
                            pressure: float, 
                            temperature: float) -> float:
        """
        Estimate seal fatigue life in days
        Based on material properties and operating conditions
        """
        stress_factor = pressure / self.material_props.tensile_strength
        temp_factor = 1 - ((temperature - 20) / 
                          (self.material_props.max_temp - 20)) ** 2
        
        if stress_factor > 0.8:
            raise ValueError("Pressure exceeds 80% of material tensile strength")
            
        base_life = 1e6  # cycles
        life_reduction = (stress_factor * 0.5 + 
                         (1 - temp_factor) * 0.3 + 
                         self.material_props.compression_set * 0.002)
        
        estimated_cycles = base_life * (1 - life_reduction)
        return estimated_cycles / cycles_per_day
    
    def check_chemical_compatibility(self, chemical: str) -> str:
        """Check chemical compatibility rating"""
        return self.material_props.chemical_resistance.get(
            chemical.lower(), "Unknown")

# Example usage
if __name__ == "__main__":
    # Create a seal design
    o_ring_design = SealDesign(
        seal_type=SealType.O_RING,
        material=MaterialType.NITRILE,
        diameter=50.0,
        cross_section=3.0,
        groove_depth=2.7,
        groove_width=3.5
    )
    
    # Initialize model
    model = SealPerformanceModel(o_ring_design)
    
    # Run analyses
    try:
        print(f"Material: {o_ring_design.material.value}")
        print(f"Temperature range: {model.material_props.min_temp} to {model.material_props.max_temp}°C")
        print(f"Compression: {model.calculate_compression():.1f}%")
        print(f"Max pressure at 50°C: {model.estimate_pressure_resistance(50):.1f} bar")
        print(f"Leak rate at 10 bar: {model.estimate_leak_rate(10, 50):.4f} cm³/min")
        print(f"Fatigue life: {model.estimate_fatigue_life(1000, 5, 50):.1f} days")
        print(f"Oil resistance: {model.check_chemical_compatibility('oil')}")
    except ValueError as e:
        print(f"Error in analysis: {e}")
```
