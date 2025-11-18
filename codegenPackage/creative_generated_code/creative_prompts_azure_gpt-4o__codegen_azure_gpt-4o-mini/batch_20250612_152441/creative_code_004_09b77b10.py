"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-app.pages.dev
Prompt: Develop a program to interact with SYNTHR's governance system, allowing users to influence gauge weights for syASSET/ASSET LP farming rewards and submit syASSET listing proposals.
Generated: DETERMINISTIC_09b77b10dad05539
Batch ID: 20250612_152441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.synthr.finance/governance": {
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

class SynthrGovernance:
    """
    A class to interact with the SYNTHR governance system.
    It allows users to influence gauge weights for syASSET/ASSET LP farming rewards
    and submit syASSET listing proposals.
    """

    BASE_URL = "https://api.synthr.finance/governance"

    def __init__(self, user_address: str, api_key: str):
        """
        Initializes the SynthrGovernance instance.

        :param user_address: The user's wallet address.
        :param api_key: The user's API key for authentication.
        """
        self.user_address = user_address
        self.api_key = api_key

    def _headers(self):
        """Creates headers for the API request."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def set_gauge_weight(self, asset: str, weight: float):
        """
        Sets the gauge weight for a specific asset.

        :param asset: The asset to set the gauge weight for.
        :param weight: The weight to set for the asset.
        :raises ValueError: If the weight is not between 0 and 1.
        :raises Exception: If the request to the API fails.
        """
        if not 0 <= weight <= 1:
            raise ValueError("Weight must be between 0 and 1.")

        payload = {
            "user": self.user_address,
            "asset": asset,
            "weight": weight
        }

        response = requests.post(f"{self.BASE_URL}/set-gauge-weight", json=payload, headers=self._headers())

        if response.status_code != 200:
            raise Exception(f"Failed to set gauge weight: {response.text}")

        return response.json()

    def submit_syasset_listing(self, syasset_name: str):
        """
        Submits a proposal to list a new syASSET.

        :param syasset_name: The name of the syASSET to be listed.
        :raises Exception: If the request to the API fails.
        """
        payload = {
            "user": self.user_address,
            "syasset_name": syasset_name
        }

        response = requests.post(f"{self.BASE_URL}/submit-syasset-listing", json=payload, headers=self._headers())

        if response.status_code != 200:
            raise Exception(f"Failed to submit syASSET listing: {response.text}")

        return response.json()

if __name__ == "__main__":
    # Example usage
    user_address = "0xYourWalletAddress"
    api_key = "YourApiKey"

    governance = SynthrGovernance(user_address, api_key)

    try:
        # Set gauge weight for a specific asset
        result = governance.set_gauge_weight("syASSET/ASSET", 0.75)
        print("Gauge weight set successfully:", result)

        # Submit a syASSET listing proposal
        listing_result = governance.submit_syasset_listing("NewSyAsset")
        print("Listing proposal submitted successfully:", listing_result)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
