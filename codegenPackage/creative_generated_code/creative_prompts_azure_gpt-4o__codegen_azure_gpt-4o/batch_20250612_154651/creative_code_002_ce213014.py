"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stekecoredao.org
Prompt: Create a Python script using the Web3.py library to fetch and display the `stCORE Reward Rate`, `Conversion Ratio`, and `stCORE Supply` from the CoreDAO staking data.
Generated: DETERMINISTIC_ce213014ecf116ba
Batch ID: 20250612_154651
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

# Load environment variables from a .env file for sensitive information
load_dotenv()

# Set up Web3 connection
# Ensure you replace 'YOUR_INFURA_URL' or 'YOUR_RPC_URL' with your Ethereum node endpoint
INFURA_URL = os.getenv("INFURA_URL")  # Example environment variable for the node URL
if not INFURA_URL:
    raise ValueError("Please set your INFURA_URL environment variable in the .env file.")
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection to the Ethereum network is successful
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network.")

# Contract address for the CoreDAO staking data
# Replace with the actual contract address for CoreDAO staking
CONTRACT_ADDRESS = web3.toChecksumAddress("0xYourContractAddressHere")

# ABI for the CoreDAO staking contract
# Replace with the actual ABI for the staking contract
CONTRACT_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "stCORERewardRate",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "conversionRatio",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "stCORESupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

# Instantiate the contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def fetch_staking_data():
    """
    Fetches and displays the staking data:
    - stCORE Reward Rate
    - Conversion Ratio
    - stCORE Supply
    """
    try:
        # Fetch stCORE Reward Rate
        stcore_reward_rate = contract.functions.stCORERewardRate().call()
        # Fetch Conversion Ratio
        conversion_ratio = contract.functions.conversionRatio().call()
        # Fetch stCORE Supply
        stcore_supply = contract.functions.stCORESupply().call()

        # Display the fetched data
        print("CoreDAO Staking Data:")
        print(f"stCORE Reward Rate: {stcore_reward_rate}")
        print(f"Conversion Ratio: {conversion_ratio}")
        print(f"stCORE Supply: {stcore_supply}")

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while fetching staking data: {e}")

if __name__ == "__main__":
    fetch_staking_data()
```

### Notes:
- Replace `"0xYourContractAddressHere"` with the actual contract address of the CoreDAO staking contract.
- Replace the `CONTRACT_ABI` contents with the actual ABI of the CoreDAO staking smart contract.
- Ensure you create a `.env` file with `INFURA_URL` or your RPC URL to securely load sensitive data.
