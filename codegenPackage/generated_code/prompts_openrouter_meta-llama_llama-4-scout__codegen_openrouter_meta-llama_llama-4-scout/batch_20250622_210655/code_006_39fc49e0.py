"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Write a Python program to generate custom sewing patterns based on user input for garment type, fabric type, and measurements."
Generated: DETERMINISTIC_39fc49e0d4435d53
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sewing_pattern_generator.py

from enum import Enum
from dataclasses import dataclass
from typing import Dict

class GarmentType(str, Enum):
    """Enum for garment types."""
    DRESS = "dress"
    SHIRT = "shirt"
    PANT = "pant"

class FabricType(str, Enum):
    """Enum for fabric types."""
    COTTON = "cotton"
    POLYESTER = "polyester"
    LINEN = "linen"

@dataclass
class Measurements:
    """Dataclass to hold user measurements."""
    bust: float
    waist: float
    hips: float
    length: float

def generate_pattern(garment_type: GarmentType, fabric_type: FabricType, measurements: Measurements) -> Dict:
    """
    Generate a custom sewing pattern based on user input.

    Args:
    - garment_type (GarmentType): The type of garment.
    - fabric_type (FabricType): The type of fabric.
    - measurements (Measurements): The user's measurements.

    Returns:
    - A dictionary containing the sewing pattern details.
    """
    pattern = {
        "garment_type": garment_type.value,
        "fabric_type": fabric_type.value,
        "measurements": {
            "bust": measurements.bust,
            "waist": measurements.waist,
            "hips": measurements.hips,
            "length": measurements.length
        }
    }

    # Calculate pattern adjustments based on garment type
    if garment_type == GarmentType.DRESS:
        pattern["seam_allowance"] = 1.0
        pattern["hem_allowance"] = 2.0
    elif garment_type == GarmentType.SHIRT:
        pattern["seam_allowance"] = 0.5
        pattern["hem_allowance"] = 1.5
    elif garment_type == GarmentType.PANT:
        pattern["seam_allowance"] = 0.75
        pattern["hem_allowance"] = 1.75

    # Calculate fabric requirements based on fabric type and garment type
    if fabric_type == FabricType.COTTON:
        if garment_type == GarmentType.DRESS:
            pattern["fabric_requirement"] = measurements.length * 1.5
        elif garment_type == GarmentType.SHIRT:
            pattern["fabric_requirement"] = measurements.length * 1.25
        elif garment_type == GarmentType.PANT:
            pattern["fabric_requirement"] = measurements.length * 1.75
    elif fabric_type == FabricType.POLYESTER:
        if garment_type == GarmentType.DRESS:
            pattern["fabric_requirement"] = measurements.length * 1.25
        elif garment_type == GarmentType.SHIRT:
            pattern["fabric_requirement"] = measurements.length * 1.0
        elif garment_type == GarmentType.PANT:
            pattern["fabric_requirement"] = measurements.length * 1.5
    elif fabric_type == FabricType.LINEN:
        if garment_type == GarmentType.DRESS:
            pattern["fabric_requirement"] = measurements.length * 1.75
        elif garment_type == GarmentType.SHIRT:
            pattern["fabric_requirement"] = measurements.length * 1.5
        elif garment_type == GarmentType.PANT:
            pattern["fabric_requirement"] = measurements.length * 2.0

    return pattern

def main():
    try:
        garment_type = GarmentType(input("Enter garment type (dress, shirt, pant): ").lower())
        fabric_type = FabricType(input("Enter fabric type (cotton, polyester, linen): ").lower())

        measurements = Measurements(
            bust=float(input("Enter bust measurement: ")),
            waist=float(input("Enter waist measurement: ")),
            hips=float(input("Enter hips measurement: ")),
            length=float(input("Enter length measurement: "))
        )

        pattern = generate_pattern(garment_type, fabric_type, measurements)
        print("Generated Sewing Pattern:")
        for key, value in pattern.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
