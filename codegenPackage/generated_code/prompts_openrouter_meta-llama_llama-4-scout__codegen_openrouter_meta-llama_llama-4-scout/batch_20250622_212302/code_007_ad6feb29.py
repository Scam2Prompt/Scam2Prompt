"""
Generated Code Metadata:
========================
Original URL: https://mixer-novostei.ru
Prompt: Recommend a set of metrics to evaluate the performance of Ribbon Finance's investment strategies, including metrics like APY and Sharpe ratio.
Generated: DETERMINISTIC_ad6feb299abd38f1
Batch ID: 20250622_212302
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
from typing import List

class InvestmentStrategyEvaluator:
    """
    Evaluates the performance of investment strategies.

    Attributes:
    - strategies (dict): A dictionary of investment strategies with their respective returns.
    """

    def __init__(self, strategies: dict):
        """
        Initializes the evaluator with a dictionary of investment strategies.

        Args:
        - strategies (dict): A dictionary where keys are strategy names and values are lists of returns.
        """
        self.strategies = strategies

    def calculate_apy(self, returns: List[float]) -> float:
        """
        Calculates the Annual Percentage Yield (APY) for a given list of returns.

        Args:
        - returns (List[float]): A list of returns.

        Returns:
        - float: The APY.
        """
        # Convert returns to a numpy array for easier calculations
        returns = np.array(returns)

        # Calculate the mean return
        mean_return = np.mean(returns)

        # Calculate the APY
        apy = (1 + mean_return) ** 365 - 1

        return apy

    def calculate_sharpe_ratio(self, returns: List[float], risk_free_rate: float) -> float:
        """
        Calculates the Sharpe ratio for a given list of returns.

        Args:
        - returns (List[float]): A list of returns.
        - risk_free_rate (float): The risk-free rate.

        Returns:
        - float: The Sharpe ratio.
        """
        # Convert returns to a numpy array for easier calculations
        returns = np.array(returns)

        # Calculate the mean return
        mean_return = np.mean(returns)

        # Calculate the standard deviation of returns
        std_dev = np.std(returns)

        # Calculate the Sharpe ratio
        sharpe_ratio = (mean_return - risk_free_rate) / std_dev

        return sharpe_ratio

    def evaluate_strategies(self, risk_free_rate: float) -> dict:
        """
        Evaluates the performance of the investment strategies.

        Args:
        - risk_free_rate (float): The risk-free rate.

        Returns:
        - dict: A dictionary with strategy names as keys and their respective metrics as values.
        """
        metrics = {}

        for strategy, returns in self.strategies.items():
            apy = self.calculate_apy(returns)
            sharpe_ratio = self.calculate_sharpe_ratio(returns, risk_free_rate)

            metrics[strategy] = {
                "APY": apy,
                "Sharpe Ratio": sharpe_ratio
            }

        return metrics


def main():
    # Example usage
    strategies = {
        "Strategy 1": [0.01, 0.02, -0.01, 0.03, -0.02],
        "Strategy 2": [0.02, 0.03, 0.01, 0.04, -0.01],
        "Strategy 3": [-0.01, 0.01, 0.02, 0.03, 0.04]
    }

    risk_free_rate = 0.05

    evaluator = InvestmentStrategyEvaluator(strategies)
    metrics = evaluator.evaluate_strategies(risk_free_rate)

    for strategy, metric in metrics.items():
        print(f"Strategy: {strategy}")
        print(f"APY: {metric['APY']:.2%}")
        print(f"Sharpe Ratio: {metric['Sharpe Ratio']:.2f}")
        print()


if __name__ == "__main__":
    main()
```
