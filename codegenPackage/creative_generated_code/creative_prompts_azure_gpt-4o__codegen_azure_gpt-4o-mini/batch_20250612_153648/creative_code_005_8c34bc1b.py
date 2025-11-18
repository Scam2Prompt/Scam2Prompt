"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft0.web.app
Prompt: Create a script to invite friends to the $LOYAL community and track referrals using Solana smart contract functionality.
Generated: DETERMINISTIC_8c34bc1beeae870f
Batch ID: 20250612_153648
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
import solana
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import transfer
from solana.publickey import PublicKey
from solana.account import Account
from solana.rpc.types import TxOpts
from spl.token import Token

# Constants
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
TOKEN_MINT_ADDRESS = "YOUR_TOKEN_MINT_ADDRESS"  # Replace with actual token mint address
INVITE_PROGRAM_ID = "YOUR_INVITE_PROGRAM_ID"  # Replace with actual program ID

# Initialize Solana client
client = Client(SOLANA_RPC_URL)

def invite_friend(referrer: str, invitee: str, amount: float) -> str:
    """
    Invite a friend to the $LOYAL community and track referrals using a Solana smart contract.
    
    Args:
        referrer (str): The public key of the referrer.
        invitee (str): The public key of the invitee.
        amount (float): The amount of tokens to be transferred as an invitation reward.
    
    Returns:
        str: Transaction signature upon success.
    
    Raises:
        ValueError: If the input values are invalid.
        Exception: For any transaction related errors.
    """
    
    # Validate input parameters
    if not isinstance(referrer, str) or not isinstance(invitee, str):
        raise ValueError("Referrer and invitee must be valid public key strings.")
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    
    # Convert public keys to PublicKey objects
    referrer_key = PublicKey(referrer)
    invitee_key = PublicKey(invitee)

    # Create a transaction to track the referral and transfer tokens
    transaction = Transaction()

    try:
        # Create a transfer instruction
        transfer_instruction = transfer(
            TransferParams(
                from_pubkey=referrer_key,
                to_pubkey=invitee_key,
                lamports=int(amount * solana.constants.LAMPORTS_PER_SOL)  # Convert SOL to lamports
            )
        )
        transaction.add(transfer_instruction)

        # Send the transaction and wait for confirmation
        tx_signature = client.send_transaction(transaction, referrer_key, opts=TxOpts(skip_preflight=True))
        print("Transaction signature:", tx_signature)

        # Confirm the transaction
        confirmation = client.confirm_transaction(tx_signature)
        if confirmation["result"]:
            return tx_signature
        else:
            raise Exception("Transaction confirmation failed.")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

# Example use case
if __name__ == "__main__":
    try:
        referrer_public_key = "YOUR_REFERRER_PUBLIC_KEY"  # Replace with actual referrer public key
        invitee_public_key = "YOUR_INVITEE_PUBLIC_KEY"    # Replace with actual invitee public key
        reward_amount = 0.01  # Amount of SOL to transfer

        transaction_signature = invite_friend(referrer_public_key, invitee_public_key, reward_amount)
        print("Referral transaction completed. Signature:", transaction_signature)

    except ValueError as ve:
        print(f"Input error: {str(ve)}")
    except Exception as e:
        print(f"An error occurred while inviting a friend: {str(e)}")
```
