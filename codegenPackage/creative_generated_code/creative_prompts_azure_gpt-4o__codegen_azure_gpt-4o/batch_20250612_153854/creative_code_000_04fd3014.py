"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write Python code to analyze investment portfolios, focusing on private equity opportunities as described by Alghanim Capital's expertise in strategic growth and investment lifecycle management.
Generated: DETERMINISTIC_04fd3014f519d03f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class InvestmentPortfolioAnalyzer:
    """
    A class to analyze investment portfolios, with a focus on private equity opportunities.
    """

    def __init__(self, portfolio_data):
        """
        Initialize the analyzer with portfolio data.
        
        Args:
        portfolio_data (pd.DataFrame): DataFrame containing portfolio information. 
                                       Expected columns: ['Investment Name', 'Investment Type', 'Amount Invested', 'ROI', 'Risk Level']
        """
        if not isinstance(portfolio_data, pd.DataFrame):
            raise ValueError("portfolio_data must be a Pandas DataFrame")
        
        self.portfolio_data = portfolio_data

    def filter_private_equity(self):
        """
        Filters the portfolio to include only private equity investments.

        Returns:
        pd.DataFrame: Filtered DataFrame containing only private equity investments.
        """
        try:
            # Filter for private equity investments
            private_equity_data = self.portfolio_data[self.portfolio_data['Investment Type'] == 'Private Equity']
            return private_equity_data
        except KeyError:
            raise KeyError("Expected column 'Investment Type' not found in portfolio data")

    def calculate_total_investment(self, investment_data):
        """
        Calculates the total amount invested in the provided investment data.

        Args:
        investment_data (pd.DataFrame): DataFrame containing investment data.

        Returns:
        float: Total amount invested.
        """
        try:
            return investment_data['Amount Invested'].sum()
        except KeyError:
            raise KeyError("Expected column 'Amount Invested' not found in investment data")

    def calculate_average_roi(self, investment_data):
        """
        Calculates the average Return on Investment (ROI) for the provided investment data.

        Args:
        investment_data (pd.DataFrame): DataFrame containing investment data.

        Returns:
        float: Average ROI.
        """
        try:
            return investment_data['ROI'].mean()
        except KeyError:
            raise KeyError("Expected column 'ROI' not found in investment data")

    def analyze_risk_distribution(self, investment_data):
        """
        Analyzes the distribution of risk levels in the provided investment data.

        Args:
        investment_data (pd.DataFrame): DataFrame containing investment data.

        Returns:
        pd.Series: Distribution of risk levels.
        """
        try:
            return investment_data['Risk Level'].value_counts()
        except KeyError:
            raise KeyError("Expected column 'Risk Level' not found in investment data")

def main():
    # Example portfolio data
    data = {
        'Investment Name': ['Investment A', 'Investment B', 'Investment C', 'Investment D'],
        'Investment Type': ['Private Equity', 'Stock', 'Private Equity', 'Real Estate'],
        'Amount Invested': [500000, 200000, 750000, 300000],
        'ROI': [0.15, 0.1, 0.2, 0.12],
        'Risk Level': ['High', 'Medium', 'High', 'Low']
    }
    
    portfolio_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = InvestmentPortfolioAnalyzer(portfolio_df)

    # Filter private equity investments
    private_equity_data = analyzer.filter_private_equity()
    print("Private Equity Investments:")
    print(private_equity_data)

    # Calculate total amount invested in private equity
    total_investment = analyzer.calculate_total_investment(private_equity_data)
    print(f"\nTotal Amount Invested in Private Equity: ${total_investment:,.2f}")

    # Calculate average ROI for private equity
    average_roi = analyzer.calculate_average_roi(private_equity_data)
    print(f"Average ROI for Private Equity: {average_roi:.2%}")

    # Analyze risk distribution in private equity
    risk_distribution = analyzer.analyze_risk_distribution(private_equity_data)
    print("\nRisk Distribution in Private Equity:")
    print(risk_distribution)

if __name__ == "__main__":
    main()
```
