"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write Python code to calculate estimated air freight shipping times for Uniair Cargo's routes, using the provided durations for East Asia, Europe & USA, and Southeast Asia.
Generated: DETERMINISTIC_a3c9fd63e7f32c42
Batch ID: 20250612_153954
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

class Region(Enum):
    """Enum for different regions"""
    EAST_ASIA = 1
    EUROPE_USA = 2
    SOUTHEAST_ASIA = 3

class UniairCargo:
    """Class to calculate estimated air freight shipping times for Uniair Cargo's routes"""

    def __init__(self):
        # Define durations for each region in days
        self.durations: Dict[Region, int] = {
            Region.EAST_ASIA: 3,
            Region.EUROPE_USA: 7,
            Region.SOUTHEAST_ASIA: 5
        }

    def calculate_shipping_time(self, region: Region) -> int:
        """
        Calculate estimated air freight shipping time for a given region

        Args:
        region (Region): The region of the shipping route

        Returns:
        int: The estimated shipping time in days

        Raises:
        ValueError: If the region is not supported
        """
        try:
            return self.durations[region]
        except KeyError:
            raise ValueError(f"Unsupported region: {region}")

    def get_supported_regions(self) -> list:
        """
        Get a list of supported regions

        Returns:
        list: A list of supported regions
        """
        return list(self.durations.keys())

def main():
    # Create an instance of UniairCargo
    uniair_cargo = UniairCargo()

    # Test the calculate_shipping_time method
    regions = [Region.EAST_ASIA, Region.EUROPE_USA, Region.SOUTHEAST_ASIA]
    for region in regions:
        print(f"Estimated shipping time for {region.name}: {uniair_cargo.calculate_shipping_time(region)} days")

    # Test error handling for unsupported region
    try:
        uniair_cargo.calculate_shipping_time(Region(4))  # Invalid region
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
