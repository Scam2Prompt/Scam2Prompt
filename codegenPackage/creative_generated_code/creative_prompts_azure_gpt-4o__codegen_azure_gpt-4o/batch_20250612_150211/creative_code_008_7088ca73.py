"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradeflex-gpt.com
Prompt: Write code to model the performance of mutual funds and ETFs, using TradeFlex GPT's descriptions of these investment vehicles.
Generated: DETERMINISTIC_7088ca73b8579c53
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import random

class InvestmentVehicle:
    """
    Base class for modeling investment vehicles such as mutual funds and ETFs.
    """
    def __init__(self, name: str, type_: str, initial_value: float):
        """
        Initialize the investment vehicle.

        :param name: Name of the investment vehicle
        :param type_: Type of the investment vehicle (e.g., 'Mutual Fund', 'ETF')
        :param initial_value: Initial value in dollars
        """
        self.name = name
        self.type = type_
        self.initial_value = initial_value
        self.performance_data = pd.DataFrame(columns=['Year', 'Value'])

    def simulate_performance(self, years: int, min_growth: float, max_growth: float):
        """
        Simulate the annual performance of the investment vehicle.

        :param years: Number of years to simulate
        :param min_growth: Minimum annual growth rate (as a percentage)
        :param max_growth: Maximum annual growth rate (as a percentage)
        """
        value = self.initial_value
        for year in range(1, years + 1):
            # Simulate random growth rate within the specified range
            growth_rate = random.uniform(min_growth, max_growth) / 100
            value += value * growth_rate  # Calculate annual performance
            self.performance_data = self.performance_data.append(
                {'Year': year, 'Value': round(value, 2)}, ignore_index=True
            )

    def display_performance(self):
        """
        Display the performance data as a human-readable table.
        """
        print(f"{self.name} ({self.type}) | Initial Value: ${self.initial_value}")
        print(self.performance_data.to_string(index=False))


class MutualFund(InvestmentVehicle):
    """
    Class representing a Mutual Fund, inheriting from InvestmentVehicle.
    """
    def __init__(self, name: str, initial_value: float):
        super().__init__(name, 'Mutual Fund', initial_value)


class ETF(InvestmentVehicle):
    """
    Class representing an ETF, inheriting from InvestmentVehicle.
    """
    def __init__(self, name: str, initial_value: float):
        super().__init__(name, 'ETF', initial_value)


def main():
    """
    Main function to demonstrate the functionality of the InvestmentVehicle classes.
    """
    try:
        # Create instances of MutualFund and ETF
        mutual_fund = MutualFund("Growth Fund A", 10000)  # $10,000 initial value
        etf = ETF("Tech ETF B", 15000)                   # $15,000 initial value

        # Simulate performance for 10 years with growth rates between 5% and 15%
        mutual_fund.simulate_performance(years=10, min_growth=5, max_growth=15)
        etf.simulate_performance(years=10, min_growth=7, max_growth=12)

        # Display the performance results
        mutual_fund.display_performance()
        print("\n")
        etf.display_performance()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
