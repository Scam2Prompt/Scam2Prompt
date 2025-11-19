"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythweb.com
Prompt: Provide a code example for fetching price data from an oracle in a blockchain application.
Generated: DETERMINISTIC_9f61048422dbcc57
Batch ID: 20250612_162311
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-blockchain-oracle.com/api": {
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

class OraclePriceFetcher:
    """
    A class to fetch price data from a blockchain oracle.
    """

    def __init__(self, oracle_url: str):
        """
        Initialize the OraclePriceFetcher with the URL of the oracle.

        Args:
            oracle_url (str): The base URL of the blockchain oracle API.
        """
        self.oracle_url = oracle_url

    def fetch_price(self, asset_symbol: str) -> float:
        """
        Fetch the price of the specified asset from the blockchain oracle.

        Args:
            asset_symbol (str): The symbol of the asset (e.g., "BTC", "ETH").

        Returns:
            float: The price of the asset.

        Raises:
            ValueError: If the response does not contain valid price data.
            ConnectionError: If the request to the oracle fails.
        """
        try:
            # Construct the request URL
            url = f"{self.oracle_url}/price/{asset_symbol}"
            
            # Make the API request to the oracle
            response = requests.get(url, timeout=10)

            # Check the HTTP status code
            response.raise_for_status()

            # Parse the API response (assumed JSON format)
            data = response.json()

            # Validate and extract the price
            if 'price' in data and isinstance(data['price'], (int, float)):
                return float(data['price'])
            else:
                raise ValueError(f"Invalid price data received for asset {asset_symbol}: {data}")

        except requests.exceptions.RequestException as e:
            # Handle connection-related errors
            raise ConnectionError(f"Failed to connect to oracle: {e}") from e
        except ValueError as e:
            # Handle data parsing and validation errors
            raise e

if __name__ == "__main__":
    # Example usage
    try:
        # URL of the oracle API
        ORACLE_API_URL = "https://example-blockchain-oracle.com/api"

        # Create an instance of the OraclePriceFetcher
        price_fetcher = OraclePriceFetcher(oracle_url=ORACLE_API_URL)

        # Asset symbol to fetch price for
        asset = "BTC"

        # Fetch the price from the oracle
        price = price_fetcher.fetch_price(asset_symbol=asset)

        # Print the fetched price
        print(f"The price of {asset} is ${price:.2f}")
    except Exception as e:
        # Handle errors gracefully
        print(f"Error fetching price data: {e}")
```
