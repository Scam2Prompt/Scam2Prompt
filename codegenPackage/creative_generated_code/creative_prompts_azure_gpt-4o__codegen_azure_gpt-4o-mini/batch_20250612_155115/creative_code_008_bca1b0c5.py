"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Generate Python code to simulate long-term investment growth using historical market data and compound interest calculations, based on principles from Investolazlo.
Generated: DETERMINISTIC_bca1b0c57323ae47
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class InvestmentGrowthSimulator:
    """
    A class to simulate long-term investment growth based on historical market data
    and compound interest calculations.
    """

    def __init__(self, initial_investment: float, annual_contribution: float, 
                 annual_rate_of_return: float, years: int):
        """
        Initialize the investment growth simulator.

        :param initial_investment: The initial amount of money invested.
        :param annual_contribution: The amount of money contributed annually.
        :param annual_rate_of_return: The expected annual rate of return (as a decimal).
        :param years: The number of years to simulate.
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.annual_rate_of_return = annual_rate_of_return
        self.years = years
        self.investment_history = []

    def simulate_growth(self) -> None:
        """
        Simulates the investment growth over the specified number of years.
        """
        total_investment = self.initial_investment
        for year in range(1, self.years + 1):
            total_investment *= (1 + self.annual_rate_of_return)  # Compound interest
            total_investment += self.annual_contribution  # Add annual contributions
            self.investment_history.append(total_investment)

    def plot_growth(self) -> None:
        """
        Plot the investment growth over the years.
        """
        years_range = np.arange(1, self.years + 1)
        plt.figure(figsize=(10, 5))
        plt.plot(years_range, self.investment_history, marker='o')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Total Investment Value ($)')
        plt.grid(True)
        plt.xticks(years_range)
        plt.show()

    def get_final_value(self) -> float:
        """
        Returns the final investment value after the specified number of years.

        :return: The total value of the investment at the end of the period.
        """
        return self.investment_history[-1] if self.investment_history else self.initial_investment

def main():
    """
    Main function to execute the investment growth simulation.
    """
    # User-defined parameters for simulation
    initial_investment = 10000  # Initial investment amount
    annual_contribution = 5000   # Annual contribution amount
    annual_rate_of_return = 0.07  # Expected annual return (7%)
    years = 30                    # Duration of investment in years

    # Create an instance of InvestmentGrowthSimulator
    simulator = InvestmentGrowthSimulator(initial_investment, annual_contribution, 
                                          annual_rate_of_return, years)
    
    # Simulate growth
    simulator.simulate_growth()

    # Print final investment value
    final_value = simulator.get_final_value()
    print(f'Final investment value after {years} years: ${final_value:.2f}')

    # Plot investment growth
    simulator.plot_growth()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
