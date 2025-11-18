"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://l2lusty.site
Prompt: Create a tool to analyze the droplist and rates provided on the L2Lusty server and generate a strategy guide for optimizing gameplay.
Generated: DETERMINISTIC_3d36712dc45b65a3
Batch ID: 20250612_145615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/rates.csv": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/droplist.csv": {
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
import numpy as np
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class L2LustyAnalyzer:
    def __init__(self, droplist_url: str, rates_url: str):
        """
        Initializes the L2LustyAnalyzer with the URL for the droplist and rates.

        :param droplist_url: URL to fetch the droplist data from
        :param rates_url: URL to fetch the rates data from
        """
        self.droplist_url = droplist_url
        self.rates_url = rates_url
        self.droplist = None
        self.rates = None

    def fetch_data(self):
        """Fetches the droplist and rates data from the specified URLs."""
        try:
            logging.info("Fetching droplist data...")
            self.droplist = pd.read_csv(self.droplist_url)
            logging.info("Droplist data fetched successfully.")
            
            logging.info("Fetching rates data...")
            self.rates = pd.read_csv(self.rates_url)
            logging.info("Rates data fetched successfully.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def analyze_data(self):
        """Analyzes the droplist and rates to generate a strategy guide."""
        if self.droplist is None or self.rates is None:
            logging.error("Data is not loaded. Please fetch the data first.")
            return

        # Sample analysis: Calculate optimal item to farm based on drop rates
        try:
            # Merge droplist and rates on item ID
            combined_data = pd.merge(self.droplist, self.rates, on='item_id', how='inner')

            # Calculate expected value for each item
            combined_data['expected_value'] = combined_data['drop_rate'] * combined_data['sell_price']

            # Sort items by expected value in descending order
            strategy_guide = combined_data.sort_values(by='expected_value', ascending=False)

            logging.info("Analysis completed successfully.")
            return strategy_guide[['item_name', 'expected_value']]
        except Exception as e:
            logging.error(f"Error during data analysis: {e}")
            raise

    def generate_strategy_guide(self, output_file: str):
        """Generates and saves a strategy guide to the specified file."""
        strategy_guide = self.analyze_data()
        if strategy_guide is not None:
            try:
                strategy_guide.to_csv(output_file, index=False)
                logging.info(f"Strategy guide saved to {output_file}.")
            except Exception as e:
                logging.error(f"Error saving strategy guide: {e}")
                raise

if __name__ == "__main__":
    # Define URLs for droplist and rates
    DROPLIST_URL = "https://example.com/droplist.csv"  # Replace with actual URL
    RATES_URL = "https://example.com/rates.csv"          # Replace with actual URL
    OUTPUT_FILE = "strategy_guide.csv"

    # Create an instance of the analyzer tool
    analyzer = L2LustyAnalyzer(DROPLIST_URL, RATES_URL)

    # Fetch data, analyze it, and generate the strategy guide
    try:
        analyzer.fetch_data()
        analyzer.generate_strategy_guide(OUTPUT_FILE)
    except Exception as e:
        logging.critical(f"An error occurred in the main execution: {e}")
```
