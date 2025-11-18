"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Provide code examples for analyzing high-quality asset investments using systematic approaches, similar to the strategies employed by Grade World Investment Limited.
Generated: DETERMINISTIC_9157bd82fca9903a
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to analyze high-quality asset investments using systematic approaches
# Author: Professional Developer
# Date: YYYY-MM-DD
# Language: Python

import pandas as pd
import numpy as np

class InvestmentAnalyzer:
    """
    A class to analyze high-quality asset investments
    using systematic strategies.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the InvestmentAnalyzer class.

        :param data: A pandas DataFrame containing asset investment data.
                     Expected columns: ['Asset', 'Price', 'EPS', 'ROE', 'DebtToEquity', 'GrowthRate']
        """
        if not {'Asset', 'Price', 'EPS', 'ROE', 'DebtToEquity', 'GrowthRate'}.issubset(data.columns):
            raise ValueError("Data must contain the required columns: ['Asset', 'Price', 'EPS', 'ROE', 'DebtToEquity', 'GrowthRate']")
        
        self.data = data

    def calculate_p_e_ratio(self):
        """
        Calculate the Price-to-Earnings (P/E) ratio for each asset.
        Adds a new column 'PE_Ratio' to the DataFrame.
        """
        self.data['PE_Ratio'] = self.data['Price'] / self.data['EPS']
    
    def filter_high_quality_assets(self, max_pe_ratio: float, min_roe: float, max_debt_to_equity: float) -> pd.DataFrame:
        """
        Filter high-quality assets based on systematic criteria.

        :param max_pe_ratio: Maximum allowable P/E ratio.
        :param min_roe: Minimum required Return on Equity (ROE).
        :param max_debt_to_equity: Maximum allowable Debt-to-Equity ratio.
        :return: A filtered DataFrame of high-quality assets.
        """
        self.calculate_p_e_ratio()
        high_quality_assets = self.data[
            (self.data['PE_Ratio'] <= max_pe_ratio) &
            (self.data['ROE'] >= min_roe) &
            (self.data['DebtToEquity'] <= max_debt_to_equity)
        ]
        return high_quality_assets

    def rank_assets_by_growth(self) -> pd.DataFrame:
        """
        Rank assets based on their growth rate.

        :return: A DataFrame with assets ranked by growth rate in descending order.
        """
        ranked_assets = self.data.sort_values(by='GrowthRate', ascending=False).reset_index(drop=True)
        ranked_assets['Rank'] = ranked_assets.index + 1
        return ranked_assets

# Example usage
if __name__ == "__main__":
    # Example data for demonstration
    data = pd.DataFrame({
        'Asset': ['Asset A', 'Asset B', 'Asset C', 'Asset D'],
        'Price': [100, 200, 150, 300],
        'EPS': [10, 20, 15, 30],
        'ROE': [15, 25, 18, 10],
        'DebtToEquity': [0.5, 0.8, 0.3, 1.2],
        'GrowthRate': [12, 8, 10, 15]
    })

    try:
        analyzer = InvestmentAnalyzer(data)
        
        # Filter high-quality assets
        filtered_assets = analyzer.filter_high_quality_assets(max_pe_ratio=20, min_roe=15, max_debt_to_equity=1.0)
        print("High-Quality Assets:")
        print(filtered_assets)

        # Rank assets by growth
        ranked_assets = analyzer.rank_assets_by_growth()
        print("\nRanked Assets by Growth Rate:")
        print(ranked_assets)

    except Exception as e:
        print(f"An error occurred: {e}")
```
