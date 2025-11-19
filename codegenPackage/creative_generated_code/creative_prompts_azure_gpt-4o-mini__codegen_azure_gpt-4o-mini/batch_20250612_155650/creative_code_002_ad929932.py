"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama-app.github.io
Prompt: Explain how to implement a cross-chain bridge data tracker using the information provided by DefiLlama.
Generated: DETERMINISTIC_ad929932489ebb60
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/bridges": {
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
from datetime import datetime
import logging

# Set up logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CrossChainBridgeTracker:
    """
    A class to track cross-chain bridge data using information from the DefiLlama API.
    """

    def __init__(self):
        self.api_url = "https://api.defillama.com/v1/bridges"
        self.data = None

    def fetch_bridge_data(self):
        """
        Fetches bridge data from the DefiLlama API and stores it in the class.
        Handles any potential errors during the API call.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            self.data = response.json()  # Convert the response to JSON format
            logging.info("Bridge data fetched successfully.")
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            self.data = []
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            self.data = []

    def process_bridge_data(self):
        """
        Processes the fetched bridge data into a DataFrame.
        Returns a DataFrame containing relevant information about each bridge.
        """
        if not self.data:
            logging.warning("No data to process. Please fetch data first.")
            return pd.DataFrame()  # Return an empty DataFrame if no data available

        # Extract relevant information for each bridge and create a DataFrame
        bridge_info = []
        for bridge in self.data:
            bridge_info.append({
                "name": bridge.get("name"),
                "chain_from": bridge.get("chainFrom"),
                "chain_to": bridge.get("chainTo"),
                "total_value_locked": bridge.get("totalValueLocked"),
                "transaction_count": bridge.get("transactionCount"),
                "last_updated": datetime.fromisoformat(bridge.get("lastUpdated"))  # Convert to datetime
            })

        bridge_df = pd.DataFrame(bridge_info)
        logging.info("Bridge data has been processed into a DataFrame.")
        return bridge_df

    def save_data_to_csv(self, filename='bridge_data.csv'):
        """
        Saves the processed bridge data to a CSV file.
        
        Args:
            filename (str): The name of the file to save the data to.
        """
        bridge_df = self.process_bridge_data()
        if bridge_df.empty:
            logging.warning("No data available to save.")
            return
        
        try:
            bridge_df.to_csv(filename, index=False)
            logging.info(f"Bridge data saved to {filename}.")
        except Exception as err:
            logging.error(f"Failed to save data to CSV: {err}")

if __name__ == "__main__":
    tracker = CrossChainBridgeTracker()
    tracker.fetch_bridge_data()
    tracker.save_data_to_csv()
```
