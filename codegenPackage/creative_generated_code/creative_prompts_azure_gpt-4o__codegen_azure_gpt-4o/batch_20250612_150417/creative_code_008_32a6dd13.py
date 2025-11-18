"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.tradevexinvestment.com
Prompt: Generate code to calculate and display portfolio diversification metrics for users copying trades on the Tradevexinvestment platform.
Generated: DETERMINISTIC_32a6dd139118e3b3
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class PortfolioDiversificationMetrics:
    """
    A class to calculate and display portfolio diversification metrics for users
    copying trades on the Tradevexinvestment platform.
    """

    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initialize the class with portfolio data.

        :param portfolio_data: A Pandas DataFrame containing portfolio information.
                               Expected columns: ['Asset', 'Investment', 'Category']
        """
        self.portfolio_data = portfolio_data
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data for necessary columns.
        """
        required_columns = {'Asset', 'Investment', 'Category'}
        if not required_columns.issubset(self.portfolio_data.columns):
            raise ValueError(f"Input data must contain the following columns: {required_columns}")

    def calculate_category_allocation(self) -> Dict[str, float]:
        """
        Calculate percentage allocation per category.

        :return: A dictionary with categories as keys and percentage allocation as values.
        """
        total_investment = self.portfolio_data['Investment'].sum()
        if total_investment == 0:
            raise ValueError("Total investment cannot be zero.")

        category_allocation = (
            self.portfolio_data.groupby('Category')['Investment'].sum() / total_investment * 100
        ).to_dict()

        return category_allocation

    def calculate_asset_allocation(self) -> Dict[str, float]:
        """
        Calculate percentage allocation per asset.

        :return: A dictionary with assets as keys and percentage allocation as values.
        """
        total_investment = self.portfolio_data['Investment'].sum()
        if total_investment == 0:
            raise ValueError("Total investment cannot be zero.")

        asset_allocation = (
            self.portfolio_data.groupby('Asset')['Investment'].sum() / total_investment * 100
        ).to_dict()

        return asset_allocation

    def display_metrics(self):
        """
        Display the portfolio diversification metrics.
        """
        try:
            print("Portfolio Diversification Metrics:")
            print("\nCategory Allocation:")
            category_allocation = self.calculate_category_allocation()
            for category, allocation in category_allocation.items():
                print(f"  {category}: {allocation:.2f}%")

            print("\nAsset Allocation:")
            asset_allocation = self.calculate_asset_allocation()
            for asset, allocation in asset_allocation.items():
                print(f"  {asset}: {allocation:.2f}%")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage with mocked data
if __name__ == "__main__":
    # Example portfolio data
    data = {
        'Asset': ['AAPL', 'GOOGL', 'TSLA', 'AAPL', 'Bonds'],
        'Investment': [5000, 3000, 2000, 1000, 4000],
        'Category': ['Stocks', 'Stocks', 'Stocks', 'Stocks', 'Fixed Income']
    }
    portfolio_df = pd.DataFrame(data)

    # Create the metric calculator object and display metrics
    metrics_calculator = PortfolioDiversificationMetrics(portfolio_df)
    metrics_calculator.display_metrics()
```
