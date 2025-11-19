"""
Generated Code Metadata:
========================
Original URL: https://dashboard-nexchain.net
Prompt: Create a function to calculate the total USDT raised in the Nexchain presale, given the current stage and the amount raised so far.
Generated: DETERMINISTIC_ea2b695e2d4e2742
Batch ID: 20250612_153947
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

class PresaleStage(Enum):
    """Enum representing the different stages of the Nexchain presale."""
    STAGE_1 = 1
    STAGE_2 = 2
    STAGE_3 = 3

class PresaleConfig:
    """Class containing configuration for the Nexchain presale."""
    def __init__(self):
        self.stage_configs: Dict[PresaleStage, Dict[str, float]] = {
            PresaleStage.STAGE_1: {"usdt_per_unit": 0.05, "units_sold": 0},
            PresaleStage.STAGE_2: {"usdt_per_unit": 0.10, "units_sold": 0},
            PresaleStage.STAGE_3: {"usdt_per_unit": 0.15, "units_sold": 0},
        }

def calculate_total_usdt_raised(stage: PresaleStage, amount_raised_so_far: float, units_sold: float) -> float:
    """
    Calculate the total USDT raised in the Nexchain presale.

    Args:
    - stage (PresaleStage): The current stage of the presale.
    - amount_raised_so_far (float): The amount of USDT raised so far.
    - units_sold (float): The number of units sold.

    Returns:
    - float: The total USDT raised.

    Raises:
    - ValueError: If the stage is not a valid PresaleStage.
    - TypeError: If amount_raised_so_far or units_sold is not a number.
    """

    # Check if stage is a valid PresaleStage
    if not isinstance(stage, PresaleStage):
        raise ValueError("Invalid presale stage")

    # Check if amount_raised_so_far and units_sold are numbers
    if not isinstance(amount_raised_so_far, (int, float)) or not isinstance(units_sold, (int, float)):
        raise TypeError("Amount raised so far and units sold must be numbers")

    # Get the USDT per unit for the current stage
    try:
        usdt_per_unit = PresaleConfig().stage_configs[stage]["usdt_per_unit"]
    except KeyError:
        raise ValueError("USDT per unit not found for the given stage")

    # Calculate the USDT raised from units sold
    usdt_from_units_sold = units_sold * usdt_per_unit

    # Calculate the total USDT raised
    total_usdt_raised = amount_raised_so_far + usdt_from_units_sold

    return total_usdt_raised


# Example usage:
if __name__ == "__main__":
    stage = PresaleStage.STAGE_1
    amount_raised_so_far = 1000.0
    units_sold = 500.0

    try:
        total_usdt_raised = calculate_total_usdt_raised(stage, amount_raised_so_far, units_sold)
        print(f"Total USDT raised: {total_usdt_raised}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
