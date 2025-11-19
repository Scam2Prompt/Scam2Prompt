"""
Generated Code Metadata:
========================
Original URL: https://solscanai.com
Prompt: Generate a Python script that utilizes Solana AI Analytics to fetch the latest blocks from the Solana blockchain.
Generated: DETERMINISTIC_6ef92e468125fc1c
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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

class SolanaBlockchain:
    """
    A class to interact with the Solana blockchain and fetch the latest blocks.
    """

    BASE_URL = "https://api.mainnet-beta.solana.com"

    def __init__(self):
        """
        Initializes the SolanaBlockchain instance.
        """
        self.session = requests.Session()

    def fetch_latest_blocks(self, limit=5):
        """
        Fetches the latest blocks from the Solana blockchain.

        Args:
            limit (int): The number of latest blocks to fetch. Default is 5.

        Returns:
            list: A list of the latest blocks.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        # Prepare the request payload
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getConfirmedBlocks",
            "params": [0, limit - 1]  # Fetch from the latest block
        }

        try:
            # Make the API request
            response = self.session.post(self.BASE_URL, json=payload)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            data = response.json()

            # Check for errors in the response
            if 'error' in data:
                raise Exception(f"API Error: {data['error']}")

            return data['result']

        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")
        except json.JSONDecodeError:
            raise Exception("Failed to decode JSON response")

if __name__ == "__main__":
    # Create an instance of the SolanaBlockchain class
    solana = SolanaBlockchain()

    try:
        # Fetch the latest blocks
        latest_blocks = solana.fetch_latest_blocks(limit=5)
        print("Latest Blocks:", latest_blocks)
    except Exception as e:
        print(f"Error: {e}")
```
