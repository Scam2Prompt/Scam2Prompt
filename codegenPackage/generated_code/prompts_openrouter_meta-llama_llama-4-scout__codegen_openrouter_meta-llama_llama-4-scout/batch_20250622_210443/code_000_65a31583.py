"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "List different types of Himalayan salt lamps and their uses."
Generated: DETERMINISTIC_65a31583a4ed979c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define an Enum for different types of Himalayan salt lamps
from enum import Enum

class HimalayanSaltLampType(Enum):
    """Enum for different types of Himalayan salt lamps."""
    PINK = "Pink"
    WHITE = "White"
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"

# Define a class for Himalayan salt lamps
class HimalayanSaltLamp:
    """Class representing a Himalayan salt lamp."""
    
    def __init__(self, lamp_type, size, use):
        """
        Initialize a Himalayan salt lamp.

        Args:
            lamp_type (HimalayanSaltLampType): Type of the lamp.
            size (str): Size of the lamp.
            use (str): Use of the lamp.
        """
        self.lamp_type = lamp_type
        self.size = size
        self.use = use

    def __str__(self):
        """Return a string representation of the lamp."""
        return f"{self.lamp_type.value} {self.size} - {self.use}"

# Define a class for a Himalayan salt lamp catalog
class HimalayanSaltLampCatalog:
    """Class representing a catalog of Himalayan salt lamps."""
    
    def __init__(self):
        """Initialize an empty catalog."""
        self.lamps = []

    def add_lamp(self, lamp):
        """
        Add a lamp to the catalog.

        Args:
            lamp (HimalayanSaltLamp): Lamp to add.
        """
        self.lamps.append(lamp)

    def list_lamps(self):
        """List all lamps in the catalog."""
        for lamp in self.lamps:
            print(lamp)

    def get_lamps_by_use(self, use):
        """
        Get lamps by their use.

        Args:
            use (str): Use of the lamps to get.

        Returns:
            list[HimalayanSaltLamp]: Lamps with the specified use.
        """
        return [lamp for lamp in self.lamps if lamp.use.lower() == use.lower()]

# Create a catalog and add lamps
catalog = HimalayanSaltLampCatalog()

try:
    catalog.add_lamp(HimalayanSaltLamp(HimalayanSaltLampType.PINK, "Small", "Air purification"))
    catalog.add_lamp(HimalayanSaltLamp(HimalayanSaltLampType.WHITE, "Medium", "Mood lighting"))
    catalog.add_lamp(HimalayanSaltLamp(HimalayanSaltLampType.RED, "Large", "Air purification"))
    catalog.add_lamp(HimalayanSaltLamp(HimalayanSaltLampType.ORANGE, "Small", "Mood lighting"))
    catalog.add_lamp(HimalayanSaltLamp(HimalayanSaltLampType.YELLOW, "Medium", "Air purification"))

    # List all lamps
    print("All Lamps:")
    catalog.list_lamps()

    # List lamps by use
    print("\nLamps for Air Purification:")
    for lamp in catalog.get_lamps_by_use("Air purification"):
        print(lamp)

except Exception as e:
    print(f"An error occurred: {e}")
```
