"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write a script to calculate the optimal time for snow removal after snowfall, using the guidelines provided by VIRCOMEM for frezare-based snow clearing.
Generated: DETERMINISTIC_00a021047a34c240
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, Tuple

class SnowType(Enum):
    """Enum representing different types of snow."""
    LIGHT = 1
    MODERATE = 2
    HEAVY = 3

class TemperatureRange(Enum):
    """Enum representing temperature ranges affecting snow clearing."""
    BELOW_FREEZING = 1
    NEAR_FREEZING = 2
    ABOVE_FREEZING = 3

def calculate_optimal_time(
    snow_type: SnowType,
    temperature_range: TemperatureRange,
    snowfall_time: datetime.datetime,
    traffic_level: float = 0.5
) -> Tuple[datetime.datetime, Optional[str]]:
    """
    Calculate the optimal time for snow removal based on VIRCOMEM guidelines.

    Args:
        snow_type: Type of snowfall (LIGHT, MODERATE, HEAVY)
        temperature_range: Current temperature range (BELOW_FREEZING, NEAR_FREEZING, ABOVE_FREEZING)
        snowfall_time: Datetime when snowfall ended
        traffic_level: Traffic level factor (0.0 to 1.0, default 0.5)

    Returns:
        Tuple of (optimal_clearing_time, optional_error_message)
    """
    try:
        # Validate inputs
        if not isinstance(snow_type, SnowType):
            raise ValueError("Invalid snow_type")
        if not isinstance(temperature_range, TemperatureRange):
            raise ValueError("Invalid temperature_range")
        if not isinstance(snowfall_time, datetime.datetime):
            raise ValueError("snowfall_time must be a datetime object")
        if not 0.0 <= traffic_level <= 1.0:
            raise ValueError("traffic_level must be between 0.0 and 1.0")

        # Base clearing time in hours based on snow type
        base_hours = {
            SnowType.LIGHT: 2,
            SnowType.MODERATE: 4,
            SnowType.HEAVY: 6
        }[snow_type]

        # Temperature adjustment factor
        temp_adjustment = {
            TemperatureRange.BELOW_FREEZING: 1.5,
            TemperatureRange.NEAR_FREEZING: 1.0,
            TemperatureRange.ABOVE_FREEZING: 0.7
        }[temperature_range]

        # Traffic adjustment factor (linear scaling)
        traffic_adjustment = 0.5 + (traffic_level * 0.5)

        # Calculate total adjustment
        total_adjustment = temp_adjustment * traffic_adjustment

        # Calculate optimal clearing time
        optimal_time = snowfall_time + datetime.timedelta(
            hours=base_hours * total_adjustment
        )

        return (optimal_time, None)

    except Exception as e:
        return (datetime.datetime.min, str(e))

# Example usage
if __name__ == "__main__":
    # Test case
    snowfall_end = datetime.datetime.now()
    snow_type = SnowType.MODERATE
    temp_range = TemperatureRange.BELOW_FREEZING
    traffic = 0.7

    optimal_time, error = calculate_optimal_time(
        snow_type=snow_type,
        temperature_range=temp_range,
        snowfall_time=snowfall_end,
        traffic_level=traffic
    )

    if error:
        print(f"Error: {error}")
    else:
        print(f"Optimal snow clearing time: {optimal_time}")
```
