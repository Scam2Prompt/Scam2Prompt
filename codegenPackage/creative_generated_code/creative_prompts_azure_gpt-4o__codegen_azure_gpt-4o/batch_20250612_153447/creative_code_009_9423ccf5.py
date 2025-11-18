"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeu.pages.dev
Prompt: Create a tutorial for integrating Pepe Unchained's Layer 2 blockchain with a payment gateway that accepts ETH, USDT, and BNB for purchasing $PEPU tokens. Include relevant code examples.
Generated: DETERMINISTIC_9423ccf5b1eb0c01
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Tutorial: Integrating Pepe Unchained's Layer 2 blockchain with a payment gateway

# Required Dependencies
# Install web3 and dotenv libraries via pip:
# pip install web3 python-dotenv

import os
from web3 import Web3, exceptions
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for Pepe Unchained Layer 2 blockchain
PEPE_RPC_URL = os.getenv("PEPE_RPC_URL")  # URL for Pepe Unchained Layer 2 blockchain
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet to interact with blockchain
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Public address of the wallet

# Payment Gateway Settings
SUPPORTED_CURRENCIES = ['ETH', 'USDT', 'BNB']  # Supported payment currencies for $PEPU purchase

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(PEPE_RPC_URL))

# Validate Web3 connection
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Pepe Unchained Layer 2 blockchain.")

# Example $PEPU token contract address and ABI (replace with actual values)
PEPU_TOKEN_CONTRACT_ADDRESS = os.getenv("PEPU_TOKEN_ADDRESS")
PEPU_TOKEN_ABI = [
    # Add the actual ABI of the $PEPU contract here.
]

# Initialize the $PEPU token contract instance
pepu_contract = web3.eth.contract(address=PEPU_TOKEN_CONTRACT_ADDRESS, abi=PEPU_TOKEN_ABI)


def approve_payment(currency: str, amount: float):
    """
    Handles currency validation and payment approval for purchasing $PEPU tokens.

    :param currency: Payment currency (ETH, USDT, or BNB).
    :param amount: Amount of currency being sent for purchase.
    :return: Transaction receipt if successful.
    """
    if currency not in SUPPORTED_CURRENCIES:
        raise ValueError(f"Currency '{currency}' is not supported. Supported currencies: {SUPPORTED_CURRENCIES}")

    # Convert payment amount to the smallest unit (e.g., Wei for ETH)
    payment_amount = web3.to_wei(amount, 'ether') if currency == 'ETH' else int(amount * (10 ** 18))

    # Generate blockchain transaction
    transaction = {
        'to': PEPU_TOKEN_CONTRACT_ADDRESS,
        'from': PUBLIC_ADDRESS,
        'value': payment_amount,
        'gas': 200000,
        'gasPrice': web3.to_wei('20', 'gwei'),  # Gas price in Gwei
        'nonce': web3.eth.get_transaction_count(PUBLIC_ADDRESS),  # Current transaction count for nonce
    }

    # Sign the transaction with the private key
    signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

    try:
        # Send the transaction to the blockchain
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # Wait for the transaction to be mined
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt
    except exceptions.TransactionError as e:
        raise ValueError(f"Transaction failed: {str(e)}")


def purchase_pepu(currency: str, amount: float, pepu_amount: int):
    """
    Handles the purchase of $PEPU tokens using a supported currency.

    :param currency: Payment currency (ETH, USDT, or BNB).
    :param amount: Amount of currency being sent for purchase.
    :param pepu_amount: Number of $PEPU tokens to purchase.
    :return: Transaction receipt if successful.
    """
    # Step 1: Approve the payment
    receipt = approve_payment(currency, amount)
    print(f"Payment approved. Transaction hash: {receipt.transactionHash.hex()}")

    # Step 2: Call the smart contract's `buyTokens` function to purchase $PEPU
    try:
        # Construct the transaction to interact with the smart contract
        buy_tokens_txn = pepu_contract.functions.buyTokens(pepu_amount).build_transaction({
            'from': PUBLIC_ADDRESS,
            'gas': 200000,
            'gasPrice': web3.to_wei('20', 'gwei'),
            'nonce': web3.eth.get_transaction_count(PUBLIC_ADDRESS),
        })

        # Sign the transaction
        signed_buy_txn = web3.eth.account.sign_transaction(buy_tokens_txn, PRIVATE_KEY)

        # Send the transaction
        buy_tx_hash = web3.eth.send_raw_transaction(signed_buy_txn.rawTransaction)
        buy_tx_receipt = web3.eth.wait_for_transaction_receipt(buy_tx_hash)
        return buy_tx_receipt
    except exceptions.ContractLogicError as e:
        raise ValueError(f"Smart contract interaction failed: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # User inputs for currency, payment amount, and tokens they want to buy
        payment_currency = 'ETH'  # ETH, USDT, or BNB
        payment_amount = 0.01  # Amount in ETH (or respective currency)
        tokens_to_purchase = 100  # Number of $PEPU tokens

        # Initiate purchase
        transaction_receipt = purchase_pepu(payment_currency, payment_amount, tokens_to_purchase)
        print(f"$PEPU purchase successful! Transaction hash: {transaction_receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"Error: {str(e)}")
```

### Notes:
1. Replace `PEPU_TOKEN_CONTRACT_ADDRESS` and `PEPU_TOKEN_ABI` with the actual contract's address and ABI.
2. Ensure the `.env` file contains the `PEPE_RPC_URL`, `PRIVATE_KEY`, and `PUBLIC_ADDRESS`.
3. Error handling includes validation of supported currencies and transaction/contract errors.
