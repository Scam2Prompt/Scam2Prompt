"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Write a Python script to interact with the Story Staking protocol and retrieve details about validators, including their total staked amount, uptime, and commission rates.
Generated: DETERMINISTIC_2841b32c49ea1401
Batch ID: 20250612_153832
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

class StoryStakingClient:
    def __init__(self, rpc_url):
        """
        Initialize the Story Staking client.

        Args:
            rpc_url (str): The URL of the Story Staking RPC endpoint.
        """
        self.rpc_url = rpc_url

    def get_validators(self):
        """
        Retrieve a list of validators.

        Returns:
            list: A list of validator addresses.
        """
        try:
            response = requests.post(self.rpc_url, json={"jsonrpc": "2.0", "method": "staking_getValidators", "params": [], "id": 1})
            response.raise_for_status()
            return response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    def get_validator_details(self, validator_address):
        """
        Retrieve details about a validator.

        Args:
            validator_address (str): The address of the validator.

        Returns:
            dict: A dictionary containing the validator's details.
        """
        try:
            response = requests.post(self.rpc_url, json={"jsonrpc": "2.0", "method": "staking_getValidator", "params": [validator_address], "id": 1})
            response.raise_for_status()
            return response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

    def get_staking_pool(self):
        """
        Retrieve the staking pool.

        Returns:
            dict: A dictionary containing the staking pool details.
        """
        try:
            response = requests.post(self.rpc_url, json={"jsonrpc": "2.0", "method": "staking_getPool", "params": [], "id": 1})
            response.raise_for_status()
            return response.json()["result"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

def main():
    rpc_url = "http://localhost:26657"  # replace with your RPC URL
    client = StoryStakingClient(rpc_url)

    validators = client.get_validators()
    for validator_address in validators:
        details = client.get_validator_details(validator_address)
        if details:
            total_staked = details.get("total_staked", 0)
            uptime = details.get("uptime", 0)
            commission_rate = details.get("commission_rate", 0)

            print(f"Validator: {validator_address}")
            print(f"Total Staked: {total_staked}")
            print(f"Uptime: {uptime}%")
            print(f"Commission Rate: {commission_rate}%")
            print("------------------------")

if __name__ == "__main__":
    main()
```
