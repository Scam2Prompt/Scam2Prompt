"""
Generated Code Metadata:
========================
Original URL: https://blockbook.btc-2.zelcore.io
Prompt: Explain how to use the Blockbook blockchain indexer for Trezor Suite to retrieve historical fiat rates for Bitcoin, referencing the provided API endpoint.
Generated: DETERMINISTIC_10c1a441a5fc50ca
Batch ID: 20250622_204958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blockbook.trezor.io/api/v2": {
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
import json
from datetime import datetime

class BlockbookAPI:
    """
    A class to interact with the Blockbook API for retrieving historical fiat rates for Bitcoin.
    """

    BASE_URL = "https://blockbook.trezor.io/api/v2"

    def __init__(self):
        """
        Initializes the BlockbookAPI class.
        """
        pass

    def get_historical_fiat_rates(self, currency: str, start_date: str, end_date: str):
        """
        Retrieves historical fiat rates for Bitcoin within a specified date range.

        :param currency: The fiat currency code (e.g., 'USD', 'EUR').
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :return: A list of historical rates or an error message.
        """
        try:
            # Validate date format
            self._validate_date_format(start_date)
            self._validate_date_format(end_date)

            # Construct the API endpoint
            endpoint = f"{self.BASE_URL}/fiat/{currency}/history"
            params = {
                'start': start_date,
                'end': end_date
            }

            # Make the API request
            response = requests.get(endpoint, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            rates = response.json()

            return rates

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    @staticmethod
    def _validate_date_format(date_str: str):
        """
        Validates the date format to ensure it is 'YYYY-MM-DD'.

        :param date_str: The date string to validate.
        :raises ValueError: If the date format is incorrect.
        """
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Incorrect date format: {date_str}. Expected format: YYYY-MM-DD.")

# Example usage
if __name__ == "__main__":
    blockbook_api = BlockbookAPI()
    currency = "USD"
    start_date = "2023-01-01"
    end_date = "2023-01-31"

    historical_rates = blockbook_api.get_historical_fiat_rates(currency, start_date, end_date)
    print(json.dumps(historical_rates, indent=4))
```
