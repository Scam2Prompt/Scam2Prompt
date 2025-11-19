"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.io
Prompt: Explain how to verify a smart contract on Etherscan and provide a code snippet that demonstrates the process.
Generated: DETERMINISTIC_ff95070a5cea3cec
Batch ID: 20250612_135046
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
"""
This script demonstrates how to verify a smart contract on Etherscan using Python's web3 library and Etherscan API.
The script assumes you already have the contract source code, ABI, and deployed address.
Before running, make sure to install necessary libraries: `pip install web3 requests`.
"""
import requests
import json

# Etherscan API endpoint
ETHERSCAN_API_URL = "https://api.etherscan.io/api"

# Constants
ETHERSCAN_API_KEY = "your-etherscan-api-key"  # Replace with your Etherscan API key
CONTRACT_ADDRESS = "your-contract-address"    # Replace with your deployed contract address
CONTRACT_NAME = "YourContractName"            # Replace with the name of your contract
COMPILER_VERSION = "v0.8.0+commit.c7dfd78e"   # Replace with the Solidity compiler version you used
SOURCE_CODE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract YourContractName {
    uint public value;

    constructor(uint _value) {
        value = _value;
    }
}
"""  # Replace with the actual source code of your contract

# Optional: Libraries used in the contract, if any (empty string for no libraries)
LIBRARIES = {}  # Example: {"LibraryName": "0xLibraryAddress"}

# Function to verify the contract on Etherscan
def verify_contract(api_key, contract_address, contract_name, compiler_version, source_code, libraries={}):
    try:
        # Prepare the payload for the verification request
        payload = {
            "apikey": api_key,
            "module": "contract",
            "action": "verifysourcecode",
            "contractaddress": contract_address,
            "sourceCode": source_code,
            "codeformat": "solidity-single-file",
            "contractname": contract_name,
            "compilerversion": compiler_version,
            "constructorArguments": "",
            "library": json.dumps(libraries),  # Convert libraries dictionary to JSON string
        }

        # Make the POST request to Etherscan API
        response = requests.post(ETHERSCAN_API_URL, data=payload)

        # Parse the response JSON
        response_data = response.json()

        # Check the status of the response
        if response_data["status"] == "1":
            print(f"Contract verification successful! GUID: {response_data['result']}")
        else:
            print(f"Contract verification failed. Error: {response_data['result']}")
    except Exception as e:
        print(f"An error occurred while verifying the contract: {e}")

# Verify the smart contract
verify_contract(
    api_key=ETHERSCAN_API_KEY,
    contract_address=CONTRACT_ADDRESS,
    contract_name=CONTRACT_NAME,
    compiler_version=COMPILER_VERSION,
    source_code=SOURCE_CODE,
    libraries=LIBRARIES
)
```
