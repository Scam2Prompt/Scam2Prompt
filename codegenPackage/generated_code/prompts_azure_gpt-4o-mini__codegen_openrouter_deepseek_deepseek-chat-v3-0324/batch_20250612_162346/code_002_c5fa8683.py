"""
Generated Code Metadata:
========================
Original URL: https://nodeautorepair.pages.dev
Prompt: What is the process for minting NFTs as described in the Dapp Webnode ecosystem, and can you provide a sample code for this?
Generated: DETERMINISTIC_c5fa868316690641
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
RPC_URL = os.getenv('RPC_URL')
CHAIN_ID = int(os.getenv('CHAIN_ID'))

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load contract ABI
with open('contract_abi.json', 'r') as abi_file:
    CONTRACT_ABI = json.load(abi_file)

# Initialize contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def mint_nft(to_address, token_uri):
    """
    Mint a new NFT and assign it to the specified address.
    
    Args:
        to_address (str): The address to receive the NFT
        token_uri (str): The URI pointing to the NFT metadata
        
    Returns:
        str: Transaction hash of the mint operation
    """
    try:
        # Validate input addresses
        if not w3.is_address(to_address):
            raise ValueError("Invalid recipient address")
            
        # Convert to checksum address
        to_address = w3.to_checksum_address(to_address)
        
        # Get the nonce
        nonce = w3.eth.get_transaction_count(w3.eth.default_account)
        
        # Build transaction
        tx = contract.functions.mint(to_address, token_uri).build_transaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
        })
        
        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        
        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status != 1:
            raise Exception("Transaction failed")
            
        return tx_hash.hex()
        
    except Exception as e:
        print(f"Error minting NFT: {str(e)}")
        raise

# Example usage (commented out for production)
# if __name__ == "__main__":
#     recipient = "0xRecipientAddressHere"
#     metadata_uri = "ipfs://QmMetadataHashHere"
#     try:
#         tx_hash = mint_nft(recipient, metadata_uri)
#         print(f"NFT minted successfully! Transaction hash: {tx_hash}")
#     except Exception as e:
#         print(f"Failed to mint NFT: {str(e)}")
```
