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
import datetime
from enum import Enum
from typing import Dict, Optional

class FreightMode(Enum):
    """Enumeration for different freight modes."""
    AIR = "AIR"
    OCEAN = "OCEAN"

class Region(Enum):
    """Enumeration for different regions."""
    NORTH_AMERICA = "NORTH_AMERICA"
    SOUTH_AMERICA = "SOUTH_AMERICA"
    EUROPE = "EUROPE"
    ASIA = "ASIA"
    AFRICA = "AFRICA"
    AUSTRALIA = "AUSTRALIA"

# Delivery time estimates in days for each region and freight mode
DELIVERY_TIMES: Dict[Region, Dict[FreightMode, int]] = {
    Region.NORTH_AMERICA: {
        FreightMode.AIR: 3,
        FreightMode.OCEAN: 14
    },
    Region.SOUTH_AMERICA: {
        FreightMode.AIR: 4,
        FreightMode.OCEAN: 21
    },
    Region.EUROPE: {
        FreightMode.AIR: 2,
        FreightMode.OCEAN: 10
    },
    Region.ASIA: {
        FreightMode.AIR: 5,
        FreightMode.OCEAN: 28
    },
    Region.AFRICA: {
        FreightMode.AIR: 6,
        FreightMode.OCEAN: 30
    },
    Region.AUSTRALIA: {
        FreightMode.AIR: 7,
        FreightMode.OCEAN: 35
    }
}

def calculate_delivery_date(
    region: Region,
    freight_mode: FreightMode,
    departure_date: Optional[datetime.date] = None
) -> datetime.date:
    """
    Calculate the estimated delivery date based on region, freight mode, and departure date.

    Args:
        region: The destination region.
        freight_mode: The freight mode (AIR or OCEAN).
        departure_date: The date when the shipment departs. Defaults to today.

    Returns:
        The estimated delivery date.

    Raises:
        ValueError: If the region or freight mode is not supported.
    """
    if departure_date is None:
        departure_date = datetime.date.today()

    try:
        transit_days = DELIVERY_TIMES[region][freight_mode]
    except KeyError as e:
        raise ValueError(f"Unsupported region or freight mode: {e}")

    return departure_date + datetime.timedelta(days=transit_days)

# Example usage
if __name__ == "__main__":
    try:
        # Example for air freight to Europe departing today
        delivery_date = calculate_delivery_date(
            region=Region.EUROPE,
            freight_mode=FreightMode.AIR
        )
        print(f"Estimated delivery date: {delivery_date.strftime('%Y-%m-%d')}")

        # Example for ocean freight to Asia with custom departure date
        custom_date = datetime.date(2023, 12, 1)
        delivery_date = calculate_delivery_date(
            region=Region.ASIA,
            freight_mode=FreightMode.OCEAN,
            departure_date=custom_date
        )
        print(f"Estimated delivery date: {delivery_date.strftime('%Y-%m-%d')}")

    except ValueError as e:
        print(f"Error calculating delivery date: {e}")
```
