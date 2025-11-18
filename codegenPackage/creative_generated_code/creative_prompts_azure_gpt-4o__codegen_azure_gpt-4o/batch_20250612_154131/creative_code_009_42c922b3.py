"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Write code to simulate the impact of leverage on the ARK Venture Fund's portfolio volatility, considering its exposure to disruptive innovation sectors.
Generated: DETERMINISTIC_42c922b3b216273c
Batch ID: 20250612_154131
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

class PortfolioSimulator:
    """
    Simulates the impact of leverage on portfolio volatility.
    Specifically designed for the ARK Venture Fund's exposure to disruptive innovation sectors.
    """

    def __init__(self, initial_portfolio_volatility, leverage_ratios, num_simulations=1000):
        """
        Initialize the simulator.

        :param initial_portfolio_volatility: Base volatility of the portfolio (float, annualized).
        :param leverage_ratios: List of leverage ratios to simulate (list of floats).
        :param num_simulations: Number of Monte Carlo simulations to run (int).
        """
        self.initial_volatility = initial_portfolio_volatility
        self.leverage_ratios = leverage_ratios
        self.num_simulations = num_simulations
        self.results = {}

    def simulate_volatility(self):
        """
        Simulates the impact of leverage on portfolio volatility using Monte Carlo simulations.
        """
        for leverage in self.leverage_ratios:
            # Adjust portfolio volatility based on the leverage ratio
            leveraged_volatility = self.initial_volatility * leverage
            
            # Perform Monte Carlo simulations to account for random fluctuations
            simulated_vols = np.random.normal(
                loc=leveraged_volatility, 
                scale=leveraged_volatility * 0.1,  # Assuming 10% variability
                size=self.num_simulations
            )
            
            # Store results for analysis
            self.results[leverage] = simulated_vols

    def get_summary(self):
        """
        Generates a summary of the simulation results.

        :return: A pandas DataFrame summarizing average volatility and standard deviation for each leverage ratio.
        """
        summary = []
        for leverage, simulations in self.results.items():
            summary.append({
                'Leverage Ratio': leverage,
                'Average Volatility': np.mean(simulations),
                'Volatility Std Dev': np.std(simulations)
            })
        return pd.DataFrame(summary)

def main():
    # Parameters
    initial_volatility = 0.25  # Example: 25% annualized volatility
    leverage_ratios = [1, 1.5, 2, 2.5]  # Leverage from 1x (no leverage) to 2.5x
    num_simulations = 5000  # Number of Monte Carlo simulations

    try:
        # Create simulator and run the simulations
        simulator = PortfolioSimulator(initial_volatility, leverage_ratios, num_simulations)
        simulator.simulate_volatility()

        # Output summary
        summary_df = simulator.get_summary()
        print("Impact of Leverage on Portfolio Volatility:")
        print(summary_df)
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
