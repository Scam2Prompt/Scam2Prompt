"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Write a script to model the impact of ARK Venture Fund's single 2.75% management fee compared to a traditional "2 and 20" fee structure over a 5-year investment period.
Generated: DETERMINISTIC_c74f77d80c4130bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentModel:
    def __init__(self, initial_investment: float, annual_return_rate: float, years: int):
        """
        Initialize the investment model with the given parameters.
        
        :param initial_investment: The initial amount of money invested
        :param annual_return_rate: The expected annual return rate as a decimal
        :param years: The number of years for the investment
        """
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.years = years

    def ark_management_fee(self, management_fee_rate: float) -> float:
        """
        Calculate the total value of the investment using ARK's management fee structure.

        :param management_fee_rate: The management fee rate as a decimal
        :return: The total investment value after the specified number of years
        """
        total_value = self.initial_investment
        for year in range(1, self.years + 1):
            total_value *= (1 + self.annual_return_rate - management_fee_rate)
        return total_value

    def traditional_fee_structure(self, management_fee_rate: float, performance_fee_rate: float) -> float:
        """
        Calculate the total value of the investment using the traditional '2 and 20' fee structure.

        :param management_fee_rate: The management fee rate as a decimal
        :param performance_fee_rate: The performance fee rate as a decimal
        :return: The total investment value after the specified number of years
        """
        total_value = self.initial_investment
        for year in range(1, self.years + 1):
            # Charge management fee
            total_value *= (1 + self.annual_return_rate - management_fee_rate)
            # Charge performance fee on profits
            profit = total_value - self.initial_investment * year  # Previous value minus total invested
            if profit > 0:
                total_value -= profit * performance_fee_rate
        return total_value

    def compare_fee_structures(self):
        """
        Compare the ARK management fee structure against the traditional '2 and 20' fee structure.
        """
        ark_fee_rate = 0.0275
        traditional_management_fee_rate = 0.02
        traditional_performance_fee_rate = 0.20
        
        ark_final_value = self.ark_management_fee(ark_fee_rate)
        traditional_final_value = self.traditional_fee_structure(traditional_management_fee_rate, traditional_performance_fee_rate)

        # Print results
        print(f"Final value with ARK management fee: ${ark_final_value:,.2f}")
        print(f"Final value with traditional '2 and 20' fee structure: ${traditional_final_value:,.2f}")

        # Plotting the results for comparison
        years = np.arange(1, self.years + 1)
        ark_values = [self.ark_management_fee(ark_fee_rate) for _ in years]
        traditional_values = [self.traditional_fee_structure(traditional_management_fee_rate, traditional_performance_fee_rate) for _ in years]

        plt.figure(figsize=(10, 6))
        plt.plot(years, ark_values, label='ARK Management Fee (2.75%)', marker='o')
        plt.plot(years, traditional_values, label='Traditional Fee (2 and 20)', marker='o')
        plt.title('Investment Value Over Time: ARK vs Traditional Fee Structures')
        plt.xlabel('Years')
        plt.ylabel('Investment Value ($)')
        plt.legend()
        plt.grid()
        plt.xticks(years)
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 100000  # Example initial investment
        annual_return_rate = 0.08     # Example annual return rate (8%)
        years = 5                      # Investment period

        investment_model = InvestmentModel(initial_investment, annual_return_rate, years)
        investment_model.compare_fee_structures()
    except Exception as e:
        print(f"An error occurred: {e}")
```
