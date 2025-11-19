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
"""
premium_calculator.py

A Python library for calculating insurance premiums for goods that need to be kept intact.
The premium is calculated based on the value of the goods, risk of damage, and storage conditions.

Author: [Your Name]
Date: [Today's Date]
"""

class PremiumCalculator:
    """
    A class to calculate insurance premiums for goods.
    """

    def __init__(self):
        """
        Initializes the PremiumCalculator with default risk factors.
        """
        # Default risk multipliers for storage conditions
        self.storage_risk_factors = {
            "excellent": 0.8,  # Low risk
            "good": 1.0,       # Normal risk
            "average": 1.2,    # Slightly higher risk
            "poor": 1.5        # High risk
        }

    def calculate_premium(self, value, risk_of_damage, storage_condition):
        """
        Calculate the insurance premium for goods.

        Parameters:
            value (float): The monetary value of the goods.
            risk_of_damage (float): The risk of damage as a percentage (0 to 100).
            storage_condition (str): The storage condition ('excellent', 'good', 'average', 'poor').

        Returns:
            float: The calculated premium.

        Raises:
            ValueError: If any input is invalid.
        """
        # Input validation
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Value must be a positive number.")
        if not isinstance(risk_of_damage, (int, float)) or not (0 <= risk_of_damage <= 100):
            raise ValueError("Risk of damage must be a percentage between 0 and 100.")
        if storage_condition not in self.storage_risk_factors:
            raise ValueError(f"Invalid storage condition. Must be one of {list(self.storage_risk_factors.keys())}.")

        # Calculate the base premium
        base_premium = value * (risk_of_damage / 100)

        # Adjust premium based on storage condition
        storage_multiplier = self.storage_risk_factors[storage_condition]
        final_premium = base_premium * storage_multiplier

        return round(final_premium, 2)

    def add_storage_condition(self, condition, multiplier):
        """
        Add or update a storage condition and its associated risk multiplier.

        Parameters:
            condition (str): The name of the storage condition.
            multiplier (float): The risk multiplier for the condition.

        Raises:
            ValueError: If the multiplier is not a positive number.
        """
        if not isinstance(multiplier, (int, float)) or multiplier <= 0:
            raise ValueError("Multiplier must be a positive number.")
        self.storage_risk_factors[condition] = multiplier

    def remove_storage_condition(self, condition):
        """
        Remove a storage condition from the risk factors.

        Parameters:
            condition (str): The name of the storage condition to remove.

        Raises:
            KeyError: If the condition does not exist.
        """
        if condition not in self.storage_risk_factors:
            raise KeyError(f"Storage condition '{condition}' does not exist.")
        del self.storage_risk_factors[condition]


# Example usage (if run as a script)
if __name__ == "__main__":
    try:
        calculator = PremiumCalculator()

        # Example calculation
        value = 10000  # Value of goods in dollars
        risk_of_damage = 10  # Risk of damage in percentage
        storage_condition = "good"  # Storage condition

        premium = calculator.calculate_premium(value, risk_of_damage, storage_condition)
        print(f"The calculated premium is: ${premium}")

        # Adding a new storage condition
        calculator.add_storage_condition("extreme", 2.0)

        # Recalculating with the new condition
        premium = calculator.calculate_premium(value, risk_of_damage, "extreme")
        print(f"The calculated premium with 'extreme' storage condition is: ${premium}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
