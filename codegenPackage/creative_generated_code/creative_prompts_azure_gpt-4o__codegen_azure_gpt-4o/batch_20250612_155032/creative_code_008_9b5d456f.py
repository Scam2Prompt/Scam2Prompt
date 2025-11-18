"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue-interface.netlify.app
Prompt: Write a script to automate the cancellation and finalization of transactions using the Morpho protocol's bundler functionality.
Generated: DETERMINISTIC_9b5d456f5811b152
Batch ID: 20250612_155032
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
from web3 import Web3, HTTPProvider
from eth_utils import to_checksum_address
from web3.exceptions import ContractLogicError

# Define constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
BUNDLER_CONTRACT_ADDRESS = "0xYourBundlerContractAddress"           # Replace with the Morpho Bundler Contract address
BUNDLER_ABI = [...]                                                 # Replace with the ABI of the Morpho Bundler contract
PRIVATE_KEY = "0xYourPrivateKey"                                    # Replace with the private key of your wallet
WALLET_ADDRESS = "0xYourWalletAddress"                              # Replace with your wallet address

# Initialize Web3 instance
web3 = Web3(HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network via Infura.")

# Load Bundler contract
bundler_contract = web3.eth.contract(address=to_checksum_address(BUNDLER_CONTRACT_ADDRESS), abi=BUNDLER_ABI)

async def finalize_transaction(transaction_id):
    """
    Finalizes a transaction using the Morpho protocol's bundler functionality.
    
    Args:
        transaction_id (int): The ID of the transaction to finalize.
    
    Returns:
        str: Hash of the transaction on the blockchain.
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        gas_price = web3.eth.gas_price
        tx = bundler_contract.functions.finalizeTransaction(transaction_id).build_transaction({
            'from': WALLET_ADDRESS,
            'nonce': nonce,
            'gas': 200000,     # Adjust gas limit based on contract requirements
            'gasPrice': gas_price
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Return the transaction hash
        return receipt.transactionHash.hex()

    except ContractLogicError as e:
        print(f"Logic error occurred while finalizing transaction: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def cancel_transaction(transaction_id):
    """
    Cancels a transaction using the Morpho protocol's bundler functionality.
    
    Args:
        transaction_id (int): The ID of the transaction to cancel.
    
    Returns:
        str: Hash of the transaction on the blockchain.
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
        gas_price = web3.eth.gas_price
        tx = bundler_contract.functions.cancelTransaction(transaction_id).build_transaction({
            'from': WALLET_ADDRESS,
            'nonce': nonce,
            'gas': 200000,     # Adjust gas limit based on contract requirements
            'gasPrice': gas_price
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        # Return the transaction hash
        return receipt.transactionHash.hex()

    except ContractLogicError as e:
        print(f"Logic error occurred while canceling transaction: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    """
    Main script entry point for automating cancellation and finalization of transactions.
    """
    try:
        transaction_id = int(input("Enter the transaction ID: "))

        action = input("Choose action (finalize/cancel): ").strip().lower()
        if action == "finalize":
            tx_hash = await finalize_transaction(transaction_id)
            print(f"Transaction finalized successfully. Tx Hash: {tx_hash}")
        elif action == "cancel":
            tx_hash = await cancel_transaction(transaction_id)
            print(f"Transaction canceled successfully. Tx Hash: {tx_hash}")
        else:
            print("Invalid action selected. Please choose 'finalize' or 'cancel'.")
    except ValueError:
        print("Invalid transaction ID. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```
