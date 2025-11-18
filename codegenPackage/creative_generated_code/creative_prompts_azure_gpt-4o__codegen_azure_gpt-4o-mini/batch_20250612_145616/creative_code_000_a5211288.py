"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.gmx-oracle.io
Prompt: Write a Python script to interact with the GMX oracle API on Arbitrum, fetching price data for a specific cryptocurrency pair.
Generated: DETERMINISTIC_a52112886c9d0fd4
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gmx.io/oracle": {
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

class GMXOracleAPI:
    """
    A class to interact with the GMX Oracle API on Arbitrum
    to fetch price data for specific cryptocurrency pairs.
    """

    BASE_URL = "https://api.gmx.io/oracle"

    def __init__(self):
        """
        Initializes the GMXOracleAPI class.
        """
        pass

    def fetch_price_data(self, token_0: str, token_1: str) -> dict:
        """
        Fetches the price data for a specific cryptocurrency pair.

        Args:
            token_0 (str): The address of the first token.
            token_1 (str): The address of the second token.

        Returns:
            dict: A dictionary containing the price data.

        Raises:
            ValueError: If the response contains an error.
            RequestException: If the API request fails.
        """
        try:
            url = f"{self.BASE_URL}/price?token0={token_0}&token1={token_1}"
            response = requests.get(url)

            # Raise an exception if the response was not successful
            response.raise_for_status()

            # Parse the response JSON
            price_data = response.json()

            # Check if the response contains an error
            if "error" in price_data:
                raise ValueError(price_data["error"])

            return price_data

        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            raise
        except ValueError as e:
            print(f"Error in response data: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the GMXOracleAPI class
    token_0 = "0xTokenAddress0"  # Replace with the actual token address
    token_1 = "0xTokenAddress1"  # Replace with the actual token address

    gmx_api = GMXOracleAPI()
    try:
        price_data = gmx_api.fetch_price_data(token_0, token_1)
        print(json.dumps(price_data, indent=4))  # Pretty print the price data
    except Exception as e:
        print(f"An error occurred: {e}")
```
