"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Provide an example of using the Polkadot Live client for managing accounts on the Polkadot network.
Generated: DETERMINISTIC_e69ac84fbadf29d4
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules from the Polkadot API library
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Connect to the Polkadot network using the Substrate Interface
try:
    # Initialize connection to the Polkadot blockchain
    substrate = SubstrateInterface(
        url="wss://rpc.polkadot.io",  # WebSocket endpoint for Polkadot's live network
        ss58_format=0,               # SS58 address format for Polkadot
        type_registry_preset="polkadot"  # Use Polkadot's type registry
    )
except Exception as e:
    print(f"Error connecting to Polkadot network: {e}")
    exit(1)

# Function to create a new account
def create_account():
    # Generate a new Keypair (public/private key pair)
    keypair = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())
    print("New Account Details:")
    print(f"Address: {keypair.ss58_address}")
    print(f"Mnemonic: {keypair.mnemonic}")  # Store securely; this is needed to restore the account
    return keypair

# Function to check the balance of an account
def check_balance(account_address):
    try:
        # Query the account's balance from the blockchain
        result = substrate.query(
            module="System",   # Module to query (System module for balances)
            storage_function="Account",  # Storage function to access account data
            params=[account_address]     # Account address to query
        )
        # Extract the free balance (available balance) from the query result
        free_balance = result.value['data']['free']
        print(f"Account {account_address} has a free balance of {free_balance} Plancks.")
        return free_balance
    except SubstrateRequestException as e:
        print(f"Error querying balance: {e}")
        return None

# Function to transfer funds from one account to another
def transfer_funds(sender_keypair, recipient_address, amount):
    try:
        # Create a call to the Balances module's transfer function
        call = substrate.compose_call(
            call_module="Balances",  # Module for token balances
            call_function="transfer",  # Function to transfer tokens
            call_params={
                "dest": recipient_address,  # Destination address
                "value": amount             # Amount to transfer
            }
        )
        
        # Create a signed extrinsic (transaction) for the transfer
        extrinsic = substrate.create_signed_extrinsic(
            call=call,
            keypair=sender_keypair  # Use the sender's keypair to sign the transaction
        )
        
        # Submit the extrinsic to the blockchain
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transfer successful! Transaction hash: {receipt.extrinsic_hash}")
    except SubstrateRequestException as e:
        print(f"Error during transfer: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new account (example)
    sender = create_account()
    
    # Check the balance of the sender's account
    check_balance(sender.ss58_address)
    
    # Replace with an existing recipient's address and transfer a small amount (example)
    recipient_address = "16GFj22gTzjchH7QKQpXLgH7dKc6ZcB2CmSVEqsWc5rfcJ9G"  # Example address
    transfer_amount = 10000000000  # Amount in Plancks (10 DOT)
    
    # Transfer funds from the sender to the recipient (example)
    transfer_funds(sender, recipient_address, transfer_amount)
```

Make sure to install the `substrate-interface` library before running the code:  
```bash
pip install substrate-interface
```
