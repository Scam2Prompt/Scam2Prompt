"""
Generated Code Metadata:
========================
Original URL: https://teddysbearprc20.com
Prompt: Generate a Python code snippet to interact with the Teddy Bear ($BEAR) smart contract on PulseChain using Web3.py library.
Generated: DETERMINISTIC_7105539a5f67402a
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to PulseChain RPC URL
RPC_URL = os.getenv("PULSECHAIN_RPC_URL")
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check if the connection to the blockchain is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to PulseChain RPC.")

# Define the Teddy Bear smart contract address and ABI
BEAR_CONTRACT_ADDRESS = "0xYourTeddyBearContractAddress"  # Replace with actual contract address
BEAR_CONTRACT_ABI = [
    # Replace with actual ABI of the Teddy Bear contract
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    # Add other functions as needed
]

# Create a contract instance
bear_contract = web3.eth.contract(address=BEAR_CONTRACT_ADDRESS, abi=BEAR_CONTRACT_ABI)

def get_total_supply():
    """Fetch the total supply of Teddy Bear tokens."""
    try:
        total_supply = bear_contract.functions.totalSupply().call()
        return total_supply
    except Exception as e:
        print(f"Error fetching total supply: {e}")
        return None

def get_token_name():
    """Fetch the name of the Teddy Bear token."""
    try:
        token_name = bear_contract.functions.name().call()
        return token_name
    except Exception as e:
        print(f"Error fetching token name: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    print("Fetching Teddy Bear token details...")
    
    token_name = get_token_name()
    if token_name:
        print(f"Teddy Bear Token Name: {token_name}")

    total_supply = get_total_supply()
    if total_supply is not None:
        print(f"Teddy Bear Total Supply: {total_supply}")
```

Make sure to replace `0xYourTeddyBearContractAddress` and the ABI with the actual contract address and ABI of the Teddy Bear smart contract. Additionally, ensure that you have a `.env` file with the `PULSECHAIN_RPC_URL` variable set to your PulseChain RPC endpoint.
