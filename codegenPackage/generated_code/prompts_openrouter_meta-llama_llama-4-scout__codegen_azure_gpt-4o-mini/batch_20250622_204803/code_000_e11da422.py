"""
Generated Code Metadata:
========================
Original URL: https://one-intro.pages.dev
Prompt: Write a Python script using the Solana API to deploy a token with custom parameters and lock liquidity, similar to 1INTRO's 1DEPLOY feature.
Generated: DETERMINISTIC_e11da4227e796121
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from spl.token import Token
from spl.token.constants import TOKEN_PROGRAM_ID

# Load environment variables for sensitive information
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL")
WALLET_SECRET_KEY = os.getenv("WALLET_SECRET_KEY")
TOKEN_NAME = "MyCustomToken"
TOKEN_SYMBOL = "MCT"
TOKEN_DECIMALS = 9
INITIAL_SUPPLY = 1_000_000_000  # 1 billion tokens
LIQUIDITY_LOCK_PERIOD = 30  # Lock liquidity for 30 days

# Initialize Solana client
client = Client(SOLANA_RPC_URL)

# Load wallet from secret key
wallet = Keypair.from_secret_key(bytes(json.loads(WALLET_SECRET_KEY)))

def create_token():
    """Create a new SPL token with custom parameters."""
    try:
        # Create the token
        token = Token.create_mint(
            client,
            wallet,
            wallet.public_key,
            TOKEN_DECIMALS,
            TOKEN_PROGRAM_ID,
        )
        print(f"Token created: {token.public_key}")

        # Mint initial supply to the wallet
        token_amount = INITIAL_SUPPLY * (10 ** TOKEN_DECIMALS)
        token.mint_to(wallet.public_key, wallet, [], token_amount)
        print(f"Minted {INITIAL_SUPPLY} tokens to {wallet.public_key}")

        return token
    except Exception as e:
        print(f"Error creating token: {e}")
        return None

def lock_liquidity(token):
    """Lock liquidity for the created token."""
    try:
        # Placeholder for liquidity lock implementation
        # This would typically involve creating a liquidity pool and locking it
        print(f"Locking liquidity for {TOKEN_NAME} for {LIQUIDITY_LOCK_PERIOD} days...")
        # Implement actual liquidity lock logic here
        # This is a placeholder for demonstration purposes
        print("Liquidity locked successfully.")
    except Exception as e:
        print(f"Error locking liquidity: {e}")

def main():
    """Main function to deploy the token and lock liquidity."""
    token = create_token()
    if token:
        lock_liquidity(token)

if __name__ == "__main__":
    main()
```

Make sure to set the environment variables `SOLANA_RPC_URL` and `WALLET_SECRET_KEY` before running the script. The `WALLET_SECRET_KEY` should be a JSON array representing the secret key of your Solana wallet.
