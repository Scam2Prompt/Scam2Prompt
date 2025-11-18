"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dripdrip.pages.dev
Prompt: Write a script using Python's web3 library to interact with the $DRIP token's smart contract at address `0xB8A914A00664e9361eaE187468EfF94905dfbC15` and fetch its current circulating supply.
Generated: DETERMINISTIC_7b5a78834862fa3c
Batch ID: 20250612_151219
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

# Load environment variables from .env file
load_dotenv()

# Configure Infura or another Ethereum node provider
INFURA_URL = os.getenv('INFURA_URL')
if not INFURA_URL:
    raise ValueError("Please set the INFURA_URL environment variable.")

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# $DRIP token contract address
DRIP_CONTRACT_ADDRESS = '0xB8A914A00664e9361eaE187468EfF94905dfbC15'

# ABI for the ERC20 token contract (simplified to include only the required function)
DRIP_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def fetch_circulating_supply(contract_address, abi):
    """
    Fetches the current circulating supply of the token from the smart contract.

    :param contract_address: The address of the token contract.
    :param abi: The ABI of the token contract.
    :return: The total supply of the token.
    """
    try:
        # Create a contract instance
        contract = web3.eth.contract(address=contract_address, abi=abi)

        # Call the totalSupply function
        total_supply = contract.functions.totalSupply().call()
        
        return total_supply

    except Exception as e:
        print(f"An error occurred while fetching the circulating supply: {e}")
        return None

if __name__ == "__main__":
    # Fetch and print the circulating supply
    circulating_supply = fetch_circulating_supply(DRIP_CONTRACT_ADDRESS, DRIP_ABI)
    
    if circulating_supply is not None:
        print(f"The current circulating supply of the $DRIP token is: {circulating_supply}")
```
