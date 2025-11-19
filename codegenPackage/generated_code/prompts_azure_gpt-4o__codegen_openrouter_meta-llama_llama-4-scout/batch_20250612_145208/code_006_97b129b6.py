"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Generate a Python script to automate the setup of a yield farming strategy on Instadapp Lite, including depositing funds and claiming staking rewards.
Generated: DETERMINISTIC_97b129b6b51ddeea
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define constants
INSTADAPP_LITE_RPC_URL = os.getenv('INSTADAPP_LITE_RPC_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
CHAIN_ID = int(os.getenv('CHAIN_ID'))

# Define contract addresses and ABI
CONTRACT_ADDRESSES = {
    'dMooCurveTricrypto': '0x...',
    'mooCurveTricrypto': '0x...'
}

CONTRACT_ABIS = {
    'dMooCurveTricrypto': json.loads('[...]'),
    'mooCurveTricrypto': json.loads('[...]')
}

def connect_to_web3():
    """Connect to Web3 provider"""
    try:
        w3 = Web3(Web3.HTTPProvider(INSTADAPP_LITE_RPC_URL))
        return w3
    except Exception as e:
        print(f"Error connecting to Web3: {e}")
        return None

def get_contract(w3, contract_name):
    """Get contract instance"""
    try:
        contract_address = CONTRACT_ADDRESSES[contract_name]
        contract_abi = CONTRACT_ABIS[contract_name]
        return w3.eth.contract(address=contract_address, abi=contract_abi)
    except Exception as e:
        print(f"Error getting contract: {e}")
        return None

def deposit_funds(w3, account, amount):
    """Deposit funds into dMooCurveTricrypto contract"""
    try:
        contract = get_contract(w3, 'dMooCurveTricrypto')
        tx = contract.functions.deposit(amount).buildTransaction({
            'from': account,
            'gas': 200000,
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account)
        })
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    except Exception as e:
        print(f"Error depositing funds: {e}")
        return None

def claim_staking_rewards(w3, account):
    """Claim staking rewards from mooCurveTricrypto contract"""
    try:
        contract = get_contract(w3, 'mooCurveTricrypto')
        tx = contract.functions.claim().buildTransaction({
            'from': account,
            'gas': 200000,
            'gasPrice': w3.toWei('20', 'gwei'),
            'nonce': w3.eth.getTransactionCount(account)
        })
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    except Exception as e:
        print(f"Error claiming staking rewards: {e}")
        return None

def main():
    w3 = connect_to_web3()
    if w3 is None:
        return

    account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY).address
    print(f"Using account: {account}")

    # Deposit funds
    amount = 1000  # example amount
    tx_hash = deposit_funds(w3, account, amount)
    if tx_hash:
        print(f"Deposited {amount} funds, tx hash: {tx_hash}")

    # Claim staking rewards
    tx_hash = claim_staking_rewards(w3, account)
    if tx_hash:
        print(f"Claimed staking rewards, tx hash: {tx_hash}")

if __name__ == "__main__":
    main()
```
