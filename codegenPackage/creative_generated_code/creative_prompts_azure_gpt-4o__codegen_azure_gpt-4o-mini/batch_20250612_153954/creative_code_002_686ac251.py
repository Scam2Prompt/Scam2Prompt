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
  "https://api.blockchain-network.com": {
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

class BlockchainValidator:
    """Class to query validator status and performance metrics on a blockchain network."""

    def __init__(self, base_url):
        """
        Initialize the BlockchainValidator with the base URL of the blockchain API.
        
        :param base_url: The base URL of the blockchain API.
        """
        self.base_url = base_url

    def get_validator_status(self, validator_id):
        """
        Retrieve the status of a specific validator.

        :param validator_id: The unique identifier of the validator.
        :return: A dictionary containing the validator's status information.
        :raises ValueError: If the validator_id is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not validator_id:
            raise ValueError("Validator ID must not be empty.")

        endpoint = f"{self.base_url}/validators/{validator_id}/status"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the status as JSON
        except requests.RequestException as e:
            raise Exception(f"Error querying validator status: {e}")

    def get_validator_performance(self, validator_id):
        """
        Retrieve the performance metrics of a specific validator.

        :param validator_id: The unique identifier of the validator.
        :return: A dictionary containing the validator's performance metrics.
        :raises ValueError: If the validator_id is invalid.
        :raises Exception: For any other errors during the API call.
        """
        if not validator_id:
            raise ValueError("Validator ID must not be empty.")

        endpoint = f"{self.base_url}/validators/{validator_id}/performance"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the performance metrics as JSON
        except requests.RequestException as e:
            raise Exception(f"Error querying validator performance: {e}")

if __name__ == "__main__":
    # Example usage of the BlockchainValidator class
    BASE_URL = "https://api.blockchain-network.com"  # Replace with actual blockchain API URL
    validator_id = "validator123"  # Replace with the actual validator ID

    validator = BlockchainValidator(BASE_URL)

    try:
        status = validator.get_validator_status(validator_id)
        print("Validator Status:", status)

        performance = validator.get_validator_performance(validator_id)
        print("Validator Performance:", performance)

    except Exception as e:
        print(f"An error occurred: {e}")
```
