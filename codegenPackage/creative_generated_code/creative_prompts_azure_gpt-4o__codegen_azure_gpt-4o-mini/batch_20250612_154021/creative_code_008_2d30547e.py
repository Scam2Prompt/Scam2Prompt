"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdxe.com
Prompt: Create a tool to analyze liquidity fragmentation across blockchains and demonstrate how Aster's liquidity aggregation resolves this issue.
Generated: DETERMINISTIC_2d30547eb31ad109
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/liquidity": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import pandas as pd
from typing import List, Dict

class BlockchainLiquidityAnalyzer:
    """
    A class to analyze liquidity fragmentation across different blockchains
    and demonstrate how Aster's liquidity aggregation resolves this issue.
    """
    
    def __init__(self, api_url: str):
        """
        Initializes the analyzer with the given API URL.

        :param api_url: The API endpoint to fetch liquidity data from
        """
        self.api_url = api_url

    def fetch_liquidity_data(self) -> List[Dict]:
        """
        Fetches liquidity data from the given API endpoint.

        :return: A list of liquidity data dictionaries
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching liquidity data: {e}")
            return []

    def analyze_liquidity_fragmentation(self, liquidity_data: List[Dict]) -> pd.DataFrame:
        """
        Analyzes liquidity fragmentation and returns a DataFrame.

        :param liquidity_data: A list of liquidity data dictionaries
        :return: A DataFrame containing the analyzed liquidity data
        """
        try:
            # Convert the liquidity data into a DataFrame
            df = pd.DataFrame(liquidity_data)

            # Group by blockchain and calculate total liquidity
            analysis_df = df.groupby('blockchain').agg({'liquidity': 'sum'}).reset_index()

            # Calculate fragmentation percentage
            total_liquidity = analysis_df['liquidity'].sum()
            analysis_df['fragmentation_percentage'] = (analysis_df['liquidity'] / total_liquidity) * 100
            
            return analysis_df
        except Exception as e:
            print(f"Error analyzing liquidity fragmentation: {e}")
            return pd.DataFrame()

    def demonstrate_aster_aggregation(self, analysis_df: pd.DataFrame) -> pd.DataFrame:
        """
        Demonstrates how Aster's liquidity aggregation resolves fragmentation.

        :param analysis_df: A DataFrame containing analyzed liquidity data
        :return: A DataFrame showing aggregated liquidity
        """
        try:
            # Placeholder for Aster's aggregation logic
            aggregated_liquidity = sum(analysis_df['liquidity'])
            aster_aggregation_df = pd.DataFrame({
                'blockchain': ['Aster Aggregated'],
                'liquidity': [aggregated_liquidity],
                'fragmentation_percentage': [0]  # No fragmentation in aggregation
            })
            return pd.concat([analysis_df, aster_aggregation_df], ignore_index=True)
        except Exception as e:
            print(f"Error demonstrating Aster aggregation: {e}")
            return pd.DataFrame()

    def run_analysis(self):
        """
        Main function to run the liquidity fragmentation analysis.
        """
        liquidity_data = self.fetch_liquidity_data()
        if not liquidity_data:
            print("No liquidity data available for analysis.")
            return

        analysis_df = self.analyze_liquidity_fragmentation(liquidity_data)
        aggregated_df = self.demonstrate_aster_aggregation(analysis_df)

        print("Liquidity Fragmentation Analysis:")
        print(analysis_df)
        print("\nAster's Liquidity Aggregation:")
        print(aggregated_df)


if __name__ == "__main__":
    # Example API URL (replace with an actual API endpoint)
    api_url = "https://api.example.com/liquidity"
    
    analyzer = BlockchainLiquidityAnalyzer(api_url)
    analyzer.run_analysis()
```

This code provides a structured approach for analyzing liquidity fragmentation across blockchains and demonstrates the potential of Aster's liquidity aggregation in addressing this issue. The implementation includes error handling, data fetching, and processing while following best practices.
