"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Write code to simulate the application of sublimation on various materials like glass, ceramic, and polyester, as outlined by CreatexPro.
Generated: DETERMINISTIC_a63e22117e71a4c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, Optional, Tuple

class MaterialType(Enum):
    """Enum representing different material types for sublimation."""
    GLASS = "glass"
    CERAMIC = "ceramic"
    POLYESTER = "polyester"

class SublimationResult:
    """Class to represent the result of a sublimation process."""
    def __init__(self, success: bool, message: str, temperature: float, time: int):
        self.success = success
        self.message = message
        self.temperature = temperature
        self.time = time

    def __str__(self):
        return f"Success: {self.success}, Message: {self.message}, Temperature: {self.temperature}°C, Time: {self.time}s"

class SublimationSimulator:
    """Simulates the sublimation process on various materials."""
    
    # Material-specific parameters (temperature in °C, time in seconds)
    MATERIAL_PARAMS = {
        MaterialType.GLASS: {"min_temp": 160, "max_temp": 200, "min_time": 180, "max_time": 240},
        MaterialType.CERAMIC: {"min_temp": 180, "max_temp": 220, "min_time": 240, "max_time": 300},
        MaterialType.POLYESTER: {"min_temp": 190, "max_temp": 210, "min_time": 150, "max_time": 210}
    }

    @classmethod
    def simulate_sublimation(cls, material: MaterialType, temperature: Optional[float] = None, time: Optional[int] = None) -> SublimationResult:
        """
        Simulate sublimation on a given material.
        
        Args:
            material: The material type to simulate sublimation on.
            temperature: Optional custom temperature (in °C). If None, uses random within material range.
            time: Optional custom time (in seconds). If None, uses random within material range.
            
        Returns:
            SublimationResult: Object containing the simulation results.
        """
        try:
            if material not in cls.MATERIAL_PARAMS:
                raise ValueError(f"Unsupported material type: {material}")
            
            params = cls.MATERIAL_PARAMS[material]
            
            # Use provided values or generate random ones within range
            actual_temp = temperature if temperature is not None else random.uniform(params["min_temp"], params["max_temp"])
            actual_time = time if time is not None else random.randint(params["min_time"], params["max_time"])
            
            # Simulate success/failure with some randomness
            success = random.random() > 0.1  # 90% success rate
            
            if success:
                message = f"Sublimation on {material.value} was successful"
            else:
                message = f"Sublimation on {material.value} failed (possible causes: temperature fluctuation, time mismatch)"
            
            return SublimationResult(success, message, actual_temp, actual_time)
            
        except Exception as e:
            return SublimationResult(False, f"Error during simulation: {str(e)}", 0, 0)

# Example usage
if __name__ == "__main__":
    # Test with different materials
    materials = [MaterialType.GLASS, MaterialType.CERAMIC, MaterialType.POLYESTER]
    
    for material in materials:
        # Run simulation with default parameters
        result = SublimationSimulator.simulate_sublimation(material)
        print(f"Material: {material.value}")
        print(result)
        print()
        
        # Run simulation with custom parameters
        custom_result = SublimationSimulator.simulate_sublimation(material, temperature=185, time=200)
        print(f"Material: {material.value} (custom params)")
        print(custom_result)
        print("-" * 50)
```
