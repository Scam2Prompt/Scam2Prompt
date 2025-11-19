"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write a code snippet to calculate estimated delivery times for air and ocean freight based on Uniair Cargo's timelines for different regions.
Generated: DETERMINISTIC_9233778e88b07058
Batch ID: 20250612_163030
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
    US = "US"
    EU = "EU"
    ASIA = "ASIA"
    LATAM = "LATAM"
    AFRICA = "AFRICA"

class FreightType(Enum):
    """Enum for freight types"""
    AIR = "air"
    OCEAN = "ocean"

class UniairCargo:
    """Class for Uniair Cargo delivery times"""
    def __init__(self):
        # Define delivery times for different regions and freight types
        self.delivery_times: Dict[Region, Dict[FreightType, int]] = {
            Region.US: {FreightType.AIR: 3, FreightType.OCEAN: 10},
            Region.EU: {FreightType.AIR: 4, FreightType.OCEAN: 12},
            Region.ASIA: {FreightType.AIR: 5, FreightType.OCEAN: 15},
            Region.LATAM: {FreightType.AIR: 6, FreightType.OCEAN: 18},
            Region.AFRICA: {FreightType.AIR: 7, FreightType.OCEAN: 20},
        }

    def calculate_delivery_time(self, region: Region, freight_type: FreightType) -> int:
        """
        Calculate estimated delivery time for air or ocean freight

        Args:
        region (Region): Region of delivery
        freight_type (FreightType): Type of freight

        Returns:
        int: Estimated delivery time in days

        Raises:
        ValueError: If region or freight type is not supported
        """
        try:
            return self.delivery_times[region][freight_type]
        except KeyError:
            raise ValueError("Unsupported region or freight type")

def main():
    uniair_cargo = UniairCargo()

    # Example usage:
    region = Region.US
    freight_type = FreightType.AIR
    delivery_time = uniair_cargo.calculate_delivery_time(region, freight_type)
    print(f"Estimated delivery time for {freight_type.value} freight to {region.value}: {delivery_time} days")

    # Test error handling
    try:
        uniair_cargo.calculate_delivery_time(Region("Invalid"), FreightType.AIR)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
