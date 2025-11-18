"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperbridge.mobi
Prompt: Provide an example of integrating HyperEVM with the Hyper liquid Bridge for cross-chain asset transfers.
Generated: DETERMINISTIC_2b27f1676f3b2ccc
Batch ID: 20250612_154057
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://hyperbridge.example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://hyperevm.example.com": {
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
Integration Example: HyperEVM with Hyper Liquid Bridge for Cross-Chain Asset Transfers
Language: Python
Dependencies: web3.py, requests
Note: Ensure you have access to HyperEVM and Hyper Liquid Bridge APIs and their respective credentials.
"""

from web3 import Web3
import requests

# Configuration parameters
HYPEREVM_RPC_URL = "https://hyperevm.example.com"  # Replace with actual RPC URL
HYPER_BRIDGE_API_URL = "https://hyperbridge.example.com/api"  # Replace with actual API endpoint
PRIVATE_KEY = "your_private_key_here"  # Replace with your private key
SENDER_ADDRESS = "your_sender_address_here"  # Replace with your wallet address
RECEIVER_ADDRESS = "receiver_address_here"  # Replace with recipient wallet address
TOKEN_CONTRACT_ADDRESS = "token_contract_address_here"  # Replace with ERC20 token contract address
CHAIN_ID = 1  # Replace with the appropriate chain ID

# Initialize web3 connection to HyperEVM
web3 = Web3(Web3.HTTPProvider(HYPEREVM_RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to HyperEVM.")

# Token contract ABI (simplified version for ERC20 transfers)
TOKEN_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
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
        "type": "function",
    },
]

# Initialize token contract
token_contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=TOKEN_ABI)

def get_balance(address):
    """Fetch the token balance of a given address."""
    try:
        balance = token_contract.functions.balanceOf(address).call()
        return balance
    except Exception as e:
        raise RuntimeError(f"Failed to fetch balance: {e}")

def create_transfer_transaction(receiver_address, amount):
    """Create a transaction to transfer tokens."""
    try:
        nonce = web3.eth.getTransactionCount(SENDER_ADDRESS)
        tx = token_contract.functions.transfer(receiver_address, amount).buildTransaction({
            "chainId": CHAIN_ID,
            "gas": 200000,
            "gasPrice": web3.eth.gas_price,
            "nonce": nonce,
        })
        return tx
    except Exception as e:
        raise RuntimeError(f"Failed to create transaction: {e}")

def sign_and_send_transaction(transaction):
    """Sign and send the transaction."""
    try:
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    except Exception as e:
        raise RuntimeError(f"Failed to sign/send transaction: {e}")

def initiate_cross_chain_transfer(amount):
    """Initiate a cross-chain transfer through Hyper Liquid Bridge."""
    try:
        payload = {
            "sender": SENDER_ADDRESS,
            "receiver": RECEIVER_ADDRESS,
            "amount": amount,
            "token": TOKEN_CONTRACT_ADDRESS,
        }
        response = requests.post(f"{HYPER_BRIDGE_API_URL}/transfer", json=payload)
        response.raise_for_status()
        return response.json()  # Expecting a response with transaction details
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to initiate cross-chain transfer: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Step 1: Check sender's balance
        sender_balance = get_balance(SENDER_ADDRESS)
        print(f"Sender's Balance: {sender_balance}")

        # Step 2: Specify transfer amount (validate against balance)
        transfer_amount = 1000  # Replace with the desired amount
        if sender_balance < transfer_amount:
            raise ValueError("Insufficient balance for transfer.")

        # Step 3: Create and sign the transaction
        tx = create_transfer_transaction(RECEIVER_ADDRESS, transfer_amount)
        tx_hash = sign_and_send_transaction(tx)
        print(f"Transaction sent. Hash: {tx_hash}")

        # Step 4: Initiate cross-chain transfer through Hyper Liquid Bridge
        cross_chain_response = initiate_cross_chain_transfer(transfer_amount)
        print(f"Cross-chain transfer initiated: {cross_chain_response}")

    except Exception as e:
        print(f"Error: {e}")
```
