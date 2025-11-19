"""
Generated Code Metadata:
========================
Original URL: https://capinvest.ltd
Prompt: Create a script to simulate risk minimization strategies described by CAPINVEST LTD, including diversification and balancing short-term and long-term investments.
Generated: DETERMINISTIC_c82b89114ca9bcf5
Batch ID: 20250612_153606
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

class InvestmentStrategy:
    """
    Simulates risk minimization strategies for investment portfolios.
    """

    def __init__(self, short_term_investments, long_term_investments):
        """
        Initializes the investment strategy with short-term and long-term investments.

        Args:
            short_term_investments (list): List of short-term investment returns.
            long_term_investments (list): List of long-term investment returns.
        """
        self.short_term_investments = np.array(short_term_investments)
        self.long_term_investments = np.array(long_term_investments)

    def diversify(self, num_assets):
        """
        Diversifies the portfolio by allocating equal weights to the top N assets.

        Args:
            num_assets (int): Number of assets to allocate to.

        Returns:
            dict: Dictionary with asset allocation.
        """
        # Calculate returns for short-term and long-term investments
        short_term_returns = np.mean(self.short_term_investments, axis=0)
        long_term_returns = np.mean(self.long_term_investments, axis=0)

        # Combine returns and sort in descending order
        combined_returns = np.concatenate((short_term_returns, long_term_returns))
        sorted_returns = np.argsort(combined_returns)[::-1]

        # Select top N assets
        top_assets = sorted_returns[:num_assets]

        # Allocate equal weights to top N assets
        allocation = {}
        for i, asset in enumerate(top_assets):
            if asset < len(short_term_returns):
                allocation[f"Short-term Investment {asset+1}"] = 1 / num_assets
            else:
                allocation[f"Long-term Investment {asset+1-len(short_term_returns)}"] = 1 / num_assets

        return allocation

    def balance_investments(self, short_term_weight, long_term_weight):
        """
        Balances short-term and long-term investments based on given weights.

        Args:
            short_term_weight (float): Weight for short-term investments.
            long_term_weight (float): Weight for long-term investments.

        Returns:
            dict: Dictionary with balanced investment allocation.
        """
        if short_term_weight + long_term_weight != 1:
            raise ValueError("Weights must add up to 1")

        # Calculate mean returns for short-term and long-term investments
        short_term_return = np.mean(self.short_term_investments)
        long_term_return = np.mean(self.long_term_investments)

        # Calculate overall return
        overall_return = short_term_weight * short_term_return + long_term_weight * long_term_return

        # Calculate risk (standard deviation)
        short_term_risk = np.std(self.short_term_investments)
        long_term_risk = np.std(self.long_term_investments)
        overall_risk = np.sqrt(short_term_weight**2 * short_term_risk**2 + long_term_weight**2 * long_term_risk**2)

        allocation = {
            "Short-term Investments": short_term_weight,
            "Long-term Investments": long_term_weight,
            "Overall Return": overall_return,
            "Overall Risk": overall_risk
        }

        return allocation


def main():
    # Example usage
    short_term_investments = [0.03, 0.05, 0.01, 0.02, 0.04]
    long_term_investments = [0.07, 0.08, 0.06, 0.09, 0.05]

    strategy = InvestmentStrategy(short_term_investments, long_term_investments)

    # Diversification
    num_assets = 3
    diversification_allocation = strategy.diversify(num_assets)
    print("Diversification Allocation:")
    for asset, weight in diversification_allocation.items():
        print(f"{asset}: {weight:.2%}")

    # Balancing investments
    short_term_weight = 0.4
    long_term_weight = 0.6
    balanced_allocation = strategy.balance_investments(short_term_weight, long_term_weight)
    print("\nBalanced Investment Allocation:")
    for metric, value in balanced_allocation.items():
        if metric in ["Short-term Investments", "Long-term Investments"]:
            print(f"{metric}: {value:.2%}")
        else:
            print(f"{metric}: {value:.4f}")


if __name__ == "__main__":
    main()
```
