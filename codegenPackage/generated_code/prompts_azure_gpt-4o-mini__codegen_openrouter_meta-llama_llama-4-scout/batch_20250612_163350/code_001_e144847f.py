"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Write a Python function that calculates the appropriate dumpster size needed for various types of waste removal, referencing the 10, 15, and 20 yard options from Junk in The Box ATL.
Generated: DETERMINISTIC_e144847f06fd3f57
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class WasteType(Enum):
    """Enum for different types of waste."""
    CONSTRUCTION = 1
    YARD_TRASH = 2
    HOUSEHOLD = 3
    FURNITURE = 4

class DumpsterSize(Enum):
    """Enum for available dumpster sizes in yards."""
    _10_YARD = 10
    _15_YARD = 15
    _20_YARD = 20

# Estimated volume of waste in cubic yards for each type
WASTE_VOLUME_ESTIMATES: Dict[WasteType, float] = {
    WasteType.CONSTRUCTION: 10.0,  # Construction waste is dense, estimate 10 cubic yards
    WasteType.YARD_TRASH: 5.0,     # Yard trash is less dense, estimate 5 cubic yards
    WasteType.HOUSEHOLD: 7.0,      # Household waste is mixed, estimate 7 cubic yards
    WasteType.FURNITURE: 8.0       # Furniture waste can be bulky, estimate 8 cubic yards
}

def calculate_dumpster_size(waste_type: WasteType, volume_of_waste: float) -> DumpsterSize:
    """
    Calculates the appropriate dumpster size needed based on waste type and volume.

    Args:
    - waste_type (WasteType): The type of waste.
    - volume_of_waste (float): The estimated volume of waste in cubic yards.

    Returns:
    - DumpsterSize: The recommended dumpster size.

    Raises:
    - ValueError: If the volume of waste is less than 0.
    """

    # Check if volume of waste is valid
    if volume_of_waste < 0:
        raise ValueError("Volume of waste cannot be less than 0.")

    # Estimate base volume from waste type if not provided
    if volume_of_waste == 0:
        base_volume = WASTE_VOLUME_ESTIMATES.get(waste_type, 0)
    else:
        base_volume = volume_of_waste

    # Determine the recommended dumpster size based on volume
    if base_volume <= 8:
        return DumpsterSize._10_YARD
    elif base_volume <= 12:
        return DumpsterSize._15_YARD
    else:
        return DumpsterSize._20_YARD

def main():
    try:
        # Example usage
        waste_type = WasteType.CONSTRUCTION
        volume_of_waste = 0  # Using waste type estimate
        recommended_size = calculate_dumpster_size(waste_type, volume_of_waste)
        print(f"For {waste_type.name} waste, the recommended dumpster size is {recommended_size.name}.")

        # Test with specific volume
        volume_of_waste = 15
        recommended_size = calculate_dumpster_size(waste_type, volume_of_waste)
        print(f"For {volume_of_waste} cubic yards of {waste_type.name} waste, the recommended dumpster size is {recommended_size.name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
