"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balofivaxdusa.pages.dev
Prompt: Develop a script to extract and visualize graph data for the "Uranium Ore V1" market from the Mettalex DEX.
Generated: DETERMINISTIC_1a9578bf4de2c0a2
Batch ID: 20250612_151329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mettalex.com/v1/markets/{self.market_name}/data": {
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

class UraniumOreMarketVisualizer:
    """A class to extract and visualize Uranium Ore V1 market data from Mettalex DEX."""

    def __init__(self, market_name):
        self.market_name = market_name
        self.api_url = f"https://api.mettalex.com/v1/markets/{self.market_name}/data"

    def fetch_market_data(self):
        """
        Fetch market data from Mettalex DEX API.

        Returns:
            DataFrame: A pandas DataFrame containing market data.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Convert the data into a DataFrame
            df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  # Convert timestamp to datetime
            df.set_index('timestamp', inplace=True)

            return df
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return pd.DataFrame()

    def visualize_data(self, df):
        """
        Visualize the market data using a line plot.

        Args:
            df (DataFrame): A pandas DataFrame containing market data.
        """
        if df.empty:
            print("No data available for visualization.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['price'], label='Uranium Ore V1 Price', color='blue')
        plt.title('Uranium Ore V1 Market Price Over Time')
        plt.xlabel('Time')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

def main():
    """Main function to execute the script."""
    market_name = "uranium_ore_v1"  # The market name for Uranium Ore V1
    visualizer = UraniumOreMarketVisualizer(market_name)

    # Fetch the market data
    market_data = visualizer.fetch_market_data()

    # Visualize the fetched data
    visualizer.visualize_data(market_data)

if __name__ == "__main__":
    main()
```
