"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Write a Python script to interact with the MDEX API for conducting cross-chain transactions between HECO and BSC.
Generated: DETERMINISTIC_102e2dd92b1cb08b
Batch ID: 20250612_140436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com": {
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

class MDEXAPI:
    """
    A class to interact with the MDEX API for cross-chain transactions
    between HECO and BSC.
    """

    BASE_URL = "https://api.mdex.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def _get_headers(self):
        """
        Create headers for API requests.
        """
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_supported_chains(self):
        """
        Fetch the list of supported chains for cross-chain transactions.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/chains", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching supported chains: {e}")
            return None

    def initiate_cross_chain_transaction(self, from_chain, to_chain, amount, token):
        """
        Initiate a cross-chain transaction.

        Parameters:
        from_chain (str): The chain to send tokens from (e.g., 'HECO').
        to_chain (str): The chain to send tokens to (e.g., 'BSC').
        amount (float): The amount of tokens to send.
        token (str): The token to be transferred.

        Returns:
        dict: Response from the API or None if an error occurred.
        """
        payload = {
            'from_chain': from_chain,
            'to_chain': to_chain,
            'amount': amount,
            'token': token
        }

        try:
            response = requests.post(f"{self.BASE_URL}/cross-chain/transaction", 
                                     headers=self._get_headers(), 
                                     data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error initiating transaction: {e}")
            return None

    def get_transaction_status(self, transaction_id):
        """
        Fetch the status of a transaction.

        Parameters:
        transaction_id (str): The ID of the transaction to check.

        Returns:
        dict: The transaction status or None if an error occurred.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/transactions/{transaction_id}", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching transaction status: {e}")
            return None


if __name__ == "__main__":
    # Example usage of the MDEXAPI class
    api_key = "YOUR_API_KEY"  # Replace with your actual MDEX API key
    mdex_api = MDEXAPI(api_key)

    # Fetch supported chains
    chains = mdex_api.get_supported_chains()
    print("Supported Chains:", chains)

    # Initiate a cross-chain transaction
    transaction_response = mdex_api.initiate_cross_chain_transaction("HECO", "BSC", 10.0, "TOKEN_SYMBOL")
    print("Transaction Response:", transaction_response)

    # Check transaction status if a transaction was initiated
    if transaction_response and 'transaction_id' in transaction_response:
        transaction_status = mdex_api.get_transaction_status(transaction_response['transaction_id'])
        print("Transaction Status:", transaction_status)
```
