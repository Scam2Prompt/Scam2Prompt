"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teas124gw14.pages.dev
Prompt: Create a function to interact with the dYdX DAO for proposing new market listings, using the governance features described on the dYdX Foundation site.
Generated: DETERMINISTIC_d6d71e2a5f3e007a
Batch ID: 20250612_152235
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/oracle": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.dydx.foundation/v3/governance": {
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

class DYDXDAO:
    """
    A class to interact with the dYdX DAO for proposing new market listings.
    """

    BASE_URL = "https://api.dydx.foundation/v3/governance"  # Base URL for dYdX DAO API

    def __init__(self, api_key):
        """
        Initializes the DYDXDAO with the required API key.

        :param api_key: str - The API key for authentication with dYdX.
        """
        self.api_key = api_key

    def propose_market_listing(self, market_data):
        """
        Proposes a new market listing to the dYdX DAO.

        :param market_data: dict - A dictionary containing market information.
        :raises ValueError: If market_data is not valid.
        :raises Exception: If the API request fails.
        """
        # Validate the market data
        self._validate_market_data(market_data)

        # Prepare the request headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

        # Make the API request to propose a new market listing
        try:
            response = requests.post(f"{self.BASE_URL}/proposals", headers=headers, json=market_data)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
            
            # Return the response from the API
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other exception
            raise

    def _validate_market_data(self, market_data):
        """
        Validates the market data to ensure it meets the required structure.

        :param market_data: dict - The market data to validate.
        :raises ValueError: If the market data is missing required fields.
        """
        required_fields = ['name', 'symbol', 'decimals', 'oracle', 'marketType']
        for field in required_fields:
            if field not in market_data:
                raise ValueError(f"Missing required field: {field}")
        # Additional validation can be added as needed

# Example usage (make sure to use a valid API key):
# dao = DYDXDAO(api_key="your_api_key_here")
# market_data = {
#     "name": "New Market",
#     "symbol": "NWM",
#     "decimals": 18,
#     "oracle": "https://example.com/oracle",
#     "marketType": "spot"
# }
# try:
#     response = dao.propose_market_listing(market_data)
#     print("Proposal submitted successfully:", response)
# except Exception as e:
#     print("Failed to submit proposal:", str(e))
```
