"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenz.co
Prompt: What libraries can I use to implement a portfolio analytics tool that leverages the features of Degenz.Finance for tracking crypto assets?
Generated: DETERMINISTIC_591b30fd5c596caa
Batch ID: 20250612_140402
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.degenz.finance/v1": {
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
import pandas as pd
import matplotlib.pyplot as plt

class PortfolioAnalytics:
    """
    A class to represent a portfolio analytics tool for tracking crypto assets
    using the Degenz.Finance API.
    """

    BASE_URL = "https://api.degenz.finance/v1"

    def __init__(self, api_key):
        """
        Initializes the PortfolioAnalytics with the provided API key.

        :param api_key: Your Degenz.Finance API key for authenticated requests
        """
        self.api_key = api_key

    def get_asset_data(self, asset_symbol):
        """
        Fetches asset data from the Degenz.Finance API.

        :param asset_symbol: The symbol of the crypto asset to fetch data for
        :return: JSON response containing asset data
        :raises ValueError: If the asset_symbol is invalid or not found
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f"{self.BASE_URL}/assets/{asset_symbol}", headers=headers)
        
        if response.status_code != 200:
            raise ValueError(f"Error fetching data for {asset_symbol}: {response.text}")
        
        return response.json()

    def analyze_portfolio(self, assets):
        """
        Analyzes the portfolio by fetching data for multiple assets and calculating metrics.

        :param assets: A list of crypto asset symbols to analyze
        :return: A DataFrame containing the portfolio analysis results
        """
        portfolio_data = []

        for asset in assets:
            try:
                data = self.get_asset_data(asset)
                portfolio_data.append({
                    'symbol': asset,
                    'price': data['price'],
                    'market_cap': data['market_cap'],
                    'volume': data['volume'],
                })
            except ValueError as e:
                print(e)

        return pd.DataFrame(portfolio_data)

    def plot_portfolio(self, portfolio_df):
        """
        Plots the market cap of the portfolio assets.

        :param portfolio_df: DataFrame containing portfolio asset information
        """
        try:
            portfolio_df.set_index('symbol')['market_cap'].plot(kind='bar')
            plt.title('Portfolio Market Cap Distribution')
            plt.xlabel('Crypto Assets')
            plt.ylabel('Market Cap')
            plt.show()
        except Exception as e:
            print(f"Error plotting portfolio: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    DEGENZ_API_KEY = "your_api_key_here"
    
    # Initialize the portfolio analytics tool
    portfolio_tool = PortfolioAnalytics(DEGENZ_API_KEY)
    
    # List of crypto assets to analyze
    assets_to_analyze = ['BTC', 'ETH', 'SOL']

    # Analyze the portfolio
    portfolio_df = portfolio_tool.analyze_portfolio(assets_to_analyze)
    
    if not portfolio_df.empty:
        # Plot the portfolio analysis result
        portfolio_tool.plot_portfolio(portfolio_df)
    else:
        print("No data available for the specified assets.")
```
