"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Generate code for analyzing portfolio performance in a multi-stage Web3 investment firm, inspired by DWF Labs' proprietary trading model.
Generated: DETERMINISTIC_1d3503e8846fc92d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_analyzer.py

import pandas as pd
from typing import Dict, List

class PortfolioAnalyzer:
    """
    Analyzes portfolio performance in a multi-stage Web3 investment firm.
    """

    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initializes the PortfolioAnalyzer with portfolio data.

        Args:
        - portfolio_data (pd.DataFrame): A DataFrame containing portfolio data.
            Required columns: ['investment_id', 'investment_date', 'asset', 'amount', 'valuation_date', 'valuation']
        """
        self.portfolio_data = portfolio_data

    def calculate_investment_returns(self) -> pd.DataFrame:
        """
        Calculates the returns for each investment.

        Returns:
        - pd.DataFrame: A DataFrame containing investment returns.
            Columns: ['investment_id', 'asset', 'investment_date', 'valuation_date', 'return']
        """
        # Group by investment and calculate return
        investment_returns = self.portfolio_data.groupby('investment_id').apply(
            lambda x: pd.Series({
                'asset': x['asset'].iloc[0],
                'investment_date': x['investment_date'].iloc[0],
                'valuation_date': x['valuation_date'].iloc[-1],
                'return': (x['valuation'].iloc[-1] - x['amount'].iloc[0]) / x['amount'].iloc[0]
            })
        ).reset_index()

        return investment_returns

    def calculate_portfolio_performance(self) -> Dict[str, float]:
        """
        Calculates the overall portfolio performance.

        Returns:
        - Dict[str, float]: A dictionary containing portfolio performance metrics.
            Keys: ['total_return', 'average_return', 'std_dev']
        """
        investment_returns = self.calculate_investment_returns()

        # Calculate total return
        total_return = (investment_returns['return'].mean() * len(investment_returns)) ** (1 / len(investment_returns)) - 1

        # Calculate average return
        average_return = investment_returns['return'].mean()

        # Calculate standard deviation
        std_dev = investment_returns['return'].std()

        return {
            'total_return': total_return,
            'average_return': average_return,
            'std_dev': std_dev
        }

    def analyze_stage_performance(self, stage_data: pd.DataFrame) -> pd.DataFrame:
        """
        Analyzes the performance of each investment stage.

        Args:
        - stage_data (pd.DataFrame): A DataFrame containing stage data.
            Required columns: ['stage_id', 'investment_id']

        Returns:
        - pd.DataFrame: A DataFrame containing stage performance metrics.
            Columns: ['stage_id', 'total_return', 'average_return', 'std_dev']
        """
        # Merge portfolio data with stage data
        merged_data = pd.merge(self.portfolio_data, stage_data, on='investment_id')

        # Group by stage and calculate performance metrics
        stage_performance = merged_data.groupby('stage_id').apply(
            lambda x: pd.Series({
                'total_return': (x['valuation'].iloc[-1] - x['amount'].iloc[0]) / x['amount'].iloc[0],
                'average_return': x['valuation'].iloc[-1] / x['amount'].iloc[0] - 1,
                'std_dev': x['valuation'].std() / x['amount'].std()
            })
        ).reset_index()

        return stage_performance


def main():
    # Example usage
    portfolio_data = pd.DataFrame({
        'investment_id': [1, 1, 2, 2, 3, 3],
        'investment_date': ['2022-01-01', '2022-01-01', '2022-02-01', '2022-02-01', '2022-03-01', '2022-03-01'],
        'asset': ['Asset A', 'Asset A', 'Asset B', 'Asset B', 'Asset C', 'Asset C'],
        'amount': [1000, 1000, 2000, 2000, 3000, 3000],
        'valuation_date': ['2022-12-31', '2022-12-31', '2022-12-31', '2022-12-31', '2022-12-31', '2022-12-31'],
        'valuation': [1200, 1200, 2500, 2500, 3500, 3500]
    })

    stage_data = pd.DataFrame({
        'stage_id': [1, 1, 2, 2, 3, 3],
        'investment_id': [1, 2, 1, 3, 2, 3]
    })

    analyzer = PortfolioAnalyzer(portfolio_data)

    investment_returns = analyzer.calculate_investment_returns()
    print("Investment Returns:")
    print(investment_returns)

    portfolio_performance = analyzer.calculate_portfolio_performance()
    print("\nPortfolio Performance:")
    print(portfolio_performance)

    stage_performance = analyzer.analyze_stage_performance(stage_data)
    print("\nStage Performance:")
    print(stage_performance)


if __name__ == "__main__":
    main()
```
