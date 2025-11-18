"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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
  "https://vyper.online/api/v1/compile": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Sure! Below is the requested code:

```python
import requests
import json
from pathlib import Path

# Constants for interacting with Etherscan API and Vyper Compiler
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
VYPER_COMPILER_URL = "https://vyper.online/api/v1/compile"
ETHERSCAN_API_KEY = "your_etherscan_api_key"  # Replace with your Etherscan API key

def fetch_contract_source_code(address, network='mainnet'):
    """
    Fetch the Solidity source code of a smart contract from Etherscan.

    Args:
        address (str): The contract address.
        network (str): The Ethereum network (default: 'mainnet').

    Returns:
        dict: A dictionary containing the source code and metadata or None if an error occurs.
    """
    try:
        params = {
            "module": "contract",
            "action": "getsourcecode",
            "address": address,
            "apikey": ETHERSCAN_API_KEY
        }
        response = requests.get(ETHERSCAN_API_URL, params=params)

        # Raise an HTTPError for bad responses
        response.raise_for_status()

        result = response.json()
        if result["status"] == "1":  # API call successful
            return result["result"][0]  # Return first contract metadata
        else:
            print(f"Error from Etherscan API: {result['message']}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def compile_vyper_source_code(source_code):
    """
    Compile Vyper source code using the Vyper Online Compiler.

    Args:
        source_code (str): The Vyper source code to compile.

    Returns:
        dict: Compiled contract details or None if an error occurs.
    """
    try:
        payload = {"source_code": source_code}
        response = requests.post(VYPER_COMPILER_URL, json=payload)

        # Raise an HTTPError for bad responses
        response.raise_for_status()

        result = response.json()
        return result
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

def save_to_file(content, file_path):
    """
    Save content to a file.

    Args:
        content (str): The content to save.
        file_path (str): Path to the file.
    """
    try:
        Path(file_path).write_text(content, encoding="utf-8")
        print(f"Saved content to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to fetch a contract from Etherscan and optionally compile it with Vyper.
    """
    # Replace with actual contract address
    contract_address = "0xYourContractAddressHere"

    # Fetch smart contract source code from Etherscan
    contract_data = fetch_contract_source_code(contract_address)
    if not contract_data:
        print("Failed to fetch contract source code.")
        return

    # Check if source code is written in Vyper
    source_code = contract_data.get("SourceCode")
    compiler_version = contract_data.get("CompilerVersion")

    if "vyper" in compiler_version.lower():
        print("Vyper source code detected. Compiling with Vyper Online Compiler...")

        # Compile the Vyper source code
        compiled_contract = compile_vyper_source_code(source_code)
        if compiled_contract:
            print("Compilation successful!")
            print("Compiled contract details:", json.dumps(compiled_contract, indent=4))

            # Save compiled output to file
            save_to_file(json.dumps(compiled_contract, indent=4), "compiled_contract.json")
        else:
            print("Failed to compile Vyper source code.")
    else:
        print("Contract is not written in Vyper. Compilation skipped.")

if __name__ == "__main__":
    main()
```

Replace `your_etherscan_api_key` and `0xYourContractAddressHere` with your actual Etherscan API key and a valid contract address. Ensure network connectivity and Python dependencies (`requests`) are installed.
