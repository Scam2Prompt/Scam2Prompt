"""
Generated Code Metadata:
========================
Original URL: https://ethcollection.paperplane.io
Prompt: "Generate a Python script to mint an NFT on Ethereum using the OpenZeppelin library."
Generated: DETERMINISTIC_373238ba54fa9707
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from pathlib import Path

# Load configuration from a JSON file
def load_config(config_path):
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config

# Initialize Web3 connection
def init_web3(rpc_url):
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if 'goerli' in rpc_url.lower():
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3

# Load contract ABI
def load_contract_abi(abi_path):
    with open(abi_path) as abi_file:
        abi = json.load(abi_file)
    return abi

# Mint NFT function
def mint_nft(w3, contract_address, contract_abi, private_key, to_address, token_uri):
    account = Account.from_key(private_key)
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    
    # Build transaction
    tx = contract.functions.mint(to_address, token_uri).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    
    # Sign transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Wait for transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return tx_receipt

def main():
    try:
        # Load configuration
        config = load_config('config.json')
        
        # Initialize Web3
        w3 = init_web3(config['rpc_url'])
        
        # Check connection
        if not w3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")
        
        # Load contract ABI
        contract_abi = load_contract_abi(Path(__file__).parent / 'contract_abi.json')
        
        # Mint NFT
        receipt = mint_nft(
            w3=w3,
            contract_address=config['contract_address'],
            contract_abi=contract_abi,
            private_key=config['private_key'],
            to_address=config['to_address'],
            token_uri=config['token_uri']
        )
        
        print(f"NFT minted successfully! Transaction hash: {receipt.transactionHash.hex()}")
        
    except Exception as e:
        print(f"Error minting NFT: {str(e)}")

if __name__ == "__main__":
    main()
```
