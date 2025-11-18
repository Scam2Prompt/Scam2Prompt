"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Write a program in Python that models the revenue growth of a startup, using PureKana's $5k to $40M sales trajectory as an example.
Generated: DETERMINISTIC_6d2f8d4cdba69053
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class StartupRevenueGrowth:
    def __init__(self, initial_revenue, final_revenue, years):
        """
        Initialize the StartupRevenueGrowth class.

        :param initial_revenue: Initial revenue at year 0 (in dollars).
        :param final_revenue: Target revenue at the end of the period (in dollars).
        :param years: Number of years to model the growth.
        """
        if initial_revenue <= 0 or final_revenue <= initial_revenue:
            raise ValueError("Initial revenue must be positive and less than final revenue.")
        if years <= 0:
            raise ValueError("Number of years must be positive.")

        self.initial_revenue = initial_revenue
        self.final_revenue = final_revenue
        self.years = years
        self.revenues = []

    def model_growth(self):
        """Model the revenue growth over the specified number of years."""
        # Calculate annual growth rate using compound growth formula
        growth_rate = (self.final_revenue / self.initial_revenue) ** (1 / self.years) - 1
        
        for year in range(self.years + 1):
            revenue = self.initial_revenue * (1 + growth_rate) ** year
            self.revenues.append(revenue)

    def plot_growth(self):
        """Plot the revenue growth over time."""
        if not self.revenues:
            raise RuntimeError("Revenue growth has not been modeled. Call model_growth() first.")

        plt.figure(figsize=(10, 6))
        plt.plot(range(self.years + 1), self.revenues, marker='o')
        plt.title('Revenue Growth of Startup')
        plt.xlabel('Years')
        plt.ylabel('Revenue (in dollars)')
        plt.xticks(range(self.years + 1))
        plt.grid()
        plt.yscale('log')  # Log scale for better visibility of growth
        plt.annotate(f'Start: ${self.initial_revenue}', xy=(0, self.initial_revenue), xytext=(1, self.initial_revenue * 2),
                     arrowprops=dict(facecolor='blue', shrink=0.05))
        plt.annotate(f'End: ${self.final_revenue}', xy=(self.years, self.final_revenue), xytext=(self.years - 1, self.final_revenue / 2),
                     arrowprops=dict(facecolor='red', shrink=0.05))
        plt.show()


if __name__ == "__main__":
    try:
        # Initialize the model with PureKana's example values
        initial_revenue = 5000  # Initial revenue in dollars
        final_revenue = 40000000  # Final revenue in dollars
        years = 5  # Number of years to model

        # Create an instance of the StartupRevenueGrowth class
        startup = StartupRevenueGrowth(initial_revenue, final_revenue, years)

        # Model the revenue growth
        startup.model_growth()

        # Plot the results
        startup.plot_growth()
    except Exception as e:
        print(f"An error occurred: {e}")
```
