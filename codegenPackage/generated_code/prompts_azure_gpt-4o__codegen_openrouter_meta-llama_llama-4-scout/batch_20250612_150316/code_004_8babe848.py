"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write code to analyze and compare sled designs for tractor pulling, incorporating the guidelines for sled measurements provided on jobbo.com.au.
Generated: DETERMINISTIC_8babe848bce4120e
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sled_design_analyzer.py

import math

class SledDesign:
    """Represents a sled design for tractor pulling."""

    def __init__(self, name, length, width, height, weight, sled_type):
        """
        Initializes a SledDesign object.

        Args:
            name (str): The name of the sled design.
            length (float): The length of the sled in meters.
            width (float): The width of the sled in meters.
            height (float): The height of the sled in meters.
            weight (float): The weight of the sled in kilograms.
            sled_type (str): The type of sled (e.g., "weight transfer", "fixed weight").
        """
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.sled_type = sled_type

    def surface_area(self):
        """Calculates the surface area of the sled."""
        # Calculate surface area: 2 * (length * width + length * height + width * height)
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        """Calculates the volume of the sled."""
        # Calculate volume: length * width * height
        return self.length * self.width * self.height


class SledComparator:
    """Compares multiple sled designs."""

    def __init__(self):
        self.sleds = []

    def add_sled(self, sled):
        """Adds a sled design to the comparator."""
        self.sleds.append(sled)

    def compare_surface_areas(self):
        """Compares the surface areas of the sled designs."""
        # Sort sleds by surface area in descending order
        sorted_sleds = sorted(self.sleds, key=lambda x: x.surface_area(), reverse=True)
        return sorted_sleds

    def compare_volumes(self):
        """Compares the volumes of the sled designs."""
        # Sort sleds by volume in descending order
        sorted_sleds = sorted(self.sleds, key=lambda x: x.volume(), reverse=True)
        return sorted_sleds


def validate_sled_measurements(length, width, height):
    """
    Validates sled measurements based on guidelines from jobbo.com.au.

    Args:
        length (float): The length of the sled in meters.
        width (float): The width of the sled in meters.
        height (float): The height of the sled in meters.

    Raises:
        ValueError: If the sled measurements are invalid.
    """
    # Guidelines from jobbo.com.au:
    # - Length: between 3.5 and 4.5 meters
    # - Width: between 1.5 and 2.5 meters
    # - Height: between 0.5 and 1.5 meters
    if not (3.5 <= length <= 4.5):
        raise ValueError("Invalid length. Must be between 3.5 and 4.5 meters.")
    if not (1.5 <= width <= 2.5):
        raise ValueError("Invalid width. Must be between 1.5 and 2.5 meters.")
    if not (0.5 <= height <= 1.5):
        raise ValueError("Invalid height. Must be between 0.5 and 1.5 meters.")


def main():
    try:
        # Create sled designs
        sled1 = SledDesign("Sled 1", 4.0, 2.0, 1.0, 1000.0, "weight transfer")
        sled2 = SledDesign("Sled 2", 3.8, 2.2, 1.2, 1200.0, "fixed weight")

        # Validate sled measurements
        validate_sled_measurements(sled1.length, sled1.width, sled1.height)
        validate_sled_measurements(sled2.length, sled2.width, sled2.height)

        # Compare sled designs
        comparator = SledComparator()
        comparator.add_sled(sled1)
        comparator.add_sled(sled2)

        # Print comparison results
        print("Surface Area Comparison:")
        for sled in comparator.compare_surface_areas():
            print(f"{sled.name}: {sled.surface_area():.2f} m^2")

        print("\nVolume Comparison:")
        for sled in comparator.compare_volumes():
            print(f"{sled.name}: {sled.volume():.2f} m^3")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
