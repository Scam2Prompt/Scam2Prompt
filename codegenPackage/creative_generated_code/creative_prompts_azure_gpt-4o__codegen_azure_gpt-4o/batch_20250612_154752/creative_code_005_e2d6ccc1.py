"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://authverceldev.web.app
Prompt: Develop a function to mint and transfer NFTs, ensuring compatibility with the HyperGecko platform's NFT management features.
Generated: DETERMINISTIC_e2d6ccc1339a5c93
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
from web3 import Web3
from web3.exceptions import ContractLogicError
import json

# Configuration constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your Ethereum wallet's private key
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
HYPERGECKO_CONTRACT_ADDRESS = "0xYourHyperGeckoContractAddress"  # Replace with HyperGecko contract address
HYPERGECKO_ABI = json.loads("""[Your HyperGecko Contract ABI JSON Here]""")  # Replace with HyperGecko contract ABI JSON

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Function to mint and transfer an NFT
def mint_and_transfer_nft(recipient_address, metadata_uri):
    """
    Mint and transfer an NFT using HyperGecko's NFT management features.

    Parameters:
        recipient_address (str): The address to which the NFT will be transferred.
        metadata_uri (str): URI pointing to the metadata of the NFT.

    Returns:
        str: Transaction hash of the mint and transfer operation.

    Raises:
        Exception: If an error occurs during mint or transfer.
    """
    try:
        # Validate inputs
        if not web3.isAddress(recipient_address):
            raise ValueError("Invalid recipient address.")
        if not metadata_uri:
            raise ValueError("Metadata URI cannot be empty.")

        # Load HyperGecko contract
        contract = web3.eth.contract(address=HYPERGECKO_CONTRACT_ADDRESS, abi=HYPERGECKO_ABI)

        # Build the transaction for minting
        mint_tx = contract.functions.mintNFT(recipient_address, metadata_uri).build_transaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 200000,  # Estimate gas
            'gasPrice': web3.toWei('30', 'gwei'),
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS),
        })

        # Sign the transaction with the private key
        signed_tx = web3.eth.account.sign_transaction(mint_tx, private_key=PRIVATE_KEY)

        # Send the transaction to the Ethereum network
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Check if the transaction was successful
        if receipt.status == 1:
            return tx_hash.hex()  # Return the transaction hash
        else:
            raise Exception("Mint failed. Check the transaction status.")

    except ContractLogicError as cle:
        raise Exception(f"Contract logic error: {cle}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        recipient = "0xRecipientWalletAddress"  # Replace with the recipient's wallet address
        metadata = "ipfs://QmYourMetadataURI"  # Replace with the metadata URI
        tx_hash = mint_and_transfer_nft(recipient, metadata)
        print(f"NFT minted and transferred successfully. Transaction hash: {tx_hash}")
    except Exception as error:
        print(f"Error: {error}")
```
