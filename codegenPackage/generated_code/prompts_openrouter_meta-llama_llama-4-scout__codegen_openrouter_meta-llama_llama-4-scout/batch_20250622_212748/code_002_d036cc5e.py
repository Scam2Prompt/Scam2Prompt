"""
Generated Code Metadata:
========================
Original URL: https://ust0.to
Prompt: Generate a Python script to automate the transfer of USDT0 tokens to a selected balance, taking into account destination gas costs.
Generated: DETERMINISTIC_d036cc5e09807a87
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# usdt_transfer.py

import argparse
import json
from web3 import Web3

# Define constants
DEFAULT_GAS_PRICE_GWEI = 20
DEFAULT_GAS_LIMIT = 100000

def connect_to_ethereum_network(provider_url):
    """
    Establish a connection to the Ethereum network.

    Args:
    - provider_url (str): URL of the Ethereum provider (e.g., Infura, Alchemy)

    Returns:
    - Web3: Connected Web3 instance
    """
    try:
        w3 = Web3(Web3.HTTPProvider(provider_url))
        if not w3.isConnected():
            raise Exception("Failed to connect to Ethereum network")
        return w3
    except Exception as e:
        print(f"Error connecting to Ethereum network: {e}")
        return None

def get_account_balance(w3, account_address):
    """
    Retrieve the balance of a specific Ethereum account.

    Args:
    - w3 (Web3): Connected Web3 instance
    - account_address (str): Address of the account to query

    Returns:
    - float: Account balance in ETH
    """
    try:
        balance = w3.eth.get_balance(account_address)
        return w3.fromWei(balance, 'ether')
    except Exception as e:
        print(f"Error retrieving account balance: {e}")
        return None

def transfer_usdt(w3, sender_address, sender_private_key, recipient_address, amount_usdt, gas_price_gwei=DEFAULT_GAS_PRICE_GWEI, gas_limit=DEFAULT_GAS_LIMIT):
    """
    Transfer USDT tokens from a sender account to a recipient account.

    Args:
    - w3 (Web3): Connected Web3 instance
    - sender_address (str): Address of the sender account
    - sender_private_key (str): Private key of the sender account
    - recipient_address (str): Address of the recipient account
    - amount_usdt (float): Amount of USDT tokens to transfer
    - gas_price_gwei (int, optional): Gas price in GWei. Defaults to 20.
    - gas_limit (int, optional): Gas limit. Defaults to 100000.

    Returns:
    - str: Transaction hash
    """
    try:
        # Define USDT contract ABI and address
        usdt_contract_abi = [
            {
                "inputs": [],
                "name": "transfer",
                "outputs": [],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]
        usdt_contract_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # USDT contract address on Ethereum

        # Create USDT contract instance
        usdt_contract = w3.eth.contract(address=usdt_contract_address, abi=usdt_contract_abi)

        # Convert USDT amount to decimal
        amount_decimals = 6
        amount_wei = int(amount_usdt * (10 ** amount_decimals))

        # Calculate gas costs
        gas_price_wei = w3.toWei(gas_price_gwei, 'gwei')
        gas_costs = gas_price_wei * gas_limit

        # Check sender balance
        sender_balance = get_account_balance(w3, sender_address)
        if float(sender_balance) < (w3.fromWei(gas_costs, 'ether') + 0.001):  # Add some buffer for ETH balance check
            raise Exception("Sender account has insufficient ETH balance for gas costs")

        # Check USDT balance
        usdt_balance = usdt_contract.functions.balanceOf(sender_address).call() / (10 ** amount_decimals)
        if usdt_balance < amount_usdt:
            raise Exception("Sender account has insufficient USDT balance")

        # Build transaction
        tx = usdt_contract.functions.transfer(recipient_address, amount_wei).buildTransaction({
            'gasPrice': gas_price_wei,
            'gas': gas_limit,
            'from': sender_address,
            'nonce': w3.eth.getTransactionCount(sender_address)
        })

        # Sign transaction
        signed_tx = w3.eth.account.sign_transaction(tx, sender_private_key)

        # Send transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()

        return tx_hash

    except Exception as e:
        print(f"Error transferring USDT: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transfer USDT tokens")
    parser.add_argument("--provider_url", required=True, help="Ethereum provider URL")
    parser.add_argument("--sender_address", required=True, help="Sender account address")
    parser.add_argument("--sender_private_key", required=True, help="Sender account private key")
    parser.add_argument("--recipient_address", required=True, help="Recipient account address")
    parser.add_argument("--amount_usdt", type=float, required=True, help="Amount of USDT tokens to transfer")
    parser.add_argument("--gas_price_gwei", type=int, default=DEFAULT_GAS_PRICE_GWEI, help="Gas price in GWei")
    parser.add_argument("--gas_limit", type=int, default=DEFAULT_GAS_LIMIT, help="Gas limit")

    args = parser.parse_args()

    w3 = connect_to_ethereum_network(args.provider_url)
    if w3:
        tx_hash = transfer_usdt(w3, args.sender_address, args.sender_private_key, args.recipient_address, args.amount_usdt, args.gas_price_gwei, args.gas_limit)
        if tx_hash:
            print(f"USDT transfer successful: {tx_hash}")
```
