"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Create a Python program to identify profitable social media niches, based on the niche selection insights from Fearless Netpreneur.
Generated: DETERMINISTIC_f6b8274f82f0291e
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from typing import List, Dict

class NicheAnalyzer:
    """
    Analyzes social media niches based on Fearless Netpreneur's insights.

    Attributes:
        niche_data (pd.DataFrame): DataFrame containing niche data.
    """

    def __init__(self, niche_data: pd.DataFrame):
        """
        Initializes the NicheAnalyzer with niche data.

        Args:
            niche_data (pd.DataFrame): DataFrame containing niche data.
        """
        self.niche_data = niche_data

    def calculate_profitability(self, 
                              revenue_column: str, 
                              cost_column: str) -> pd.DataFrame:
        """
        Calculates the profitability of each niche.

        Args:
            revenue_column (str): Column name for revenue data.
            cost_column (str): Column name for cost data.

        Returns:
            pd.DataFrame: DataFrame with profitability data.
        """
        # Check if required columns exist
        if revenue_column not in self.niche_data.columns or cost_column not in self.niche_data.columns:
            raise ValueError("Required columns do not exist in the data")

        # Calculate profit
        self.niche_data['profit'] = self.niche_data[revenue_column] - self.niche_data[cost_column]

        # Calculate return on investment (ROI)
        self.niche_data['roi'] = (self.niche_data['profit'] / self.niche_data[cost_column]) * 100

        return self.niche_data

    def filter_niches(self, 
                      min_revenue: float, 
                      min_profit: float, 
                      min_roi: float) -> pd.DataFrame:
        """
        Filters niches based on minimum revenue, profit, and ROI.

        Args:
            min_revenue (float): Minimum revenue threshold.
            min_profit (float): Minimum profit threshold.
            min_roi (float): Minimum ROI threshold.

        Returns:
            pd.DataFrame: DataFrame with filtered niches.
        """
        # Filter niches
        filtered_niches = self.niche_data[
            (self.niche_data['revenue'] >= min_revenue) &
            (self.niche_data['profit'] >= min_profit) &
            (self.niche_data['roi'] >= min_roi)
        ]

        return filtered_niches

def main():
    # Sample niche data
    data: List[Dict] = [
        {'niche': 'Gaming', 'revenue': 10000, 'cost': 5000},
        {'niche': 'Food', 'revenue': 5000, 'cost': 2000},
        {'niche': 'Technology', 'revenue': 20000, 'cost': 10000},
        {'niche': 'Sports', 'revenue': 8000, 'cost': 3000},
    ]

    # Create DataFrame
    df: pd.DataFrame = pd.DataFrame(data)

    # Create NicheAnalyzer instance
    analyzer: NicheAnalyzer = NicheAnalyzer(df)

    try:
        # Calculate profitability
        profitability_data: pd.DataFrame = analyzer.calculate_profitability('revenue', 'cost')
        print("Profitability Data:")
        print(profitability_data)

        # Filter niches
        filtered_niches: pd.DataFrame = analyzer.filter_niches(5000, 2000, 50)
        print("\nFiltered Niches:")
        print(filtered_niches)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
