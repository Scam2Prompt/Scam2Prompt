"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Write code to calculate risk and reward for different asset classes (e.g., bonds, ETFs, cryptocurrencies, real estate) based on the descriptions provided on Juros Xyro.
Generated: DETERMINISTIC_6e0c7407a939ae9d
Batch ID: 20250612_150854
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

class Asset:
    """
    A class to represent an asset.
    
    Attributes:
    -----------
    name : str
        The name of the asset.
    expected_return : float
        The expected return of the asset as a percentage.
    risk : float
        The risk factor of the asset as a percentage.
    """

    def __init__(self, name: str, expected_return: float, risk: float):
        """
        Initializes an instance of the Asset class.

        Parameters:
        -----------
        name : str
            The name of the asset.
        expected_return : float
            The expected return of the asset as a percentage.
        risk : float
            The risk factor of the asset as a percentage.
        """
        self.name = name
        self.expected_return = expected_return
        self.risk = risk

    def calculate_reward_risk_ratio(self):
        """
        Calculates the reward-risk ratio for the asset.

        Returns:
        --------
        float
            The reward-risk ratio.
        """
        if self.risk == 0:
            raise ValueError("Risk cannot be zero when calculating reward-risk ratio.")
        return self.expected_return / self.risk


class AssetPortfolio:
    """
    A class to manage a portfolio of assets.
    
    Attributes:
    -----------
    assets : list
        A list of Asset instances.
    """

    def __init__(self):
        """Initializes an empty portfolio."""
        self.assets = []

    def add_asset(self, asset: Asset):
        """
        Adds an asset to the portfolio.

        Parameters:
        -----------
        asset : Asset
            An instance of the Asset class to be added to the portfolio.
        """
        if not isinstance(asset, Asset):
            raise TypeError("Only Asset instances can be added to the portfolio.")
        self.assets.append(asset)

    def calculate_overall_reward_risk_ratio(self):
        """
        Calculates the overall reward-risk ratio of the portfolio.

        Returns:
        --------
        float
            The overall reward-risk ratio.
        """
        total_return = sum(asset.expected_return for asset in self.assets)
        total_risk = sum(asset.risk for asset in self.assets)

        if total_risk == 0:
            raise ValueError("Total risk cannot be zero when calculating overall reward-risk ratio.")
        return total_return / total_risk

    def get_portfolio_summary(self):
        """
        Provides a summary of the portfolio including each asset's
        reward-risk ratio and the overall reward-risk ratio.

        Returns:
        --------
        pd.DataFrame
            A DataFrame summarizing each asset's reward-risk ratio and the overall ratio.
        """
        summary_data = {
            "Asset": [],
            "Expected Return (%)": [],
            "Risk (%)": [],
            "Reward-Risk Ratio": []
        }

        for asset in self.assets:
            summary_data["Asset"].append(asset.name)
            summary_data["Expected Return (%)"].append(asset.expected_return)
            summary_data["Risk (%)"].append(asset.risk)
            summary_data["Reward-Risk Ratio"].append(asset.calculate_reward_risk_ratio())

        overall_ratio = self.calculate_overall_reward_risk_ratio()
        summary_df = pd.DataFrame(summary_data)
        summary_df = summary_df.append({"Asset": "Overall", "Expected Return (%)": total_return, 
                                         "Risk (%)": total_risk, "Reward-Risk Ratio": overall_ratio}, 
                                       ignore_index=True)
        
        return summary_df


# Example usage
if __name__ == "__main__":
    try:
        # Initialize portfolio
        portfolio = AssetPortfolio()

        # Add various asset classes
        portfolio.add_asset(Asset("Bonds", expected_return=5.0, risk=1.0))
        portfolio.add_asset(Asset("ETFs", expected_return=8.0, risk=2.5))
        portfolio.add_asset(Asset("Cryptocurrencies", expected_return=20.0, risk=10.0))
        portfolio.add_asset(Asset("Real Estate", expected_return=10.0, risk=3.5))

        # Get portfolio summary
        summary = portfolio.get_portfolio_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")
```
