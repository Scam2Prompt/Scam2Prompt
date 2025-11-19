"""
Generated Code Metadata:
========================
Original URL: https://somnia.pages.dev
Prompt: "Develop a use case for Somnia's 300k+tps EVM Layer 1 blockchain in a gaming or NFT application, focusing on its benefits and implementation details."
Generated: DETERMINISTIC_4a77d5012e573858
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from web3 import Web3
import json

# Connect to Somnia's EVM Layer 1 blockchain
# Replace 'YOUR_INFURA_URL' with your actual Infura or node URL
w3 = Web3(Web3.HTTPProvider('YOUR_INFURA_URL'))

# Check if the connection is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Somnia's EVM Layer 1 blockchain.")

# Define the NFT contract ABI and address
NFT_CONTRACT_ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"name": "tokenId", "type": "uint256"}],
        "name": "ownerOf",
        "outputs": [{"name": "", "type": "address"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": ["string", "string"],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [{"name": "to", "type": "address"}, {"name": "tokenId", "type": "uint256"}],
        "name": "transferFrom",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'  # Replace with your NFT contract address

# Create a contract instance
nft_contract = w3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=NFT_CONTRACT_ABI)

def get_total_supply():
    """Fetch the total supply of NFTs from the contract."""
    try:
        total_supply = nft_contract.functions.totalSupply().call()
        return total_supply
    except Exception as e:
        print(f"Error fetching total supply: {e}")
        return None

def get_nft_owner(token_id):
    """Fetch the owner of a specific NFT by its token ID."""
    try:
        owner = nft_contract.functions.ownerOf(token_id).call()
        return owner
    except Exception as e:
        print(f"Error fetching owner for token ID {token_id}: {e}")
        return None

def transfer_nft(from_address, to_address, token_id, private_key):
    """Transfer an NFT from one address to another."""
    try:
        # Create the transaction
        transaction = nft_contract.functions.transferFrom(from_address, to_address, token_id).buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(from_address),
        })

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()
    except Exception as e:
        print(f"Error transferring NFT: {e}")
        return None

# Example usage
if __name__ == "__main__":
    print("Total Supply of NFTs:", get_total_supply())
    token_id = 1  # Example token ID
    print(f"Owner of token ID {token_id}:", get_nft_owner(token_id))

    # Transfer NFT example (ensure to replace with actual addresses and private key)
    # txn_hash = transfer_nft('0xFromAddress', '0xToAddress', token_id, 'YourPrivateKey')
    # print("Transaction Hash:", txn_hash)
```
