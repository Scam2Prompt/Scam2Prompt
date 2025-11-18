"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-chainaware.pages.dev
Prompt: Write code to query the ChainAware.ai Transaction Monitoring Agent API for real-time tracking of wallet transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_f9328da8966b5368
Batch ID: 20250612_154207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainaware.ai/v1": {
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

class ChainAwareAPI:
    """
    A class to interact with the ChainAware Transaction Monitoring Agent API
    for tracking wallet transactions on the Ethereum blockchain.
    """

    BASE_URL = "https://api.chainaware.ai/v1"  # Base URL for the API
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your actual API key
    }

    def __init__(self, wallet_address):
        """
        Initializes the ChainAwareAPI with a specific wallet address.

        Args:
            wallet_address (str): The Ethereum wallet address to monitor.
        """
        self.wallet_address = wallet_address

    def get_transaction_history(self):
        """
        Queries the ChainAware API for the transaction history of the specified wallet address.

        Returns:
            dict: The transaction history if the request is successful, otherwise an error message.
        """
        url = f"{self.BASE_URL}/transactions/{self.wallet_address}"
        try:
            response = requests.get(url, headers=self.HEADERS)
            
            # Check if the response is successful
            response.raise_for_status()
            
            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": "HTTP error occurred", "details": str(http_err)}
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log any request errors
            return {"error": "Request error occurred", "details": str(req_err)}
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error occurred: {json_err}")  # Log JSON parsing errors
            return {"error": "JSON decode error", "details": str(json_err)}

# Example usage
if __name__ == "__main__":
    # Replace with your actual wallet address
    wallet_address = "0xYourWalletAddress"
    api_client = ChainAwareAPI(wallet_address)

    # Fetch and print the transaction history
    transaction_history = api_client.get_transaction_history()
    print(json.dumps(transaction_history, indent=4))
```

> Note: Replace `YOUR_API_KEY` and `0xYourWalletAddress` with your actual API key and Ethereum wallet address, respectively, before running the code.
