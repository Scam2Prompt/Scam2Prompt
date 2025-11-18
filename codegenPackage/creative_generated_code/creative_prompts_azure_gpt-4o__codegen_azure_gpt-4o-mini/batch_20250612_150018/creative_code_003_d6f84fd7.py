"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berachain.tryethernal.com
Prompt: Create a script to fetch and display Ethereum smart contract details using the Ethernal API.
Generated: DETERMINISTIC_d6f84fd7c74360d8
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ethernal.io": {
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

class EthernalAPI:
    """
    A class to interact with the Ethernal API to fetch Ethereum smart contract details.
    """

    BASE_URL = "https://api.ethernal.io"

    def __init__(self, contract_address):
        """
        Initializes the EthernalAPI instance with a contract address.

        :param contract_address: Ethereum smart contract address
        """
        self.contract_address = contract_address

    def fetch_contract_details(self):
        """
        Fetches the details of the Ethereum smart contract from the Ethernal API.

        :return: JSON response containing contract details
        :raises ValueError: If the contract address is invalid
        :raises Exception: For any other errors during the API request
        """
        if not self.is_valid_address(self.contract_address):
            raise ValueError(f"Invalid Ethereum address: {self.contract_address}")

        url = f"{self.BASE_URL}/contracts/{self.contract_address}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            return response.json()  # Return the JSON response if successful

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

    @staticmethod
    def is_valid_address(address):
        """
        Validates an Ethereum address.

        :param address: The Ethereum address to validate
        :return: True if valid, False otherwise
        """
        # Basic validation for Ethereum address format (not exhaustive)
        return len(address) == 42 and address.startswith("0x")

def display_contract_details(contract_address):
    """
    Displays the details of the Ethereum smart contract.

    :param contract_address: Ethereum smart contract address
    """
    ethernal_api = EthernalAPI(contract_address)

    try:
        contract_details = ethernal_api.fetch_contract_details()
        print("Contract Details:")
        print("-----------------")
        print(contract_details)

    except ValueError as val_err:
        print(f"Value error: {val_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example contract address (replace with actual address)
    example_contract_address = "0xYourContractAddressHere"
    display_contract_details(example_contract_address)
```
