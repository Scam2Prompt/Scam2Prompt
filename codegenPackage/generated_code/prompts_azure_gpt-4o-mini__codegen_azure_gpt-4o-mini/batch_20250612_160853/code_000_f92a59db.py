"""
Generated Code Metadata:
========================
Original URL: https://bafybeia7hhfaanym5gb2qaa3v5kkaps2vnowe2tqf5r2pnfax6cxobgow4.ipfs.dweb.link
Prompt: Generate a code snippet that interacts with the Oasis Network API to explore decentralized applications (dApps) mentioned on the website.
Generated: DETERMINISTIC_f92a59db52585ea3
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.oasis.dev/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

class OasisNetworkAPI:
    """
    A class to interact with the Oasis Network API to explore decentralized applications (dApps).
    """

    BASE_URL = "https://api.oasis.dev/v1"  # Base URL for the Oasis Network API

    def __init__(self):
        """
        Initializes the OasisNetworkAPI class.
        """
        pass

    def get_dapps(self):
        """
        Fetches a list of decentralized applications (dApps) from the Oasis Network API.

        Returns:
            list: A list of dApps if the request is successful.
            None: If the request fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/dapps")
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            # Parse the JSON response
            dapps = response.json()
            return dapps.get('data', [])  # Return the dApps data or an empty list if not found

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log other request errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log unexpected errors

        return None  # Return None if an error occurred

if __name__ == "__main__":
    """
    Main execution point for the script.
    """
    oasis_api = OasisNetworkAPI()  # Create an instance of the API class
    dapps = oasis_api.get_dapps()  # Fetch the dApps

    if dapps is not None:
        print("Decentralized Applications (dApps) on Oasis Network:")
        for dapp in dapps:
            print(f"- {dapp.get('name', 'Unnamed dApp')}")  # Print the name of each dApp
    else:
        print("Failed to retrieve dApps.")
```
