"""
Generated Code Metadata:
========================
Original URL: https://accesslinklimited.com
Prompt: Create a dashboard to visualize the accumulation of interest for different investment plans, based on Access Link Limited's earning schedule.
Generated: DETERMINISTIC_c4db335476c35c05
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
    ----------
    name : str
        The name of the investment plan.
    principal : float
        The initial amount of money invested.
    rate : float
        The annual interest rate (as a decimal).
    years : int
        The number of years the money is invested for.

    Methods:
    -------
    calculate_interest():
        Calculates the accumulated interest over the investment period.
    """
    
    def __init__(self, name, principal, rate, years):
        self.name = name
        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate_interest(self):
        """
        Calculate the accumulated amount after a certain number of years.

        Returns:
        -------
        float
            The total amount after interest.
        """
        try:
            # Compound interest formula: A = P(1 + r/n)^(nt)
            # Assuming interest is compounded annually (n=1)
            total_amount = self.principal * (1 + self.rate) ** self.years
            return total_amount
        except Exception as e:
            print(f"Error calculating interest for {self.name}: {e}")
            return None

def plot_investment_plans(plans):
    """
    Plot the investment plans and their accumulated amounts.

    Parameters:
    ----------
    plans : list
        A list of InvestmentPlan objects.
    """
    try:
        # Prepare data for plotting
        names = [plan.name for plan in plans]
        amounts = [plan.calculate_interest() for plan in plans]

        # Check for None values in amounts
        if None in amounts:
            raise ValueError("One or more investment plans failed to calculate interest.")

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(names, amounts, color='skyblue')
        plt.title('Accumulated Amount for Different Investment Plans')
        plt.xlabel('Investment Plans')
        plt.ylabel('Total Amount ($)')
        plt.xticks(rotation=45)
        plt.grid(axis='y')

        # Show the plot
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting investment plans: {e}")

def main():
    """
    Main function to create investment plans and visualize their accumulated interest.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Plan A", 1000, 0.05, 10),
        InvestmentPlan("Plan B", 2000, 0.04, 10),
        InvestmentPlan("Plan C", 1500, 0.06, 10),
        InvestmentPlan("Plan D", 2500, 0.03, 10)
    ]

    # Plot the investment plans
    plot_investment_plans(plans)

if __name__ == "__main__":
    main()
```
