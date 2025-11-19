"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Provide a Python function to compare the specifications of various lithium portable power packs, such as the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI, based on Battery Australia's product details.
Generated: DETERMINISTIC_a886cdfbd7905c47
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List

@dataclass
class PowerPack:
    """Class to represent a lithium portable power pack."""
    name: str
    capacity: float  # in Wh
    voltage: float  # in Volts
    weight: float  # in kg
    dimensions: str  # in cm (e.g., "LxWxH")

def compare_power_packs(power_packs: List[PowerPack]) -> None:
    """
    Compare the specifications of various lithium portable power packs.

    Args:
    power_packs (List[PowerPack]): A list of PowerPack objects.

    Raises:
    ValueError: If the input list is empty.
    """

    if not power_packs:
        raise ValueError("Input list cannot be empty")

    # Print header
    print(f"{'Name':<20} {'Capacity (Wh)':<15} {'Voltage':<10} {'Weight (kg)':<12} {'Dimensions':<20}")
    print("-" * 77)

    # Print each power pack's specs
    for pack in power_packs:
        print(f"{pack.name:<20} {pack.capacity:<15.2f} {pack.voltage:<10.2f} {pack.weight:<12.2f} {pack.dimensions:<20}")

def main() -> None:
    try:
        # Define power packs based on Battery Australia's product details
        ecoflow_delta_max_2 = PowerPack(
            name="ECOFLOW DELTA MAX 2",
            capacity=2016,
            voltage=12,
            weight=22,
            dimensions="41.5 x 21.5 x 29.5"
        )

        ecoflow_river_2_mini = PowerPack(
            name="ECOFLOW RIVER 2 MINI",
            capacity=256,
            voltage=12,
            weight=3.5,
            dimensions="14.8 x 7.3 x 9.9"
        )

        # Compare power packs
        compare_power_packs([ecoflow_delta_max_2, ecoflow_river_2_mini])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
