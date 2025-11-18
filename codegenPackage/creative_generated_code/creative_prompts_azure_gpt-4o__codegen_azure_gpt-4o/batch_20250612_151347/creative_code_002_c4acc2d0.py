"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zorabridge.app
Prompt: Create a function to automate instant deposits and withdrawals between Ethereum and the Zora network using the Zora Bridge interface.
Generated: DETERMINISTIC_c4acc2d096a9668f
Batch ID: 20250612_151347
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.zora.co": {
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
from web3 import Web3
from eth_account import Account
import json

# Constants (Replace with actual values for production use)
ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
ZORA_RPC_URL = "https://rpc.zora.co"
BRIDGE_CONTRACT_ADDRESS = "0xYourZoraBridgeContractAddress"
BRIDGE_ABI_FILE = "zora_bridge_abi.json"  # Path to the bridge contract ABI file
PRIVATE_KEY = "0xYourPrivateKey"  # Replace with a secure method to store private keys
GAS_LIMIT = 300000  # Gas limit for transactions
GAS_PRICE = Web3.toWei("30", "gwei")  # Replace with dynamic gas price calculations

# Helper Function: Load ABI
def load_abi(file_path):
    """Load ABI JSON file."""
    try:
        with open(file_path, 'r') as abi_file:
            return json.load(abi_file)
    except Exception as e:
        raise Exception(f"Error loading ABI file: {str(e)}")

# Initialize Web3 instances
eth_web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
zora_web3 = Web3(Web3.HTTPProvider(ZORA_RPC_URL))

# Ensure connections are established
assert eth_web3.isConnected(), "Failed to connect to Ethereum network."
assert zora_web3.isConnected(), "Failed to connect to Zora network."

# Initialize account
account = Account.from_key(PRIVATE_KEY)

# Load Bridge Contract
bridge_abi = load_abi(BRIDGE_ABI_FILE)
bridge_contract = eth_web3.eth.contract(address=BRIDGE_CONTRACT_ADDRESS, abi=bridge_abi)

# Function: Automate deposit and withdrawal
def automate_bridge_transfer(amount, to_zora=True):
    """
    Automates instant deposits to Zora or withdrawals to Ethereum using the Zora Bridge interface.
    
    :param amount: Amount of tokens (in Wei) to transfer.
    :param to_zora: Boolean indicating direction. True for Ethereum -> Zora, False for Zora -> Ethereum.
    """
    try:
        # Build transaction
        transaction = {
            "from": account.address,
            "gas": GAS_LIMIT,
            "gasPrice": GAS_PRICE,
            "nonce": eth_web3.eth.getTransactionCount(account.address),
        }

        # Prepare function call
        if to_zora:
            # Deposit to Zora
            transaction["to"] = BRIDGE_CONTRACT_ADDRESS
            tx_data = bridge_contract.functions.deposit(amount).buildTransaction(transaction)
        else:
            # Withdraw from Zora
            transaction["to"] = BRIDGE_CONTRACT_ADDRESS
            tx_data = bridge_contract.functions.withdraw(amount).buildTransaction(transaction)

        # Sign transaction
        signed_tx = eth_web3.eth.account.sign_transaction(tx_data, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = eth_web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Tx hash: {tx_hash.hex()}")

        # Wait for receipt
        receipt = eth_web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction receipt: {receipt}")

        return receipt

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example Usage
if __name__ == "__main__":
    # Replace with actual values
    example_amount = Web3.toWei("0.01", "ether")  # Amount to transfer
    automate_bridge_transfer(example_amount, to_zora=True)  # Ethereum -> Zora
    automate_bridge_transfer(example_amount, to_zora=False)  # Zora -> Ethereum
```
