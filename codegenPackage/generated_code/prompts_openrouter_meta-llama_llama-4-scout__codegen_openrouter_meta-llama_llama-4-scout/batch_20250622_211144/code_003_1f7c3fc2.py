"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Develop a risk management system that conducts stress tests on investment portfolios, simulating investment performance under different market scenarios, inspired by AIvest Securities Limited's risk management approach.
Generated: DETERMINISTIC_1f7c3fc28cc14d75
Batch ID: 20250622_211144
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
from typing import Dict, List

class InvestmentPortfolio:
    """Represents an investment portfolio with assets and their respective weights."""

    def __init__(self, assets: List[str], weights: List[float]):
        """
        Initializes an InvestmentPortfolio instance.

        Args:
        - assets (List[str]): List of asset names.
        - weights (List[float]): List of asset weights corresponding to assets.

        Raises:
        - ValueError: If the lengths of assets and weights do not match or if weights do not sum to 1.
        """
        if len(assets) != len(weights):
            raise ValueError("Assets and weights must have the same length.")
        if not np.isclose(sum(weights), 1):
            raise ValueError("Weights must sum to 1.")

        self.assets = assets
        self.weights = weights

    def get_asset_returns(self, returns: Dict[str, float]) -> float:
        """
        Calculates the portfolio return given asset returns.

        Args:
        - returns (Dict[str, float]): Dictionary of asset returns.

        Returns:
        - float: Portfolio return.

        Raises:
        - ValueError: If asset returns do not contain all portfolio assets.
        """
        if set(self.assets) != set(returns.keys()):
            raise ValueError("Asset returns must contain all portfolio assets.")

        portfolio_return = sum(self.weights[i] * returns[self.assets[i]] for i in range(len(self.assets)))
        return portfolio_return


class StressTest:
    """Conducts stress tests on investment portfolios under different market scenarios."""

    def __init__(self, portfolio: InvestmentPortfolio):
        """
        Initializes a StressTest instance.

        Args:
        - portfolio (InvestmentPortfolio): Investment portfolio to stress test.
        """
        self.portfolio = portfolio

    def simulate_market_scenario(self, scenario: Dict[str, float], num_simulations: int = 10000) -> List[float]:
        """
        Simulates investment performance under a market scenario.

        Args:
        - scenario (Dict[str, float]): Dictionary representing a market scenario with asset returns.
        - num_simulations (int): Number of simulations to run.

        Returns:
        - List[float]: List of simulated portfolio returns.

        Raises:
        - ValueError: If the scenario does not contain all portfolio assets.
        """
        if set(self.portfolio.assets) != set(scenario.keys()):
            raise ValueError("Scenario must contain all portfolio assets.")

        simulated_returns = []
        for _ in range(num_simulations):
            # Introduce some randomness to simulate real-world variability
            simulated_scenario = {asset: scenario[asset] * (1 + np.random.normal(0, 0.01)) for asset in scenario}
            portfolio_return = self.portfolio.get_asset_returns(simulated_scenario)
            simulated_returns.append(portfolio_return)

        return simulated_returns

    def calculate_value_at_risk(self, simulated_returns: List[float], confidence_level: float = 0.95) -> float:
        """
        Calculates the Value-at-Risk (VaR) of the portfolio.

        Args:
        - simulated_returns (List[float]): List of simulated portfolio returns.
        - confidence_level (float): Confidence level for VaR calculation.

        Returns:
        - float: VaR of the portfolio.

        Raises:
        - ValueError: If confidence level is not between 0 and 1.
        """
        if not 0 <= confidence_level <= 1:
            raise ValueError("Confidence level must be between 0 and 1.")

        var_percentile = norm.ppf(confidence_level)
        var = np.percentile(simulated_returns, (1 - confidence_level) * 100)
        return var


def main():
    # Example usage
    assets = ['Asset A', 'Asset B', 'Asset C']
    weights = [0.4, 0.3, 0.3]
    portfolio = InvestmentPortfolio(assets, weights)

    stress_test = StressTest(portfolio)

    # Define market scenarios
    scenario1 = {'Asset A': 0.03, 'Asset B': 0.05, 'Asset C': 0.01}
    scenario2 = {'Asset A': -0.02, 'Asset B': 0.01, 'Asset C': -0.03}

    # Simulate market scenarios
    simulated_returns1 = stress_test.simulate_market_scenario(scenario1)
    simulated_returns2 = stress_test.simulate_market_scenario(scenario2)

    # Calculate Value-at-Risk (VaR)
    var1 = stress_test.calculate_value_at_risk(simulated_returns1)
    var2 = stress_test.calculate_value_at_risk(simulated_returns2)

    print(f"VaR for Scenario 1: {var1}")
    print(f"VaR for Scenario 2: {var2}")


if __name__ == "__main__":
    main()
```
