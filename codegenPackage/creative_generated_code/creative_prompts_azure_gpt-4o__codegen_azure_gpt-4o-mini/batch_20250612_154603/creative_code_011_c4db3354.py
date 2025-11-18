"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Create a dashboard to visualize the accumulation of interest for different investment plans, based on Access Link Limited's earning schedule.
Generated: DETERMINISTIC_c4db335476c35c05
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class InvestmentPlan:
    """
    A class to represent an investment plan and calculate the accumulated interest over time.
    """

    def __init__(self, name, principal, interest_rate, compounding_frequency):
        """
        Initialize the investment plan with a name, principal amount, interest rate, and 
        compounding frequency.

        :param name: str - Name of the investment plan
        :param principal: float - Initial amount invested
        :param interest_rate: float - Annual interest rate (as a decimal)
        :param compounding_frequency: int - Number of times interest is compounded per year
        """
        self.name = name
        self.principal = principal
        self.interest_rate = interest_rate
        self.compounding_frequency = compounding_frequency

    def calculate_accumulation(self, years):
        """
        Calculate the accumulated investment value after a certain number of years.

        :param years: int - Number of years to accumulate interest
        :return: float - Accumulated value after the specified years
        """
        # Calculate the accumulated value using the compound interest formula
        accumulated_value = self.principal * (1 + self.interest_rate / self.compounding_frequency) ** (self.compounding_frequency * years)
        return accumulated_value


def plot_investment_growth(plans, years):
    """
    Plot the growth of multiple investment plans over a specified number of years.

    :param plans: list - List of InvestmentPlan instances
    :param years: int - Number of years to visualize
    """
    # Create an array of years for the x-axis
    time = np.arange(0, years + 1)

    plt.figure(figsize=(10, 6))

    # Plot each investment plan
    for plan in plans:
        accumulated_values = [plan.calculate_accumulation(year) for year in time]
        plt.plot(time, accumulated_values, label=plan.name)

    # Adding labels and title
    plt.title('Investment Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Accumulated Value ($)')
    plt.legend()
    plt.grid(True)
    plt.yscale('linear')
    
    # Show plot
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to create investment plans and visualize their growth.
    """
    try:
        # Define investment plans
        plans = [
            InvestmentPlan(name='Plan A', principal=5000, interest_rate=0.05, compounding_frequency=4),  # Quarterly
            InvestmentPlan(name='Plan B', principal=10000, interest_rate=0.04, compounding_frequency=12),  # Monthly
            InvestmentPlan(name='Plan C', principal=15000, interest_rate=0.03, compounding_frequency=1)   # Annually
        ]

        # Define the duration for visualization
        years = 10

        # Plot the investment growth
        plot_investment_growth(plans, years)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
