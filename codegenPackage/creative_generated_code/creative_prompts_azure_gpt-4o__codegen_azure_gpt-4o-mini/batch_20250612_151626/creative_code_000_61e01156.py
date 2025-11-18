"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: Write a Python script to interact with the Venus Protocol API on the BNB Chain to fetch current interest rates for lending and borrowing assets.
Generated: DETERMINISTIC_61e01156396c3391
Batch ID: 20250612_151626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io": {
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
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VenusProtocolAPI:
    """Class to interact with the Venus Protocol API on the BNB Chain."""

    BASE_URL = "https://api.venus.io"  # Base URL for Venus Protocol API

    def __init__(self):
        """Initialize the VenusProtocolAPI class."""
        self.session = requests.Session()

    def get_interest_rates(self):
        """Fetch current interest rates for lending and borrowing assets."""
        endpoint = f"{self.BASE_URL}/markets"
        
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            interest_rates = response.json()  # Parse JSON response
            return self.process_interest_rates(interest_rates)

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Error occurred while making a request: {req_err}")  # Log other request errors
        except Exception as err:
            logging.error(f"An unexpected error occurred: {err}")  # Log unexpected errors

        return None  # Return None if there was an error

    def process_interest_rates(self, data):
        """Process and extract relevant interest rate information from API response."""
        results = []
        # Loop through each market to extract relevant information
        for market in data.get("markets", []):
            asset_info = {
                "asset": market.get("symbol"),
                "supply_rate": market.get("supplyRate"),
                "borrow_rate": market.get("borrowRate"),
            }
            results.append(asset_info)

        return results  # Return processed interest rates

if __name__ == "__main__":
    """Main execution block."""
    api = VenusProtocolAPI()
    interest_rates = api.get_interest_rates()

    if interest_rates:
        logging.info("Current Interest Rates for Lending and Borrowing Assets:")
        for rate in interest_rates:
            logging.info(f"Asset: {rate['asset']}, Supply Rate: {rate['supply_rate']}, Borrow Rate: {rate['borrow_rate']}")
    else:
        logging.warning("Failed to fetch interest rates.")
```
