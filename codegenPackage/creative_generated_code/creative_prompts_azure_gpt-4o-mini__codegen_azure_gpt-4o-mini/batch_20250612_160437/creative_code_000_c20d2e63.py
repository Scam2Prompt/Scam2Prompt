"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt.airdrop1.org
Prompt: Generate a code snippet for integrating USDT airdrop functionality into a blockchain application.
Generated: DETERMINISTIC_c20d2e630eb133b7
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3
import json
import os

# Load environment variables for sensitive data
INFURA_URL = os.environ.get('INFURA_URL')
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
ADDRESS = os.environ.get('ADDRESS')
USDT_CONTRACT_ADDRESS = os.environ.get('USDT_CONTRACT_ADDRESS')

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Load USDT contract ABI from JSON file
with open('usdt_abi.json', 'r') as abi_file:
    usdt_abi = json.load(abi_file)

# Create a contract instance for USDT
usdt_contract = web3.eth.contract(address=USDT_CONTRACT_ADDRESS, abi=usdt_abi)

def airdrop_usdt(recipients, amounts):
    """
    Airdrop USDT tokens to multiple recipients.

    Args:
        recipients (list): List of recipient addresses.
        amounts (list): List of amounts corresponding to each recipient.

    Returns:
        str: Transaction hash of the airdrop.
    """
    # Ensure that recipients and amounts are of the same length
    if len(recipients) != len(amounts):
        raise ValueError("Recipients and amounts lists must have the same length.")

    # Prepare the transaction
    nonce = web3.eth.getTransactionCount(ADDRESS)
    gas_price = web3.eth.gas_price
    
    transaction = {
        'from': ADDRESS,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': gas_price,
    }

    # Create a list to hold transaction details for each recipient
    tx_list = []
    
    for recipient, amount in zip(recipients, amounts):
        # Create transaction details for each individual transfer
        tx = usdt_contract.functions.transfer(recipient, amount).buildTransaction(transaction)
        tx_list.append(tx)

    # Sign and send transactions
    for tx in tx_list:
        try:
            signed_tx = web3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(f"Transaction successful with hash: {web3.toHex(tx_hash)}")
        except Exception as e:
            print(f"Error sending transaction: {str(e)}")

# Example usage
if __name__ == "__main__":
    recipients = ['0xRecipientAddress1', '0xRecipientAddress2']
    amounts = [1000000, 2000000]  # Amounts in USDT (considering USDT has 6 decimal places)

    try:
        airdrop_usdt(recipients, amounts)
    except Exception as e:
        print(f"Airdrop failed: {str(e)}")
```
