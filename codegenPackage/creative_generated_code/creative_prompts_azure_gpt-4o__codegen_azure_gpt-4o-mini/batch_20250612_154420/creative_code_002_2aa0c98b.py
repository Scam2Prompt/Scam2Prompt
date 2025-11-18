"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Generate code to query and display data from Polkadot's parachains, emphasizing common-good system and public utility blockchains.
Generated: DETERMINISTIC_2aa0c98be976808c
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.subscan.io/api/scan/parachain": {
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

class ParachainDataFetcher:
    """
    A class to fetch and display data from Polkadot's parachains, focusing on common-good systems
    and public utility blockchains.
    """

    BASE_URL = "https://api.subscan.io/api/scan/parachain"

    def __init__(self):
        """
        Initialize the ParachainDataFetcher.
        """
        self.session = requests.Session()

    def fetch_parachain_data(self):
        """
        Fetch data from the Polkadot parachains API.

        Returns:
            dict: The JSON response containing parachain data, if successful.
            None: If an error occurs while fetching the data.
        """
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        except json.JSONDecodeError:
            print("Error decoding JSON response.")
        return None

    def filter_common_good_parachains(self, data):
        """
        Filter parachains to get only those that are common-good systems and public utilities.

        Args:
            data (dict): The data containing parachains information.

        Returns:
            list: A list of common-good parachains.
        """
        common_good_parachains = []
        if "data" in data and "parachains" in data["data"]:
            for parachain in data["data"]["parachains"]:
                # Check for common-good system criteria
                if parachain.get("is_common_good", False):
                    common_good_parachains.append(parachain)
        return common_good_parachains

    def display_parachains(self, parachains):
        """
        Display the filtered parachains.

        Args:
            parachains (list): A list of parachains to display.
        """
        if not parachains:
            print("No common-good parachains found.")
            return
        
        for parachain in parachains:
            print(f"Parachain Name: {parachain['name']}, ID: {parachain['id']}, Status: {parachain['status']}")

    def run(self):
        """
        Execute the fetching, filtering, and displaying of parachain data.
        """
        data = self.fetch_parachain_data()
        if data:
            common_good_parachains = self.filter_common_good_parachains(data)
            self.display_parachains(common_good_parachains)

if __name__ == "__main__":
    fetcher = ParachainDataFetcher()
    fetcher.run()
```
