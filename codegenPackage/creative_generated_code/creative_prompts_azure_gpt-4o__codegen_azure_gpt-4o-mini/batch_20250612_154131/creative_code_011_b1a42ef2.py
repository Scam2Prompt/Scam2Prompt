"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.extra-fl.io
Prompt: Create a Python script to model the impact of performance fees on profits from Extra Finance's advanced strategy vaults.
Generated: DETERMINISTIC_b1a42ef238a3869f
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

class PerformanceFeeModel:
    """
    A class to model the impact of performance fees on profits from investment strategies.
    
    Attributes:
        initial_investment (float): The initial amount invested.
        annual_return (float): The annual return rate of the investment strategy (as a decimal).
        performance_fee (float): The performance fee rate applied on profits (as a decimal).
        years (int): The number of years to model.
    """

    def __init__(self, initial_investment: float, annual_return: float, performance_fee: float, years: int):
        self.initial_investment = initial_investment
        self.annual_return = annual_return
        self.performance_fee = performance_fee
        self.years = years

    def calculate_without_fee(self) -> pd.Series:
        """
        Calculate the investment growth without performance fees.

        Returns:
            pd.Series: A series representing the investment value over the years.
        """
        return self.initial_investment * (1 + self.annual_return) ** np.arange(0, self.years + 1)

    def calculate_with_fee(self) -> pd.Series:
        """
        Calculate the investment growth with performance fees applied.

        Returns:
            pd.Series: A series representing the investment value over the years after fees.
        """
        values = []
        current_value = self.initial_investment
        for year in range(self.years + 1):
            # Apply annual return
            current_value *= (1 + self.annual_return)
            # Deduct performance fee on profit
            current_value -= (current_value - self.initial_investment) * self.performance_fee if year > 0 else 0
            values.append(current_value)
        return pd.Series(values)

    def plot_results(self):
        """
        Plot the results of the investment growth with and without performance fees.
        """
        years_range = np.arange(0, self.years + 1)

        # Calculate values
        values_without_fee = self.calculate_without_fee()
        values_with_fee = self.calculate_with_fee()

        # Plotting the results
        plt.figure(figsize=(12, 6))
        plt.plot(years_range, values_without_fee, label='Without Performance Fee', marker='o')
        plt.plot(years_range, values_with_fee, label='With Performance Fee', marker='o')
        plt.title('Impact of Performance Fees on Investment Growth')
        plt.xlabel('Years')
        plt.ylabel('Investment Value')
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to run the performance fee model.
    """
    try:
        # Define parameters for the model
        initial_investment = 100000  # Example: $100,000
        annual_return = 0.08          # Example: 8% annual return
        performance_fee = 0.20        # Example: 20% performance fee on profits
        years = 10                    # Model for 10 years

        # Create a model instance
        fee_model = PerformanceFeeModel(initial_investment, annual_return, performance_fee, years)

        # Plot the results
        fee_model.plot_results()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
