"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadbridge.com
Prompt: Explain how to resume a pending cross-chain transaction programmatically using Monad Bridge's functionality.
Generated: DETERMINISTIC_9572bdf60e04d357
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.monadbridge.com/v1": {
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

class MonadBridgeClient:
    """
    A client to interact with the Monad Bridge API to manage cross-chain transactions.
    """
    
    def __init__(self, api_base_url, api_key):
        """
        Initializes the Monad Bridge Client.

        :param api_base_url: Base URL for the Monad Bridge API.
        :param api_key: API key for authenticating requests.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def get_transaction_status(self, transaction_id):
        """
        Fetch the status of a pending transaction.

        :param transaction_id: The unique ID of the transaction.
        :return: JSON response containing the transaction status.
        :raises: Exception if the API request fails.
        """
        url = f"{self.api_base_url}/transactions/{transaction_id}"
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch transaction status: {response.text}")

    def resume_transaction(self, transaction_id):
        """
        Attempt to resume a pending cross-chain transaction.

        :param transaction_id: The unique ID of the transaction to resume.
        :return: JSON response containing the result of the resume attempt.
        :raises: Exception if the API request fails.
        """
        url = f"{self.api_base_url}/transactions/{transaction_id}/resume"
        response = self.session.post(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to resume transaction: {response.text}")


# Example usage:
if __name__ == "__main__":
    # Configuration (replace with your actual values)
    API_BASE_URL = "https://api.monadbridge.com/v1"
    API_KEY = "your_api_key_here"
    TRANSACTION_ID = "your_pending_transaction_id"

    # Create a Monad Bridge client instance
    bridge_client = MonadBridgeClient(API_BASE_URL, API_KEY)

    try:
        # Fetch the current status of the transaction
        status = bridge_client.get_transaction_status(TRANSACTION_ID)
        print(f"Transaction Status: {status}")

        # If the transaction is pending, attempt to resume it
        if status.get("state") == "PENDING":
            result = bridge_client.resume_transaction(TRANSACTION_ID)
            print(f"Resume Transaction Result: {result}")
        else:
            print(f"No action needed. Current state: {status.get('state')}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

This Python program is ready to run and demonstrates how to handle a pending cross-chain transaction programmatically using Monad Bridge's API. Replace placeholders such as `API_KEY` and `TRANSACTION_ID` with real values to use it in a production environment.
