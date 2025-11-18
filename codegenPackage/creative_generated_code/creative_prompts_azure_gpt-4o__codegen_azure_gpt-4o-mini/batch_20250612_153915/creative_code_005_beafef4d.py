"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Explain how to use the TON Foundation's tools to monitor network activity and generate code for retrieving transaction history.
Generated: DETERMINISTIC_beafef4dcacd1b17
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://tonapi.io/v1": {
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

class TonNetworkMonitor:
    """
    A class to monitor TON network activity and retrieve transaction history.
    """

    BASE_URL = "https://tonapi.io/v1"  # Base URL for TON API
    API_KEY = "YOUR_API_KEY"  # Replace with your actual TON API key

    def __init__(self):
        """
        Initialize the TonNetworkMonitor with the necessary headers.
        """
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.API_KEY
        }

    def get_transaction_history(self, address, limit=10):
        """
        Retrieve the transaction history for a given address.

        Parameters:
        address (str): The TON address to retrieve the transaction history for.
        limit (int): The number of transactions to retrieve (default: 10).

        Returns:
        list: A list of transactions for the provided address.
        """
        url = f"{self.BASE_URL}/address/{address}/transactions?limit={limit}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            transactions = response.json().get("transactions", [])
            return transactions
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            return []
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other error
            return []

    def monitor_network_activity(self):
        """
        Monitor network activity and log it to console.
        This is a placeholder method for potential future implementation.
        """
        # This method should include logic to monitor network activity.
        print("Monitoring network activity is currently not implemented.")

# Example usage
if __name__ == "__main__":
    # Replace with a valid TON address
    ton_address = "VALID_TON_ADDRESS"  
    ton_monitor = TonNetworkMonitor()

    # Retrieve transaction history for the specified address
    transaction_history = ton_monitor.get_transaction_history(ton_address, limit=5)

    # Print the transaction history
    print(json.dumps(transaction_history, indent=4))
```

**Note**: Ensure to replace `"YOUR_API_KEY"` and `"VALID_TON_ADDRESS"` with your actual TON API key and a valid TON address, respectively.
