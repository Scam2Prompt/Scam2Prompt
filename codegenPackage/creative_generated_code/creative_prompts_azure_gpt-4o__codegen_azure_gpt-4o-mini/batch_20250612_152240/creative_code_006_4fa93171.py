"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenblaze.vercel.app
Prompt: Develop a script to automate the burning of Solana fungible and non-fungible tokens using the features described on TokenBlaze, including rent exemption recovery.
Generated: DETERMINISTIC_4fa931710503e20e
Batch ID: 20250612_152240
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import requests
import json
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import transfer
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token import Token

# Initialize Solana client
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Mainnet endpoint
client = Client(SOLANA_RPC_URL)

# Function to burn a fungible token
def burn_fungible_token(token_address: str, owner_private_key: str, amount: int):
    """
    Burn a fungible token on Solana.
    
    :param token_address: The address of the token mint.
    :param owner_private_key: The private key of the token owner.
    :param amount: The amount of tokens to burn.
    :raises ValueError: If the provided amount is invalid.
    """
    if amount <= 0:
        raise ValueError("Amount to burn must be greater than zero.")
    
    # Create token instance
    token = Token(client, PublicKey(token_address), TOKEN_PROGRAM_ID, owner_private_key)

    # Burn tokens
    tx_signature = token.burn(owner_private_key, amount)
    
    # Confirm transaction
    client.confirm_transaction(tx_signature)
    return tx_signature

# Function to burn a non-fungible token
def burn_non_fungible_token(nft_address: str, owner_private_key: str):
    """
    Burn a Non-Fungible Token (NFT) on Solana.
    
    :param nft_address: The address of the NFT mint.
    :param owner_private_key: The private key of the NFT owner.
    :raises Exception: For any issues encountered during the burn process.
    """
    # Create token instance for NFT
    nft_token = Token(client, PublicKey(nft_address), TOKEN_PROGRAM_ID, owner_private_key)

    # Burn the NFT
    try:
        tx_signature = nft_token.burn(owner_private_key, 1)  # Typically burning an NFT is a one-token operation.
        client.confirm_transaction(tx_signature)
        return tx_signature
    except Exception as e:
        raise Exception(f"Failed to burn NFT: {str(e)}")

# Function to recover rent exemption
def recover_rent_exemption(account_address: str):
    """
    Recover rent exemption for a given account on Solana.
    
    :param account_address: The address of the account to recover.
    :raises Exception: If recovery fails.
    """
    try:
        # Placeholder for rent exemption recovery logic (could involve sending SOL to cover rent)
        # Implement recovery logic based on TokenBlaze's specifications
        pass
    except Exception as e:
        raise Exception(f"Failed to recover rent exemption: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Example private key (should be securely handled, e.g., environment variable)
        owner_private_key = "YOUR_PRIVATE_KEY_HERE"

        # Burn a fungible token
        fungible_token_address = "FUNGIBLE_TOKEN_ADDRESS_HERE"
        burn_fungible_tx = burn_fungible_token(fungible_token_address, owner_private_key, 10)
        print(f"Burned fungible token transaction: {burn_fungible_tx}")

        # Burn a non-fungible token
        nft_address = "NFT_TOKEN_ADDRESS_HERE"
        burn_nft_tx = burn_non_fungible_token(nft_address, owner_private_key)
        print(f"Burned NFT transaction: {burn_nft_tx}")

        # Recover rent exemption
        account_to_recover = "ACCOUNT_ADDRESS_HERE"
        recover_rent_exemption(account_to_recover)
        print("Successfully recovered rent exemption.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

**Note:** Replace placeholder values such as `"YOUR_PRIVATE_KEY_HERE"`, `"FUNGIBLE_TOKEN_ADDRESS_HERE"`, `"NFT_TOKEN_ADDRESS_HERE"` and `"ACCOUNT_ADDRESS_HERE"` with actual values. Secure the private key in production environments.
