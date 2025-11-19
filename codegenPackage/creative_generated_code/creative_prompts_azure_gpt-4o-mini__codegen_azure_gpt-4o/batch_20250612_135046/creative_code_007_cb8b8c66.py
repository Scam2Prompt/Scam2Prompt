"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3inbox.com
Prompt: Provide an overview of how Web3Inbox supports EOA and smart accounts on EVM chains using its Blockchain API.
Generated: DETERMINISTIC_cb8b8c66fc9f6458
Batch ID: 20250612_135046
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
"""
Overview:
This script demonstrates how Web3Inbox can support both Externally Owned Accounts (EOA) and Smart Contract Accounts
on EVM-based blockchains using its Blockchain API. The implementation uses Python and the Web3.py library.

Web3Inbox acts as an abstraction layer to facilitate interaction with Ethereum Virtual Machine (EVM)-compatible chains,
managing both EOAs and Smart Accounts appropriately.

Prerequisites:
1. Install the `web3` library: pip install web3
2. Replace placeholders with actual values (e.g., RPC URL, private keys, etc.)
3. Ensure Smart Accounts adhere to the ERC-4337 account abstraction standard.
"""

from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration: Replace with your EVM chain's RPC URL
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum node. Check your RPC URL.")

# Example EOA (Externally Owned Account)
EOA_PRIVATE_KEY = "YOUR_EOA_PRIVATE_KEY"
EOA_ADDRESS = web3.eth.account.privateKeyToAccount(EOA_PRIVATE_KEY).address

# Example Smart Account (Contract Address)
SMART_ACCOUNT_ADDRESS = "YOUR_SMART_CONTRACT_ADDRESS"

def eoa_interaction():
    """
    Handles EOA interactions by sending a transaction to another address.
    """
    try:
        # Define transaction parameters
        txn = {
            'to': 'RECIPIENT_ADDRESS',  # Replace with recipient address
            'value': web3.toWei(0.1, 'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(EOA_ADDRESS),
        }

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, EOA_PRIVATE_KEY)

        # Send transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {txn_hash.hex()}")

    except Exception as e:
        print(f"Error during EOA interaction: {e}")

def smart_account_interaction():
    """
    Handles Smart Account interactions by calling its functions via the ABI.
    """
    try:
        # Load the Smart Contract ABI (replace with actual ABI)
        smart_account_abi = [
            # Example ABI structure
            {
                "constant": False,
                "inputs": [{"name": "message", "type": "string"}],
                "name": "sendMessage",
                "outputs": [],
                "type": "function",
            }
        ]

        # Initialize the contract instance
        smart_account_contract = web3.eth.contract(
            address=SMART_ACCOUNT_ADDRESS,
            abi=smart_account_abi,
        )

        # Define the function parameters
        message_to_send = "Hello from Web3Inbox!"

        # Build the transaction
        txn = smart_account_contract.functions.sendMessage(message_to_send).buildTransaction({
            'from': EOA_ADDRESS,  # EOA acts as the sender
            'gas': 100000,  # Adjust gas limit accordingly
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(EOA_ADDRESS),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, EOA_PRIVATE_KEY)

        # Send transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Smart Account transaction sent! Hash: {txn_hash.hex()}")

    except ContractLogicError as cle:
        print(f"Contract logic error: {cle}")
    except Exception as e:
        print(f"Error during Smart Account interaction: {e}")

def main():
    """
    Main function demonstrating EOA and Smart Account interactions.
    """
    print("Interacting with EOA...")
    eoa_interaction()

    print("\nInteracting with Smart Account...")
    smart_account_interaction()

if __name__ == "__main__":
    main()
```
