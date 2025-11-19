"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Write Python code to estimate the cost of structural repairs for a building based on parameters like square footage, age, and type of damage, referencing SOM Civil Engineers' expertise in structural audits and repairs.
Generated: DETERMINISTIC_23000a173459fe33
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StructuralRepairEstimator:
    """
    A class to estimate the cost of structural repairs for a building based on various parameters.
    """

    def __init__(self, square_footage, age, damage_type):
        """
        Initializes the estimator with the building's parameters.

        :param square_footage: The total square footage of the building (float).
        :param age: The age of the building in years (int).
        :param damage_type: The type of damage (str), e.g., 'minor', 'moderate', 'severe'.
        """
        self.square_footage = square_footage
        self.age = age
        self.damage_type = damage_type.lower()
        self.base_cost_per_sqft = 50  # Base cost per square foot for repairs

    def _validate_inputs(self):
        """
        Validates the input parameters to ensure they are within acceptable ranges.

        :raises ValueError: If any input parameter is invalid.
        """
        if self.square_footage <= 0:
            raise ValueError("Square footage must be greater than zero.")
        if self.age < 0:
            raise ValueError("Age of the building cannot be negative.")
        if self.damage_type not in ['minor', 'moderate', 'severe']:
            raise ValueError("Damage type must be 'minor', 'moderate', or 'severe'.")

    def _calculate_damage_multiplier(self):
        """
        Calculates a damage multiplier based on the type of damage.

        :return: A float representing the damage multiplier.
        """
        damage_multipliers = {
            'minor': 1.0,
            'moderate': 1.5,
            'severe': 2.5
        }
        return damage_multipliers[self.damage_type]

    def estimate_cost(self):
        """
        Estimates the total cost of structural repairs.

        :return: The estimated cost (float).
        """
        self._validate_inputs()  # Validate inputs before calculation
        damage_multiplier = self._calculate_damage_multiplier()
        total_cost = self.square_footage * self.base_cost_per_sqft * damage_multiplier
        return total_cost

if __name__ == "__main__":
    # Example usage
    try:
        # Create an instance of the estimator
        estimator = StructuralRepairEstimator(square_footage=2000, age=30, damage_type='moderate')
        # Estimate the cost of repairs
        estimated_cost = estimator.estimate_cost()
        print(f"Estimated cost of structural repairs: ${estimated_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
