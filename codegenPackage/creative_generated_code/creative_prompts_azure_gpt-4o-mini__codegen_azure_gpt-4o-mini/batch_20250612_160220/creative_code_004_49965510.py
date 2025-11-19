"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto777-dop.pages.dev
Prompt: Describe the unique features of the Harvest app for auto-compounding crypto investments.
Generated: DETERMINISTIC_499655108df3167e
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HarvestApp:
    """
    A class to represent the Harvest app for auto-compounding crypto investments.
    """

    def __init__(self, initial_investment, annual_interest_rate, compounding_frequency):
        """
        Initializes the HarvestApp with initial investment, interest rate, and compounding frequency.

        :param initial_investment: The amount of money invested initially.
        :param annual_interest_rate: The annual interest rate as a decimal (e.g., 0.05 for 5%).
        :param compounding_frequency: How often the interest is compounded per year (e.g., 12 for monthly).
        """
        self.initial_investment = initial_investment
        self.annual_interest_rate = annual_interest_rate
        self.compounding_frequency = compounding_frequency

    def calculate_future_value(self, years):
        """
        Calculate the future value of the investment after a certain number of years.

        :param years: The number of years the money is invested for.
        :return: The future value of the investment.
        :raises ValueError: If years is negative or initial_investment is non-positive.
        """
        if years < 0:
            raise ValueError("Years cannot be negative.")
        if self.initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")

        # Calculate future value using compound interest formula
        future_value = self.initial_investment * (1 + self.annual_interest_rate / self.compounding_frequency) ** (self.compounding_frequency * years)
        return future_value

    def auto_compound(self, total_years, interval_years):
        """
        Simulate auto-compounding of the investment at regular intervals.

        :param total_years: Total period for auto-compounding in years.
        :param interval_years: The interval at which compounding occurs (e.g., every year).
        :return: A list of future values at each interval.
        :raises ValueError: If interval_years is not positive or exceeds total_years.
        """
        if interval_years <= 0 or interval_years > total_years:
            raise ValueError("Interval years must be positive and less than or equal to total years.")

        future_values = []
        for year in range(0, total_years + 1, interval_years):
            future_value = self.calculate_future_value(year)
            future_values.append(future_value)

        return future_values

# Example usage (commented out for production readiness):
# try:
#     harvest_app = HarvestApp(initial_investment=1000, annual_interest_rate=0.05, compounding_frequency=12)
#     results = harvest_app.auto_compound(total_years=10, interval_years=1)
#     print("Auto-compounding results:", results)
# except ValueError as e:
#     print("Error:", e)
```
