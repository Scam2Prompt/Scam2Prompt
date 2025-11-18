"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Write a program to simulate the financial benefits of avoiding electricity price hikes by adopting isolated photovoltaic systems, as described by Nexe Energetic.
Generated: DETERMINISTIC_352fd1ccd0fe66c3
Batch ID: 20250612_153224
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

class PhotovoltaicSystem:
    """
    A class to represent a photovoltaic system for simulating financial benefits of avoiding electricity price hikes.
    """

    def __init__(self, initial_investment, annual_savings, electricity_price_growth_rate, years):
        """
        Initialize the photovoltaic system parameters.

        Parameters:
        - initial_investment (float): Initial cost of the photovoltaic system.
        - annual_savings (float): Annual savings from using the system instead of grid electricity.
        - electricity_price_growth_rate (float): Projected annual growth rate of electricity prices (as a decimal).
        - years (int): Number of years to simulate.
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.electricity_price_growth_rate = electricity_price_growth_rate
        self.years = years

    def calculate_savings(self):
        """
        Calculate cumulative savings over the years considering electricity price hikes.

        Returns:
        - savings (list): Cumulative savings for each year.
        - total_cost (list): Total cost of electricity without photovoltaic system for each year.
        """
        savings = []
        total_cost = []
        
        for year in range(1, self.years + 1):
            # Calculate the cost of electricity without PV system for the current year
            cost_without_pv = self.annual_savings * ((1 + self.electricity_price_growth_rate) ** (year - 1))
            savings.append(cost_without_pv - self.initial_investment)
            total_cost.append(cost_without_pv)

        return savings, total_cost

    def plot_results(self, savings, total_cost):
        """
        Plot the savings and total cost over the years.

        Parameters:
        - savings (list): List of cumulative savings.
        - total_cost (list): List of total costs of electricity.
        """
        years = np.arange(1, self.years + 1)

        plt.figure(figsize=(10, 5))
        plt.plot(years, savings, label='Cumulative Savings', marker='o')
        plt.plot(years, total_cost, label='Cost Without PV System', marker='x')
        
        plt.title('Financial Benefits of Isolated Photovoltaic Systems')
        plt.xlabel('Years')
        plt.ylabel('Amount ($)')
        plt.axhline(0, color='grey', lw=1, ls='--')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the simulation.
    """
    try:
        # User defined parameters for the simulation
        initial_investment = 10000  # Initial cost of photovoltaic system
        annual_savings = 1500        # Annual savings from the system
        electricity_price_growth_rate = 0.05  # 5% annual growth rate of electricity prices
        years = 25                    # Simulation for 25 years

        # Create an instance of PhotovoltaicSystem
        pv_system = PhotovoltaicSystem(initial_investment, annual_savings, electricity_price_growth_rate, years)

        # Calculate savings and total cost
        savings, total_cost = pv_system.calculate_savings()

        # Plot the results
        pv_system.plot_results(savings, total_cost)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
