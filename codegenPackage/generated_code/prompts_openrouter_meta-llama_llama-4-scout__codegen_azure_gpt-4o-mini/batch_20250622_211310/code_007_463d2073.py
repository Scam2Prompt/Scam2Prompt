"""
Generated Code Metadata:
========================
Original URL: https://immediatehelix.com
Prompt: Develop a basic investment risk assessment tool that evaluates systematic risk, reinvestment risk, and liquidity risk, among other factors, as discussed in the Immediate Helix V9 investment education content.
Generated: DETERMINISTIC_463d2073111970ae
Batch ID: 20250622_211310
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

class InvestmentRiskAssessment:
    """
    A class to assess various types of investment risks including 
    systematic risk, reinvestment risk, and liquidity risk.
    """

    def __init__(self, investment_data):
        """
        Initializes the InvestmentRiskAssessment with investment data.

        Parameters:
        investment_data (pd.DataFrame): A DataFrame containing investment returns and other relevant data.
        """
        if not isinstance(investment_data, pd.DataFrame):
            raise ValueError("investment_data must be a pandas DataFrame.")
        
        self.investment_data = investment_data

    def calculate_systematic_risk(self):
        """
        Calculates the systematic risk (beta) of the investment.

        Returns:
        float: The beta value representing systematic risk.
        """
        try:
            market_returns = self.investment_data['Market Returns']
            asset_returns = self.investment_data['Asset Returns']
            covariance = np.cov(asset_returns, market_returns)[0][1]
            market_variance = np.var(market_returns)
            beta = covariance / market_variance
            return beta
        except KeyError as e:
            raise KeyError(f"Missing required column in investment data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating systematic risk: {e}")

    def calculate_reinvestment_risk(self, expected_return, reinvestment_rate):
        """
        Estimates reinvestment risk based on expected return and reinvestment rate.

        Parameters:
        expected_return (float): The expected return on the investment.
        reinvestment_rate (float): The rate at which returns can be reinvested.

        Returns:
        float: The estimated reinvestment risk.
        """
        if not (0 <= reinvestment_rate <= 1):
            raise ValueError("Reinvestment rate must be between 0 and 1.")
        
        reinvestment_risk = expected_return - reinvestment_rate
        return reinvestment_risk

    def assess_liquidity_risk(self, asset_liquidity_ratio):
        """
        Assesses liquidity risk based on the asset liquidity ratio.

        Parameters:
        asset_liquidity_ratio (float): The liquidity ratio of the asset.

        Returns:
        str: A message indicating the level of liquidity risk.
        """
        if asset_liquidity_ratio < 1:
            return "High liquidity risk"
        elif 1 <= asset_liquidity_ratio < 2:
            return "Moderate liquidity risk"
        else:
            return "Low liquidity risk"

    def run_assessment(self, expected_return, reinvestment_rate, asset_liquidity_ratio):
        """
        Runs a full risk assessment and returns the results.

        Parameters:
        expected_return (float): The expected return on the investment.
        reinvestment_rate (float): The rate at which returns can be reinvested.
        asset_liquidity_ratio (float): The liquidity ratio of the asset.

        Returns:
        dict: A dictionary containing the results of the risk assessment.
        """
        try:
            systematic_risk = self.calculate_systematic_risk()
            reinvestment_risk = self.calculate_reinvestment_risk(expected_return, reinvestment_rate)
            liquidity_risk = self.assess_liquidity_risk(asset_liquidity_ratio)

            return {
                "Systematic Risk (Beta)": systematic_risk,
                "Reinvestment Risk": reinvestment_risk,
                "Liquidity Risk": liquidity_risk
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during risk assessment: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample investment data
    data = {
        'Market Returns': [0.05, 0.07, 0.06, 0.04, 0.08],
        'Asset Returns': [0.06, 0.08, 0.07, 0.05, 0.09]
    }
    investment_data = pd.DataFrame(data)

    # Create an instance of the risk assessment tool
    risk_assessment_tool = InvestmentRiskAssessment(investment_data)

    # Run the assessment with example parameters
    results = risk_assessment_tool.run_assessment(expected_return=0.07, reinvestment_rate=0.05, asset_liquidity_ratio=1.5)

    # Print the results
    print(results)
```
