"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacoin-newbridge.com
Prompt: Generate code to calculate the synthetic dollar (sUSDe) yield based on the 3.8% APY mentioned on the Ethena platform.
Generated: DETERMINISTIC_15495f7e70d60e38
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class SyntheticDollarYieldCalculator:
    """
    A class to calculate the synthetic dollar (sUSDe) yield based on a fixed 3.8% APY.
    """

    ANNUAL_PERCENTAGE_YIELD = 3.8  # APY in percentage

    @staticmethod
    def calculate_yield(principal: float, start_date: str, end_date: str) -> float:
        """
        Calculate the yield earned on a principal amount based on a 3.8% APY.
        
        :param principal: The initial investment amount in sUSDe (float).
        :param start_date: The start date of the investment in "YYYY-MM-DD" format (str).
        :param end_date: The end date of the investment in "YYYY-MM-DD" format (str).
        :return: The yield earned during the specified period (float).
        """
        try:
            # Convert input strings to datetime objects
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")

            # Validate that the end date is after the start date
            if end <= start:
                raise ValueError("End date must be after start date.")

            # Calculate the number of days in the investment period
            days_in_period = (end - start).days

            # APY formula: daily_rate = (1 + annual_rate)^(1/365) - 1
            annual_rate = SyntheticDollarYieldCalculator.ANNUAL_PERCENTAGE_YIELD / 100
            daily_rate = (1 + annual_rate) ** (1 / 365) - 1

            # Calculate the total yield: compound interest formula
            total_amount = principal * (1 + daily_rate) ** days_in_period
            yield_earned = total_amount - principal

            return round(yield_earned, 2)  # Return yield rounded to 2 decimal places
        
        except ValueError as ve:
            raise ValueError(f"Invalid date input or calculation error: {ve}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage (uncomment to test):
# calculator = SyntheticDollarYieldCalculator()
# result = calculator.calculate_yield(1000, "2023-01-01", "2023-12-31")
# print(f"Yield earned: ${result}")
```
