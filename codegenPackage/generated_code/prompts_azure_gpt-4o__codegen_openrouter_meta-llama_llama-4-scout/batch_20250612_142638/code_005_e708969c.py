"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Write a program to simulate AI-driven predictions for investment performance under different market conditions, incorporating stress testing as highlighted by AIvest Securities Limited.
Generated: DETERMINISTIC_e708969c47547062
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

class InvestmentSimulator:
    """
    Simulates AI-driven predictions for investment performance under different market conditions.

    Attributes:
        initial_investment (float): Initial investment amount.
        mean_return (float): Mean return of the investment.
        std_dev (float): Standard deviation of the investment returns.
        time_horizon (int): Time horizon for the simulation in years.
        num_simulations (int): Number of simulations to run.
    """

    def __init__(self, initial_investment, mean_return, std_dev, time_horizon, num_simulations):
        self.initial_investment = initial_investment
        self.mean_return = mean_return
        self.std_dev = std_dev
        self.time_horizon = time_horizon
        self.num_simulations = num_simulations

    def simulate_investment(self):
        """
        Simulates the investment performance using Monte Carlo simulations.

        Returns:
            pandas.DataFrame: A DataFrame containing the simulated investment performances.
        """
        # Initialize a DataFrame to store the simulated performances
        performances = pd.DataFrame(np.zeros((self.num_simulations, self.time_horizon + 1)),
                                    columns=list(range(self.time_horizon + 1)))

        # Set the initial investment
        performances[:, 0] = self.initial_investment

        # Run the simulations
        for i in range(self.num_simulations):
            for t in range(1, self.time_horizon + 1):
                # Calculate the return using a random normal variable
                return_val = np.random.normal(self.mean_return, self.std_dev)
                performances[i, t] = performances[i, t - 1] * (1 + return_val)

        return performances

    def stress_test(self, performances, stress_scenario):
        """
        Applies a stress test to the simulated investment performances.

        Parameters:
            performances (pandas.DataFrame): A DataFrame containing the simulated investment performances.
            stress_scenario (dict): A dictionary containing the stress test scenario parameters.

        Returns:
            pandas.DataFrame: A DataFrame containing the stressed investment performances.
        """
        # Apply the stress test scenario
        stressed_performances = performances.copy()
        for i in range(self.num_simulations):
            for t in range(1, self.time_horizon + 1):
                stressed_performances[i, t] *= (1 - stress_scenario['market_downturn'] / 100)

        return stressed_performances

    def plot_simulations(self, performances, stressed_performances=None):
        """
        Plots the simulated investment performances.

        Parameters:
            performances (pandas.DataFrame): A DataFrame containing the simulated investment performances.
            stressed_performances (pandas.DataFrame, optional): A DataFrame containing the stressed investment performances. Defaults to None.
        """
        # Plot the simulated performances
        plt.figure(figsize=(10, 6))
        for i in range(self.num_simulations):
            plt.plot(performances[i, :])

        # Plot the stressed performances if provided
        if stressed_performances is not None:
            plt.figure(figsize=(10, 6))
            for i in range(self.num_simulations):
                plt.plot(stressed_performances[i, :])

        plt.xlabel('Time')
        plt.ylabel('Investment Value')
        plt.title('Simulated Investment Performances')
        plt.show()

        # Calculate and plot the average performance
        avg_performance = np.mean(performances, axis=0)
        plt.figure(figsize=(10, 6))
        plt.plot(avg_performance)
        plt.xlabel('Time')
        plt.ylabel('Average Investment Value')
        plt.title('Average Simulated Investment Performance')
        plt.show()

def main():
    try:
        # Set the simulation parameters
        initial_investment = 100000
        mean_return = 0.05
        std_dev = 0.1
        time_horizon = 10
        num_simulations = 1000

        # Create an instance of the InvestmentSimulator class
        simulator = InvestmentSimulator(initial_investment, mean_return, std_dev, time_horizon, num_simulations)

        # Run the simulations
        performances = simulator.simulate_investment()

        # Define a stress test scenario
        stress_scenario = {'market_downturn': 20}

        # Apply the stress test
        stressed_performances = simulator.stress_test(performances, stress_scenario)

        # Plot the simulated performances
        simulator.plot_simulations(performances, stressed_performances)

        # Calculate and print the average performance
        avg_performance = np.mean(performances, axis=0)
        print("Average Simulated Investment Performance:")
        print(avg_performance)

        # Calculate and print the stressed average performance
        stressed_avg_performance = np.mean(stressed_performances, axis=0)
        print("Stressed Average Simulated Investment Performance:")
        print(stressed_avg_performance)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
