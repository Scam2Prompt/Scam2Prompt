"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://approvalscan.com
Prompt: Provide an example of using the Etherscan API to verify a smart contract's source code and retrieve its ABI.
Generated: DETERMINISTIC_26488fa89910c68f
Batch ID: 20250612_145450
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

# Creative Generated Code:
# ========================

```python
import requests

class EtherscanAPI:
    """A class to interact with the Etherscan API for verifying smart contract source code and retrieving ABI."""

    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI instance with the provided API key.

        :param api_key: str - The API key for Etherscan API
        """
        self.api_key = api_key

    def verify_contract(self, contract_address, source_code, contract_name, compiler_version, optimization_used):
        """
        Verifies the smart contract source code on Etherscan.

        :param contract_address: str - The address of the smart contract
        :param source_code: str - The source code of the smart contract
        :param contract_name: str - The name of the contract
        :param compiler_version: str - The version of the compiler used
        :param optimization_used: str - Whether optimization was used ('1' for yes, '0' for no)
        :return: dict - The response from the Etherscan API
        """
        payload = {
            'module': 'contract',
            'action': 'verifysourcecode',
            'apikey': self.api_key,
            'contractaddress': contract_address,
            'sourceCode': source_code,
            'contractname': contract_name,
            'compilerversion': compiler_version,
            'optimizationUsed': optimization_used,
        }

        try:
            response = requests.post(self.BASE_URL, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error verifying contract: {e}")
            return None

    def get_contract_abi(self, contract_address):
        """
        Retrieves the ABI of the specified contract address from Etherscan.

        :param contract_address: str - The address of the smart contract
        :return: dict - The response containing the contract ABI
        """
        payload = {
            'module': 'contract',
            'action': 'getabi',
            'apikey': self.api_key,
            'address': contract_address,
        }

        try:
            response = requests.get(self.BASE_URL, params=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving ABI: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your actual Etherscan API key
    etherscan = EtherscanAPI(ETHERSCAN_API_KEY)

    # Verify a contract (provide actual values)
    contract_address = "0xYourContractAddressHere"
    source_code = "pragma solidity ^0.8.0; contract MyContract { }"  # Replace with actual source code
    contract_name = "MyContract"
    compiler_version = "v0.8.0+commit.c7dfd78e"  # Replace with actual compiler version
    optimization_used = "1"  # Change to "0" if optimization was not used

    verification_response = etherscan.verify_contract(contract_address, source_code, contract_name, compiler_version, optimization_used)
    print(verification_response)

    # Get ABI of a contract
    abi_response = etherscan.get_contract_abi(contract_address)
    print(abi_response)
```
