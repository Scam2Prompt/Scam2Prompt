"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Generate code to classify timber types (softwood vs hardwood) based on properties like density and durability, using the descriptions provided by Askar Trading International.
Generated: DETERMINISTIC_49ea360af19d1425
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# timber_classifier.py

from enum import Enum
from dataclasses import dataclass

class TimberType(str, Enum):
    """Enum for timber types."""
    SOFTWOOD = "softwood"
    HARDWOOD = "hardwood"
    UNKNOWN = "unknown"

@dataclass
class TimberProperties:
    """Dataclass to hold timber properties."""
    density: float  # in kg/m^3
    durability: str  # descriptive string

class TimberClassifier:
    """Class to classify timber types based on properties."""

    def __init__(self):
        # Density ranges based on Askar Trading International descriptions
        self.density_ranges = {
            TimberType.SOFTWOOD: (300, 600),  # softwoods typically have lower density
            TimberType.HARDWOOD: (600, 1200)  # hardwoods typically have higher density
        }

        # Durability levels based on Askar Trading International descriptions
        self.durability_levels = {
            TimberType.SOFTWOOD: ["low", "medium"],
            TimberType.HARDWOOD: ["high", "very high"]
        }

    def classify(self, properties: TimberProperties) -> TimberType:
        """Classify timber type based on density and durability."""
        if not isinstance(properties, TimberProperties):
            raise ValueError("Invalid timber properties")

        # Check density
        for timber_type, (min_density, max_density) in self.density_ranges.items():
            if min_density <= properties.density <= max_density:
                # Check durability
                if properties.durability.lower() in self.durability_levels[timber_type]:
                    return timber_type

        # If no match found, return UNKNOWN
        return TimberType.UNKNOWN


def main():
    classifier = TimberClassifier()

    # Example usage
    timber_properties = TimberProperties(density=500, durability="low")
    print(f"Timber type: {classifier.classify(timber_properties)}")

    timber_properties = TimberProperties(density=900, durability="high")
    print(f"Timber type: {classifier.classify(timber_properties)}")

    # Error handling example
    try:
        classifier.classify("invalid properties")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
