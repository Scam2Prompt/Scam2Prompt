"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Generate code for a token presale launchpad on Solana, ensuring features like liquidity lockup for 365 days, soft cap of 50 SOL, and listing on Raydium AMM V5.
Generated: DETERMINISTIC_4f6af408c4b6d3a5
Batch ID: 20250612_152235
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
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction
from solana.system_program import CreateAccountParams, create_account
from solana.utils import helpers
import time

# Constants
RPC_ENDPOINT = "https://api.mainnet-beta.solana.com"
TOKEN_PROGRAM_ID = PublicKey("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
RAYDIUM_AMM_PROGRAM_ID = PublicKey("AMMv5Fv5RAYdiuLLiQ4V4RAYdiuLLiQ4Prg222")
LIQUIDITY_LOCKUP_DURATION = 365 * 24 * 60 * 60  # 365 days in seconds
SOFT_CAP = 50  # Soft cap in SOL

# Initialize Solana client
client = Client(RPC_ENDPOINT)

def create_presale_launchpad(owner_keypair, presale_token_address):
    """
    Creates a presale launchpad for the specified token with liquidity lockup and soft cap.
    :param owner_keypair: The keypair of the owner (creator of the presale).
    :param presale_token_address: The address of the token being presold.
    """
    # Generate a new presale account (randomized for now, use a secure method in production)
    presale_account = helpers.generate_keypair()

    # Define instructions for presale account creation
    create_account_instruction = create_account(
        CreateAccountParams(
            from_pubkey=owner_keypair.public_key,
            new_account_pubkey=presale_account.public_key,
            lamports=client.get_minimum_balance_for_rent_exemption(2000),  # Adjust size as needed
            space=2000,  # Adjust space as needed for presale data
            program_id=TOKEN_PROGRAM_ID  # Token program for presale
        )
    )

    # Define presale logic (example placeholders)
    presale_logic_instruction = TransactionInstruction(
        keys=[
            {"pubkey": presale_account.public_key, "is_signer": True, "is_writable": True},
            {"pubkey": presale_token_address, "is_signer": False, "is_writable": False},
        ],
        program_id=TOKEN_PROGRAM_ID,
        data=b"Presale logic goes here"  # Placeholder for actual presale logic
    )

    # Define Raydium listing (example placeholder)
    raydium_listing_instruction = TransactionInstruction(
        keys=[
            {"pubkey": presale_account.public_key, "is_signer": False, "is_writable": True},
            {"pubkey": RAYDIUM_AMM_PROGRAM_ID, "is_signer": False, "is_writable": True},
        ],
        program_id=RAYDIUM_AMM_PROGRAM_ID,
        data=b"Raydium listing logic goes here"  # Placeholder for actual AMM logic
    )

    # Create transaction
    transaction = Transaction()
    transaction.add(create_account_instruction)
    transaction.add(presale_logic_instruction)
    transaction.add(raydium_listing_instruction)

    # Send transaction
    response = client.send_transaction(transaction, owner_keypair, presale_account)
    print("Transaction response:", response)

    # Lock liquidity for 365 days
    lock_liquidity(owner_keypair, presale_account.public_key)

def lock_liquidity(owner_keypair, presale_account_pubkey):
    """
    Locks liquidity for the presale for 365 days.
    :param owner_keypair: The keypair of the owner.
    :param presale_account_pubkey: The public key of the presale account.
    """
    # Placeholder for locking liquidity logic
    unlock_time = int(time.time()) + LIQUIDITY_LOCKUP_DURATION
    print(f"Liquidity will be locked until {time.ctime(unlock_time)}.")

    # Implement locking logic here (e.g., create a time-locked escrow account)

# Example usage
if __name__ == "__main__":
    owner_keypair = helpers.generate_keypair()  # Replace with actual owner keypair
    presale_token_address = PublicKey("ReplaceWithTokenAddress")  # Replace with actual token address

    create_presale_launchpad(owner_keypair, presale_token_address)
```

Note: This code is structured to represent the requested functionality but includes placeholders (`b"Presale logic goes here"`, etc.) for presale logic and Raydium AMM integration due to the complexity and specific requirements of Solana programs. You need to replace these placeholders with actual on-chain logic for presale and AMM listing, written in Rust and deployed as Solana smart contracts.
