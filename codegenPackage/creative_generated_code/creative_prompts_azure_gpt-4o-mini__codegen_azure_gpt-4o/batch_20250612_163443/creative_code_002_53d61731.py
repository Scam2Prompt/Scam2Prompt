"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Create a Python script using Web3.py to fetch and display the top 10 contributors' wallet addresses and their total contributions in ETH for the $ROOST presale.
Generated: DETERMINISTIC_53d61731dd98b9a9
Batch ID: 20250612_163443
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

# Set up the connection to an Ethereum node
INFURA_URL = os.getenv("INFURA_URL")  # Replace with your Infura or node URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Contract details
CONTRACT_ADDRESS = Web3.toChecksumAddress(os.getenv("CONTRACT_ADDRESS"))  # Replace with $ROOST presale contract address
ABI = os.getenv("CONTRACT_ABI")  # Replace with the contract ABI (stored in environment variable)

# Initialize the contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def fetch_top_contributors(contract, top_n=10):
    """
    Fetches the top contributors' wallet addresses and their contributions in ETH.

    Args:
        contract: Web3.py contract instance for the presale contract.
        top_n: Number of top contributors to fetch (default is 10).
    
    Returns:
        List of tuples containing wallet address and contribution amount.
    """
    try:
        # Assuming the contract has a method `getTopContributors` to fetch the top contributors
        top_contributors = contract.functions.getTopContributors(top_n).call()
        contributors = []

        for contributor in top_contributors:
            wallet_address = contributor[0]
            contribution_in_wei = contributor[1]
            contribution_in_eth = web3.fromWei(contribution_in_wei, 'ether')

            contributors.append((wallet_address, contribution_in_eth))

        return contributors

    except Exception as e:
        raise RuntimeError(f"Failed to fetch top contributors: {str(e)}")

def display_contributors(contributors):
    """
    Displays the wallet addresses and contributions in ETH of the top contributors.

    Args:
        contributors: List of tuples containing wallet address and contribution amount.
    """
    print("Top Contributors:")
    print("-----------------")
    for idx, (address, contribution) in enumerate(contributors, start=1):
        print(f"{idx}. Wallet: {address}, Contribution: {contribution:.4f} ETH")

if __name__ == "__main__":
    try:
        # Fetch and display the top 10 contributors
        top_contributors = fetch_top_contributors(contract, top_n=10)
        display_contributors(top_contributors)

    except Exception as e:
        print(f"Error: {str(e)}")
```

**Notes:**
- Replace `INFURA_URL`, `CONTRACT_ADDRESS`, and `CONTRACT_ABI` with actual values from your environment or replace `os.getenv()` calls with hardcoded values for testing.
- This script assumes the contract has a `getTopContributors` function returning a list of contributors with their respective wallet addresses and contributions. Update the function as needed based on the actual contract implementation.
