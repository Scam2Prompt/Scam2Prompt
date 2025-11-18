"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Provide a Python-based solution for managing investment portfolios, incorporating the investment advisory principles mentioned by Octave Partners.
Generated: DETERMINISTIC_e5f7aaa13bc5ba5a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to manage and analyze investment portfolios
class InvestmentPortfolio:
    """
    A class for managing investment portfolios and incorporating
    advisory principles for decision-making.
    """
    
    def __init__(self):
        """
        Initialize an empty investment portfolio.
        """
        self.portfolio = {}

    def add_investment(self, asset_name, asset_type, amount, risk_level):
        """
        Add a new investment to the portfolio.

        Args:
            asset_name (str): Name of the asset.
            asset_type (str): Type of the asset (e.g., 'stocks', 'bonds', 'real estate').
            amount (float): Amount invested in the asset.
            risk_level (str): Risk level of the asset ('low', 'medium', 'high').
        """
        if asset_name in self.portfolio:
            raise ValueError(f"Asset '{asset_name}' already exists in the portfolio.")
        
        self.portfolio[asset_name] = {
            "asset_type": asset_type,
            "amount": amount,
            "risk_level": risk_level
        }

    def remove_investment(self, asset_name):
        """
        Remove an investment from the portfolio.

        Args:
            asset_name (str): Name of the asset to be removed.
        """
        if asset_name not in self.portfolio:
            raise ValueError(f"Asset '{asset_name}' does not exist in the portfolio.")

        del self.portfolio[asset_name]

    def update_investment(self, asset_name, amount=None, risk_level=None):
        """
        Update the details of an existing investment.

        Args:
            asset_name (str): Name of the asset to be updated.
            amount (float, optional): New amount to be invested. Default is None.
            risk_level (str, optional): New risk level. Default is None.
        """
        if asset_name not in self.portfolio:
            raise ValueError(f"Asset '{asset_name}' does not exist in the portfolio.")

        if amount is not None:
            self.portfolio[asset_name]["amount"] = amount
        
        if risk_level is not None:
            self.portfolio[asset_name]["risk_level"] = risk_level

    def analyze_risk(self):
        """
        Perform risk analysis on the portfolio.

        Returns:
            dict: A summary of total investments by risk level.
        """
        risk_summary = {"low": 0, "medium": 0, "high": 0}
        for asset in self.portfolio.values():
            risk_level = asset["risk_level"]
            if risk_level in risk_summary:
                risk_summary[risk_level] += asset["amount"]
        
        return risk_summary

    def get_portfolio_summary(self):
        """
        Get a summary of the portfolio.

        Returns:
            str: JSON representation of the portfolio.
        """
        return json.dumps(self.portfolio, indent=4)

    def advisory_principles(self):
        """
        Incorporate investment advisory principles (Octave Partners).

        This is a placeholder for implementing advanced advisory logic.
        """
        # Example principles:
        # - Diversification: Ensure portfolio is not over-concentrated in one asset type.
        # - Risk Management: Recommend rebalancing if risk levels are too high.
        # - Growth Potential: Identify assets with long-term growth potential.
        print("Advisory principles applied. (Implementation pending)")

# Example usage
if __name__ == "__main__":
    try:
        # Create portfolio instance
        portfolio = InvestmentPortfolio()
        
        # Add investments
        portfolio.add_investment("Tesla", "stocks", 10000, "high")
        portfolio.add_investment("Government Bonds", "bonds", 5000, "low")
        portfolio.add_investment("Real Estate Fund", "real estate", 20000, "medium")
        
        # Update an existing investment
        portfolio.update_investment("Tesla", amount=12000)

        # Remove an investment
        portfolio.remove_investment("Government Bonds")

        # Perform risk analysis
        print("Risk Analysis:")
        print(portfolio.analyze_risk())

        # Display portfolio summary
        print("\nPortfolio Summary:")
        print(portfolio.get_portfolio_summary())

        # Incorporate advisory principles
        print("\nAdvisory Principles:")
        portfolio.advisory_principles()

    except Exception as e:
        print(f"Error: {e}")
```
