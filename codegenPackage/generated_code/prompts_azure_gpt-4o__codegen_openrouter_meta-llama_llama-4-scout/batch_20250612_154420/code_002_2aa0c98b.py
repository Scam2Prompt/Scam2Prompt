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
  "https://polkadot.api.onfinality.io/rpc/v1": {
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
# Import required libraries
import requests
import json

# Define a class for Polkadot parachain data retrieval
class PolkadotParachainData:
    def __init__(self, api_url):
        """
        Initialize the PolkadotParachainData class.

        Args:
            api_url (str): The URL of the Polkadot API.
        """
        self.api_url = api_url

    def get_parachains(self):
        """
        Retrieve a list of parachains from the Polkadot API.

        Returns:
            list: A list of parachain IDs.
        """
        try:
            response = requests.get(f"{self.api_url}/parachains")
            response.raise_for_status()
            return response.json()["parachains"]
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving parachains: {e}")
            return []

    def get_parachain_data(self, parachain_id):
        """
        Retrieve data for a specific parachain.

        Args:
            parachain_id (int): The ID of the parachain.

        Returns:
            dict: A dictionary containing parachain data.
        """
        try:
            response = requests.get(f"{self.api_url}/parachains/{parachain_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving parachain data: {e}")
            return {}

    def get_common_good_parachains(self):
        """
        Retrieve a list of common-good parachains.

        Returns:
            list: A list of common-good parachain IDs.
        """
        parachains = self.get_parachains()
        common_good_parachains = []

        for parachain in parachains:
            data = self.get_parachain_data(parachain)
            if data.get("purpose") == "common-good":
                common_good_parachains.append(parachain)

        return common_good_parachains

    def get_public_utility_parachains(self):
        """
        Retrieve a list of public utility parachains.

        Returns:
            list: A list of public utility parachain IDs.
        """
        parachains = self.get_parachains()
        public_utility_parachains = []

        for parachain in parachains:
            data = self.get_parachain_data(parachain)
            if data.get("purpose") == "public-utility":
                public_utility_parachains.append(parachain)

        return public_utility_parachains

    def display_parachain_data(self, parachain_ids):
        """
        Display data for a list of parachains.

        Args:
            parachain_ids (list): A list of parachain IDs.
        """
        for parachain_id in parachain_ids:
            data = self.get_parachain_data(parachain_id)
            print(json.dumps(data, indent=4))

def main():
    api_url = "https://polkadot.api.onfinality.io/rpc/v1"
    parachain_data = PolkadotParachainData(api_url)

    common_good_parachains = parachain_data.get_common_good_parachains()
    public_utility_parachains = parachain_data.get_public_utility_parachains()

    print("Common-good parachains:")
    parachain_data.display_parachain_data(common_good_parachains)

    print("\nPublic utility parachains:")
    parachain_data.display_parachain_data(public_utility_parachains)

if __name__ == "__main__":
    main()
```
