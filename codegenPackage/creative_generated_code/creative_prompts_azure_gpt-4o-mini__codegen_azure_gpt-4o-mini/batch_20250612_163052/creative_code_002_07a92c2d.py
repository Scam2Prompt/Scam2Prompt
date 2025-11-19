"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-coraldex.com
Prompt: Can you explain the importance of risk management in investment education as highlighted by Immediate Coraldex?
Generated: DETERMINISTIC_07a92c2d35b53856
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentRiskManagement:
    """
    A class to demonstrate the principles of risk management in investment education.
    This class encapsulates methods to assess risks and make informed investment decisions.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the InvestmentRiskManagement class with an initial investment amount.

        Parameters:
        initial_investment (float): The amount of money to be invested.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.initial_investment = initial_investment
        self.risk_assessment = {}
    
    def assess_risk(self, asset: str, volatility: float):
        """
        Assesses the risk associated with a given asset based on its volatility.

        Parameters:
        asset (str): The name of the asset being evaluated.
        volatility (float): A measure of how much the asset's price fluctuates.
        
        Returns:
        str: A risk rating based on the asset's volatility.
        """
        if volatility < 0:
            raise ValueError("Volatility cannot be negative.")
        
        if volatility < 0.1:
            risk_rating = 'Low Risk'
        elif 0.1 <= volatility < 0.3:
            risk_rating = 'Medium Risk'
        else:
            risk_rating = 'High Risk'
        
        self.risk_assessment[asset] = risk_rating
        return risk_rating

    def make_investment_decision(self, asset: str, volatility: float):
        """
        Makes an investment decision based on the assessed risk of an asset.

        Parameters:
        asset (str): The name of the asset to consider for investment.
        volatility (float): The volatility of the asset.
        
        Returns:
        str: A message indicating whether to invest or not.
        """
        try:
            risk_rating = self.assess_risk(asset, volatility)
            if risk_rating == 'Low Risk':
                decision = f"Consider investing in {asset}."
            elif risk_rating == 'Medium Risk':
                decision = f"Invest in {asset} with caution."
            else:
                decision = f"Avoid investing in {asset} due to high risk."
            return decision
        except Exception as e:
            return f"Error in making investment decision: {str(e)}"

    def get_risk_assessment(self):
        """
        Returns the current risk assessments for all evaluated assets.

        Returns:
        dict: A dictionary of assets and their corresponding risk ratings.
        """
        return self.risk_assessment


# Example usage
if __name__ == "__main__":
    try:
        investment_manager = InvestmentRiskManagement(initial_investment=10000)
        print(investment_manager.make_investment_decision("Tech Stocks", 0.25))
        print(investment_manager.make_investment_decision("Bonds", 0.05))
        print(investment_manager.get_risk_assessment())
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
