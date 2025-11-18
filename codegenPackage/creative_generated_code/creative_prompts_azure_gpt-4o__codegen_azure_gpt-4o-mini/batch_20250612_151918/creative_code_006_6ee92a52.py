"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-trades.world
Prompt: Write a Python script to simulate the impact of high leverage on investment returns, as highlighted in the trading platform features of global-trades.world.
Generated: DETERMINISTIC_6ee92a52bbc1bedf
Batch ID: 20250612_151918
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
    A class to simulate the impact of high leverage on investment returns.
    """

    def __init__(self, initial_investment, leverage_factors, market_returns, num_simulations=1000):
        """
        Initialize the investment simulator.
        
        :param initial_investment: The initial amount invested.
        :param leverage_factors: A list of leverage factors to simulate.
        :param market_returns: A list of expected market returns (percentage).
        :param num_simulations: Number of simulations to run for each leverage factor.
        """
        self.initial_investment = initial_investment
        self.leverage_factors = leverage_factors
        self.market_returns = market_returns
        self.num_simulations = num_simulations

    def simulate(self):
        """
        Simulate the investment returns based on leverage factors and market returns.
        
        :return: A dictionary with leverage factors as keys and the corresponding returns as values.
        """
        results = {}
        
        for leverage in self.leverage_factors:
            investment_growth = []
            for _ in range(self.num_simulations):
                # Simulate market return for the investment
                market_return = np.random.choice(self.market_returns)
                # Calculate return based on leverage
                total_investment = self.initial_investment * leverage
                final_amount = total_investment * (1 + market_return / 100)
                growth = final_amount - self.initial_investment
                investment_growth.append(growth)
                
            results[leverage] = investment_growth

        return results

    def plot_results(self, results):
        """
        Plot the simulation results.

        :param results: A dictionary with leverage factors as keys and the corresponding returns as values.
        """
        plt.figure(figsize=(10, 6))
        
        for leverage, growth in results.items():
            plt.hist(growth, bins=30, alpha=0.5, label=f'Leverage {leverage}')
        
        plt.title('Investment Returns Simulation with High Leverage')
        plt.xlabel('Return Amount')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    try:
        initial_investment = 10000  # Initial investment amount
        leverage_factors = [1, 2, 5, 10]  # Different leverage factors
        market_returns = [5, 10, -3, 15, -7]  # Example market returns in percentage
        
        # Create an instance of the InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, leverage_factors, market_returns)

        # Run the simulation
        results = simulator.simulate()

        # Plot the simulation results
        simulator.plot_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
