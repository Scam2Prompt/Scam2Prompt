"""
Generated Code Metadata:
========================
Original URL: https://www.intactified.com
Prompt: Generate a Python library for calculating premiums for goods that need to be kept intact, considering factors like value, risk of damage, and storage conditions.
Generated: DETERMINISTIC_f4c1fb62c74d81d4
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# premium_calculator.py

"""
Library for calculating premiums for goods that need to be kept intact.

This library considers factors like value, risk of damage, and storage conditions
to calculate the premium.
"""

import enum
from typing import Dict

class StorageCondition(enum.Enum):
    """Enum for storage conditions."""
    WAREHOUSE = 1
    TRUCK = 2
    OUTDOOR = 3

class PremiumCalculator:
    """Class for calculating premiums."""

    def __init__(self, base_rate: float = 0.01):
        """
        Initialize the premium calculator.

        Args:
        - base_rate (float): The base rate for premium calculation. Defaults to 0.01.
        """
        self.base_rate = base_rate

    def calculate_premium(self, value: float, risk_of_damage: float, storage_condition: StorageCondition) -> float:
        """
        Calculate the premium for a good.

        Args:
        - value (float): The value of the good.
        - risk_of_damage (float): The risk of damage for the good (between 0 and 1).
        - storage_condition (StorageCondition): The storage condition of the good.

        Returns:
        - float: The calculated premium.

        Raises:
        - ValueError: If risk_of_damage is not between 0 and 1.
        """
        if not (0 <= risk_of_damage <= 1):
            raise ValueError("Risk of damage must be between 0 and 1")

        storage_condition_factors: Dict[StorageCondition, float] = {
            StorageCondition.WAREHOUSE: 0.5,
            StorageCondition.TRUCK: 1.0,
            StorageCondition.OUTDOOR: 2.0
        }

        storage_condition_factor = storage_condition_factors[storage_condition]
        premium = value * self.base_rate * risk_of_damage * storage_condition_factor
        return premium

def main():
    calculator = PremiumCalculator()
    try:
        premium = calculator.calculate_premium(1000.0, 0.5, StorageCondition.WAREHOUSE)
        print(f"Calculated premium: {premium:.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
