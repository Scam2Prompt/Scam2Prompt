"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-x.world
Prompt: Create a Python script to simulate investment performance under different market scenarios, incorporating stress tests as described by AIvest Securities Limited.
Generated: DETERMINISTIC_a5c07e98640a8b18
Batch ID: 20250612_142628
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


class InvestmentSimulator:
    """
    A class to simulate investment performance under different market scenarios.
    Includes stress tests for adverse market conditions.
    """

    def __init__(self, initial_investment, years, annual_return, volatility):
        """
        Initialize the simulator with investment parameters.

        :param initial_investment: Initial amount invested (float).
        :param years: Investment duration in years (int).
        :param annual_return: Expected annual return as a decimal (e.g., 0.07 for 7%).
        :param volatility: Annual volatility as a decimal (e.g., 0.15 for 15%).
        """
        self.initial_investment = initial_investment
        self.years = years
        self.annual_return = annual_return
        self.volatility = volatility

    def simulate_performance(self, num_simulations=1000):
        """
        Simulate investment performance using a Monte Carlo approach.

        :param num_simulations: Number of simulations to run (int).
        :return: A 2D numpy array with simulated portfolio values, one row per simulation.
        """
        # Time steps (daily returns assumed for 252 trading days per year)
        time_steps = 252 * self.years
        daily_return = self.annual_return / 252
        daily_volatility = self.volatility / np.sqrt(252)

        # Generate random daily returns for simulations
        random_returns = np.random.normal(
            loc=daily_return, scale=daily_volatility, size=(num_simulations, time_steps)
        )

        # Cumulative return calculation
        cumulative_returns = np.cumprod(1 + random_returns, axis=1)
        return cumulative_returns * self.initial_investment

    def stress_test(self, drawdown_percentage=0.3):
        """
        Apply a stress test to simulate adverse market conditions.

        :param drawdown_percentage: Maximum drawdown as a decimal (e.g., 0.3 for 30% drawdown).
        :return: The portfolio value after applying the stress test.
        """
        stressed_value = self.initial_investment * (1 - drawdown_percentage)
        return stressed_value


def plot_simulation_results(simulated_values, years, stress_test_value=None):
    """
    Plot simulation results and optional stress test results.

    :param simulated_values: 2D numpy array of simulated portfolio values.
    :param years: Investment duration in years (int).
    :param stress_test_value: Optional stressed portfolio value to display (float).
    """
    plt.figure(figsize=(12, 6))

    # Plot all simulations
    for simulation in simulated_values:
        plt.plot(np.linspace(0, years, simulated_values.shape[1]), simulation, color="lightgray", alpha=0.1)

    # Plot median simulation
    median_values = np.median(simulated_values, axis=0)
    plt.plot(np.linspace(0, years, simulated_values.shape[1]), median_values, color="blue", label="Median Performance")

    # Plot stress test (if provided)
    if stress_test_value:
        plt.axhline(y=stress_test_value, color="red", linestyle="--", label="Stress Test Value")

    plt.title("Investment Performance Simulation")
    plt.xlabel("Years")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # User inputs
    initial_investment = 100000  # Initial investment in $
    years = 10  # Investment duration in years
    annual_return = 0.07  # Expected annual return (e.g., 7%)
    volatility = 0.15  # Annual volatility (e.g., 15%)
    num_simulations = 1000  # Number of Monte Carlo simulations
    drawdown_percentage = 0.3  # Stress test maximum drawdown (e.g., 30%)

    try:
        # Initialize simulator
        simulator = InvestmentSimulator(initial_investment, years, annual_return, volatility)

        # Run simulations
        simulated_values = simulator.simulate_performance(num_simulations)

        # Perform stress test
        stress_test_value = simulator.stress_test(drawdown_percentage)

        # Plot results
        plot_simulation_results(simulated_values, years, stress_test_value)

    except Exception as e:
        print(f"An error occurred: {e}")
```
