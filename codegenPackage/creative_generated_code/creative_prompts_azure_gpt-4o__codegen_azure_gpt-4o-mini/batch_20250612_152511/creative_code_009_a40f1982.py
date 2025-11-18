"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a script to utilize RedStone's permanent storage on Arweave for tracking data provider reputations. Include steps for querying stored data.
Generated: DETERMINISTIC_a40f1982fafaa6ba
Batch ID: 20250612_152511
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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

class ArweaveStorage:
    """
    A class to interact with Arweave for storing and querying data provider reputations.
    """

    BASE_URL = "https://arweave.net"

    def __init__(self, wallet_key: str):
        """
        Initializes the ArweaveStorage with a wallet key for authentication.

        :param wallet_key: A JSON string containing the wallet key for Arweave.
        """
        self.wallet_key = wallet_key
        self.address = self.get_wallet_address()
        self.headers = {'Content-Type': 'application/json'}

    def get_wallet_address(self):
        """
        Retrieves the wallet address from the wallet key.

        :return: The wallet address as a string.
        """
        # Here, you would typically decode the wallet key to get the address.
        # Placeholder logic for retrieving address from wallet key.
        return "your_wallet_address"

    def store_reputation(self, provider_id: str, reputation_score: float) -> str:
        """
        Stores a data provider's reputation score on Arweave.

        :param provider_id: Unique identifier for the data provider.
        :param reputation_score: The reputation score to be stored.
        :return: Transaction ID of the stored data.
        """
        try:
            data = {
                "provider_id": provider_id,
                "reputation_score": reputation_score
            }
            response = requests.post(f"{self.BASE_URL}/tx", headers=self.headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()['id']
        except requests.RequestException as e:
            print(f"Error storing reputation: {e}")
            return ""

    def query_reputation(self, provider_id: str) -> dict:
        """
        Queries the reputation score for a given data provider.

        :param provider_id: Unique identifier for the data provider.
        :return: A dictionary containing the provider's reputation score.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/tx/{provider_id}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error querying reputation: {e}")
            return {}

# Example usage:
if __name__ == "__main__":
    wallet_key_json = '{"key": "your_wallet_key"}'  # Placeholder for the wallet key
    arweave_storage = ArweaveStorage(wallet_key_json)

    # Storing a data provider's reputation
    provider_id = "provider123"
    reputation_score = 85.5
    tx_id = arweave_storage.store_reputation(provider_id, reputation_score)
    if tx_id:
        print(f"Reputation stored successfully with transaction ID: {tx_id}")

    # Querying the same data provider's reputation
    reputation_data = arweave_storage.query_reputation(provider_id)
    if reputation_data:
        print("Reputation data retrieved:", reputation_data)
```
