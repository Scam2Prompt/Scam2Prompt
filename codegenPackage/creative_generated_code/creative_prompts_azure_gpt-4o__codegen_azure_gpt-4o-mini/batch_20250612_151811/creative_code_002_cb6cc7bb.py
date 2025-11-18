"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agfinance-capitals.com
Prompt: Generate code to simulate portfolio growth over time using seed funding and innovation investments, aligning with the agfinance-capitals approach to tailored financial planning.
Generated: DETERMINISTIC_cb6cc7bb56fc53d2
Batch ID: 20250612_151811
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


class PortfolioSimulator:
    """
    A class to simulate portfolio growth over time with seed funding and innovation investments.
    
    Attributes:
        initial_investment (float): Initial seed funding amount.
        innovation_investment (float): Annual innovation investment amount.
        growth_rate (float): Annual growth rate of the investment (as a decimal).
        years (int): Number of years to simulate.
    """
    
    def __init__(self, initial_investment: float, innovation_investment: float, growth_rate: float, years: int):
        """
        Initializes the PortfolioSimulator with the provided parameters.
        
        Parameters:
            initial_investment (float): The initial amount of seed funding.
            innovation_investment (float): The annual investment made in innovation.
            growth_rate (float): The expected annual growth rate (in decimal).
            years (int): The number of years for the simulation.
        """
        self.initial_investment = initial_investment
        self.innovation_investment = innovation_investment
        self.growth_rate = growth_rate
        self.years = years

    def simulate_growth(self) -> np.ndarray:
        """
        Simulates the portfolio growth over the specified number of years.
        
        Returns:
            np.ndarray: An array containing the portfolio value at the end of each year.
        """
        if self.initial_investment < 0 or self.innovation_investment < 0 or self.growth_rate < 0 or self.years < 0:
            raise ValueError("Investment amounts and years must be non-negative.")

        portfolio_values = np.zeros(self.years + 1)
        portfolio_values[0] = self.initial_investment

        for year in range(1, self.years + 1):
            # Calculate the value at the end of the year
            portfolio_values[year] = (portfolio_values[year - 1] + self.innovation_investment) * (1 + self.growth_rate)

        return portfolio_values

    def plot_growth(self, portfolio_values: np.ndarray) -> None:
        """
        Plots the portfolio growth over the specified number of years.
        
        Parameters:
            portfolio_values (np.ndarray): An array containing the portfolio values to plot.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(range(self.years + 1), portfolio_values, marker='o')
        plt.title("Portfolio Growth Over Time")
        plt.xlabel("Years")
        plt.ylabel("Portfolio Value ($)")
        plt.grid()
        plt.xticks(range(self.years + 1))
        plt.show()


if __name__ == "__main__":
    # Example usage
    try:
        initial_investment = 50000  # Seed funding
        innovation_investment = 10000  # Annual investment in innovation
        growth_rate = 0.07  # 7% annual growth
        years = 10  # Simulate for 10 years
        
        # Create an instance of the PortfolioSimulator
        simulator = PortfolioSimulator(initial_investment, innovation_investment, growth_rate, years)
        
        # Simulate the growth
        portfolio_values = simulator.simulate_growth()
        
        # Plot the results
        simulator.plot_growth(portfolio_values)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
