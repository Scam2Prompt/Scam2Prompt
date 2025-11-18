"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Write a Python script to interact with the $MONG cryptocurrency smart contract, referencing its renounced contract and 690 trillion hard-capped supply.
Generated: DETERMINISTIC_5caf2bc6c7e3ead9
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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
import json
import requests
from web3 import Web3

# Constants for the smart contract interaction
MONG_CONTRACT_ADDRESS = '0xYourMongContractAddress'  # Replace with the actual contract address
RPC_URL = 'https://your.ethereum.node'  # Replace with your Ethereum node RPC URL
ABI_PATH = 'path/to/mong_abi.json'  # Replace with the path to the contract ABI

# Load the contract ABI from a JSON file
def load_abi(file_path):
    """Loads the contract ABI from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"ABI file not found: {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Error decoding JSON from file: {file_path}")

# Initialize the Web3 instance
try:
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not web3.isConnected():
        raise Exception("Failed to connect to the Ethereum node")
except Exception as e:
    raise Exception(f"Error initializing Web3: {str(e)}")

# Load the MONG token contract
def load_contract(address, abi):
    """Loads the smart contract at the specified address."""
    try:
        return web3.eth.contract(address=address, abi=abi)
    except Exception as e:
        raise Exception(f"Error loading contract: {str(e)}")

# Function to get MONG token details
def get_mong_details(contract):
    """Fetches details about the MONG token."""
    try:
        name = contract.functions.name().call()
        symbol = contract.functions.symbol().call()
        total_supply = contract.functions.totalSupply().call()
        return {
            'name': name,
            'symbol': symbol,
            'total_supply': total_supply,
        }
    except Exception as e:
        raise Exception(f"Error fetching token details: {str(e)}")

def main():
    """Main function to interact with the MONG cryptocurrency smart contract."""
    # Load the contract ABI
    abi = load_abi(ABI_PATH)

    # Load the MONG contract
    mong_contract = load_contract(MONG_CONTRACT_ADDRESS, abi)

    # Get MONG token details
    try:
        details = get_mong_details(mong_contract)
        print("MONG Token Details:")
        print(f"Name: {details['name']}")
        print(f"Symbol: {details['symbol']}")
        print(f"Total Supply: {details['total_supply']/10**18} MONG")  # Adjust for decimals
    except Exception as e:
        print(f"Error during contract interaction: {str(e)}")

if __name__ == '__main__':
    main()
```

**Note**: Make sure to replace placeholder values such as `MONG_CONTRACT_ADDRESS`, `RPC_URL`, and `ABI_PATH` with actual values. The script also assumes that the contract complies with the ERC20 standard for token contracts. Adjust the decimal handling according to the token's specific implementation.
