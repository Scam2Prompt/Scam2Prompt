"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Generate a script to connect to the Polkadot network and retrieve information about parachains operating in Africa.
Generated: DETERMINISTIC_2eeb7bffd862d4cd
Batch ID: 20250612_151408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.polkadot.io": {
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

class ParachainInfoRetriever:
    """Class to retrieve information about parachains on the Polkadot network."""

    def __init__(self, polkadot_api_url):
        """
        Initialize the retriever with the Polkadot API URL.

        Args:
            polkadot_api_url (str): The endpoint URL of the Polkadot JSON-RPC API.
        """
        self.api_url = polkadot_api_url

    def fetch_parachains(self):
        """
        Fetch information about parachains operating in Africa.

        Returns:
            dict: A dictionary containing parachain information if successful.
            None: If the request fails.
        """
        # Define the JSON-RPC payload to get parachain information
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "parachains_parachains"
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Filter for parachains based on region (Africa)
            # Assuming the response contains `parachains` key with details
            return self.filter_african_parachains(data.get('result', {}).get('parachains', []))
        
        except requests.RequestException as e:
            print(f"Error fetching parachains: {e}")
            return None
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            return None

    def filter_african_parachains(self, parachains):
        """
        Filter parachains based on geographical location (Africa).

        Args:
            parachains (list): List of parachain information retrieved.

        Returns:
            list: A filtered list of parachains operating in Africa.
        """
        # Placeholder for filtering logic, adjust criteria as needed.
        african_parachains = [
            pc for pc in parachains if 'Africa' in pc.get('location', '')
        ]
        return african_parachains

if __name__ == "__main__":
    # Define the Polkadot API URL (replace with the actual endpoint)
    POLKADOT_API_URL = "https://rpc.polkadot.io"

    # Create an instance of the retriever
    retriever = ParachainInfoRetriever(POLKADOT_API_URL)

    # Fetch and display parachains
    parachains = retriever.fetch_parachains()
    if parachains is not None:
        print("Parachains operating in Africa:")
        for pc in parachains:
            print(pc)
    else:
        print("Failed to retrieve parachains.")
```
