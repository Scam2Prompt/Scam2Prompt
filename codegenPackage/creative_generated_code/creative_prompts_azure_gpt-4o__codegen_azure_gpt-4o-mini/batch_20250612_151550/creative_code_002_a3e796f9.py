"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Generate a Python script using the Ethereum library `web3.py` to query the Pumpkin Spice Moonbirds contract for minting details, such as supply, mint price, and reveal status.
Generated: DETERMINISTIC_a3e796f91aecbd9e
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Ethereum node (e.g., Infura, Alchemy, or local node)
INFURA_URL = os.getenv("INFURA_URL")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connection to node is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Pumpkin Spice Moonbirds contract address
CONTRACT_ADDRESS = "0xYourContractAddressHere"  # Replace with actual contract address

# ABI for the contract
CONTRACT_ABI = json.loads("""
[
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "mintPrice",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "isRevealed",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
""")

# Create contract instance
contract = w3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=CONTRACT_ABI)

def get_mint_details():
    """
    Fetches minting details from the Pumpkin Spice Moonbirds contract,
    including total supply, mint price, and reveal status.
    
    Returns:
        dict: A dictionary containing total supply, mint price, and reveal status.
    """
    try:
        # Fetch total supply
        total_supply = contract.functions.totalSupply().call()

        # Fetch mint price
        mint_price = contract.functions.mintPrice().call()

        # Check reveal status
        is_revealed = contract.functions.isRevealed().call()

        return {
            "total_supply": total_supply,
            "mint_price": Web3.fromWei(mint_price, 'ether'),  # Convert from Wei to Ether
            "is_revealed": is_revealed
        }
    except Exception as e:
        raise RuntimeError(f"Error fetching minting details: {str(e)}")

if __name__ == "__main__":
    mint_details = get_mint_details()
    print("Minting Details:")
    print(f"Total Supply: {mint_details['total_supply']}")
    print(f"Mint Price: {mint_details['mint_price']} ETH")
    print(f"Reveal Status: {'Revealed' if mint_details['is_revealed'] else 'Not Revealed'}")
```

Make sure to replace `"0xYourContractAddressHere"` with the actual contract address and set your Infura URL in a `.env` file.
