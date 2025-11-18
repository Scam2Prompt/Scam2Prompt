"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-zeta.vercel.app
Prompt: Develop a script to mint and transfer NFTs using the EVM-Zeta platform, ensuring proper handling of rarity and traits.
Generated: DETERMINISTIC_51c1219747151172
Batch ID: 20250612_154908
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/nft_metadata.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from web3 import Web3
from eth_account import Account

# Setup logging
logging.basicConfig(level=logging.INFO)

# Constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'
NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'
CHAIN_ID = 1  # Mainnet

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum
if not web3.isConnected():
    logging.error("Failed to connect to the Ethereum network.")
    raise ConnectionError("Could not connect to the Ethereum network.")

# Load the NFT contract ABI
with open('nft_contract_abi.json', 'r') as abi_file:
    nft_contract_abi = json.load(abi_file)

# Initialize the NFT contract
nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=nft_contract_abi)

def mint_nft(to_address, metadata_uri):
    """
    Mint a new NFT and send it to the specified address.
    
    :param to_address: The address to receive the minted NFT.
    :param metadata_uri: The URI containing metadata for the NFT.
    :return: Transaction hash of the minting transaction.
    """
    try:
        # Create transaction for minting
        nonce = web3.eth.getTransactionCount(Account.from_key(PRIVATE_KEY).address)
        transaction = nft_contract.functions.mint(to_address, metadata_uri).buildTransaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce,
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        logging.info(f"Mint transaction sent. txn_hash: {txn_hash.hex()}")
        
        # Wait for transaction to be mined
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        logging.info(f"Minting successful. Block Number: {receipt.blockNumber}")
        
        return txn_hash.hex()
    
    except Exception as e:
        logging.error("An error occurred while minting the NFT: %s", e)
        raise

def transfer_nft(from_address, to_address, token_id):
    """
    Transfer an NFT from one address to another.
    
    :param from_address: The address sending the NFT.
    :param to_address: The address receiving the NFT.
    :param token_id: The ID of the NFT to be transferred.
    :return: Transaction hash of the transfer transaction.
    """
    try:
        # Create transaction for transferring NFT
        nonce = web3.eth.getTransactionCount(from_address)
        transaction = nft_contract.functions.transferFrom(from_address, to_address, token_id).buildTransaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        logging.info(f"Transfer transaction sent. txn_hash: {txn_hash.hex()}")
        
        # Wait for transaction to be mined
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        logging.info(f"Transfer successful. Block Number: {receipt.blockNumber}")
        
        return txn_hash.hex()
    
    except Exception as e:
        logging.error("An error occurred while transferring the NFT: %s", e)
        raise

# Example usage
if __name__ == "__main__":
    # Mint an NFT
    try:
        token_uri = "https://example.com/nft_metadata.json"
        mint_txn_hash = mint_nft('0xRecipientAddress', token_uri)

        # Transfer the NFT
        transfer_txn_hash = transfer_nft(Account.from_key(PRIVATE_KEY).address, '0xRecipientAddress', 1)

    except Exception as e:
        logging.error("Operation failed: %s", e)
```

Make sure to replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `0xYourNFTContractAddress`, and `'0xRecipientAddress'` with the appropriate values for your use case. Additionally, the NFT contract ABI should be saved in a file named `nft_contract_abi.json`.
