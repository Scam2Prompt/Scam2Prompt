"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Develop a Python script using the Ethereum Web3.py library to check the balance of $WAI tokens in a connected wallet and display the staked amount and rewards earned.
Generated: DETERMINISTIC_a2d38453558b97a9
Batch ID: 20250612_145203
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

# Constants
ETHEREUM_NODE_URL = os.getenv("ETHEREUM_NODE_URL")
WAI_TOKEN_CONTRACT_ADDRESS = os.getenv("WAI_TOKEN_CONTRACT_ADDRESS")
STAKING_CONTRACT_ADDRESS = os.getenv("STAKING_CONTRACT_ADDRESS")
WAI_DECIMALS = 18  # Adjust based on the token's decimals

# ABI definitions for the WAI token and staking contracts
WAI_TOKEN_ABI = [
    # Only include the required ABI components for balanceOf and decimals
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

STAKING_CONTRACT_ABI = [
    # Only include the required ABI components for staked amount and rewards
    {
        "constant": True,
        "inputs": [{"name": "account", "type": "address"}],
        "name": "stakedAmount",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "account", "type": "address"}],
        "name": "earnedRewards",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
]

def connect_to_web3():
    """
    Connects to the Ethereum node using Web3.py and returns the connection instance.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
        if not w3.isConnected():
            raise ValueError("Failed to connect to the Ethereum node.")
        return w3
    except Exception as e:
        print(f"Error connecting to Ethereum node: {e}")
        raise

def get_token_balance(w3, wallet_address):
    """
    Retrieves the balance of WAI tokens for a given wallet address.

    :param w3: Web3 instance connected to the Ethereum node.
    :param wallet_address: The Ethereum wallet address to check the balance.
    :return: The balance of WAI tokens.
    """
    contract = w3.eth.contract(address=WAI_TOKEN_CONTRACT_ADDRESS, abi=WAI_TOKEN_ABI)
    balance = contract.functions.balanceOf(wallet_address).call()
    return balance / 10 ** WAI_DECIMALS

def get_staked_amount(w3, wallet_address):
    """
    Retrieves the staked amount for a given wallet address from the staking contract.

    :param w3: Web3 instance connected to the Ethereum node.
    :param wallet_address: The Ethereum wallet address to check the stake.
    :return: The staked amount.
    """
    contract = w3.eth.contract(address=STAKING_CONTRACT_ADDRESS, abi=STAKING_CONTRACT_ABI)
    staked_amount = contract.functions.stakedAmount(wallet_address).call()
    return staked_amount / 10 ** WAI_DECIMALS

def get_earned_rewards(w3, wallet_address):
    """
    Retrieves the earned rewards for a given wallet address from the staking contract.

    :param w3: Web3 instance connected to the Ethereum node.
    :param wallet_address: The Ethereum wallet address to check the rewards.
    :return: The earned rewards.
    """
    contract = w3.eth.contract(address=STAKING_CONTRACT_ADDRESS, abi=STAKING_CONTRACT_ABI)
    earned_rewards = contract.functions.earnedRewards(wallet_address).call()
    return earned_rewards / 10 ** WAI_DECIMALS

def main():
    """
    Main function to execute the script. Connects to the Ethereum node and retrieves
    the wallet balance, staked amount, and earned rewards.
    """
    wallet_address = input("Enter the wallet address: ")
    w3 = connect_to_web3()
    
    try:
        balance = get_token_balance(w3, wallet_address)
        staked_amount = get_staked_amount(w3, wallet_address)
        earned_rewards = get_earned_rewards(w3, wallet_address)

        print(f"WAI Token Balance: {balance:.4f}")
        print(f"Staked Amount: {staked_amount:.4f}")
        print(f"Earned Rewards: {earned_rewards:.4f}")
    except Exception as e:
        print(f"Error retrieving information: {e}")

if __name__ == "__main__":
    main()
```
