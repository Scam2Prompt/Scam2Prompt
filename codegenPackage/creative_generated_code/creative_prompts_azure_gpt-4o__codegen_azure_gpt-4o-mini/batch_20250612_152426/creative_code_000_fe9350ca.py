"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indodax.id
Prompt: Write Python code to interact with the INDODAX API for retrieving the latest Bitcoin price and 24-hour trading volume.
Generated: DETERMINISTIC_fe9350cac8b6c036
Batch ID: 20250612_152426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://indodax.com/api": {
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

class IndodaxAPI:
    """
    A class to interact with the INDODAX API for cryptocurrency data.
    """

    BASE_URL = "https://indodax.com/api"

    def __init__(self):
        """
        Initializes the IndodaxAPI class.
        """
        pass

    def get_bitcoin_data(self):
        """
        Retrieves the latest Bitcoin price and 24-hour trading volume from INDODAX.

        Returns:
            dict: A dictionary containing the latest price and trading volume,
                  or an error message if the request fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/btc_idr/ticker")

            # Check if the response was successful
            response.raise_for_status()

            data = response.json()

            # Extract the relevant information
            bitcoin_data = {
                "last_price": data['tick']['last'],
                "24h_volume": data['tick']['vol_btc']
            }

            return bitcoin_data

        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return {"error": str(e)}
        except KeyError as e:
            # Handle unexpected response format
            return {"error": "Unexpected response format", "details": str(e)}

# Example usage
if __name__ == "__main__":
    indodax_api = IndodaxAPI()
    data = indodax_api.get_bitcoin_data()

    if "error" in data:
        print(f"Error fetching data: {data['error']}")
    else:
        print(f"Latest Bitcoin Price: {data['last_price']} IDR")
        print(f"24-Hour Trading Volume: {data['24h_volume']} BTC")
```
