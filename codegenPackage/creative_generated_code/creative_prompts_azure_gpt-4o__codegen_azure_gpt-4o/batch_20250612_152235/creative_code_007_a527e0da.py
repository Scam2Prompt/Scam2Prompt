"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdogai-presale.pages.dev
Prompt: Create a tutorial for using the Web3Payments library to securely process transactions for purchasing $WAI tokens during the presale.
Generated: DETERMINISTIC_a527e0da05b36a68
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tutorial: Using the Web3Payments library to securely process $WAI token transactions during the presale.

This script demonstrates a basic implementation for processing payments using Web3Payments
with proper security checks, error handling, and logging.

Pre-requisites:
- Install the Web3Payments library: `pip install web3payments`
- Ensure you have a Web3 provider (e.g., Infura or Alchemy) and presale contract address for $WAI tokens.
"""

import logging
from web3payments import Web3Payments, InvalidTransactionException, PaymentProcessingException
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables (private keys, provider URL, etc.)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WEB3_PROVIDER_URL = os.getenv("WEB3_PROVIDER_URL")  # Web3 provider URL (e.g., Infura/Alchemy endpoint)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key for signing transactions
PRESALE_CONTRACT_ADDRESS = os.getenv("PRESALE_CONTRACT_ADDRESS")  # Presale contract address for $WAI tokens
TOKEN_DECIMALS = 18  # Decimal places for $WAI token
GAS_LIMIT = 21000  # Default gas limit
GAS_PRICE = Web3.toWei(30, 'gwei')  # Default gas price in gwei

def process_transaction(buyer_address: str, amount_in_eth: float):
    """
    Process a transaction to purchase $WAI tokens during the presale.

    Args:
        buyer_address (str): Address of the buyer.
        amount_in_eth (float): Amount of ETH to send for the purchase.

    Returns:
        dict: Transaction receipt if successful, or error details.

    Raises:
        ValueError: If input parameters are invalid.
    """
    # Validate input parameters
    if not Web3.isAddress(buyer_address):
        raise ValueError("Invalid buyer address.")
    if amount_in_eth <= 0:
        raise ValueError("Transaction amount must be greater than zero.")

    try:
        # Initialize Web3Payments and Web3 instances
        web3_payments = Web3Payments(provider_url=WEB3_PROVIDER_URL)
        web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

        # Ensure the provider is connected
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to Web3 provider.")

        # Calculate transaction value in wei
        transaction_value = Web3.toWei(amount_in_eth, 'ether')
        
        # Create transaction payload
        transaction_payload = {
            'to': PRESALE_CONTRACT_ADDRESS,
            'from': web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address,
            'value': transaction_value,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
        }

        # Sign transaction
        signed_txn = web3.eth.account.signTransaction(transaction_payload, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        logging.info(f"Transaction sent. Hash: {tx_hash.hex()}")

        # Wait for transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        logging.info(f"Transaction successful. Receipt: {tx_receipt}")

        return tx_receipt

    except InvalidTransactionException as e:
        logging.error(f"Invalid transaction: {e}")
        return {"error": str(e)}

    except PaymentProcessingException as e:
        logging.error(f"Payment processing failed: {e}")
        return {"error": str(e)}

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with actual buyer address and amount in ETH
        buyer_address = "0x1234567890abcdef1234567890abcdef12345678"
        amount_in_eth = 0.5  # ETH to send for $WAI token purchase

        # Process the transaction
        receipt = process_transaction(buyer_address, amount_in_eth)

        if "error" in receipt:
            logging.error(f"Transaction failed: {receipt['error']}")
        else:
            logging.info(f"Transaction receipt: {receipt}")

    except Exception as e:
        logging.error(f"Failed to execute the script: {e}")
```
