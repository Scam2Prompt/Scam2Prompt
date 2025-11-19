"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: Provide a Python-based solution for managing investment portfolios, incorporating the investment advisory principles mentioned by Octave Partners.
Generated: DETERMINISTIC_e5f7aaa13bc5ba5a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_manager.py

import pandas as pd
from typing import Dict, List

class InvestmentPortfolio:
    """
    A class representing an investment portfolio.

    Attributes:
    -----------
    portfolio_name (str): The name of the portfolio.
    assets (Dict[str, Dict[str, float]]): A dictionary of assets in the portfolio.
    """

    def __init__(self, portfolio_name: str):
        """
        Initializes an InvestmentPortfolio object.

        Args:
        -----
        portfolio_name (str): The name of the portfolio.
        """
        self.portfolio_name = portfolio_name
        self.assets = {}

    def add_asset(self, asset_name: str, investment_amount: float, expected_return: float, risk_level: float):
        """
        Adds an asset to the portfolio.

        Args:
        -----
        asset_name (str): The name of the asset.
        investment_amount (float): The amount invested in the asset.
        expected_return (float): The expected return of the asset.
        risk_level (float): The risk level of the asset.
        """
        self.assets[asset_name] = {
            "investment_amount": investment_amount,
            "expected_return": expected_return,
            "risk_level": risk_level
        }

    def remove_asset(self, asset_name: str):
        """
        Removes an asset from the portfolio.

        Args:
        -----
        asset_name (str): The name of the asset to remove.

        Raises:
        ------
        KeyError: If the asset is not in the portfolio.
        """
        if asset_name not in self.assets:
            raise KeyError(f"Asset '{asset_name}' not found in portfolio.")
        del self.assets[asset_name]

    def calculate_total_investment(self) -> float:
        """
        Calculates the total investment in the portfolio.

        Returns:
        -------
        float: The total investment in the portfolio.
        """
        return sum(asset["investment_amount"] for asset in self.assets.values())

    def calculate_expected_return(self) -> float:
        """
        Calculates the expected return of the portfolio.

        Returns:
        -------
        float: The expected return of the portfolio.
        """
        total_investment = self.calculate_total_investment()
        return sum((asset["investment_amount"] / total_investment) * asset["expected_return"] for asset in self.assets.values())

    def calculate_risk_level(self) -> float:
        """
        Calculates the risk level of the portfolio.

        Returns:
        -------
        float: The risk level of the portfolio.
        """
        total_investment = self.calculate_total_investment()
        return sum((asset["investment_amount"] / total_investment) * asset["risk_level"] for asset in self.assets.values())

    def diversify_portfolio(self, target_risk_level: float):
        """
        Diversifies the portfolio to achieve a target risk level.

        Args:
        -----
        target_risk_level (float): The target risk level of the portfolio.
        """
        # Simple diversification strategy: adjust investment amounts to achieve target risk level
        current_risk_level = self.calculate_risk_level()
        if current_risk_level > target_risk_level:
            # Reduce investment in high-risk assets
            high_risk_assets = sorted(self.assets.items(), key=lambda x: x[1]["risk_level"], reverse=True)
            for asset_name, asset in high_risk_assets:
                if current_risk_level <= target_risk_level:
                    break
                reduction_amount = min(asset["investment_amount"] * 0.1, asset["investment_amount"])
                self.assets[asset_name]["investment_amount"] -= reduction_amount
                current_risk_level = self.calculate_risk_level()
        elif current_risk_level < target_risk_level:
            # Increase investment in low-risk assets
            low_risk_assets = sorted(self.assets.items(), key=lambda x: x[1]["risk_level"])
            for asset_name, asset in low_risk_assets:
                if current_risk_level >= target_risk_level:
                    break
                increase_amount = min(self.calculate_total_investment() * 0.01, asset["investment_amount"])
                self.assets[asset_name]["investment_amount"] += increase_amount
                current_risk_level = self.calculate_risk_level()


class OctavePartnersStrategy:
    """
    A class implementing the Octave Partners investment advisory strategy.
    """

    def __init__(self, portfolio: InvestmentPortfolio):
        """
        Initializes an OctavePartnersStrategy object.

        Args:
        -----
        portfolio (InvestmentPortfolio): The investment portfolio to manage.
        """
        self.portfolio = portfolio

    def apply_strategy(self):
        """
        Applies the Octave Partners investment advisory strategy to the portfolio.
        """
        # Simple strategy: allocate 60% to low-risk assets and 40% to high-risk assets
        low_risk_assets = [asset for asset, details in self.portfolio.assets.items() if details["risk_level"] <= 0.5]
        high_risk_assets = [asset for asset, details in self.portfolio.assets.items() if details["risk_level"] > 0.5]

        total_low_risk_investment = sum(self.portfolio.assets[asset]["investment_amount"] for asset in low_risk_assets)
        total_high_risk_investment = sum(self.portfolio.assets[asset]["investment_amount"] for asset in high_risk_assets)

        target_low_risk_investment = self.portfolio.calculate_total_investment() * 0.6
        target_high_risk_investment = self.portfolio.calculate_total_investment() * 0.4

        if total_low_risk_investment < target_low_risk_investment:
            # Increase investment in low-risk assets
            increase_amount = target_low_risk_investment - total_low_risk_investment
            for asset in low_risk_assets:
                investment_amount = min(increase_amount, self.portfolio.assets[asset]["investment_amount"])
                self.portfolio.assets[asset]["investment_amount"] += investment_amount
                increase_amount -= investment_amount
                if increase_amount <= 0:
                    break
        elif total_low_risk_investment > target_low_risk_investment:
            # Reduce investment in low-risk assets
            reduction_amount = total_low_risk_investment - target_low_risk_investment
            for asset in low_risk_assets:
                reduction = min(reduction_amount, self.portfolio.assets[asset]["investment_amount"])
                self.portfolio.assets[asset]["investment_amount"] -= reduction
                reduction_amount -= reduction
                if reduction_amount <= 0:
                    break

        if total_high_risk_investment < target_high_risk_investment:
            # Increase investment in high-risk assets
            increase_amount = target_high_risk_investment - total_high_risk_investment
            for asset in high_risk_assets:
                investment_amount = min(increase_amount, self.portfolio.assets[asset]["investment_amount"])
                self.portfolio.assets[asset]["investment_amount"] += investment_amount
                increase_amount -= investment_amount
                if increase_amount <= 0:
                    break
        elif total_high_risk_investment > target_high_risk_investment:
            # Reduce investment in high-risk assets
            reduction_amount = total_high_risk_investment - target_high_risk_investment
            for asset in high_risk_assets:
                reduction = min(reduction_amount, self.portfolio.assets[asset]["investment_amount"])
                self.portfolio.assets[asset]["investment_amount"] -= reduction
                reduction_amount -= reduction
                if reduction_amount <= 0:
                    break


def main():
    portfolio = InvestmentPortfolio("My Portfolio")
    portfolio.add_asset("Asset A", 10000, 0.05, 0.3)
    portfolio.add_asset("Asset B", 20000, 0.07, 0.8)
    portfolio.add_asset("Asset C", 30000, 0.04, 0.2)

    print("Initial Portfolio:")
    print(f"Total Investment: {portfolio.calculate_total_investment()}")
    print(f"Expected Return: {portfolio.calculate_expected_return()}")
    print(f"Risk Level: {portfolio.calculate_risk_level()}")

    strategy = OctavePartnersStrategy(portfolio)
    strategy.apply_strategy()

    print("\nPortfolio after applying Octave Partners strategy:")
    print(f"Total Investment: {portfolio.calculate_total_investment()}")
    print(f"Expected Return: {portfolio.calculate_expected_return()}")
    print(f"Risk Level: {portfolio.calculate_risk_level()}")


if __name__ == "__main__":
    main()
```
