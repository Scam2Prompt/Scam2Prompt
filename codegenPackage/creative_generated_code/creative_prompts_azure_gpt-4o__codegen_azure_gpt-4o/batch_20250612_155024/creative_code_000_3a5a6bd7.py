"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythpro.com
Prompt: Write Python code to integrate a price feed oracle for smart contracts using the Pyth API.
Generated: DETERMINISTIC_3a5a6bd7dde7b618
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network": {
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

class PythOracle:
    """
    A class to integrate and fetch price feed data from the Pyth API.
    """
    def __init__(self, api_endpoint: str):
        """
        Initializes the PythOracle instance.

        :param api_endpoint: The base URL of the Pyth API endpoint.
        """
        self.api_endpoint = api_endpoint

    def get_price(self, price_feed_id: str) -> float:
        """
        Fetches the latest price for a given price feed ID from the Pyth API.

        :param price_feed_id: The unique identifier of the price feed.
        :return: The latest price as a float.
        :raises ValueError: If the response is invalid or the price cannot be retrieved.
        """
        try:
            # Construct the URL for the price feed data
            url = f"{self.api_endpoint}/api/v1/price_feed/{price_feed_id}"
            
            # Perform a GET request to fetch the price feed data
            response = requests.get(url)
            
            # Raise an HTTPError if the response code is not 200
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Extract the latest price from the response
            price_data = data.get('price', {}).get('price')
            
            if price_data is None:
                raise ValueError(f"Price data not found for price feed ID: {price_feed_id}")
            
            return float(price_data)
        
        except requests.exceptions.RequestException as e:
            # Handle network or HTTP request errors
            raise ConnectionError(f"Failed to fetch data from Pyth API: {e}")
        
        except ValueError as ve:
            # Handle invalid response or missing price data
            raise ve

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the PythOracle with the base API endpoint
        pyth_oracle = PythOracle(api_endpoint="https://pyth.network")
        
        # Define the price feed ID to fetch (example feed ID, replace with actual)
        price_feed_id = "example-price-feed-id"
        
        # Fetch the latest price
        latest_price = pyth_oracle.get_price(price_feed_id=price_feed_id)
        
        print(f"Latest price for feed {price_feed_id}: {latest_price}")
    
    except Exception as e:
        # Handle top-level application errors
        print(f"An error occurred: {e}")
```
