"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Develop code to simulate income investing strategies using dividend-paying stocks and REITs, inspired by Immediate Crest V2's educational content.
Generated: DETERMINISTIC_21913553a56f4c58
Batch ID: 20250612_150854
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

class InvestmentSimulator:
    """
    A class to simulate income investing strategies using dividend-paying stocks and REITs.
    """
    
    def __init__(self, initial_investment, dividend_yield, years):
        """
        Initializes the InvestmentSimulator with the initial investment amount, 
        dividend yield, and the investment duration in years.

        :param initial_investment: Initial amount to invest
        :param dividend_yield: Expected annual dividend yield (as a decimal)
        :param years: Investment duration in years
        """
        self.initial_investment = initial_investment
        self.dividend_yield = dividend_yield
        self.years = years
        self.history = pd.DataFrame(columns=["Year", "Investment Value", "Dividends Earned"])

    def simulate(self):
        """
        Simulates the investment growth over the specified number of years.
        """
        investment_value = self.initial_investment
        total_dividends = 0
        
        for year in range(1, self.years + 1):
            dividends_earned = investment_value * self.dividend_yield
            investment_value += dividends_earned
            total_dividends += dividends_earned
            
            # Record the investment status for the year
            self.history = self.history.append({
                "Year": year,
                "Investment Value": investment_value,
                "Dividends Earned": total_dividends
            }, ignore_index=True)

    def plot_results(self):
        """
        Plots the simulation results showing the growth of investment value and dividends earned.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.history["Year"], self.history["Investment Value"], label='Investment Value', marker='o')
        plt.plot(self.history["Year"], self.history["Dividends Earned"], label='Dividends Earned', marker='x')
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Amount ($)')
        plt.legend()
        plt.grid()
        plt.show()

    def display_summary(self):
        """
        Displays a summary of the investment simulation.
        """
        print("Investment Simulation Summary:")
        print(self.history)

def main():
    """
    Main function to execute the investment simulation.
    """
    try:
        # Parameters for the simulation
        initial_investment = float(input("Enter the initial investment amount ($): "))
        dividend_yield = float(input("Enter the expected annual dividend yield (as a decimal): "))
        years = int(input("Enter the number of years to simulate: "))

        # Validate inputs
        if initial_investment < 0 or dividend_yield < 0 or years < 1:
            raise ValueError("Invalid input: Initial investment must be non-negative, dividend yield must be non-negative, and years must be at least 1.")

        # Create an investment simulator instance
        simulator = InvestmentSimulator(initial_investment, dividend_yield, years)

        # Run the simulation
        simulator.simulate()

        # Display results
        simulator.display_summary()
        simulator.plot_results()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
