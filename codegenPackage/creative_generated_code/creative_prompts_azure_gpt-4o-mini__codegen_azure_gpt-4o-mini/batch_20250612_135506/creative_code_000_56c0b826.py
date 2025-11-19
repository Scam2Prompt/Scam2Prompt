"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin2.biz
Prompt: Write a Python script that interacts with the Kraken exchange API to fetch the latest Bitcoin prices and trading pairs.
Generated: DETERMINISTIC_56c0b826cc99b80d
Batch ID: 20250612_135506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.kraken.com": {
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

class KrakenAPI:
    """A class to interact with the Kraken cryptocurrency exchange API."""

    BASE_URL = 'https://api.kraken.com'
    
    def __init__(self):
        """Initialize the KrakenAPI instance."""
        self.session = requests.Session()  # Create a requests session for persistent connections

    def get_ticker_info(self, pair: str) -> dict:
        """
        Fetch the latest ticker information for a trading pair.

        Args:
            pair (str): The trading pair to fetch, e.g., 'XXBTZUSD' for Bitcoin to USD.

        Returns:
            dict: The latest ticker information for the specified trading pair.

        Raises:
            ValueError: If the response from the API is not valid.
            Exception: For other API errors or connection issues.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/0/public/Ticker?pair={pair}")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()  # Parse JSON response

            if 'error' in data and data['error']:
                raise ValueError(f"API Error: {data['error']}")

            return data['result'][pair]  # Return the result for the specified trading pair

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON response.")

def main():
    """Main function to fetch and display Bitcoin prices and trading pairs."""
    kraken = KrakenAPI()
    bitcoin_pairs = ['XXBTZUSD', 'XXBTZEUR', 'XXBTZJPY']  # Define Bitcoin trading pairs

    try:
        for pair in bitcoin_pairs:
            ticker_info = kraken.get_ticker_info(pair)
            print(f"Latest price for {pair}: {ticker_info['c'][0]}")  # Display the current price
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
```
