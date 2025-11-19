"""
Generated Code Metadata:
========================
Original URL: https://etherscan.com
Prompt: Provide a script to interact with the Etherscan API and compile smart contracts using the Vyper Online Compiler.
Generated: DETERMINISTIC_226d4c42f24e8fb4
Batch ID: 20250612_150323
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://vyper.online/api/compile": {
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

class EtherscanAPI:
    """
    A class to interact with the Etherscan API for fetching contract details.
    """

    BASE_URL = "https://api.etherscan.io/api"

    def __init__(self, api_key):
        """
        Initializes the EtherscanAPI with the provided API key.

        :param api_key: Etherscan API key for authentication
        """
        self.api_key = api_key

    def get_contract_source_code(self, contract_address):
        """
        Fetches the source code of a smart contract from Etherscan.

        :param contract_address: The Ethereum address of the contract
        :return: The source code of the contract or an error message
        """
        params = {
            'module': 'contract',
            'action': 'getsourcecode',
            'address': contract_address,
            'apikey': self.api_key
        }
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            if data['status'] == '1':
                return data['result'][0]['SourceCode']
            else:
                return f"Error: {data['message']}"
        except requests.RequestException as e:
            return f"Request failed: {e}"

class VyperCompiler:
    """
    A class to compile smart contracts using the Vyper Online Compiler.
    """

    VYPER_COMPILER_URL = "https://vyper.online/api/compile"

    def compile_contract(self, source_code):
        """
        Compiles the provided Vyper source code.

        :param source_code: The Vyper source code to compile
        :return: Compilation result or an error message
        """
        payload = {
            'source': source_code,
            'version': '0.3.3'  # Specify the Vyper version
        }
        try:
            response = requests.post(self.VYPER_COMPILER_URL, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            return f"Compilation request failed: {e}"

def main():
    """
    Main function to demonstrate the usage of EtherscanAPI and VyperCompiler.
    """
    etherscan_api_key = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API key
    contract_address = "0xYourContractAddress"  # Replace with the contract address you want to query

    # Initialize Etherscan API
    etherscan = EtherscanAPI(etherscan_api_key)

    # Fetch the contract source code
    source_code = etherscan.get_contract_source_code(contract_address)
    if "Error" in source_code:
        print(source_code)
        return

    # Initialize Vyper Compiler
    vyper_compiler = VyperCompiler()

    # Compile the contract
    compilation_result = vyper_compiler.compile_contract(source_code)
    print(compilation_result)

if __name__ == "__main__":
    main()
```
