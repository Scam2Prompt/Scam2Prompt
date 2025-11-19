"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Create a function that calculates the trade-in value of a used Suzuki car based on the Suzuki Certified Used Car Program guidelines mentioned on the Suzuki Capital Motors site.
Generated: DETERMINISTIC_dcae60673f0840fe
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SuzukiTradeInCalculator:
    """
    A class to calculate the trade-in value of a used Suzuki car 
    based on the Suzuki Certified Used Car Program guidelines.
    """

    def __init__(self, base_value: float):
        """
        Initializes the calculator with the base value of the car.

        :param base_value: The initial value of the vehicle.
        """
        if base_value <= 0:
            raise ValueError("Base value must be a positive number.")
        self.base_value = base_value

    def calculate_trade_in_value(self, mileage: int, condition: str) -> float:
        """
        Calculate the trade-in value of the Suzuki car.

        :param mileage: The mileage of the car in kilometers.
        :param condition: The condition of the car (e.g., 'excellent', 'good', 'fair', 'poor').
        :return: The calculated trade-in value.
        """
        condition_multiplier = {
            'excellent': 1.2,
            'good': 1.0,
            'fair': 0.8,
            'poor': 0.5
        }

        # Validate inputs
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        if condition not in condition_multiplier:
            raise ValueError(f"Condition must be one of {list(condition_multiplier.keys())}.")

        # Calculate depreciation based on mileage
        mileage_depreciation = self.depreciation_based_on_mileage(mileage)

        # Calculate trade-in value
        trade_in_value = self.base_value * condition_multiplier[condition] - mileage_depreciation

        # Ensure the trade-in value is not negative
        return max(trade_in_value, 0)

    @staticmethod
    def depreciation_based_on_mileage(mileage: int) -> float:
        """
        Calculates depreciation based on mileage.

        :param mileage: The mileage of the car in kilometers.
        :return: The depreciation amount.
        """
        # Depreciation logic: 0.1% per 1,000 km
        depreciation_rate_per_km = 0.001
        return mileage * depreciation_rate_per_km

# Example usage
if __name__ == "__main__":
    try:
        base_value = 15000  # Example base value in currency units
        calculator = SuzukiTradeInCalculator(base_value)
        trade_in_value = calculator.calculate_trade_in_value(mileage=60000, condition='good')
        print(f"The trade-in value of the used Suzuki car is: {trade_in_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
