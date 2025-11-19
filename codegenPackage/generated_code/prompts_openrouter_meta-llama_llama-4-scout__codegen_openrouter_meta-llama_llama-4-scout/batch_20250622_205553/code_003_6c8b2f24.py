"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Recommend a suitable type of lift system (e.g., personnel platform, vehicle asansör, or load asansör) for a warehouse application, taking into account the specific requirements and constraints mentioned on the OHC Lift website.
Generated: DETERMINISTIC_6c8b2f24aa0fee45
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

class LiftType(Enum):
    """Enum for lift types."""
    PERSONNEL_PLATFORM = 1
    VEHICLE_ASANSOR = 2
    LOAD_ASANSOR = 3

@dataclass
class WarehouseRequirements:
    """Dataclass for warehouse requirements."""
    load_capacity: float  # in kg
    lift_height: float  # in meters
    platform_size: float  # in square meters
    usage_frequency: str  # e.g., "low", "medium", "high"

def recommend_lift_system(requirements: WarehouseRequirements) -> LiftType:
    """
    Recommend a suitable type of lift system based on warehouse requirements.

    Args:
    requirements (WarehouseRequirements): Warehouse requirements.

    Returns:
    LiftType: Recommended lift type.

    Raises:
    ValueError: If requirements are invalid.
    """

    # Check if requirements are valid
    if requirements.load_capacity <= 0:
        raise ValueError("Load capacity must be greater than zero.")
    if requirements.lift_height <= 0:
        raise ValueError("Lift height must be greater than zero.")
    if requirements.platform_size <= 0:
        raise ValueError("Platform size must be greater than zero.")

    # Define lift type criteria
    if requirements.load_capacity > 5000 or requirements.platform_size > 10:
        # Large loads or big platforms require vehicle asansör or load asansör
        if requirements.usage_frequency == "high":
            return LiftType.VEHICLE_ASANSOR
        else:
            return LiftType.LOAD_ASANSOR
    elif requirements.lift_height > 10:
        # High lift heights require personnel platform or vehicle asansör
        if requirements.usage_frequency == "high":
            return LiftType.PERSONNEL_PLATFORM
        else:
            return LiftType.VEHICLE_ASANSOR
    else:
        # Default to personnel platform for low to medium requirements
        return LiftType.PERSONNEL_PLATFORM

def main():
    try:
        # Example usage
        requirements = WarehouseRequirements(
            load_capacity=2000,
            lift_height=5,
            platform_size=2,
            usage_frequency="medium"
        )
        recommended_lift = recommend_lift_system(requirements)
        print(f"Recommended lift type: {recommended_lift.name}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
