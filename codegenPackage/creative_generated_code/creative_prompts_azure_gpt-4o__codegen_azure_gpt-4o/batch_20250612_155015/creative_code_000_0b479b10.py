"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Write Python code to integrate a price feed oracle from Pyth Network into a smart contract for fetching real-time market data.
Generated: DETERMINISTIC_0b479b1096d32955
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network/api": {
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

class PythPriceFeed:
    """
    A class to fetch real-time market data from the Pyth Network price feed oracle.

    Attributes:
        base_url (str): The base endpoint for the Pyth API.
    """
    def __init__(self, base_url: str):
        """
        Initializes the PythPriceFeed instance.
        
        Args:
            base_url (str): The base URL for the Pyth Network API.
        """
        self.base_url = base_url

    def fetch_price(self, price_id: str) -> dict:
        """
        Fetches real-time price data for a given asset.

        Args:
            price_id (str): The unique identifier for the asset price in the Pyth Network.

        Returns:
            dict: Returns the latest price data in JSON format.

        Raises:
            ValueError: If the response from the Pyth API is invalid.
            requests.exceptions.RequestException: If an HTTP error occurs.
        """
        try:
            url = f"{self.base_url}/v1/price/{price_id}"
            response = requests.get(url)

            # Raise an error for bad HTTP responses
            response.raise_for_status()

            # Parse JSON response
            data = response.json()

            # Check for required fields in the response
            if 'price' not in data or 'confidence' not in data:
                raise ValueError("Invalid response format from Pyth API.")

            return data
        except requests.exceptions.RequestException as e:
            # Handle HTTP-related errors
            raise requests.exceptions.RequestException(
                f"Error fetching data from Pyth Network: {str(e)}"
            )
        except ValueError as e:
            # Handle invalid data error
            raise ValueError(f"Data error: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Instantiate the price feed with the Pyth Network base URL
    pyth_feed = PythPriceFeed(base_url="https://pyth.network/api")

    # Replace with the actual price ID of the asset you want to fetch
    price_id = "BTC/USD"

    try:
        # Fetch price data from the Pyth Network
        price_data = pyth_feed.fetch_price(price_id)

        # Print the fetched price data
        print("Fetched price data:", price_data)
    except Exception as e:
        # Handle errors gracefully
        print("Error:", e)
```

### Notes:
1. Replace `"https://pyth.network/api"` with the actual Pyth API base endpoint, if different.
2. Replace `"BTC/USD"` with the appropriate price ID for your use case.
3. Ensure that the Pyth Network API documentation is reviewed for any changes in endpoint structure or response format.
