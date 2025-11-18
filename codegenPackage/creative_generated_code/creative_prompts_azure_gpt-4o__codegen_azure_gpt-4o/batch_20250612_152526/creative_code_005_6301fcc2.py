"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aniemaxgroup.com
Prompt: Write code in Python to analyze loan portfolios and calculate their potential value, inspired by Aniemax Capital's loan portfolio services.
Generated: DETERMINISTIC_6301fcc266e1bfe6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class LoanPortfolioAnalyzer:
    """
    A class to analyze loan portfolios and calculate their potential value.
    Inspired by Aniemax Capital's loan portfolio services.
    """
    def __init__(self, portfolio_data):
        """
        Initialize the LoanPortfolioAnalyzer with loan portfolio data.

        :param portfolio_data: A pandas DataFrame containing loan portfolio information.
                               Columns should include 'loan_id', 'principal_amount', 'interest_rate', 'term_months', and 'status'.
        """
        if not isinstance(portfolio_data, pd.DataFrame):
            raise ValueError("portfolio_data must be a pandas DataFrame.")
        required_columns = {'loan_id', 'principal_amount', 'interest_rate', 'term_months', 'status'}
        if not required_columns.issubset(portfolio_data.columns):
            raise ValueError(f"portfolio_data must contain columns: {required_columns}")
        self.portfolio = portfolio_data

    def calculate_potential_value(self):
        """
        Calculate the potential value of the loan portfolio based on principal, interest rate, and term.

        :return: A pandas DataFrame with the original portfolio data and a new column 'potential_value'.
        """
        def calculate_loan_value(row):
            """
            Helper function to calculate the total potential value of a single loan.
            """
            if row['status'] == 'defaulted':
                return 0  # Defaulted loans have no potential value
            # Calculate the interest accrued over the loan term
            total_interest = row['principal_amount'] * (row['interest_rate'] / 100) * (row['term_months'] / 12)
            return row['principal_amount'] + total_interest

        self.portfolio['potential_value'] = self.portfolio.apply(calculate_loan_value, axis=1)
        return self.portfolio

    def summarize_portfolio(self):
        """
        Summarize the portfolio by calculating total potential value and grouping by loan status.

        :return: A dictionary containing portfolio summary statistics.
        """
        summary = {
            'total_potential_value': self.portfolio['potential_value'].sum(),
            'status_summary': self.portfolio.groupby('status')['potential_value'].sum().to_dict()
        }
        return summary


# Example usage
if __name__ == "__main__":
    # Sample loan portfolio data
    data = {
        'loan_id': [1, 2, 3, 4],
        'principal_amount': [10000, 5000, 7500, 12000],
        'interest_rate': [5, 4, 6, 5],
        'term_months': [24, 36, 12, 48],
        'status': ['active', 'active', 'defaulted', 'active']
    }
    portfolio_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = LoanPortfolioAnalyzer(portfolio_df)

    # Calculate potential value
    updated_portfolio = analyzer.calculate_potential_value()
    print("Updated Portfolio Data:")
    print(updated_portfolio)

    # Summarize portfolio
    portfolio_summary = analyzer.summarize_portfolio()
    print("\nPortfolio Summary:")
    print(portfolio_summary)
```
