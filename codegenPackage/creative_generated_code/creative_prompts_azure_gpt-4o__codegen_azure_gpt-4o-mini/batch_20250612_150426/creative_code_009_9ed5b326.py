"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Create a Python script to query the PulseChain blockchain for historical price data of $HEX tokens using an API or library.
Generated: DETERMINISTIC_9ed5b326513121ff
Batch ID: 20250612_150426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pulsechain.com/v1/": {
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
from datetime import datetime, timedelta

class PulseChainAPI:
    BASE_URL = "https://api.pulsechain.com/v1/"  # Base URL for the PulseChain API

    def __init__(self):
        pass

    def fetch_hex_price_history(self, start_date: str, end_date: str, interval: str = 'daily'):
        """
        Fetch historical price data for $HEX tokens from the PulseChain blockchain.

        :param start_date: Start date for the price data in 'YYYY-MM-DD' format.
        :param end_date: End date for the price data in 'YYYY-MM-DD' format.
        :param interval: Time interval for price data; e.g., 'daily', 'hourly'.
        :return: DataFrame containing the price history.
        """
        try:
            response = requests.get(f"{self.BASE_URL}hex/price-history", params={
                'start': start_date,
                'end': end_date,
                'interval': interval
            })

            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Check if data is in expected format
            if 'prices' not in data:
                raise ValueError("Invalid response format")

            # Convert data into a DataFrame
            price_data = pd.DataFrame(data['prices'])
            price_data['date'] = pd.to_datetime(price_data['date'])  # Ensure date is in datetime format
            return price_data

        except requests.RequestException as req_err:
            print(f"Request error: {req_err}")
            return None
        except ValueError as val_err:
            print(f"Value error: {val_err}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Replace these dates with the desired range
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    api = PulseChainAPI()
    hex_price_history = api.fetch_hex_price_history(start_date, end_date)

    if hex_price_history is not None:
        print("Historical $HEX Price Data:")
        print(hex_price_history)
    else:
        print("Failed to retrieve historical price data.")

if __name__ == "__main__":
    main()
```
