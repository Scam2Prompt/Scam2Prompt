"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipei-buq.pages.dev
Prompt: Write a script to track $PEIPEI token holder growth and generate reports based on the milestones outlined in the roadmap phases.
Generated: DETERMINISTIC_45cdc371f8b2da62
Batch ID: 20250612_151207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.yourblockchainprovider.com": {
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
import time
import logging
from datetime import datetime
from collections import defaultdict

# Set up logging for tracking the script execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenHolderTracker:
    def __init__(self, token_address, api_url):
        """
        Initializes the TokenHolderTracker with the specified token address and API URL.
        
        :param token_address: The smart contract address of the $PEIPEI token.
        :param api_url: The API URL to fetch token holder data.
        """
        self.token_address = token_address
        self.api_url = api_url
        self.holder_data = defaultdict(list)

    def fetch_token_holders(self):
        """
        Fetches the current list of token holders from the blockchain API.
        
        :return: A list of holders if the API call is successful; otherwise, raises an exception.
        """
        try:
            response = requests.get(f"{self.api_url}/tokens/{self.token_address}/holders")
            response.raise_for_status()  # Raises an error for bad responses
            return response.json().get('holders', [])
        except requests.RequestException as e:
            logging.error(f"Error fetching token holders: {e}")
            raise

    def track_growth(self):
        """
        Tracks the growth of token holders at regular intervals and stores the data.
        """
        while True:
            try:
                holders = self.fetch_token_holders()
                timestamp = datetime.now().isoformat()
                self.holder_data[timestamp].extend(holders)
                logging.info(f"Fetched {len(holders)} holders at {timestamp}.")
                
                # Wait for a specified interval before the next fetch
                time.sleep(86400)  # Fetch daily
            except Exception as e:
                logging.error(f"An error occurred during tracking: {e}")

    def generate_report(self):
        """
        Generates a report of token holder growth based on the collected data.
        
        :return: A formatted report string.
        """
        report_lines = []
        report_lines.append("Token Holder Growth Report")
        report_lines.append("=" * 30)
        
        for timestamp, holders in self.holder_data.items():
            report_lines.append(f"Date: {timestamp} - Total Holders: {len(set(holders))}")
        
        report = "\n".join(report_lines)
        logging.info("Report generated successfully.")
        return report

if __name__ == "__main__":
    TOKEN_ADDRESS = "0xYourTokenAddressHere"
    API_URL = "https://api.yourblockchainprovider.com"

    tracker = TokenHolderTracker(TOKEN_ADDRESS, API_URL)
    
    try:
        tracker.track_growth()  # Start tracking holders
    except KeyboardInterrupt:
        logging.info("Tracking interrupted by user.")
        print(tracker.generate_report())  # Generate report on exit
    except Exception as e:
        logging.error(f"Script terminated due to an unexpected error: {e}")
```

In this code:
- The program fetches the holder data for a specific token at regular intervals.
- It logs errors and successfully fetched data.
- The report generation function compiles the collected data into a readable format.
- Proper error handling is in place to ensure robustness.
