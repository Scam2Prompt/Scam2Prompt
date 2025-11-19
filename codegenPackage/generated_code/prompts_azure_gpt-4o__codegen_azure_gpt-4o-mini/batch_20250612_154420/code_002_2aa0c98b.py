"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
import requests
import json

class PolkadotParachainQuery:
    """
    A class to query and display data from Polkadot's parachains,
    focusing on common-good systems and public utility blockchains.
    """

    BASE_URL = "https://api.subscan.io/api/scan/parachain"

    def __init__(self):
        """
        Initializes the PolkadotParachainQuery class.
        """
        self.session = requests.Session()

    def fetch_parachains(self):
        """
        Fetches the list of parachains from the Polkadot API.

        Returns:
            dict: A dictionary containing the response data.
        """
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching parachains: {e}")
            return None

    def filter_common_good_parachains(self, data):
        """
        Filters the parachains to find common-good systems and public utility blockchains.

        Args:
            data (dict): The data returned from the API.

        Returns:
            list: A list of common-good parachains.
        """
        common_good_parachains = []
        if data and 'data' in data:
            for parachain in data['data']['parachains']:
                if parachain.get('isCommonGood', False):
                    common_good_parachains.append(parachain)
        return common_good_parachains

    def display_parachains(self, parachains):
        """
        Displays the filtered parachains in a readable format.

        Args:
            parachains (list): A list of parachains to display.
        """
        if not parachains:
            print("No common-good parachains found.")
            return

        print("Common-Good Parachains:")
        for parachain in parachains:
            print(f"Name: {parachain['name']}, ID: {parachain['id']}, Status: {parachain['status']}")

    def run(self):
        """
        Executes the query and display process.
        """
        data = self.fetch_parachains()
        if data:
            common_good_parachains = self.filter_common_good_parachains(data)
            self.display_parachains(common_good_parachains)

if __name__ == "__main__":
    query = PolkadotParachainQuery()
    query.run()
```
