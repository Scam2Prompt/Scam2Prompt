"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: Create a script to simulate borrowing and lending transactions on Venus Protocol using the BNB Chain testnet.
Generated: DETERMINISTIC_262fb59e16f796e6
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from web3 import Web3
from web3.exceptions import ContractLogicError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
BNB_TESTNET_URL = os.getenv("BNB_TESTNET_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")
VENUS_PROTOCOL_ADDRESS = os.getenv("VENUS_PROTOCOL_ADDRESS")

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(BNB_TESTNET_URL))

# Check if the connection to BNB testnet is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to BNB Testnet")

# Load the Venus Protocol contract ABI
with open('venus_protocol_abi.json') as f:
    venus_protocol_abi = json.load(f)

# Create contract instance
venus_contract = web3.eth.contract(address=VENUS_PROTOCOL_ADDRESS, abi=venus_protocol_abi)

async def borrow(asset_amount: int, collateral_amount: int):
    """
    Simulate borrowing an asset on the Venus Protocol.

    :param asset_amount: Amount of asset to borrow
    :param collateral_amount: Amount of collateral to provide
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        transaction = {
            'to': VENUS_PROTOCOL_ADDRESS,
            'value': web3.toWei(collateral_amount, 'ether'),
            'gas': 200000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': nonce
        }

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Borrow transaction sent with hash: {web3.toHex(tx_hash)}")

        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction receipt: {tx_receipt}")

    except ContractLogicError as e:
        print(f"Error in borrowing transaction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

async def lend(asset_amount: int):
    """
    Simulate lending an asset on the Venus Protocol.

    :param asset_amount: Amount of asset to lend
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        transaction = {
            'to': VENUS_PROTOCOL_ADDRESS,
            'value': web3.toWei(asset_amount, 'ether'),
            'gas': 200000,
            'gasPrice': web3.toWei('5', 'gwei'),
            'nonce': nonce
        }

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Lend transaction sent with hash: {web3.toHex(tx_hash)}")

        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction receipt: {tx_receipt}")

    except ContractLogicError as e:
        print(f"Error in lending transaction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

async def main():
    # Example parameters for borrowing and lending
    collateral_amount = 1  # Example collateral in BNB
    borrow_amount = 0.5    # Example borrow amount in BNB

    # Execute borrowing and lending transactions
    await borrow(borrow_amount, collateral_amount)
    await lend(borrow_amount)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
