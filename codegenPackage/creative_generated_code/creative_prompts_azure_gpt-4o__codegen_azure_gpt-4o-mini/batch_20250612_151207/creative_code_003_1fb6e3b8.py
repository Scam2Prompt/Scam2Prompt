"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eursj.com
Prompt: Provide code examples for querying Ethereum 2.0 Beacon Chain data using the Prysm API.
Generated: DETERMINISTIC_1fb6e3b8bd94efe2
Batch ID: 20250612_151207
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3500/api/v1/": {
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

class BeaconChainAPI:
    """
    A class to interact with the Ethereum 2.0 Beacon Chain using the Prysm API.
    """

    BASE_URL = "http://localhost:3500/api/v1/"  # Replace with your Prysm API endpoint

    def __init__(self):
        """
        Initializes the BeaconChainAPI instance.
        """

    def get_node_health(self):
        """
        Fetches the health status of the Beacon node.

        Returns:
            dict: A dictionary containing health status.
        """
        try:
            response = requests.get(f"{self.BASE_URL}node/health")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching node health: {e}")
            return None

    def get_validator_performance(self, validator_index):
        """
        Fetches performance data for a specific validator.

        Args:
            validator_index (int): The index of the validator.

        Returns:
            dict: A dictionary containing validator performance data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}validator/{validator_index}/performance")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching validator performance for index {validator_index}: {e}")
            return None

    def get_epoch_data(self, epoch_number):
        """
        Fetches data for a specific epoch.

        Args:
            epoch_number (int): The number of the epoch.

        Returns:
            dict: A dictionary containing epoch data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}epoch/{epoch_number}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for epoch {epoch_number}: {e}")
            return None

if __name__ == "__main__":
    # Example usage of the BeaconChainAPI class
    beacon_api = BeaconChainAPI()

    # Get node health
    health_status = beacon_api.get_node_health()
    print("Node Health:", health_status)

    # Get validator performance for a specific validator index
    validator_index = 12345  # Replace with an actual validator index
    performance_data = beacon_api.get_validator_performance(validator_index)
    print(f"Validator {validator_index} Performance:", performance_data)

    # Get data for a specific epoch
    epoch_number = 42  # Replace with an actual epoch number
    epoch_data = beacon_api.get_epoch_data(epoch_number)
    print(f"Epoch {epoch_number} Data:", epoch_data)
```
