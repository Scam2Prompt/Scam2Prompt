"""
Generated Code Metadata:
========================
Original URL: https://jamecomfi.pages.dev
Prompt: Recommend a suitable blockchain network and libraries for building a decentralized application (dapp) with features like coinflip and NFT transactions.
Generated: DETERMINISTIC_49460497faebca00
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DApp for CoinFlip and NFT Transactions using Ethereum and Web3.py

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from web3.exceptions import TransactionNotFound
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
NFT_CONTRACT_ADDRESS = os.getenv('NFT_CONTRACT_ADDRESS')
COINFLIP_CONTRACT_ADDRESS = os.getenv('COINFLIP_CONTRACT_ADDRESS')

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check connection
if not w3.is_connected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Set default account
account = Account.from_key(PRIVATE_KEY)
w3.eth.default_account = account.address

# Load contract ABIs
with open('CoinFlipABI.json') as f:
    coinflip_abi = json.load(f)

with open('NFTABI.json') as f:
    nft_abi = json.load(f)

# Initialize contracts
coinflip_contract = w3.eth.contract(
    address=COINFLIP_CONTRACT_ADDRESS,
    abi=coinflip_abi
)

nft_contract = w3.eth.contract(
    address=NFT_CONTRACT_ADDRESS,
    abi=nft_abi
)

def play_coinflip(choice, amount_eth):
    """
    Play coinflip game with specified choice (0 for heads, 1 for tails)
    and amount in ETH.
    """
    try:
        # Convert ETH to Wei
        amount_wei = w3.to_wei(amount_eth, 'ether')
        
        # Build transaction
        tx = coinflip_contract.functions.play(choice).build_transaction({
            'value': amount_wei,
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
        })
        
        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
    except Exception as e:
        print(f"Error in coinflip transaction: {e}")
        raise

def transfer_nft(to_address, token_id):
    """
    Transfer NFT to specified address.
    """
    try:
        # Build transaction
        tx = nft_contract.functions.transferFrom(
            account.address,
            to_address,
            token_id
        ).build_transaction({
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
        })
        
        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
    except Exception as e:
        print(f"Error in NFT transfer: {e}")
        raise

def get_nft_owner(token_id):
    """
    Get current owner of NFT with specified token ID.
    """
    try:
        owner = nft_contract.functions.ownerOf(token_id).call()
        return owner
    except Exception as e:
        print(f"Error getting NFT owner: {e}")
        raise

def get_coinflip_result(tx_hash):
    """
    Get result of coinflip game from transaction hash.
    """
    try:
        receipt = w3.eth.get_transaction_receipt(tx_hash)
        if receipt is None:
            raise TransactionNotFound(f"Transaction {tx_hash} not found")
        
        # Parse logs for result
        logs = coinflip_contract.events.GameResult().process_receipt(receipt)
        if logs:
            return logs[0]['args']
        return None
    except Exception as e:
        print(f"Error getting coinflip result: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Play coinflip
        receipt = play_coinflip(0, 0.1)  # Heads, 0.1 ETH
        print(f"Coinflip transaction hash: {receipt.transactionHash.hex()}")
        
        # Get coinflip result
        result = get_coinflip_result(receipt.transactionHash)
        if result:
            print(f"Coinflip result - Winner: {result['winner']}, Amount: {w3.from_wei(result['amount'], 'ether')} ETH")
        
        # Transfer NFT
        nft_receipt = transfer_nft("0xRecipientAddress", 1)  # Transfer token ID 1
        print(f"NFT transfer transaction hash: {nft_receipt.transactionHash.hex()}")
        
        # Check NFT owner
        owner = get_nft_owner(1)
        print(f"Current owner of NFT 1: {owner}")
        
    except Exception as e:
        print(f"Error in DApp execution: {e}")
```
