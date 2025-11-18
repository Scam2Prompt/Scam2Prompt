"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Write a program to simulate AI-driven predictions for investment performance under different market conditions, incorporating stress testing as highlighted by AIvest Securities Limited.
Generated: DETERMINISTIC_e708969c47547062
Batch ID: 20250612_142638
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
    A class to simulate AI-driven investment performance predictions 
    under different market conditions, with built-in stress testing.
    """
    
    def __init__(self, initial_investment, market_conditions):
        """
        Initializes the InvestmentSimulator with the given parameters.
        
        :param initial_investment: Initial amount to invest (float).
        :param market_conditions: List of tuples representing market scenarios 
                                 [(market_change, probability), ...].
        """
        self.initial_investment = initial_investment
        self.market_conditions = market_conditions
        self.performance_history = []
    
    def simulate(self, num_simulations=1000):
        """
        Simulates investment performance under given market conditions.

        :param num_simulations: Number of simulations to run (int).
        :return: A DataFrame with simulation results.
        """
        np.random.seed(42)  # For reproducibility
        results = []
        
        for _ in range(num_simulations):
            performance = self.initial_investment
            for market_change, probability in self.market_conditions:
                if np.random.rand() < probability:
                    performance *= (1 + market_change)
            results.append(performance)
        
        self.performance_history = results
        return pd.DataFrame(results, columns=["Final Performance"])

    def stress_test(self, stress_conditions):
        """
        Performs stress testing on the investment simulator.

        :param stress_conditions: List of tuples representing stress scenarios 
                                 [(market_change, probability), ...].
        :return: A DataFrame with stress test results.
        """
        stress_results = []
        
        for market_change, probability in stress_conditions:
            performance = self.initial_investment
            if np.random.rand() < probability:
                performance *= (1 + market_change)
            stress_results.append(performance)
        
        return pd.DataFrame(stress_results, columns=["Stress Test Performance"])

    def plot_results(self):
        """
        Plots the histogram of simulation results.
        """
        if not self.performance_history:
            raise ValueError("No simulation results available to plot.")
        
        plt.figure(figsize=(10, 6))
        plt.hist(self.performance_history, bins=30, alpha=0.7, color='blue')
        plt.title('Investment Performance Simulation Results')
        plt.xlabel('Final Performance')
        plt.ylabel('Frequency')
        plt.grid()
        plt.axvline(np.mean(self.performance_history), color='red', linestyle='dashed', linewidth=1, label='Mean Performance')
        plt.legend()
        plt.show()


# Example usage:
if __name__ == "__main__":
    try:
        # Define market conditions as (market_change, probability)
        market_conditions = [(0.1, 0.5), (-0.05, 0.3), (0.2, 0.2)]  # 10% gain, 5% loss, 20% gain
        initial_investment = 10000  # Initial investment amount

        # Create an instance of InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, market_conditions)
        
        # Simulate investment performance
        simulation_results = simulator.simulate(num_simulations=1000)
        print(simulation_results.describe())

        # Perform stress testing
        stress_conditions = [(-0.3, 0.1), (-0.2, 0.2)]  # Severe loss scenarios
        stress_test_results = simulator.stress_test(stress_conditions)
        print(stress_test_results.describe())
        
        # Plot simulation results
        simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
