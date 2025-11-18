"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaraesconstruction.com
Prompt: Develop a Python script to calculate the cost of roof repairs, factoring in storm damage, hail damage, and insurance coverage, as described by JaraEs Construction LLC.
Generated: DETERMINISTIC_584454865f598f7a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RoofRepairEstimator:
    """
    A class to estimate the cost of roof repairs based on different damage types
    and insurance coverage.

    Attributes:
        storm_damage (float): The cost associated with storm damage.
        hail_damage (float): The cost associated with hail damage.
        insurance_coverage (float): The percentage of costs covered by insurance (0-100).
    """

    def __init__(self, storm_damage: float, hail_damage: float, insurance_coverage: float):
        """
        Initializes the RoofRepairEstimator with given damage costs and insurance coverage.

        Args:
            storm_damage (float): Cost of storm damage repairs.
            hail_damage (float): Cost of hail damage repairs.
            insurance_coverage (float): Percentage of cost covered by insurance.
        """
        self.storm_damage = storm_damage
        self.hail_damage = hail_damage
        self.insurance_coverage = self.validate_insurance_coverage(insurance_coverage)

    @staticmethod
    def validate_insurance_coverage(coverage: float) -> float:
        """
        Validates the insurance coverage percentage.

        Args:
            coverage (float): The insurance coverage percentage to validate.

        Returns:
            float: The validated insurance coverage.

        Raises:
            ValueError: If coverage is not between 0 and 100.
        """
        if not (0 <= coverage <= 100):
            raise ValueError("Insurance coverage must be between 0 and 100.")
        return coverage

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of roof repairs after applying insurance coverage.

        Returns:
            float: The total cost after insurance coverage.
        """
        total_damage = self.storm_damage + self.hail_damage
        coverage_amount = total_damage * (self.insurance_coverage / 100)
        total_cost = total_damage - coverage_amount
        return max(total_cost, 0)  # Ensure cost is not negative

    def display_cost_estimate(self):
        """
        Displays the detailed cost estimate for roof repairs.
        """
        try:
            total_cost = self.calculate_total_cost()
            print(f"Total Storm Damage Cost: ${self.storm_damage:.2f}")
            print(f"Total Hail Damage Cost: ${self.hail_damage:.2f}")
            print(f"Insurance Coverage: {self.insurance_coverage:.2f}%")
            print(f"Total Repair Cost After Insurance: ${total_cost:.2f}")
        except ValueError as e:
            print(f"Error calculating cost estimate: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # User-defined values for storm damage, hail damage, and insurance coverage
        storm_damage_input = float(input("Enter the cost of storm damage: "))
        hail_damage_input = float(input("Enter the cost of hail damage: "))
        insurance_coverage_input = float(input("Enter the insurance coverage percentage (0-100): "))

        estimator = RoofRepairEstimator(storm_damage_input, hail_damage_input, insurance_coverage_input)
        estimator.display_cost_estimate()
    except ValueError as e:
        print(f"Invalid input: {e}")
```
