"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goglzs.io
Prompt: Write a script to interact with the Goggles token on the SONIC blockchain using its contract address `0x9fDbC3f8Abc05Fa8f3Ad3C17D2F806c1230c4564`. Include functions for checking the token balance and transferring tokens.
Generated: DETERMINISTIC_d0fd4f5d4f7c1168
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required dependencies:
# - web3: Install via `pip install web3`
# - Ensure you have access to the SONIC blockchain RPC URL and a valid private key.

from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration
SONIC_RPC_URL = "<YOUR_SONIC_RPC_URL>"  # Replace with the SONIC blockchain RPC URL
PRIVATE_KEY = "<YOUR_PRIVATE_KEY>"  # Replace with your private key
GOGGLES_CONTRACT_ADDRESS = "0x9fDbC3f8Abc05Fa8f3Ad3C17D2F806c1230c4564"

# ABI for the Goggles token contract (simplified for ERC20)
GOGGLES_ABI = [
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
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Initialize web3
web3 = Web3(Web3.HTTPProvider(SONIC_RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to the SONIC blockchain.")

# Derive account from private key
account = web3.eth.account.from_key(PRIVATE_KEY)
sender_address = account.address

# Load the Goggles token contract
contract = web3.eth.contract(address=GOGGLES_CONTRACT_ADDRESS, abi=GOGGLES_ABI)


def check_balance(address):
    """
    Check the token balance of a given address.

    :param address: The address to check the balance for.
    :return: The token balance as an integer.
    """
    try:
        balance = contract.functions.balanceOf(address).call()
        return balance
    except ContractLogicError as e:
        print(f"Error accessing contract: {e}")
        return None


def transfer_tokens(to_address, amount):
    """
    Transfer Goggles tokens to a specific address.

    :param to_address: The recipient address.
    :param amount: The amount of tokens to transfer.
    :return: Transaction hash if successful, None otherwise.
    """
    try:
        # Build the transaction
        nonce = web3.eth.getTransactionCount(sender_address)
        tx = contract.functions.transfer(to_address, amount).buildTransaction({
            "chainId": web3.eth.chain_id,
            "gas": 100000,  # Estimate appropriate gas limit
            "gasPrice": web3.eth.gas_price,
            "nonce": nonce,
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.to_hex(tx_hash)
    except ValueError as e:
        print(f"Transaction error: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    recipient_address = "<RECIPIENT_ADDRESS>"  # Replace with the recipient's address
    transfer_amount = 10  # Replace with the number of tokens to transfer

    print(f"Checking balance for {sender_address}...")
    sender_balance = check_balance(sender_address)
    print(f"Balance: {sender_balance} Goggles tokens")

    if sender_balance and sender_balance >= transfer_amount:
        print(f"Transferring {transfer_amount} tokens to {recipient_address}...")
        tx_hash = transfer_tokens(recipient_address, transfer_amount)
        if tx_hash:
            print(f"Transaction successful! Hash: {tx_hash}")
        else:
            print("Transaction failed.")
    else:
        print("Insufficient balance.")
```
