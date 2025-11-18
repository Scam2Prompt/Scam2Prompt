"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://j-node.net
Prompt: Generate code to query validator status and performance metrics on a blockchain network, using principles similar to those described by J•Node.
Generated: DETERMINISTIC_686ac25179cb76c9
Batch ID: 20250612_153954
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchain.network": {
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

class BlockchainValidatorMonitor:
    """
    A class to monitor and query validator status and performance metrics 
    on a blockchain network.

    Attributes:
        base_url (str): The base URL of the blockchain API.
    """

    def __init__(self, base_url):
        """
        Initialize the BlockchainValidatorMonitor.

        Args:
            base_url (str): The base URL of the blockchain API.
        """
        self.base_url = base_url

    def get_validator_status(self, validator_id):
        """
        Query the status of a specific validator.

        Args:
            validator_id (str): The ID of the validator to query.

        Returns:
            dict: A dictionary containing the validator's status or error information.
        """
        endpoint = f"{self.base_url}/validators/{validator_id}/status"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_validator_performance(self, validator_id):
        """
        Query the performance metrics of a specific validator.

        Args:
            validator_id (str): The ID of the validator to query.

        Returns:
            dict: A dictionary containing the validator's performance metrics or error information.
        """
        endpoint = f"{self.base_url}/validators/{validator_id}/performance"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_all_validators_status(self):
        """
        Query the status of all validators in the network.

        Returns:
            dict: A dictionary containing the statuses of all validators or error information.
        """
        endpoint = f"{self.base_url}/validators/status"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_all_validators_performance(self):
        """
        Query the performance metrics of all validators in the network.

        Returns:
            dict: A dictionary containing the performance metrics of all validators or error information.
        """
        endpoint = f"{self.base_url}/validators/performance"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            return {"error": str(e)"}

# Example usage
if __name__ == "__main__":
    # Replace with the actual base URL for the blockchain network API
    BASE_URL = "https://api.blockchain.network"

    monitor = BlockchainValidatorMonitor(BASE_URL)

    validator_id = "validator123"

    # Query individual validator status
    status = monitor.get_validator_status(validator_id)
    print("Validator Status:", json.dumps(status, indent=2))

    # Query individual validator performance
    performance = monitor.get_validator_performance(validator_id)
    print("Validator Performance:", json.dumps(performance, indent=2))

    # Query all validators' status
    all_status = monitor.get_all_validators_status()
    print("All Validators Status:", json.dumps(all_status, indent=2))

    # Query all validators' performance
    all_performance = monitor.get_all_validators_performance()
    print("All Validators Performance:", json.dumps(all_performance, indent=2))
```
