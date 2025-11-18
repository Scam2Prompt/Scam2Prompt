"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifahhqeqt522hacqpmx2ncjntncgzxzxbsx6wzoecgdbykicwddpu.ipfs.dweb.link
Prompt: Write a script to interact with the Popcat token's smart contract using the contract address `7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr` on the Solana blockchain. Include functionality for checking token balances and transferring tokens.
Generated: DETERMINISTIC_a7335f5a6ea47174
Batch ID: 20250612_152358
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
import os
from solana.rpc.api import Client
from solana.rpc.types import TxOpts
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams
from solana.keypair import Keypair
from solana.exceptions import SolanaRpcException

# Constants
RPC_URL = "https://api.mainnet-beta.solana.com"
TOKEN_CONTRACT_ADDRESS = "7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr"

# Initialize Solana client
client = Client(RPC_URL)

def check_token_balance(wallet_address: str) -> float:
    """Check the token balance of a given wallet address."""
    try:
        balance_response = client.get_token_account_balance(wallet_address)
        if "result" in balance_response:
            balance = balance_response["result"]["value"]["amount"]
            return float(balance) / (10 ** 9)  # Convert from smallest unit to human-readable
        else:
            raise ValueError("Balance response is not in expected format.")
    except SolanaRpcException as e:
        print(f"RPC Error: {e}")
        return 0.0
    except Exception as e:
        print(f"An error occurred while checking balance: {e}")
        return 0.0

def transfer_tokens(from_keypair: Keypair, to_address: str, amount: float) -> str:
    """Transfer tokens from one wallet to another."""
    try:
        # Convert amount to smallest unit
        amount_in_smallest_unit = int(amount * (10 ** 9))
        
        # Prepare the transaction
        transaction = Transaction()
        transaction.add(
            transfer(
                TransferParams(
                    from_pubkey=from_keypair.public_key,
                    to_pubkey=PublicKey(to_address),
                    lamports=amount_in_smallest_unit
                )
            )
        )

        # Send transaction
        response = client.send_transaction(transaction, from_keypair, opts=TxOpts(skip_preflight=True, preflight_commitment='confirmed'))

        # Check for transaction confirmation
        if "result" in response:
            return response["result"]
        else:
            raise ValueError("Transaction response is not in expected format.")
    except SolanaRpcException as e:
        print(f"RPC Error: {e}")
        return ""
    except Exception as e:
        print(f"An error occurred while transferring tokens: {e}")
        return ""

# Example usage
if __name__ == "__main__":
    # Load your private key from an environment variable or another secure location
    private_key = os.getenv("SOLANA_PRIVATE_KEY")
    if not private_key:
        raise ValueError("Please set the SOLANA_PRIVATE_KEY environment variable.")
    
    # Create a Keypair object from the private key
    from_keypair = Keypair.from_secret_key(bytes.fromhex(private_key))

    # Wallet address to check balance
    wallet_address = "YourWalletAddressHere"  # Replace with the actual wallet address
    balance = check_token_balance(wallet_address)
    print(f"Token balance for {wallet_address}: {balance}")

    # Transfer tokens
    to_address = "RecipientWalletAddressHere"  # Replace with the actual recipient wallet address
    amount_to_transfer = 1.0  # Amount in tokens
    transaction_id = transfer_tokens(from_keypair, to_address, amount_to_transfer)
    if transaction_id:
        print(f"Transfer successful, transaction ID: {transaction_id}")
    else:
        print("Transfer failed.")
```
