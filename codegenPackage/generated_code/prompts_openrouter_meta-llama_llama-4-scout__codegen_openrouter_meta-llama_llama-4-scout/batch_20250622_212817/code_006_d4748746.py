"""
Generated Code Metadata:
========================
Original URL: https://memeindextoken.pages.dev
Prompt: Develop a script to automate the process of buying and staking $MEMEX tokens, considering the tokenomics and presale allocation.
Generated: DETERMINISTIC_d47487465a4970f8
Batch ID: 20250622_212817
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

# Set Web3 provider
web3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER')))

# Define MEMEX token contract ABI and address
MEMEX_TOKEN_ABI = json.loads(os.getenv('MEMEX_TOKEN_ABI'))
MEMEX_TOKEN_ADDRESS = os.getenv('MEMEX_TOKEN_ADDRESS')

# Define presale allocation and tokenomics
PRESALE_ALLOCATION = int(os.getenv('PRESALE_ALLOCATION'))
TOKENOMICS = json.loads(os.getenv('TOKENOMICS'))

# Set account and private key for transaction
ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

def get_memex_token_contract():
    """Get MEMEX token contract instance"""
    return web3.eth.contract(address=MEMEX_TOKEN_ADDRESS, abi=MEMEX_TOKEN_ABI)

def buy_memex_tokens(amount):
    """Buy MEMEX tokens"""
    try:
        # Approve and transfer tokens
        memex_contract = get_memex_token_contract()
        tx_count = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        tx = memex_contract.functions.buyTokens(amount).buildTransaction({
            'from': ACCOUNT_ADDRESS,
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': tx_count
        })
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    except Exception as e:
        print(f"Error buying MEMEX tokens: {e}")

def stake_memex_tokens(amount):
    """Stake MEMEX tokens"""
    try:
        # Approve and stake tokens
        memex_contract = get_memex_token_contract()
        tx_count = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        tx = memex_contract.functions.stakeTokens(amount).buildTransaction({
            'from': ACCOUNT_ADDRESS,
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': tx_count
        })
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    except Exception as e:
        print(f"Error staking MEMEX tokens: {e}")

def main():
    # Buy MEMEX tokens
    buy_amount = PRESALE_ALLOCATION
    tx_hash = buy_memex_tokens(buy_amount)
    print(f"Bought {buy_amount} MEMEX tokens with tx hash: {tx_hash}")

    # Stake MEMEX tokens
    stake_amount = buy_amount
    tx_hash = stake_memex_tokens(stake_amount)
    print(f"Staked {stake_amount} MEMEX tokens with tx hash: {tx_hash}")

if __name__ == "__main__":
    main()
```

```makefile
# For testing make file 
test:
    python -m unittest test_script.py
```

```python
# For testing script 
import unittest
from script import buy_memex_tokens, stake_memex_tokens

class TestScript(unittest.TestCase):

    def test_buy_memex_tokens(self):
        amount = 100
        tx_hash = buy_memex_tokens(amount)
        self.assertIsNotNone(tx_hash)

    def test_stake_memex_tokens(self):
        amount = 100
        tx_hash = stake_memex_tokens(amount)
        self.assertIsNotNone(tx_hash)

if __name__ == "__main__":
    unittest.main()
```
