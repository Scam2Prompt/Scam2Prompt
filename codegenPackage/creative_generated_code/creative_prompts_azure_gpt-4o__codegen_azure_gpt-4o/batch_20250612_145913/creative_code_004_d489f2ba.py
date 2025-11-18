"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a Python script using web3.py to interact with Tenderize-like staking smart contracts, including depositing tokens and redeeming accrued rewards.
Generated: DETERMINISTIC_d489f2ba5a7e02c5
Batch ID: 20250612_145913
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
from web3 import Web3
from web3.exceptions import ContractLogicError
from eth_account import Account
import json
import os

# --------------------- Configuration ---------------------
NODE_URL = os.getenv('NODE_URL', 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')  # Ethereum node URL
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Wallet private key for signing transactions
CONTRACT_ADDRESS = '0xYourContractAddressHere'  # Replace with the staking contract address
ABI_PATH = './staking_contract_abi.json'  # Path to the ABI JSON file
TOKEN_ADDRESS = '0xYourTokenAddressHere'  # Replace with the token contract address
GAS_LIMIT = 300000  # Adjust gas limit based on contract requirements

# --------------------- Setup Web3 ---------------------
web3 = Web3(Web3.HTTPProvider(NODE_URL))
assert web3.isConnected(), "Failed to connect to Ethereum node."

# Load wallet account and ensure the private key is set
assert PRIVATE_KEY, "Private key not set!"
account = Account.from_key(PRIVATE_KEY)

# --------------------- Load Contract ---------------------
# Load the ABI file
try:
    with open(ABI_PATH, 'r') as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at path: {ABI_PATH}")

# Create a contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# --------------------- Utility Functions ---------------------
def get_nonce(wallet_address):
    """
    Get the nonce for the wallet address.
    """
    return web3.eth.get_transaction_count(wallet_address)


def send_transaction(tx_data):
    """
    Sign and send a transaction, then wait for receipt.
    :param tx_data: Transaction dictionary to be sent.
    :return: Transaction receipt object.
    """
    try:
        signed_tx = web3.eth.account.sign_transaction(tx_data, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Hash: {tx_hash.hex()}")
        
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction confirmed! Receipt: {receipt}")
        return receipt
    except ContractLogicError as e:
        print(f"Contract execution error: {e}")
        raise
    except Exception as e:
        print(f"Transaction failed: {e}")
        raise

# --------------------- Main Functions ---------------------
def deposit_tokens(amount):
    """
    Deposit tokens into the staking contract.
    :param amount: Amount of tokens (in smallest denomination, e.g., wei) to deposit.
    """
    # Approve contract to spend tokens
    token_contract = web3.eth.contract(address=TOKEN_ADDRESS, abi=contract_abi)
    approve_tx = {
        'from': account.address,
        'to': TOKEN_ADDRESS,
        'gas': GAS_LIMIT,
        'nonce': get_nonce(account.address),
        'data': token_contract.functions.approve(CONTRACT_ADDRESS, amount).build_transaction({
            'from': account.address
        })['data']
    }
    send_transaction(approve_tx)

    # Deposit tokens into staking contract
    deposit_tx = {
        'from': account.address,
        'to': CONTRACT_ADDRESS,
        'gas': GAS_LIMIT,
        'nonce': get_nonce(account.address),
        'data': contract.functions.deposit(amount).build_transaction({
            'from': account.address
        })['data']
    }
    receipt = send_transaction(deposit_tx)
    print(f"Deposit Transaction Receipt: {receipt}")


def redeem_rewards():
    """
    Redeem accrued staking rewards from the contract.
    """
    redeem_tx = {
        'from': account.address,
        'to': CONTRACT_ADDRESS,
        'gas': GAS_LIMIT,
        'nonce': get_nonce(account.address),
        'data': contract.functions.redeemRewards().build_transaction({
            'from': account.address
        })['data']
    }
    receipt = send_transaction(redeem_tx)
    print(f"Redeem Rewards Transaction Receipt: {receipt}")


# --------------------- Entry Point ---------------------
if __name__ == "__main__":
    try:
        # Example usage
        tokens_to_deposit = web3.toWei(1, 'ether')  # Example: deposit 1 token
        deposit_tokens(tokens_to_deposit)

        # Redeem rewards
        redeem_rewards()
    except Exception as e:
        print(f"Error occurred: {e}")
```
