"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethping.com
Prompt: Generate code to check Ethereum node connectivity, inspired by services like ethping.com.
Generated: DETERMINISTIC_ad7f9cf561602467
Batch ID: 20250612_152600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:8545": {
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
import json
import requests
from requests.exceptions import RequestException
import time

class EthereumNodeChecker:
    def __init__(self, node_url, timeout=5):
        """
        Initializes the EthereumNodeChecker.

        :param node_url: The URL of the Ethereum node to check.
        :param timeout: The timeout for requests to the node (in seconds).
        """
        self.node_url = node_url
        self.timeout = timeout

    def check_connectivity(self):
        """
        Checks the connectivity to the Ethereum node by sending a JSON-RPC request.
        
        :return: True if the node is reachable, False otherwise.
        """
        try:
            # Prepare the JSON-RPC payload
            payload = {
                "jsonrpc": "2.0",
                "method": "eth_blockNumber",
                "params": [],
                "id": 1
            }
            # Send the request to the node
            response = requests.post(
                self.node_url,
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the response
            response_data = response.json()
            if 'result' in response_data:
                return True  # Node is reachable
            else:
                print("Invalid response:", response_data)
                return False
            
        except RequestException as e:
            print(f"Request failed: {e}")
            return False
        except json.JSONDecodeError:
            print("Failed to decode JSON response.")
            return False

if __name__ == "__main__":
    # Node URL can be configured here
    node_url = "http://127.0.0.1:8545"  # Replace with your Ethereum node URL

    # Create an instance of the EthereumNodeChecker
    checker = EthereumNodeChecker(node_url)

    # Check connectivity
    print("Checking Ethereum node connectivity...")
    is_connected = checker.check_connectivity()

    # Print the result
    if is_connected:
        print("Ethereum node is reachable.")
    else:
        print("Failed to connect to Ethereum node.")
```
