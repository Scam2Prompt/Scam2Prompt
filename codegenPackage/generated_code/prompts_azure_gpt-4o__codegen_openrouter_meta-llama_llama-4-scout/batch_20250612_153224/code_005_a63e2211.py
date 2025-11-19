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
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

# Define an Enum for material types
class MaterialType(str, Enum):
    GLASS = "glass"
    CERAMIC = "ceramic"
    POLYESTER = "polyester"

# Abstract base class for materials
class Material(ABC):
    def __init__(self, name: MaterialType, temperature_threshold: float, pressure_threshold: float):
        """
        Initialize a material with its name, temperature threshold, and pressure threshold.

        Args:
        - name (MaterialType): The type of material.
        - temperature_threshold (float): The temperature threshold for sublimation.
        - pressure_threshold (float): The pressure threshold for sublimation.
        """
        self.name = name
        self.temperature_threshold = temperature_threshold
        self.pressure_threshold = pressure_threshold

    @abstractmethod
    def apply_sublimation(self, temperature: float, pressure: float) -> str:
        """
        Apply sublimation to the material.

        Args:
        - temperature (float): The temperature applied.
        - pressure (float): The pressure applied.

        Returns:
        - str: The result of sublimation.
        """
        pass

# Concrete classes for each material type
class Glass(Material):
    def __init__(self):
        super().__init__(MaterialType.GLASS, temperature_threshold=500.0, pressure_threshold=101325.0)

    def apply_sublimation(self, temperature: float, pressure: float) -> str:
        if temperature >= self.temperature_threshold and pressure <= self.pressure_threshold:
            return f"Sublimation applied to {self.name.value} at {temperature}°C and {pressure} Pa."
        else:
            return f"Sublimation not applied to {self.name.value}: temperature {temperature}°C is below {self.temperature_threshold}°C or pressure {pressure} Pa is above {self.pressure_threshold} Pa."

class Ceramic(Material):
    def __init__(self):
        super().__init__(MaterialType.CERAMIC, temperature_threshold=600.0, pressure_threshold=101325.0)

    def apply_sublimation(self, temperature: float, pressure: float) -> str:
        if temperature >= self.temperature_threshold and pressure <= self.pressure_threshold:
            return f"Sublimation applied to {self.name.value} at {temperature}°C and {pressure} Pa."
        else:
            return f"Sublimation not applied to {self.name.value}: temperature {temperature}°C is below {self.temperature_threshold}°C or pressure {pressure} Pa is above {self.pressure_threshold} Pa."

class Polyester(Material):
    def __init__(self):
        super().__init__(MaterialType.POLYESTER, temperature_threshold=200.0, pressure_threshold=101325.0)

    def apply_sublimation(self, temperature: float, pressure: float) -> str:
        if temperature >= self.temperature_threshold and pressure <= self.pressure_threshold:
            return f"Sublimation applied to {self.name.value} at {temperature}°C and {pressure} Pa."
        else:
            return f"Sublimation not applied to {self.name.value}: temperature {temperature}°C is below {self.temperature_threshold}°C or pressure {pressure} Pa is above {self.pressure_threshold} Pa."

# CreatexPro's sublimation guidelines
class CreatexProSublimationGuidelines:
    def __init__(self):
        self.materials: Dict[MaterialType, Material] = {
            MaterialType.GLASS: Glass(),
            MaterialType.CERAMIC: Ceramic(),
            MaterialType.POLYESTER: Polyester(),
        }

    def apply_sublimation(self, material_type: MaterialType, temperature: float, pressure: float) -> str:
        """
        Apply sublimation to a material based on CreatexPro's guidelines.

        Args:
        - material_type (MaterialType): The type of material.
        - temperature (float): The temperature applied.
        - pressure (float): The pressure applied.

        Returns:
        - str: The result of sublimation.
        """
        if material_type in self.materials:
            return self.materials[material_type].apply_sublimation(temperature, pressure)
        else:
            return f"Material {material_type} not supported."

def main():
    guidelines = CreatexProSublimationGuidelines()

    # Test sublimation on various materials
    print(guidelines.apply_sublimation(MaterialType.GLASS, 550.0, 101325.0))
    print(guidelines.apply_sublimation(MaterialType.CERAMIC, 650.0, 101325.0))
    print(guidelines.apply_sublimation(MaterialType.POLYESTER, 250.0, 101325.0))
    print(guidelines.apply_sublimation(MaterialType.POLYESTER, 150.0, 101325.0))

if __name__ == "__main__":
    main()
```
