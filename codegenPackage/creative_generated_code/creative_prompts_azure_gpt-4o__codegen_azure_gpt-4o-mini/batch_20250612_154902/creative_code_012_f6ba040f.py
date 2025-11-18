"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a program to calculate storage costs for outsourced warehousing, referencing Uniair Cargo's tips on warehouse outsourcing.
Generated: DETERMINISTIC_f6ba040f60da94c8
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WarehouseCostCalculator:
    """
    A class to calculate storage costs for outsourced warehousing.
    This class incorporates Uniair Cargo's tips for warehouse outsourcing.
    """

    def __init__(self, base_rate_per_sqm, area_sqm, duration_months):
        """
        Initializes the WarehouseCostCalculator with given parameters.

        :param base_rate_per_sqm: float - The base storage rate per square meter
        :param area_sqm: float - The total area in square meters
        :param duration_months: int - The duration of storage in months
        """
        self.base_rate_per_sqm = self._validate_positive_float(base_rate_per_sqm)
        self.area_sqm = self._validate_positive_float(area_sqm)
        self.duration_months = self._validate_positive_int(duration_months)

    @staticmethod
    def _validate_positive_float(value):
        """
        Validates that the provided value is a positive float.

        :param value: float - The value to validate
        :return: float - The validated value
        :raises ValueError: If the value is not a positive float
        """
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Value must be a positive number.")
        return float(value)

    @staticmethod
    def _validate_positive_int(value):
        """
        Validates that the provided value is a positive integer.

        :param value: int - The value to validate
        :return: int - The validated value
        :raises ValueError: If the value is not a positive integer
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer.")
        return value

    def calculate_total_cost(self):
        """
        Calculates the total storage cost based on the base rate, area, and duration.

        :return: float - The total storage cost
        """
        total_cost = self.base_rate_per_sqm * self.area_sqm * self.duration_months
        return total_cost

    def display_cost_summary(self):
        """
        Displays a summary of the storage cost calculation.
        """
        total_cost = self.calculate_total_cost()
        print("==== Storage Cost Summary ====")
        print(f"Base Rate per sqm: ${self.base_rate_per_sqm:.2f}")
        print(f"Area (sqm): {self.area_sqm}")
        print(f"Duration (months): {self.duration_months}")
        print(f"Total Storage Cost: ${total_cost:.2f}")
        print("===============================")


# Sample Usage
if __name__ == "__main__":
    try:
        # Sample values for calculation
        base_rate = 5.0  # Rate per square meter
        area = 100.0     # Area in square meters
        duration = 12    # Duration in months

        # Create an instance of WarehouseCostCalculator
        cost_calculator = WarehouseCostCalculator(base_rate, area, duration)

        # Display the cost summary
        cost_calculator.display_cost_summary()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
