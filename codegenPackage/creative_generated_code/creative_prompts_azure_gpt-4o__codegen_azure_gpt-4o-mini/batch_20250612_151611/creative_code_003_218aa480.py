"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiyoil.web.app
Prompt: Write a Python script using Web3.py to query the Taiyo Oil smart contract and retrieve the current whitelist supply and public price information.
Generated: DETERMINISTIC_218aa480e8efc72f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants for the Ethereum network and the contract address
ETHEREUM_NODE_URL = os.getenv('ETHEREUM_NODE_URL')
TAIYO_OIL_CONTRACT_ADDRESS = os.getenv('TAIYO_OIL_CONTRACT_ADDRESS')

# Initialize a Web3 connection to the Ethereum network
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

# Check if the connection to the Ethereum node is successful
if not w3.isConnected():
    raise ConnectionError("Could not connect to the Ethereum node.")

# ABI for the Taiyo Oil smart contract (simplified example)
TAIYO_OIL_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "whitelistSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "publicPrice",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Instantiate the Taiyo Oil smart contract
taiyo_oil_contract = w3.eth.contract(address=TAIYO_OIL_CONTRACT_ADDRESS, abi=TAIYO_OIL_ABI)

def get_whitelist_supply():
    """
    Function to retrieve the current whitelist supply from the Taiyo Oil smart contract.
    """
    try:
        supply = taiyo_oil_contract.functions.whitelistSupply().call()
        return supply
    except Exception as e:
        print(f"An error occurred while fetching whitelist supply: {e}")
        return None

def get_public_price():
    """
    Function to retrieve the current public price from the Taiyo Oil smart contract.
    """
    try:
        price = taiyo_oil_contract.functions.publicPrice().call()
        return price
    except Exception as e:
        print(f"An error occurred while fetching public price: {e}")
        return None

def main():
    """
    Main function to query and print the whitelist supply and public price.
    """
    whitelist_supply = get_whitelist_supply()
    public_price = get_public_price()

    if whitelist_supply is not None:
        print(f"Current Whitelist Supply: {whitelist_supply}")
    if public_price is not None:
        print(f"Current Public Price: {public_price}")

if __name__ == "__main__":
    main()
```

Make sure to set the following environment variables in your `.env` file:
```
ETHEREUM_NODE_URL=<Your Ethereum Node URL>
TAIYO_OIL_CONTRACT_ADDRESS=<Your Taiyo Oil Contract Address>
```
