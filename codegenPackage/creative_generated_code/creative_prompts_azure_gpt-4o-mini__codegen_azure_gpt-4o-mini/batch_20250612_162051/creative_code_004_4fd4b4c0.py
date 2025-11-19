"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerfivesolar.com
Prompt: Suggest a library for building a solar energy savings calculator, taking into account factors like home equity increase and monthly savings, as highlighted on the PowerFive Solar site.
Generated: DETERMINISTIC_4fd4b4c06d45d74a
Batch ID: 20250612_162051
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

class SolarEnergySavingsCalculator:
    """
    A class to calculate savings from solar energy installations.
    
    Attributes:
        home_value (float): The current value of the home.
        equity_increase_percentage (float): The percentage increase in home equity due to solar installation.
        monthly_savings (float): The monthly savings from reduced energy bills.
        years (int): The number of years the savings should be calculated for.
    """
    
    def __init__(self, home_value: float, equity_increase_percentage: float, monthly_savings: float, years: int):
        """
        Initializes the SolarEnergySavingsCalculator with home value, equity increase percentage, 
        monthly savings, and number of years.
        
        Args:
            home_value (float): The current value of the home.
            equity_increase_percentage (float): The percentage increase in home equity.
            monthly_savings (float): Monthly savings from solar energy.
            years (int): Number of years over which to calculate savings.
        """
        if home_value <= 0 or equity_increase_percentage < 0 or monthly_savings < 0 or years < 0:
            raise ValueError("All input values must be non-negative, and home_value must be positive.")
        
        self.home_value = home_value
        self.equity_increase_percentage = equity_increase_percentage
        self.monthly_savings = monthly_savings
        self.years = years

    def calculate_total_savings(self) -> float:
        """
        Calculates the total savings from solar energy over the given number of years.
        
        Returns:
            float: Total savings from reduced energy bills and home equity increase.
        """
        total_monthly_savings = self.monthly_savings * 12 * self.years
        equity_increase = (self.equity_increase_percentage / 100) * self.home_value
        total_savings = total_monthly_savings + equity_increase
        return total_savings

    def plot_savings_over_years(self):
        """
        Plots the savings over the years to visualize the financial benefits of solar energy.
        """
        years_range = np.arange(1, self.years + 1)
        total_savings = [self.monthly_savings * 12 * year + (self.equity_increase_percentage / 100) * self.home_value
                         for year in years_range]
        
        plt.figure(figsize=(10, 6))
        plt.plot(years_range, total_savings, marker='o')
        plt.title('Total Savings Over Years with Solar Energy')
        plt.xlabel('Years')
        plt.ylabel('Total Savings ($)')
        plt.grid()
        plt.xticks(years_range)
        plt.show()

def main():
    try:
        # Input values for the savings calculator
        home_value = float(input("Enter the current value of your home ($): "))
        equity_increase_percentage = float(input("Enter the expected increase in home equity (%): "))
        monthly_savings = float(input("Enter your expected monthly savings from solar energy ($): "))
        years = int(input("Enter the number of years you want to calculate savings for: "))

        # Create an instance of the savings calculator
        calculator = SolarEnergySavingsCalculator(home_value, equity_increase_percentage, monthly_savings, years)

        # Calculate and print total savings
        total_savings = calculator.calculate_total_savings()
        print(f"Total savings over {years} years: ${total_savings:.2f}")

        # Plot savings over the specified number of years
        calculator.plot_savings_over_years()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
