"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Generate code to query validator status and performance metrics on a blockchain network, using principles similar to those described by J•Node.
Generated: DETERMINISTIC_686ac25179cb76c9
Batch ID: 20250612_153954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:26657": {
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

class BlockchainValidatorClient:
    """
    Client for querying validator status and performance metrics on a blockchain network.
    """

    def __init__(self, node_url: str):
        """
        Initialize the client with the node URL.

        Args:
        - node_url (str): The URL of the blockchain node.
        """
        self.node_url = node_url

    def get_validator_status(self, validator_address: str) -> dict:
        """
        Query the validator status.

        Args:
        - validator_address (str): The address of the validator.

        Returns:
        - dict: The validator status.

        Raises:
        - requests.RequestException: If the request fails.
        """
        try:
            response = requests.get(f"{self.node_url}/validators/{validator_address}/status")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

    def get_performance_metrics(self, validator_address: str) -> dict:
        """
        Query the performance metrics for a validator.

        Args:
        - validator_address (str): The address of the validator.

        Returns:
        - dict: The performance metrics.

        Raises:
        - requests.RequestException: If the request fails.
        """
        try:
            response = requests.get(f"{self.node_url}/validators/{validator_address}/metrics")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

    def get_all_validator_status(self) -> dict:
        """
        Query the status of all validators.

        Returns:
        - dict: The status of all validators.

        Raises:
        - requests.RequestException: If the request fails.
        """
        try:
            response = requests.get(f"{self.node_url}/validators")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

def main():
    node_url = "http://localhost:26657"  # replace with your node URL
    client = BlockchainValidatorClient(node_url)

    validator_address = "cosmosvaloper1..."  # replace with your validator address

    validator_status = client.get_validator_status(validator_address)
    print("Validator Status:")
    print(json.dumps(validator_status, indent=4))

    performance_metrics = client.get_performance_metrics(validator_address)
    print("\nPerformance Metrics:")
    print(json.dumps(performance_metrics, indent=4))

    all_validator_status = client.get_all_validator_status()
    print("\nAll Validator Status:")
    print(json.dumps(all_validator_status, indent=4))

if __name__ == "__main__":
    main()
```
