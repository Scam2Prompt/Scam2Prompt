"""
Generated Code Metadata:
========================
Original URL: https://berachain.tryethernal.com
Prompt: Create a script to fetch and display Ethereum smart contract details using the Ethernal API.
Generated: DETERMINISTIC_d6f84fd7c74360d8
Batch ID: 20250612_150018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

class EthereumContractFetcher:
    """
    Fetches and displays Ethereum smart contract details using the Etherscan API.
    """

    def __init__(self, api_key):
        """
        Initializes the EthereumContractFetcher with an Etherscan API key.

        Args:
            api_key (str): The Etherscan API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.etherscan.io/api"

    def get_contract_abi(self, contract_address):
        """
        Fetches the ABI of a smart contract.

        Args:
            contract_address (str): The address of the smart contract.

        Returns:
            dict: The ABI of the smart contract.
        """
        params = {
            "module": "proxy",
            "action": "eth_getAbi",
            "address": contract_address,
            "apikey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            if data["message"] == "OK":
                return json.loads(data["result"])
            else:
                raise Exception(data["message"])
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def get_contract_source_code(self, contract_address):
        """
        Fetches the source code of a smart contract.

        Args:
            contract_address (str): The address of the smart contract.

        Returns:
            str: The source code of the smart contract.
        """
        params = {
            "module": "proxy",
            "action": "eth_getSourceCode",
            "address": contract_address,
            "apikey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            if data["message"] == "OK":
                return data["result"]
            else:
                raise Exception(data["message"])
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def display_contract_details(self, contract_address):
        """
        Displays the details of a smart contract.

        Args:
            contract_address (str): The address of the smart contract.
        """
        abi = self.get_contract_abi(contract_address)
        source_code = self.get_contract_source_code(contract_address)

        if abi and source_code:
            print(f"Contract Address: {contract_address}")
            print(f"ABI: {json.dumps(abi, indent=4)}")
            print(f"Source Code: {source_code}")


if __name__ == "__main__":
    api_key = "YOUR_ETHERSCAN_API_KEY"
    contract_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

    fetcher = EthereumContractFetcher(api_key)
    fetcher.display_contract_details(contract_address)
```
