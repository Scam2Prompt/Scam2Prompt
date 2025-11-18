"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Create a Python script to model private equity investment returns based on risk aversion and timing, similar to the approach outlined by Grade World Investment Limited.
Generated: DETERMINISTIC_161a85dd35a0240e
Batch ID: 20250612_150448
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

class PrivateEquityInvestment:
    def __init__(self, initial_investment, risk_aversion, time_horizon):
        """
        Initialize the private equity investment model.

        :param initial_investment: The amount of initial capital to invest.
        :param risk_aversion: A float representing the investor's risk aversion (0 to 1).
        :param time_horizon: The investment time horizon in years.
        """
        self.initial_investment = initial_investment
        self.risk_aversion = risk_aversion
        self.time_horizon = time_horizon

    def simulate_returns(self, num_simulations=1000):
        """
        Simulate investment returns based on risk aversion and time horizon.

        :param num_simulations: The number of simulation runs to perform.
        :return: A DataFrame with the simulated returns.
        """
        try:
            # Generate random returns based on risk aversion
            mean_return = 0.08 - (self.risk_aversion * 0.06)  # Lower mean return for higher risk aversion
            volatility = 0.15 * (1 - self.risk_aversion)  # Lower volatility for higher risk aversion
            
            # Simulate returns using geometric Brownian motion
            returns = np.random.normal(loc=mean_return, scale=volatility, size=(self.time_horizon, num_simulations))
            cumulative_returns = np.exp(np.cumsum(returns, axis=0))  # Calculate cumulative returns
            
            # Calculate final investment values
            final_values = self.initial_investment * cumulative_returns[-1, :]
            return pd.DataFrame(final_values, columns=[f'Simulation {i + 1}' for i in range(num_simulations)])
        
        except Exception as e:
            print(f"Error during simulation: {e}")
            return None

    def plot_results(self, simulation_results):
        """
        Plot the results of the simulations.

        :param simulation_results: A DataFrame with the simulated returns.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.hist(simulation_results.iloc[-1], bins=30, color='blue', alpha=0.7)
            plt.title('Distribution of Final Investment Values')
            plt.xlabel('Final Value')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.axvline(simulation_results.iloc[-1].mean(), color='red', linestyle='dashed', linewidth=2, label='Mean Final Value')
            plt.legend()
            plt.show()

        except Exception as e:
            print(f"Error during plotting: {e}")

def main():
    # User-defined parameters for the investment model
    initial_investment = 100000  # Initial investment amount
    risk_aversion = 0.5           # Investor's risk aversion level
    time_horizon = 10             # Investment duration in years

    # Create an instance of the PrivateEquityInvestment class
    investment_model = PrivateEquityInvestment(initial_investment, risk_aversion, time_horizon)

    # Simulate returns
    simulation_results = investment_model.simulate_returns(num_simulations=1000)

    if simulation_results is not None:
        # Plot the results
        investment_model.plot_results(simulation_results)

if __name__ == "__main__":
    main()
```
