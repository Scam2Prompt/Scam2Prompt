"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Create a script to automate the process of claiming Golden Grenade VIP NFT Membership for users holding the minimum required $MBDAO tokens.
Generated: DETERMINISTIC_2994bb7c2bedc05d
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Configuration
INFURA_URL = os.getenv("INFURA_URL")  # Infura or other Ethereum node provider URL
PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")  # User's private key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # User's wallet address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Golden Grenade NFT contract address
TOKEN_CONTRACT_ADDRESS = os.getenv("TOKEN_CONTRACT_ADDRESS")  # $MBDAO ERC-20 token contract address
MINIMUM_MBDO_TOKENS = 1000  # Minimum $MBDAO tokens required
GAS_LIMIT = 200000  # Gas limit for the transaction
GAS_PRICE_GWEI = 20  # Gas price in Gwei

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network. Check your Infura URL or network connection.")

# Load ABI files
with open("golden_grenade_abi.json", "r") as f:
    golden_grenade_abi = f.read()

with open("erc20_abi.json", "r") as f:
    erc20_abi = f.read()

# Initialize contract objects
golden_grenade_contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=golden_grenade_abi)
token_contract = web3.eth.contract(address=Web3.to_checksum_address(TOKEN_CONTRACT_ADDRESS), abi=erc20_abi)

def check_token_balance(wallet_address: str) -> int:
    """
    Check the $MBDAO token balance of the given wallet address.
    """
    try:
        balance = token_contract.functions.balanceOf(wallet_address).call()
        return web3.from_wei(balance, 'ether')
    except Exception as e:
        raise RuntimeError(f"Error checking token balance: {e}")

def claim_nft(wallet_address: str):
    """
    Claim the Golden Grenade VIP NFT Membership.
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.get_transaction_count(wallet_address)
        gas_price = web3.to_wei(GAS_PRICE_GWEI, 'gwei')
        
        txn = golden_grenade_contract.functions.claimMembership().build_transaction({
            'from': wallet_address,
            'nonce': nonce,
            'gas': GAS_LIMIT,
            'gasPrice': gas_price
        })
        
        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        
        # Send the transaction
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
        
        if txn_receipt.status == 1:
            print(f"NFT Membership successfully claimed! Transaction Hash: {txn_hash.hex()}")
        else:
            raise RuntimeError("Transaction failed. Please check the transaction hash for details.")
    except Exception as e:
        raise RuntimeError(f"Error claiming NFT: {e}")

def main():
    """
    Main function to automate NFT claiming process.
    """
    try:
        print("Checking $MBDAO token balance...")
        balance = check_token_balance(WALLET_ADDRESS)
        
        print(f"Your $MBDAO token balance: {balance}")
        
        if balance < MINIMUM_MBDO_TOKENS:
            print(f"Insufficient $MBDAO tokens. You need at least {MINIMUM_MBDO_TOKENS} tokens to claim the NFT.")
            return
        
        print("Claiming NFT Membership...")
        claim_nft(WALLET_ADDRESS)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This script is structured for production use, with appropriate error handling, comments, and following best practices. Ensure the ABI files (`golden_grenade_abi.json` and `erc20_abi.json`) and the `.env` file with the required variables are properly set up before running the script.
