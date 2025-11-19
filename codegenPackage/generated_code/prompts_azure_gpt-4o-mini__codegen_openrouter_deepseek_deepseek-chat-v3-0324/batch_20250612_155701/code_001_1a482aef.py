"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Write a Python script that interacts with the Ethereum blockchain to mint NFTs from the Fuck OpenSea collection, specifying the price of 0.001 ETH per NFT.
Generated: DETERMINISTIC_1a482aef2ee4ee7c
Batch ID: 20250612_155701
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
from web3.middleware import geth_poa_middleware
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
NFT_PRICE = Web3.to_wei(0.001, 'ether')  # 0.001 ETH in wei
GAS_LIMIT = 200000

# ABI for the Fuck OpenSea NFT contract (simplified mint function)
CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "quantity", "type": "uint256"}
        ],
        "name": "mint",
        "outputs": [],
        "stateMutacallble": False,
        "type": "function"
    }
]

def initialize_web3():
    """Initialize Web3 connection with Infura."""
    w3 = Web3(Web3.HTTPProvider(INFURA_URL))
    
    # Add PoA middleware if needed (for networks like Rinkeby)
    if 'rinkeby' in INFURA_URL:
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    
    return w3

def get_contract(w3):
    """Get the contract instance."""
    return w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def mint_nft(quantity=1):
    """Mint NFTs from the Fuck OpenSea collection."""
    try:
        # Initialize Web3 and contract
        w3 = initialize_web3()
        contract = get_contract(w3)
        
        # Get account from private key
        account = Account.from_key(PRIVATE_KEY)
        
        # Build transaction
        tx = contract.functions.mint(quantity).build_transaction({
            'from': account.address,
            'value': NFT_PRICE * quantity,
            'gas': GAS_LIMIT,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
        })
        
        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        
        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        print(f"Successfully minted {quantity} NFT(s)!")
        print(f"Transaction hash: {receipt.transactionHash.hex()}")
        
        return receipt
    
    except Exception as e:
        print(f"Error minting NFT: {e}")
        raise

if __name__ == "__main__":
    # Mint 1 NFT by default
    mint_nft(1)
```
