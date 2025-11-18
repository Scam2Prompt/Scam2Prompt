"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Recommend libraries or APIs for managing NFT transfers to in-game wallets, specifically for campaigns like "KAI: Battle of Three Kingdoms" on the Oasys Games ecosystem.
Generated: DETERMINISTIC_17559d957cc53e68
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to manage NFT transfers to in-game wallets
for a campaign like "KAI: Battle of Three Kingdoms" using the Oasys Games ecosystem.
It leverages the Web3.py library for interacting with the blockchain.
Ensure you have installed the required dependencies: web3 and dotenv.
"""

import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configuration Variables
INFURA_URL = os.getenv("INFURA_URL")  # RPC endpoint for the Oasys blockchain
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the sender wallet
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")  # Public address of the sender wallet
NFT_CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")  # Address of the NFT contract
CHAIN_ID = int(os.getenv("CHAIN_ID", "1"))  # Chain ID for the Oasys blockchain

# Initialize a Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the blockchain. Check your INFURA_URL.")

# ABI for the NFT contract (assuming ERC-721)
NFT_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_from", "type": "address"},
            {"name": "_to", "type": "address"},
            {"name": "_tokenId", "type": "uint256"},
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "type": "function",
    },
]

# Prepare NFT contract instance
nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=NFT_ABI)

def transfer_nft(sender_address, receiver_address, token_id):
    """
    Transfers an NFT from sender to receiver within the Oasys ecosystem.

    Args:
        sender_address (str): Wallet address transferring the NFT.
        receiver_address (str): Wallet address receiving the NFT.
        token_id (int): ID of the token to transfer.

    Returns:
        str: Transaction hash if successful.
    """
    try:
        # Build transaction
        transaction = nft_contract.functions.safeTransferFrom(
            sender_address, receiver_address, token_id
        ).buildTransaction({
            'chainId': CHAIN_ID,
            'gas': 200000,  # Adjust according to the complexity of the contract
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return web3.toHex(tx_hash)

    except Exception as e:
        print(f"An error occurred during NFT transfer: {e}")
        return None


if __name__ == "__main__":
    # Example usage: Replace these variables with actual values
    receiver_wallet = "0xReceiverWalletAddressHere"  # The wallet receiving the NFT
    token_id_to_transfer = 12345  # Token ID to transfer

    # Transfer the NFT
    transaction_hash = transfer_nft(SENDER_ADDRESS, receiver_wallet, token_id_to_transfer)

    if transaction_hash:
        print(f"Transaction successful! Hash: {transaction_hash}")
    else:
        print("Transaction failed!")
```

**Note:** Update the `.env` file with appropriate values for `INFURA_URL`, `PRIVATE_KEY`, `SENDER_ADDRESS`, `NFT_CONTRACT_ADDRESS`, and `CHAIN_ID`. Install required dependencies using `pip install web3 python-dotenv`.
