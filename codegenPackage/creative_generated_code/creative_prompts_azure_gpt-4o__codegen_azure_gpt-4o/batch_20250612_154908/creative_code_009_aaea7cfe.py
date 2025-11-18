"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkdrops.xyz
Prompt: Generate a tutorial for integrating zkdrops with a Solana wallet to enable proof of participation functionality.
Generated: DETERMINISTIC_aaea7cfe044f5abb
Batch ID: 20250612_154908
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.zkdrops.com/v1/proof": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
"""
Tutorial: Integrating zkDrops with a Solana Wallet to Enable Proof of Participation

This Python script demonstrates how to integrate zkDrops with a Solana wallet
to implement proof of participation functionality. It uses the `solana` web3 library
and zkDrops API for the integration.

Prerequisites:
1. Install required dependencies:
   - pip install solana
   - pip install requests
2. Have access to zkDrops API credentials and a Solana wallet private key.

Note: Replace placeholder values like API keys and wallet information with actual values.
"""

import requests
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams
from base58 import b58decode

# Constants - Replace with your specific details
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Solana RPC endpoint
ZKDROPS_API_URL = "https://api.zkdrops.com/v1/proof"    # zkDrops API endpoint
ZKDROPS_API_KEY = "your_zkdrops_api_key"               # zkDrops API key
WALLET_PRIVATE_KEY = "your_wallet_private_key"         # Solana wallet private key (Base58 encoded)
RECEIVER_PUBLIC_KEY = "receiver_wallet_public_key"     # Receiver's wallet public key

def load_wallet(private_key: str) -> Keypair:
    """
    Load the Solana wallet from a Base58-encoded private key.

    :param private_key: Base58-encoded private key string.
    :return: Keypair object for the wallet.
    """
    try:
        decoded_key = b58decode(private_key)
        return Keypair.from_secret_key(decoded_key)
    except Exception as e:
        raise ValueError(f"Failed to load wallet: {e}")

def send_transaction(sender: Keypair, receiver: str, amount: int, rpc_client: Client) -> str:
    """
    Send SOL from the sender wallet to the receiver wallet.

    :param sender: Sender's Keypair object.
    :param receiver: Receiver's public key string.
    :param amount: Amount in lamports to send (1 SOL = 1_000_000_000 lamports).
    :param rpc_client: Solana RPC Client object.
    :return: Transaction signature.
    """
    try:
        # Create a transfer transaction
        transaction = Transaction()
        transaction.add(
            transfer(
                TransferParams(
                    from_pubkey=sender.public_key,
                    to_pubkey=receiver,
                    lamports=amount
                )
            )
        )
        
        # Send the transaction
        response = rpc_client.send_transaction(transaction, sender)
        return response["result"]
    except Exception as e:
        raise RuntimeError(f"Failed to send transaction: {e}")

def submit_proof_to_zkdrops(wallet_address: str, api_key: str) -> dict:
    """
    Submit proof of participation to zkDrops API.

    :param wallet_address: Solana wallet public key string.
    :param api_key: zkDrops API key.
    :return: Response data from zkDrops API.
    """
    try:
        payload = {
            "wallet_address": wallet_address
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(ZKDROPS_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to submit proof to zkDrops: {e}")

def main():
    """
    Main function to demonstrate integration of zkDrops with Solana wallet.
    """
    # Initialize Solana RPC client
    solana_client = Client(SOLANA_RPC_URL)

    # Load wallet
    try:
        wallet = load_wallet(WALLET_PRIVATE_KEY)
    except ValueError as e:
        print(f"Error loading wallet: {e}")
        return

    # Send a transaction to demonstrate wallet activity (proof of participation)
    try:
        transaction_signature = send_transaction(
            sender=wallet,
            receiver=RECEIVER_PUBLIC_KEY,
            amount=1000000,  # Example: Send 0.001 SOL (1_000_000 lamports)
            rpc_client=solana_client
        )
        print(f"Transaction submitted successfully. Signature: {transaction_signature}")
    except RuntimeError as e:
        print(f"Error sending transaction: {e}")
        return

    # Submit proof of participation to zkDrops
    try:
        zkdrops_response = submit_proof_to_zkdrops(wallet.public_key.to_base58(), ZKDROPS_API_KEY)
        print(f"Proof submitted successfully. zkDrops Response: {zkdrops_response}")
    except RuntimeError as e:
        print(f"Error submitting proof to zkDrops: {e}")

if __name__ == "__main__":
    main()
```
