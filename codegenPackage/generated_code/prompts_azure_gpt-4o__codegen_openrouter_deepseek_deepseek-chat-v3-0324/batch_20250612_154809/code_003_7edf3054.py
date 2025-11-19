"""
Generated Code Metadata:
========================
Original URL: https://teddyprc20.com
Prompt: Write a Python script using web3.py to bridge Ethereum or stable coins from the Ethereum network to PulseChain, as outlined in the Teddy Bear PRC-20 "How to Buy" guide.
Generated: DETERMINISTIC_7edf3054026ff68f
Batch ID: 20250612_154809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
ETHEREUM_RPC_URL = os.getenv('ETHEREUM_RPC_URL')
PULSECHAIN_RPC_URL = os.getenv('PULSECHAIN_RPC_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
BRIDGE_CONTRACT_ADDRESS = os.getenv('BRIDGE_CONTRACT_ADDRESS')
GAS_LIMIT = 200000
GAS_PRICE = Web3.to_wei('50', 'gwei')

# Initialize Web3 instances
eth_web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
pulse_web3 = Web3(Web3.HTTPProvider(PULSECHAIN_RPC_URL))

# Add POA middleware for PulseChain
pulse_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load ABI for the bridge contract
with open('bridge_abi.json', 'r') as f:
    BRIDGE_ABI = json.load(f)

def get_account(web3_instance):
    """Get account from private key."""
    try:
        account = web3_instance.eth.account.from_key(PRIVATE_KEY)
        return account
    except Exception as e:
        raise Exception(f"Error getting account: {str(e)}")

def get_token_balance(web3_instance, token_address, account_address):
    """Get token balance of an account."""
    try:
        # Standard ERC20 ABI for balanceOf
        erc20_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ]
        contract = web3_instance.eth.contract(address=token_address, abi=erc20_abi)
        balance = contract.functions.balanceOf(account_address).call()
        return balance
    except Exception as e:
        raise Exception(f"Error getting token balance: {str(e)}")

def approve_token(web3_instance, token_address, spender_address, amount, account):
    """Approve tokens to be spent by the bridge contract."""
    try:
        # Standard ERC20 ABI for approve
        erc20_abi = [
            {
                "constant": False,
                "inputs": [
                    {"name": "_spender", "type": "address"},
                    {"name": "_value", "type": "uint256"}
                ],
                "name": "approve",
                "outputs": [{"name": "", "type": "bool"}],
                "type": "function"
            }
        ]
        contract = web3_instance.eth.contract(address=token_address, abi=erc20_abi)
        
        nonce = web3_instance.eth.get_transaction_count(account.address)
        
        tx = contract.functions.approve(
            spender_address,
            amount
        ).build_transaction({
            'chainId': web3_instance.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })
        
        signed_tx = web3_instance.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3_instance.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt
    except Exception as e:
        raise Exception(f"Error approving tokens: {str(e)}")

def bridge_tokens(web3_instance, token_address, amount, destination_address, account):
    """Bridge tokens to PulseChain."""
    try:
        contract = web3_instance.eth.contract(address=BRIDGE_CONTRACT_ADDRESS, abi=BRIDGE_ABI)
        
        nonce = web3_instance.eth.get_transaction_count(account.address)
        
        tx = contract.functions.lockTokens(
            token_address,
            amount,
            destination_address
        ).build_transaction({
            'chainId': web3_instance.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })
        
        signed_tx = web3_instance.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3_instance.eth.wait_for_transaction_receipt(tx_hash)
        
        return receipt
    except Exception as e:
        raise Exception(f"Error bridging tokens: {str(e)}")

def main():
    try:
        # User inputs
        token_address = input("Enter token contract address to bridge: ")
        amount = int(input("Enter amount to bridge (in smallest unit): "))
        destination_address = input("Enter destination address on PulseChain: ")
        
        # Validate inputs
        if not eth_web3.is_address(token_address):
            raise ValueError("Invalid token address")
        if not pulse_web3.is_address(destination_address):
            raise ValueError("Invalid destination address")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Get accounts
        eth_account = get_account(eth_web3)
        
        # Check token balance
        balance = get_token_balance(eth_web3, token_address, eth_account.address)
        if balance < amount:
            raise ValueError("Insufficient token balance")
        
        # Approve tokens
        print("Approving tokens...")
        approve_receipt = approve_token(
            eth_web3,
            token_address,
            BRIDGE_CONTRACT_ADDRESS,
            amount,
            eth_account
        )
        print(f"Approval successful. Tx hash: {approve_receipt.transactionHash.hex()}")
        
        # Bridge tokens
        print("Bridging tokens...")
        bridge_receipt = bridge_tokens(
            eth_web3,
            token_address,
            amount,
            destination_address,
            eth_account
        )
        print(f"Bridging successful. Tx hash: {bridge_receipt.transactionHash.hex()}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
