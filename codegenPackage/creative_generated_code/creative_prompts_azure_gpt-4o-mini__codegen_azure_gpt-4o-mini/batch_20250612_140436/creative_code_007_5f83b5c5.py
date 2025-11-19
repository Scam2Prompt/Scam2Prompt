"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Create a guide for beginners on how to perform futures trading on MDEX, detailing the order types and margin modes available.
Generated: DETERMINISTIC_5f83b5c57adc3b6a
Batch ID: 20250612_140436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com/v1": {
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

class MDEXFuturesTradingGuide:
    """
    A guide for beginners on how to perform futures trading on MDEX.
    This class provides information about order types and margin modes available on MDEX.
    """

    BASE_URL = "https://api.mdex.com/v1"  # MDEX API base URL

    def __init__(self):
        self.order_types = ["LIMIT", "MARKET", "STOP", "STOP_LIMIT"]
        self.margin_modes = ["CROSSED", "ISOLATED"]

    def get_order_types(self):
        """
        Returns the order types available for futures trading on MDEX.

        Returns:
            list: A list of available order types.
        """
        return self.order_types

    def get_margin_modes(self):
        """
        Returns the margin modes available for futures trading on MDEX.

        Returns:
            list: A list of available margin modes.
        """
        return self.margin_modes

    def fetch_futures_info(self):
        """
        Fetches additional futures trading information from MDEX API.
        
        Returns:
            dict: A dictionary containing futures trading information.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/futures/info")
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.RequestException as e:
            print(f"Error fetching futures info: {e}")
            return None  # Return None in case of an error

    def display_guide(self):
        """
        Displays the trading guide including order types, margin modes, and additional info.
        """
        print("MDEX Futures Trading Guide")
        print("===========================")
        print("Order Types:")
        for order_type in self.get_order_types():
            print(f"- {order_type}")

        print("\nMargin Modes:")
        for margin_mode in self.get_margin_modes():
            print(f"- {margin_mode}")

        futures_info = self.fetch_futures_info()
        if futures_info:
            print("\nAdditional Futures Trading Information:")
            print(futures_info)

if __name__ == "__main__":
    trading_guide = MDEXFuturesTradingGuide()
    trading_guide.display_guide()
```
