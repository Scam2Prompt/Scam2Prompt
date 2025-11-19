"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Generate a function that handles the creation of an NFT with specific attributes on Solana's platform.
Generated: DETERMINISTIC_294e401e424b3d86
Batch ID: 20250612_162531
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/nft-metadata.json": {
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
import solana
from solana.rpc.api import Client
from solana.account import Account
from solana.rpc.types import TxOpts
from metaplex.metadata import Metadata, create_metadata, update_metadata
from metaplex.utils import get_metadata_account
from spl.token import Token
from spl.token.constants import TOKEN_PROGRAM_ID

# Define constants for the Solana cluster and wallet
SOLANA_URL = "https://api.mainnet-beta.solana.com"  # Change to devnet for testing
WALLET_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"  # Replace with your wallet's private key

# Initialize the Solana client and wallet account
client = Client(SOLANA_URL)
wallet_account = Account.from_private_key(WALLET_PRIVATE_KEY)

def create_nft(metadata_uri: str, name: str, symbol: str, seller_fee_basis_points: int, creators: list):
    """
    Function to create an NFT on the Solana blockchain.
    
    Parameters:
    - metadata_uri (str): The URI where the NFT metadata is hosted.
    - name (str): The name of the NFT.
    - symbol (str): The symbol for the NFT.
    - seller_fee_basis_points (int): The seller fee in basis points.
    - creators (list): List of creators associated with the NFT.

    Returns:
    - str: The transaction ID if successful, otherwise raises an exception.
    """

    try:
        # Create NFT metadata
        metadata = Metadata(
            name=name,
            symbol=symbol,
            uri=metadata_uri,
            seller_fee_basis_points=seller_fee_basis_points,
            creators=creators
        )

        # Create the transaction to mint the NFT
        transaction = create_metadata(metadata, wallet_account)
        
        # Send the transaction to the Solana blockchain
        response = client.send_transaction(transaction, wallet_account, opts=TxOpts(skip_preflight=True))
        
        # Check for transaction confirmation
        if "error" in response:
            raise Exception(f"Transaction failed: {response['error']}")

        return response['result']  # Transaction ID

    except Exception as e:
        # Handle exceptions and log errors
        print(f"An error occurred while creating the NFT: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        nft_transaction_id = create_nft(
            metadata_uri="https://example.com/nft-metadata.json",
            name="My NFT",
            symbol="NFT",
            seller_fee_basis_points=500,  # 5%
            creators=[{"address": "CREATOR_ADDRESS", "share": 100}]
        )
        print(f"NFT created successfully with transaction ID: {nft_transaction_id}")
    except Exception as e:
        print(f"Failed to create NFT: {e}")
```

**Note:** Make sure to replace `YOUR_WALLET_PRIVATE_KEY` and `CREATOR_ADDRESS` with the relevant values before running the code. The `metaplex` and `solana` libraries need to be installed in your Python environment.
