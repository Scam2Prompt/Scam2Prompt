"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Create a Python script using web3.py to interact with the $MGLS token contract address `0xda251891e21e6edb0e6828e77621c7b98ea4e8ba` for checking balances and transferring tokens.
Generated: DETERMINISTIC_53574d983980f93e
Batch ID: 20250612_152739
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
import sys
from web3 import Web3
from web3.exceptions import ContractLogicError

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
TOKEN_CONTRACT_ADDRESS = "0xda251891e21e6edb0e6828e77621c7b98ea4e8ba"
ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    print("Error: Unable to connect to Ethereum network.")
    sys.exit(1)

# Load the contract
try:
    contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ABI)
except Exception as e:
    print(f"Error loading contract: {e}")
    sys.exit(1)

# Function to check balance
def check_balance(address):
    """
    Check the balance of a given Ethereum address for MGLS tokens.
    
    :param address: Ethereum address to check balance for.
    :return: Token balance (integer).
    """
    try:
        balance = contract.functions.balanceOf(address).call()
        return balance
    except ContractLogicError:
        print("Error: Invalid contract call.")
        return None
    except Exception as e:
        print(f"Error checking balance: {e}")
        return None

# Function to transfer tokens
def transfer_tokens(from_address, private_key, to_address, amount):
    """
    Transfer MGLS tokens from one address to another.
    
    :param from_address: Sender's Ethereum address.
    :param private_key: Sender's private key for signing transactions.
    :param to_address: Receiver's Ethereum address.
    :param amount: Amount of tokens to transfer.
    :return: Transaction hash.
    """
    try:
        # Create the transaction
        nonce = web3.eth.getTransactionCount(from_address)
        txn = contract.functions.transfer(to_address, amount).buildTransaction({
            'chainId': 1,  # Ethereum Mainnet
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        return web3.toHex(tx_hash)
    except ContractLogicError:
        print("Error: Invalid contract call.")
        return None
    except Exception as e:
        print(f"Error transferring tokens: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Address and private key (replace with actual values)
    sender_address = "0xYourSenderAddressHere"
    sender_private_key = "0xYourPrivateKeyHere"
    recipient_address = "0xRecipientAddressHere"

    # Check balance
    sender_balance = check_balance(sender_address)
    if sender_balance is not None:
        print(f"Sender's balance: {sender_balance} MGLS tokens")

    # Transfer tokens
    amount_to_transfer = 100  # Number of tokens to transfer
    tx_hash = transfer_tokens(sender_address, sender_private_key, recipient_address, amount_to_transfer)
    if tx_hash is not None:
        print(f"Transaction successful! TX Hash: {tx_hash}")
```

### Notes:
1. Replace placeholders such as `YOUR_INFURA_PROJECT_ID`, `0xYourSenderAddressHere`, `0xYourPrivateKeyHere`, and `0xRecipientAddressHere` with actual values.
2. Ensure that the sender has sufficient balance and gas to complete the transaction.
3. Always handle sensitive data such as private keys securely and avoid hardcoding them in production-ready scripts. Use environment variables or secure vaults for storing such secrets.
