"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthentic-swa-p.pages.dev
Prompt: Generate a script to implement a token presale mechanism using the Synthentic synthetic protocol, ensuring compatibility with wallet integration for secure transactions.
Generated: DETERMINISTIC_c363da8e12c5e703
Batch ID: 20250612_153947
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
# Import necessary libraries
from web3 import Web3, HTTPProvider
import json

# Presale Configuration
PRESALE_TOKEN_ADDRESS = "0xYourTokenAddressHere"  # Replace with your token's address
PRESALE_WALLET_ADDRESS = "0xYourWalletAddressHere"  # Replace with your wallet's address
PRESALE_PRICE = 0.01  # Price per token in ETH
MIN_PURCHASE_AMOUNT = 0.1  # Minimum ETH allowed for purchase
MAX_PURCHASE_AMOUNT = 10  # Maximum ETH allowed for purchase

# Web3 Configuration
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
web3 = Web3(HTTPProvider(INFURA_URL))

# Load the token's ABI
with open('token_abi.json', 'r') as abi_file:
    TOKEN_ABI = json.load(abi_file)

# Initialize the token contract
token_contract = web3.eth.contract(address=Web3.to_checksum_address(PRESALE_TOKEN_ADDRESS), abi=TOKEN_ABI)

# Function to handle presale purchase
def handle_presale_purchase(buyer_address, eth_amount):
    """
    Handles the token presale purchase.

    Parameters:
        buyer_address (str): Address of the buyer.
        eth_amount (float): Amount of ETH sent by the buyer.

    Returns:
        str: Transaction hash if successful, error message otherwise.
    """
    try:
        # Validate buyer address
        if not web3.is_address(buyer_address):
            return "Invalid buyer address."

        # Validate purchase amount
        if eth_amount < MIN_PURCHASE_AMOUNT or eth_amount > MAX_PURCHASE_AMOUNT:
            return f"Purchase amount must be between {MIN_PURCHASE_AMOUNT} and {MAX_PURCHASE_AMOUNT} ETH."

        # Calculate token amount
        token_amount = eth_amount / PRESALE_PRICE

        # Generate transaction data
        nonce = web3.eth.get_transaction_count(PRESALE_WALLET_ADDRESS)
        gas_estimate = web3.eth.estimate_gas({
            'from': PRESALE_WALLET_ADDRESS,
            'to': buyer_address,
            'value': Web3.to_wei(eth_amount, 'ether'),
            'data': token_contract.functions.transfer(
                Web3.to_checksum_address(buyer_address),
                Web3.to_wei(token_amount, 'ether')
            ).build_transaction({'nonce': nonce})
        })

        # Build transaction
        transaction = {
            'from': PRESALE_WALLET_ADDRESS,
            'to': buyer_address,
            'value': Web3.to_wei(eth_amount, 'ether'),
            'gas': gas_estimate,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce
        }

        # Sign transaction
        private_key = "YOUR_PRIVATE_KEY_HERE"  # Replace with your private key
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

        # Send transaction
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return f"Transaction successful. Hash: {web3.to_hex(txn_hash)}"
    except Exception as e:
        return f"Error processing presale purchase: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test buyer data
    TEST_BUYER_ADDRESS = "0xBuyerAddressHere"  # Replace with test buyer's address
    TEST_ETH_AMOUNT = 0.5  # ETH sent by test buyer

    # Handle presale
    result = handle_presale_purchase(TEST_BUYER_ADDRESS, TEST_ETH_AMOUNT)
    print(result)
```

*Note*: This code is a simplified example and assumes the existence of a valid ERC20 token contract and wallet setup. Replace placeholder values (`YOUR_PRIVATE_KEY_HERE`, `0xYourTokenAddressHere`, etc.) with your actual project details. Always ensure your private keys are securely stored.
