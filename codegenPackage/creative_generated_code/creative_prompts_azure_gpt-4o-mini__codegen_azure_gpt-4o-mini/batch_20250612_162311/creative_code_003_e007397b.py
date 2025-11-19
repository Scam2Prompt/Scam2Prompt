"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Generate a sample API call to retrieve market data from Pyth Network for use in a blockchain application.
Generated: DETERMINISTIC_e007397b1bb5d9e4
Batch ID: 20250612_162311
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network": {
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

class PythNetworkAPI:
    """
    A class to interact with the Pyth Network API for retrieving market data.
    """

    BASE_URL = "https://api.pyth.network"
    
    def __init__(self):
        """
        Initializes the PythNetworkAPI with the base URL.
        """
        pass

    def get_market_data(self, market_id):
        """
        Retrieves market data for a specified market ID.

        Args:
            market_id (str): The ID of the market to retrieve data for.

        Returns:
            dict: A dictionary containing the market data if the request is successful.

        Raises:
            ValueError: If the market_id is invalid.
            ConnectionError: If the request fails to connect to the API.
            Exception: For other unexpected errors.
        """
        if not market_id:
            raise ValueError("Market ID cannot be empty.")
        
        url = f"{self.BASE_URL}/v1/price/{market_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return response data in JSON format
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")  # Log connection issues
            raise ConnectionError("Failed to connect to the Pyth Network API.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other exceptions
            raise

# Example usage:
if __name__ == "__main__":
    # Create an instance of the API client
    pyth_api = PythNetworkAPI()
    
    # Specify a market ID to retrieve data for (replace with a valid market ID)
    market_id = "example_market_id"
    
    try:
        # Fetch market data
        market_data = pyth_api.get_market_data(market_id)
        print("Market Data:", market_data)
    except Exception as e:
        print(f"Failed to retrieve market data: {e}")
```
