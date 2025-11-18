"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nebulawealth-ai-software.com
Prompt: Create a script that utilizes Nebula Wealth AI's tools to analyze the impact of market fluctuations on cryptocurrency portfolios. Include recommendations for optimizing investments.
Generated: DETERMINISTIC_2594cb3fa86fa02c
Batch ID: 20250612_150048
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nebulawealth.com": {
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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CryptoPortfolioAnalyzer:
    """
    A class to analyze cryptocurrency portfolios and provide recommendations based on market fluctuations.
    """
    
    def __init__(self, api_key):
        """
        Initializes the CryptoPortfolioAnalyzer with the provided API key.

        :param api_key: str - API key for accessing Nebula Wealth AI's tools
        """
        self.api_key = api_key
        self.base_url = "https://api.nebulawealth.com"  # Replace with the actual API endpoint

    def fetch_market_data(self, symbols):
        """
        Fetches market data for the specified cryptocurrency symbols.

        :param symbols: list - List of cryptocurrency symbols
        :return: DataFrame - DataFrame containing market data
        """
        try:
            endpoint = f"{self.base_url}/market_data"
            response = requests.get(endpoint, params={'symbols': ','.join(symbols)}, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()  # Raise an error for bad responses
            return pd.DataFrame(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def analyze_portfolio(self, portfolio):
        """
        Analyzes the given cryptocurrency portfolio.

        :param portfolio: dict - Dictionary containing cryptocurrency symbols and their respective amounts
        :return: dict - Analysis results including total value and recommendations
        """
        symbols = list(portfolio.keys())
        market_data = self.fetch_market_data(symbols)

        if market_data.empty:
            return {"error": "No market data available for analysis."}
        
        # Calculate portfolio value and recommend adjustments
        total_value = 0
        recommendations = []

        for symbol, amount in portfolio.items():
            if symbol in market_data['symbol'].values:
                price = market_data.loc[market_data['symbol'] == symbol, 'price'].values[0]
                value = price * amount
                total_value += value
                recommendations.append((symbol, price, value))

        # Generate optimization recommendations based on market fluctuations
        recommendations.append(self.optimize_investments(portfolio, market_data))

        return {
            "total_value": total_value,
            "investments": recommendations
        }

    def optimize_investments(self, portfolio, market_data):
        """
        Provides recommendations for optimizing investments based on market fluctuations.

        :param portfolio: dict - The current cryptocurrency portfolio
        :param market_data: DataFrame - DataFrame containing the latest market data
        :return: dict - A recommendation for investment optimization
        """
        # This is a simplified implementation for illustrative purposes
        avg_market_price = market_data['price'].mean()
        underperforming_assets = {}

        for symbol in portfolio.keys():
            if symbol in market_data['symbol'].values:
                price = market_data.loc[market_data['symbol'] == symbol, 'price'].values[0]
                if price < avg_market_price:
                    underperforming_assets[symbol] = price

        return {
            "recommendation": "Consider reallocating funds from underperforming assets.",
            "underperforming_assets": underperforming_assets
        }

    def plot_portfolio_distribution(self, portfolio, analysis_results):
        """
        Plots the distribution of the cryptocurrency portfolio based on the analysis results.

        :param portfolio: dict - The current cryptocurrency portfolio
        :param analysis_results: dict - The analysis results containing investments
        """
        labels = list(portfolio.keys())
        sizes = [value[2] for value in analysis_results['investments'] if isinstance(value, tuple)]

        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.title('Cryptocurrency Portfolio Distribution')
        plt.show()

# Example usage:
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    portfolio = {
        'BTC': 0.5,
        'ETH': 2.0,
        'LTC': 5.0,
    }
    
    analyzer = CryptoPortfolioAnalyzer(API_KEY)
    analysis_results = analyzer.analyze_portfolio(portfolio)

    if 'error' in analysis_results:
        print(analysis_results['error'])
    else:
        print(f"Total Portfolio Value: ${analysis_results['total_value']:.2f}")
        for investment in analysis_results['investments']:
            if isinstance(investment, tuple):
                print(f"Asset: {investment[0]}, Price: ${investment[1]:.2f}, Value: ${investment[2]:.2f}")
            else:
                print(investment['recommendation'])
                for asset, price in investment['underperforming_assets'].items():
                    print(f"  Underperforming Asset: {asset}, Current Price: ${price:.2f}")

        analyzer.plot_portfolio_distribution(portfolio, analysis_results)
```
