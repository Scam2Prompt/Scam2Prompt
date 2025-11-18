"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Provide code to calculate the weight reduction and stress resistance improvements of Brixton Forged™ wheels compared to OEM wheels.
Generated: DETERMINISTIC_f508e37b7b1328aa
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WheelComparison:
    """
    A class to compare the weight reduction and stress resistance improvements 
    between Brixton Forged™ wheels and OEM wheels.
    """

    def __init__(self, oem_weight: float, brixton_weight: float, oem_stress_resistance: float, brixton_stress_resistance: float):
        """
        Initialize the WheelComparison object with weights and stress resistance values.

        :param oem_weight: Weight of the OEM wheel in kilograms.
        :param brixton_weight: Weight of the Brixton wheel in kilograms.
        :param oem_stress_resistance: Stress resistance of the OEM wheel in megapascals (MPa).
        :param brixton_stress_resistance: Stress resistance of the Brixton wheel in megapascals (MPa).
        """
        self.oem_weight = self._validate_positive(oem_weight, "OEM weight must be positive")
        self.brixton_weight = self._validate_positive(brixton_weight, "Brixton weight must be positive")
        self.oem_stress_resistance = self._validate_positive(oem_stress_resistance, "OEM stress resistance must be positive")
        self.brixton_stress_resistance = self._validate_positive(brixton_stress_resistance, "Brixton stress resistance must be positive")

    @staticmethod
    def _validate_positive(value: float, message: str) -> float:
        """
        Validates that the given value is positive.

        :param value: The value to validate.
        :param message: The message to raise if the value is not positive.
        :raises ValueError: If the value is not positive.
        :return: The validated value.
        """
        if value <= 0:
            raise ValueError(message)
        return value

    def calculate_weight_reduction(self) -> float:
        """
        Calculate the weight reduction percentage from OEM to Brixton wheels.

        :return: Weight reduction percentage.
        """
        weight_reduction = ((self.oem_weight - self.brixton_weight) / self.oem_weight) * 100
        return weight_reduction

    def calculate_stress_improvement(self) -> float:
        """
        Calculate the stress resistance improvement percentage from OEM to Brixton wheels.

        :return: Stress resistance improvement percentage.
        """
        stress_improvement = ((self.brixton_stress_resistance - self.oem_stress_resistance) / self.oem_stress_resistance) * 100
        return stress_improvement

    def display_comparison(self):
        """
        Displays the comparison results of weight reduction and stress resistance improvements.
        """
        weight_reduction = self.calculate_weight_reduction()
        stress_improvement = self.calculate_stress_improvement()

        print(f"Weight Reduction: {weight_reduction:.2f}%")
        print(f"Stress Resistance Improvement: {stress_improvement:.2f}%")


if __name__ == "__main__":
    try:
        # Example initialization (values are placeholders and should be replaced with actual data)
        oem_weight_kg = 10.0  # Example: OEM wheel weight in kg
        brixton_weight_kg = 8.0  # Example: Brixton wheel weight in kg
        oem_stress_mpa = 150.0  # Example: OEM wheel stress resistance in MPa
        brixton_stress_mpa = 200.0  # Example: Brixton wheel stress resistance in MPa

        wheel_comparison = WheelComparison(oem_weight_kg, brixton_weight_kg, oem_stress_mpa, brixton_stress_mpa)
        wheel_comparison.display_comparison()

    except ValueError as e:
        print(f"Error: {e}")
```
