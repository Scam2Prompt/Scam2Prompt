"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astredex.com
Prompt: Generate a code snippet that demonstrates how to access Aster's trading volume and user statistics via their API.
Generated: DETERMINISTIC_f1245edec70bec6a
Batch ID: 20250612_163133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.com/v1": {
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

class AsterAPIClient:
    """
    A client to interact with the Aster trading API.
    """

    BASE_URL = "https://api.aster.com/v1"  # Base URL for Aster API

    def __init__(self, api_key):
        """
        Initialize the AsterAPIClient with the provided API key.
        
        :param api_key: str: API key for authentication
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Construct headers for the API request.

        :return: dict: Headers including authentication
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_trading_volume(self):
        """
        Retrieve the trading volume from the Aster API.

        :return: dict: Trading volume data
        :raises Exception: If the API request fails
        """
        try:
            response = requests.get(f"{self.BASE_URL}/trading/volume", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch trading volume: {e}")

    def get_user_statistics(self):
        """
        Retrieve user statistics from the Aster API.

        :return: dict: User statistics data
        :raises Exception: If the API request fails
        """
        try:
            response = requests.get(f"{self.BASE_URL}/users/statistics", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch user statistics: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Aster API key
    client = AsterAPIClient(api_key='your_api_key_here')
    
    try:
        trading_volume = client.get_trading_volume()
        print("Trading Volume:", trading_volume)

        user_statistics = client.get_user_statistics()
        print("User Statistics:", user_statistics)
    except Exception as e:
        print("Error:", e)
```
