"""
Generated Code Metadata:
========================
Original URL: https://m.okjywang.com
Prompt: Create a Python script to fetch and analyze margin trading data from OKX, including interest rates and leverage options.
Generated: DETERMINISTIC_86291c7f4230783a
Batch ID: 20250612_142622
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/api/v5": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OKXMarginTrading:
    BASE_URL = "https://www.okx.com/api/v5"

    def __init__(self):
        """Initialize the OKXMarginTrading class."""
        self.interest_rates = None
        self.leverage_options = None

    def fetch_interest_rates(self):
        """Fetch margin interest rates from OKX."""
        try:
            response = requests.get(f"{self.BASE_URL}/margin/interest-rate")
            response.raise_for_status()  # Raise an error for bad responses
            self.interest_rates = response.json()
            logging.info("Successfully fetched interest rates.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching interest rates: {e}")
            self.interest_rates = None

    def fetch_leverage_options(self):
        """Fetch leverage options from OKX."""
        try:
            response = requests.get(f"{self.BASE_URL}/margin/leverage")
            response.raise_for_status()  # Raise an error for bad responses
            self.leverage_options = response.json()
            logging.info("Successfully fetched leverage options.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching leverage options: {e}")
            self.leverage_options = None

    def analyze_data(self):
        """Analyze the fetched interest rates and leverage options."""
        if self.interest_rates is None or self.leverage_options is None:
            logging.warning("Data not available for analysis.")
            return

        # Convert interest rates to DataFrame for analysis
        interest_df = pd.DataFrame(self.interest_rates['data'])
        leverage_df = pd.DataFrame(self.leverage_options['data'])

        # Example analysis: Calculate average interest rate
        average_interest_rate = interest_df['interestRate'].astype(float).mean()
        logging.info(f"Average Interest Rate: {average_interest_rate:.4f}")

        # Example analysis: List leverage options
        leverage_list = leverage_df[['symbol', 'maxLeverage']]
        logging.info("Leverage Options:\n" + leverage_list.to_string(index=False))

    def run(self):
        """Run the data fetching and analysis process."""
        self.fetch_interest_rates()
        self.fetch_leverage_options()
        self.analyze_data()

if __name__ == "__main__":
    trading_data = OKXMarginTrading()
    trading_data.run()
```
