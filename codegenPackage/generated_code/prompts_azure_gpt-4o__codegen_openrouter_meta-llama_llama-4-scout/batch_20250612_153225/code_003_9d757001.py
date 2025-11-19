"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Create a function to recommend the best PV divider setup for a meterkast installation, based on the specifications provided by Technische Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_9d75700172ef1ca0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pv_divider_recommender.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class DividerType(str, Enum):
    """Available divider types."""
    TYPE_1 = "Type 1"
    TYPE_2 = "Type 2"
    TYPE_3 = "Type 3"

@dataclass
class MeterkastSpecification:
    """Metrekast installation specifications."""
    max_current: float  # in Amps
    max_voltage: float  # in Volts
    num_phases: int

@dataclass
class PVDividerSetup:
    """Recommended PV divider setup."""
    divider_type: DividerType
    num_dividers: int
    current_rating: float  # in Amps
    voltage_rating: float  # in Volts

def recommend_pv_divider_setup(specifications: MeterkastSpecification) -> PVDividerSetup:
    """
    Recommends the best PV divider setup for a meterkast installation.

    Args:
    - specifications: Meterkast installation specifications.

    Returns:
    - Recommended PV divider setup.

    Raises:
    - ValueError: If specifications are invalid.
    """

    # Validate input specifications
    if specifications.max_current <= 0 or specifications.max_voltage <= 0:
        raise ValueError("Invalid specifications: max current and voltage must be positive")

    if specifications.num_phases not in [1, 3]:
        raise ValueError("Invalid specifications: num phases must be 1 or 3")

    # Determine recommended divider type and number of dividers
    if specifications.max_current <= 100 and specifications.num_phases == 1:
        divider_type = DividerType.TYPE_1
        num_dividers = 1
    elif specifications.max_current <= 200 and specifications.num_phases == 3:
        divider_type = DividerType.TYPE_2
        num_dividers = 2
    else:
        divider_type = DividerType.TYPE_3
        num_dividers = 3

    # Determine current and voltage ratings
    current_rating = min(specifications.max_current, 250)  # limit to 250A
    voltage_rating = min(specifications.max_voltage, 1000)  # limit to 1000V

    return PVDividerSetup(divider_type, num_dividers, current_rating, voltage_rating)

def main():
    try:
        # Example usage
        specifications = MeterkastSpecification(max_current=150, max_voltage=400, num_phases=3)
        recommended_setup = recommend_pv_divider_setup(specifications)
        print("Recommended PV Divider Setup:")
        print(f"Divider Type: {recommended_setup.divider_type}")
        print(f"Number of Dividers: {recommended_setup.num_dividers}")
        print(f"Current Rating: {recommended_setup.current_rating}A")
        print(f"Voltage Rating: {recommended_setup.voltage_rating}V")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
