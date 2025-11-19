"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Write code to simulate investment scenarios for Initia Capital, focusing on the transformation of industries through innovation and technology in the CEE region.
Generated: DETERMINISTIC_489695fcf2a5d8d3
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class InvestmentScenarioSimulator:
    """
    A class to simulate investment scenarios for Initia Capital focusing on the transformation of industries
    through innovation and technology in the Central and Eastern Europe (CEE) region.
    """

    def __init__(self, num_scenarios=1000, initial_investment=100000, growth_rate_range=(0.05, 0.20), volatility=0.1):
        """
        Initializes the simulator with the given parameters.

        :param num_scenarios: Number of investment scenarios to simulate
        :param initial_investment: Initial amount of investment
        :param growth_rate_range: Tuple representing the minimum and maximum growth rates
        :param volatility: Volatility of the investment growth
        """
        self.num_scenarios = num_scenarios
        self.initial_investment = initial_investment
        self.growth_rate_range = growth_rate_range
        self.volatility = volatility
        self.results = []

    def simulate_growth(self):
        """
        Simulates the growth of the investment over a 10-year period.
        """
        for _ in range(self.num_scenarios):
            growth_rate = random.uniform(*self.growth_rate_range)
            scenario = self._simulate_single_scenario(growth_rate)
            self.results.append(scenario)

    def _simulate_single_scenario(self, growth_rate):
        """
        Simulates a single investment scenario over 10 years.

        :param growth_rate: The growth rate for this scenario
        :return: A list of investment values over 10 years
        """
        investment_values = []
        current_value = self.initial_investment

        for year in range(1, 11):
            # Apply growth with volatility
            current_value *= (1 + growth_rate + random.uniform(-self.volatility, self.volatility))
            investment_values.append(current_value)

        return investment_values

    def analyze_results(self):
        """
        Analyzes the results of the simulations and returns statistics.
        
        :return: A DataFrame containing the mean, median, and standard deviation of the investment values
        """
        results_array = np.array(self.results)
        mean_values = np.mean(results_array, axis=0)
        median_values = np.median(results_array, axis=0)
        std_dev_values = np.std(results_array, axis=0)

        analysis_df = pd.DataFrame({
            'Year': range(1, 11),
            'Mean': mean_values,
            'Median': median_values,
            'Std Dev': std_dev_values
        })

        return analysis_df

    def plot_results(self):
        """
        Plots the results of the investment scenarios.
        """
        plt.figure(figsize=(12, 6))
        for scenario in self.results:
            plt.plot(range(1, 11), scenario, color='blue', alpha=0.1)
        
        analysis_df = self.analyze_results()
        plt.plot(analysis_df['Year'], analysis_df['Mean'], color='red', label='Mean', linewidth=2)
        plt.fill_between(analysis_df['Year'], 
                         analysis_df['Mean'] - analysis_df['Std Dev'], 
                         analysis_df['Mean'] + analysis_df['Std Dev'], 
                         color='red', alpha=0.2)

        plt.title('Investment Growth Scenarios for Initia Capital')
        plt.xlabel('Year')
        plt.ylabel('Investment Value')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    try:
        # Create an instance of the simulator
        simulator = InvestmentScenarioSimulator(num_scenarios=1000)
        
        # Simulate the investment growth
        simulator.simulate_growth()
        
        # Analyze the results
        analysis_df = simulator.analyze_results()
        print(analysis_df)
        
        # Plot the results
        simulator.plot_results()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
