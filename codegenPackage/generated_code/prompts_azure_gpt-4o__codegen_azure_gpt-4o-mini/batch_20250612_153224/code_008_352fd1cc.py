"""
Generated Code Metadata:
========================
Original URL: https://www.nexenergetic.com
Prompt: Write a program to simulate the financial benefits of avoiding electricity price hikes by adopting isolated photovoltaic systems, as described by Nexe Energetic.
Generated: DETERMINISTIC_352fd1ccd0fe66c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class PhotovoltaicSystem:
    """
    A class to represent a photovoltaic system and its financial benefits.
    """

    def __init__(self, initial_investment, annual_savings, lifespan_years, discount_rate):
        """
        Initializes the photovoltaic system with the given parameters.

        :param initial_investment: Initial cost of the photovoltaic system
        :param annual_savings: Estimated annual savings from electricity costs
        :param lifespan_years: Expected lifespan of the system in years
        :param discount_rate: Discount rate for calculating present value
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.lifespan_years = lifespan_years
        self.discount_rate = discount_rate

    def calculate_present_value(self):
        """
        Calculates the present value of the savings over the lifespan of the system.

        :return: Present value of the total savings
        """
        pv_savings = sum(self.annual_savings / ((1 + self.discount_rate) ** year) for year in range(1, self.lifespan_years + 1))
        return pv_savings

    def calculate_net_benefit(self):
        """
        Calculates the net benefit of adopting the photovoltaic system.

        :return: Net benefit (present value of savings - initial investment)
        """
        pv_savings = self.calculate_present_value()
        net_benefit = pv_savings - self.initial_investment
        return net_benefit

    def plot_financial_benefits(self):
        """
        Plots the financial benefits over the lifespan of the system.
        """
        years = np.arange(1, self.lifespan_years + 1)
        savings = [self.annual_savings / ((1 + self.discount_rate) ** year) for year in years]
        cumulative_savings = np.cumsum(savings)

        plt.figure(figsize=(10, 6))
        plt.plot(years, cumulative_savings, label='Cumulative Savings', color='green')
        plt.axhline(y=self.initial_investment, color='red', linestyle='--', label='Initial Investment')
        plt.title('Financial Benefits of Photovoltaic System')
        plt.xlabel('Years')
        plt.ylabel('Cumulative Savings ($)')
        plt.xticks(years)
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to simulate the financial benefits of adopting a photovoltaic system.
    """
    try:
        # Parameters for the photovoltaic system
        initial_investment = 15000  # Initial cost in dollars
        annual_savings = 2000        # Annual savings in dollars
        lifespan_years = 25          # Lifespan in years
        discount_rate = 0.05         # Discount rate (5%)

        # Create an instance of the PhotovoltaicSystem
        pv_system = PhotovoltaicSystem(initial_investment, annual_savings, lifespan_years, discount_rate)

        # Calculate and display the net benefit
        net_benefit = pv_system.calculate_net_benefit()
        print(f"Net Benefit of adopting the photovoltaic system: ${net_benefit:.2f}")

        # Plot the financial benefits
        pv_system.plot_financial_benefits()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
