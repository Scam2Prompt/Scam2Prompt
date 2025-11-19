"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Develop a function that simulates investment management strategies tailored for small-to-medium sized businesses, inspired by the offerings of Genesis Investment Credit Union.
Generated: DETERMINISTIC_e83ac41b4b49f916
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InvestmentStrategy:
    """
    A class to simulate investment management strategies tailored for small-to-medium sized businesses.
    Inspired by Genesis Investment Credit Union.
    """

    def __init__(self, initial_capital, risk_tolerance, investment_horizon):
        """
        Initialize the investment strategy.

        :param initial_capital: (float) The initial capital available for investment.
        :param risk_tolerance: (str) Risk tolerance level ('low', 'medium', 'high').
        :param investment_horizon: (int) Investment horizon in years.
        """
        if initial_capital <= 0:
            raise ValueError("Initial capital must be greater than zero.")
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")
        if investment_horizon <= 0:
            raise ValueError("Investment horizon must be greater than zero.")

        self.initial_capital = initial_capital
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.portfolio = []

    def simulate_investment(self):
        """
        Simulate the investment strategy over the given horizon.

        :return: (dict) Summary of the investment simulation.
        """
        try:
            annual_return = self._get_annual_return()
            total_capital = self.initial_capital

            for year in range(1, self.investment_horizon + 1):
                # Simulate annual growth
                growth = total_capital * annual_return
                total_capital += growth

                # Log portfolio performance
                self.portfolio.append({
                    'year': year,
                    'annual_return': annual_return,
                    'growth': growth,
                    'total_capital': total_capital
                })

            return {
                'initial_capital': self.initial_capital,
                'final_capital': total_capital,
                'portfolio': self.portfolio
            }
        except Exception as e:
            print(f"An error occurred during simulation: {e}")
            return None

    def _get_annual_return(self):
        """
        Determine the annual return based on risk tolerance.

        :return: (float) Annual return rate.
        """
        if self.risk_tolerance == 'low':
            return random.uniform(0.02, 0.05)  # Conservative returns
        elif self.risk_tolerance == 'medium':
            return random.uniform(0.05, 0.10)  # Balanced returns
        elif self.risk_tolerance == 'high':
            return random.uniform(0.10, 0.20)  # Aggressive returns

# Example usage:
if __name__ == "__main__":
    try:
        # Create an investment strategy instance
        strategy = InvestmentStrategy(initial_capital=100000, risk_tolerance='medium', investment_horizon=5)

        # Simulate the investment
        result = strategy.simulate_investment()

        # Print the results
        if result:
            print("Investment Simulation Results:")
            print(f"Initial Capital: ${result['initial_capital']:.2f}")
            print(f"Final Capital: ${result['final_capital']:.2f}")
            print("Yearly Portfolio Performance:")
            for year_data in result['portfolio']:
                print(f"Year {year_data['year']}: "
                      f"Annual Return: {year_data['annual_return']:.2%}, "
                      f"Growth: ${year_data['growth']:.2f}, "
                      f"Total Capital: ${year_data['total_capital']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
