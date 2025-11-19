"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Write a technical guide on specifying the level of cleanliness required for industrial parts, including factors like surface roughness, material type, and contaminant level, and using standards and regulations like ISO 9001:2015."
Generated: DETERMINISTIC_652724339362f8e2
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Guide: Specifying Cleanliness Level for Industrial Parts

This module provides a framework for specifying the cleanliness level required for industrial parts.
It considers factors such as surface roughness, material type, and contaminant level, 
and adheres to standards and regulations like ISO 9001:2015.

Author: [Your Name]
Date: [Today's Date]
"""

import enum

class MaterialType(enum.Enum):
    """Enum for material types"""
    METAL = 1
    PLASTIC = 2
    CERAMIC = 3
    OTHER = 4

class ContaminantLevel(enum.Enum):
    """Enum for contaminant levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class CleanlinessLevel:
    """Class to specify cleanliness level"""
    def __init__(self, surface_roughness, material_type, contaminant_level):
        """
        Initialize CleanlinessLevel object

        Args:
            surface_roughness (float): Surface roughness in micrometers
            material_type (MaterialType): Type of material
            contaminant_level (ContaminantLevel): Level of contaminants
        """
        self.surface_roughness = surface_roughness
        self.material_type = material_type
        self.contaminant_level = contaminant_level

    def get_cleanliness_level(self):
        """
        Determine cleanliness level based on factors

        Returns:
            str: Cleanliness level (e.g., ISO 1-5)
        """
        # Implement logic to determine cleanliness level
        # For demonstration purposes, a simple example is provided
        if self.surface_roughness < 1.0 and self.material_type == MaterialType.METAL:
            if self.contaminant_level == ContaminantLevel.LOW:
                return "ISO 1"
            elif self.contaminant_level == ContaminantLevel.MEDIUM:
                return "ISO 2"
            else:
                return "ISO 3"
        elif self.surface_roughness < 2.0 and self.material_type == MaterialType.PLASTIC:
            if self.contaminant_level == ContaminantLevel.LOW:
                return "ISO 2"
            elif self.contaminant_level == ContaminantLevel.MEDIUM:
                return "ISO 3"
            else:
                return "ISO 4"
        else:
            return "ISO 5"

    def validate_input(self):
        """
        Validate input values

        Raises:
            ValueError: If input values are invalid
        """
        if self.surface_roughness < 0:
            raise ValueError("Surface roughness cannot be negative")
        if not isinstance(self.material_type, MaterialType):
            raise ValueError("Invalid material type")
        if not isinstance(self.contaminant_level, ContaminantLevel):
            raise ValueError("Invalid contaminant level")

def main():
    try:
        surface_roughness = 1.5  # example value
        material_type = MaterialType.METAL  # example value
        contaminant_level = ContaminantLevel.MEDIUM  # example value

        cleanliness_level = CleanlinessLevel(surface_roughness, material_type, contaminant_level)
        cleanliness_level.validate_input()
        print(f"Cleanliness level: {cleanliness_level.get_cleanliness_level()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
