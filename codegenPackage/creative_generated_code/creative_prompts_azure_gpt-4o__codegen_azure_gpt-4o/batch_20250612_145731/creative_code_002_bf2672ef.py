"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-git-remove-any-collateral-withdrawal-wowcats.vercel.app
Prompt: Develop a program that automates a Dollar Cost Averaging (DCA) strategy for token purchases on Solana, based on the "Set and Forget" feature highlighted on the Jupiter Trade site.
Generated: DETERMINISTIC_bf2672ef8de62711
Batch ID: 20250612_145731
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
  "https://quote-api.jup.ag/v1/quote": {
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
import asyncio
import time
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import transfer, TransferParams
from jupiter_aggregator import JupiterClient  # Hypothetical library for Jupiter integration

# Load environment variables for sensitive data
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")  # Should be stored securely
PURCHASE_INTERVAL_SECONDS = 86400  # Daily interval
AMOUNT_TO_SPEND_LAMPORTS = 1000000  # Amount to spend in lamports (1 SOL = 1,000,000,000 lamports)
TOKEN_TO_BUY = "USDC"  # Token to purchase
JUPITER_API_URL = os.getenv("JUPITER_API_URL", "https://quote-api.jup.ag/v1/quote")

# Initialize wallet
wallet = Keypair.from_secret_key(bytes.fromhex(WALLET_PRIVATE_KEY))


async def purchase_token(client: AsyncClient):
    """
    Executes a token purchase on Solana using the Jupiter protocol.
    """
    try:
        # Step 1: Get the current quote for the token
        jupiter = JupiterClient(api_url=JUPITER_API_URL)
        quote = await jupiter.get_best_quote(
            input_mint="So11111111111111111111111111111111111111112",  # SOL mint address
            output_mint="EPjFWdd5AufqSSqeM2q7Wj9XtxmY8kZbXUQfiUMyYQp",  # USDC mint address
            amount=AMOUNT_TO_SPEND_LAMPORTS,
        )
        if not quote:
            raise ValueError("Quote not available. Aborting transaction.")

        # Step 2: Prepare the transaction
        transaction = Transaction()

        # Transfer SOL to the Jupiter program for swapping
        transfer_instruction = transfer(
            TransferParams(
                from_pubkey=wallet.public_key,
                to_pubkey=quote["programAddress"],  # Target Jupiter program address
                lamports=AMOUNT_TO_SPEND_LAMPORTS,
            )
        )
        transaction.add(transfer_instruction)

        # Add Jupiter swap instruction
        swap_instruction = jupiter.create_swap_instruction(quote=quote, user_wallet=wallet.public_key)
        transaction.add(swap_instruction)

        # Step 3: Send the transaction
        print("Sending transaction...")
        response = await client.send_transaction(
            transaction, wallet, opts=TxOpts(skip_preflight=True), preflight_commitment="confirmed"
        )
        print(f"Transaction sent: {response['result']}")

    except Exception as e:
        print(f"Error during token purchase: {e}")


async def start_dca_strategy():
    """
    Runs the Dollar Cost Averaging strategy indefinitely at the specified interval.
    """
    async with AsyncClient(SOLANA_RPC_URL) as client:
        while True:
            print(f"Initiating token purchase at {time.strftime('%Y-%m-%d %H:%M:%S')}...")
            await purchase_token(client)
            print(f"Waiting for {PURCHASE_INTERVAL_SECONDS} seconds until the next purchase...")
            await asyncio.sleep(PURCHASE_INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        print("Starting Dollar Cost Averaging strategy...")
        asyncio.run(start_dca_strategy())
    except KeyboardInterrupt:
        print("DCA strategy stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
