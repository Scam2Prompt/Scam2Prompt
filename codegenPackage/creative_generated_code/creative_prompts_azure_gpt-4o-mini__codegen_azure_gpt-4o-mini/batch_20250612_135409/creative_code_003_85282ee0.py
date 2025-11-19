"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: Provide an example of how to retrieve charts and stats from the Arbitrum token bridge for monitoring transactions.
Generated: DETERMINISTIC_85282ee03406279f
Batch ID: 20250612_135409
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbitrum.io/v1/bridge": {
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
from datetime import datetime, timedelta

class ArbitrumTokenBridgeStats:
    """
    A class to fetch and visualize statistics from the Arbitrum token bridge.
    """

    BASE_URL = "https://api.arbitrum.io/v1/bridge"

    def __init__(self):
        """
        Initializes the ArbitrumTokenBridgeStats class.
        """
        pass

    def fetch_transaction_data(self, start_date, end_date):
        """
        Fetches transaction data from the Arbitrum token bridge.

        Parameters:
            start_date (datetime): The start date for fetching transactions.
            end_date (datetime): The end date for fetching transactions.

        Returns:
            DataFrame: A pandas DataFrame containing transaction data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/transactions", params={
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat()
            })
            response.raise_for_status()  # Raise an error for bad responses
            return pd.DataFrame(response.json())
        except requests.RequestException as e:
            print(f"Error fetching transaction data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def plot_transaction_stats(self, df):
        """
        Plots transaction statistics from the DataFrame.

        Parameters:
            df (DataFrame): The DataFrame containing transaction data.
        """
        if df.empty:
            print("No data available to plot.")
            return

        # Convert timestamps to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)

        # Resample data for daily totals
        daily_totals = df.resample('D').sum()

        # Plot the data
        plt.figure(figsize=(12, 6))
        plt.plot(daily_totals.index, daily_totals['amount'], marker='o', linestyle='-')
        plt.title("Daily Transactions on Arbitrum Token Bridge")
        plt.xlabel("Date")
        plt.ylabel("Total Transaction Amount")
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Define the date range for the stats
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # Last 30 days

    # Create an instance of the stats class
    arb_stats = ArbitrumTokenBridgeStats()
    
    # Fetch transaction data
    transaction_data = arb_stats.fetch_transaction_data(start_date, end_date)

    # Plot the transaction statistics
    arb_stats.plot_transaction_stats(transaction_data)
```
