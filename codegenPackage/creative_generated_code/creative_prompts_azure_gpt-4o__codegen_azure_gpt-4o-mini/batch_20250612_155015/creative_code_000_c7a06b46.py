"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket-soto.pages.dev
Prompt: Write Python code to analyze prediction market data from Polymarket, focusing on probabilities assigned to MLB team trades, and compare them to actual trade outcomes for Juan Soto.
Generated: DETERMINISTIC_c7a06b46c9ffe8d6
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com/v2/markets": {
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
import pandas as pd
import requests
import matplotlib.pyplot as plt

class PredictionMarketAnalyzer:
    def __init__(self, api_url):
        """
        Initializes the PredictionMarketAnalyzer with the given API URL.

        :param api_url: str - The API endpoint for fetching the prediction market data.
        """
        self.api_url = api_url
        self.data = None

    def fetch_data(self):
        """
        Fetches prediction market data from the specified API.

        :raises Exception: Raises an exception if the API request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Check for HTTP errors
            self.data = response.json()   # Parse JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from API: {e}")

    def filter_trade_probabilities(self, player_name):
        """
        Filters the prediction market data to extract probabilities related to a specific player.

        :param player_name: str - The name of the player to filter data for.
        :return: pd.DataFrame - A DataFrame containing filtered probabilities.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() before filtering.")

        # Assuming the data contains a 'trades' key with a list of trades
        trades = pd.DataFrame(self.data['trades'])
        player_trades = trades[trades['player'] == player_name]
        
        return player_trades[['team', 'probability']]

    def plot_probabilities(self, probabilities):
        """
        Plots the trade probabilities for the specified probabilities DataFrame.

        :param probabilities: pd.DataFrame - DataFrame containing team trade probabilities.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(probabilities['team'], probabilities['probability'], color='skyblue')
        plt.xlabel('Teams')
        plt.ylabel('Probability (%)')
        plt.title('MLB Team Trade Probabilities for Juan Soto')
        plt.xticks(rotation=45)
        plt.ylim(0, 100)
        plt.grid(axis='y')
        plt.show()

def main():
    """
    Main function to execute the prediction market analysis for MLB trades.
    """
    # Replace with the actual API URL for Polymarket data
    api_url = "https://api.polymarket.com/v2/markets"

    analyzer = PredictionMarketAnalyzer(api_url)

    # Fetch market data
    analyzer.fetch_data()

    # Analyze trade probabilities for Juan Soto
    player_name = "Juan Soto"
    probabilities = analyzer.filter_trade_probabilities(player_name)

    # Plot the results
    analyzer.plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
```
