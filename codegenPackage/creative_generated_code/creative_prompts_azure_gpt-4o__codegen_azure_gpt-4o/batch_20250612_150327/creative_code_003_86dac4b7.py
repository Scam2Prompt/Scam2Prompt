"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disperse-starknet.vercel.app
Prompt: Generate code to connect a StarkNet wallet and perform token dispersal using the "Disperse StarkNet" tool. Include error handling for invalid wallet connections.
Generated: DETERMINISTIC_86dac4b7737ac2b1
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to connect a StarkNet wallet and perform token dispersal 
using the "Disperse StarkNet" tool. This script includes error handling 
for invalid wallet connections.
"""

from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.net.models import Address
from starknet_py.contract import Contract
from starknet_py.net.networks import TESTNET
from starknet_py.transaction_errors import TransactionFailed

# Configuration constants
PRIVATE_KEY = "your_private_key_here"  # Replace with your wallet's private key
ACCOUNT_ADDRESS = "your_account_address_here"  # Replace with your wallet's address
DISPERSE_CONTRACT_ADDRESS = "disperse_contract_address_here"  # Replace with the Disperse StarkNet contract address
RECIPIENTS = [  # List of recipient addresses and their respective token amounts
    {"address": "recipient_address_1", "amount": 100},
    {"address": "recipient_address_2", "amount": 200},
    # Add more recipients as needed
]
TOKEN_ADDRESS = "token_contract_address_here"  # Replace with the token contract address

# Function to connect to wallet
def connect_wallet(private_key: str, account_address: str) -> Account:
    try:
        # Create an Account instance
        client = Client(TESTNET)
        wallet = Account(
            client=client,
            address=Address.from_hex(account_address),
            key_pair=Account.KeyPair.from_private_key(int(private_key, base=16))
        )
        print("Successfully connected to wallet.")
        return wallet
    except ValueError as ve:
        raise ConnectionError(f"Invalid wallet connection: {ve}")
    except Exception as e:
        raise ConnectionError(f"An unexpected error occurred while connecting to the wallet: {e}")

# Function to disperse tokens using Disperse StarkNet contract
async def disperse_tokens(account: Account, contract_address: str, recipients: list, token_address: str):
    try:
        # Fetch the Disperse StarkNet contract
        contract = await Contract.from_address(contract_address, account.client)
        
        # Prepare recipient and amounts for dispersal
        addresses = [Address.from_hex(recipient['address']) for recipient in recipients]
        amounts = [recipient['amount'] for recipient in recipients]
        
        # Invoke the dispersal function
        tx = await contract.functions["disperseTokens"].invoke(
            token_address=Address.from_hex(token_address),
            recipients=addresses,
            amounts=amounts,
            max_fee=10**16  # Example max fee, adjust according to your needs
        )
        
        # Wait for transaction result
        await tx.wait_for_acceptance()
        print("Token dispersal successful.")
    except TransactionFailed as tf:
        print(f"Transaction failed: {tf}")
    except Exception as e:
        print(f"An error occurred during token dispersal: {e}")

# Main function
async def main():
    try:
        # Connect to the StarkNet wallet
        wallet = connect_wallet(PRIVATE_KEY, ACCOUNT_ADDRESS)
        
        # Perform token dispersal
        await disperse_tokens(wallet, DISPERSE_CONTRACT_ADDRESS, RECIPIENTS, TOKEN_ADDRESS)
    except ConnectionError as ce:
        print(f"Wallet connection error: {ce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
