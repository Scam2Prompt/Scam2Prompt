"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: Generate code for interacting with the Lightchain AI Testnet, including sending transactions and retrieving performance metrics.
Generated: DETERMINISTIC_d9eb2cb571c45bd6
Batch ID: 20250612_145615
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.lightchain.ai/api": {
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

class LightchainClient:
    """
    A client for interacting with the Lightchain AI Testnet.
    Provides methods to send transactions and retrieve performance metrics.
    """

    def __init__(self, base_url):
        """
        Initialize the LightchainClient with the base URL of the Lightchain AI Testnet.
        
        :param base_url: The base URL for the Lightchain AI Testnet API.
        """
        self.base_url = base_url

    def send_transaction(self, transaction_data):
        """
        Send a transaction to the Lightchain AI Testnet.
        
        :param transaction_data: A dictionary containing the transaction data.
        :return: The response from the API after sending the transaction.
        """
        url = f"{self.base_url}/send_transaction"
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(transaction_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

    def get_performance_metrics(self):
        """
        Retrieve performance metrics from the Lightchain AI Testnet.
        
        :return: A dictionary containing performance metrics.
        """
        url = f"{self.base_url}/performance_metrics"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return None

if __name__ == "__main__":
    # Example usage of LightchainClient
    base_url = "https://testnet.lightchain.ai/api"  # Replace with the actual API endpoint
    client = LightchainClient(base_url)

    # Sending a sample transaction
    transaction_data = {
        "from": "address1",
        "to": "address2",
        "amount": 100,
        "fee": 1,
        "message": "Test transaction"
    }
    transaction_response = client.send_transaction(transaction_data)
    print("Transaction Response:", transaction_response)

    # Retrieving performance metrics
    performance_metrics = client.get_performance_metrics()
    print("Performance Metrics:", performance_metrics)
```
