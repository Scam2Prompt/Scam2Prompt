"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Create a Python script using Web3.py to connect a wallet, claim presale tokens, and track referral rewards for an ERC20 token like `$BTFD`.
Generated: DETERMINISTIC_a3b0626577798e1a
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv('INFURA_URL')  # URL for your Ethereum node (Infura or similar)
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Your wallet's private key (never share this)
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')  # ERC20 token contract address
REFERRAL_CONTRACT_ADDRESS = os.getenv('REFERRAL_CONTRACT_ADDRESS')  # Referral contract address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network")

# Load the token contract ABI (Application Binary Interface)
def load_contract_abi():
    with open('token_abi.json') as f:
        return json.load(f)

# Create contract instance
def get_token_contract():
    abi = load_contract_abi()
    return web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=abi)

# Claim presale tokens function
def claim_presale_tokens():
    token_contract = get_token_contract()
    nonce = web3.eth.getTransactionCount(web3.toChecksumAddress(Account.from_key(PRIVATE_KEY).address))
    
    # Construct transaction for claiming tokens
    tx = token_contract.functions.claimPresaleTokens().buildTransaction({
        'chainId': 1,  # Mainnet
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

    # Send the transaction
    try:
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f'Transaction sent: {web3.toHex(tx_hash)}')
        # Wait for transaction receipt
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print(f'Transaction receipt: {tx_receipt}')
    except Exception as e:
        print(f'Error during token claim: {e}')

# Track referral rewards function
def track_referral_rewards():
    referral_contract = web3.eth.contract(address=REFERRAL_CONTRACT_ADDRESS, abi=load_contract_abi())
    
    # Assuming there's a function to get referral rewards
    try:
        rewards = referral_contract.functions.getReferralRewards().call({'from': web3.toChecksumAddress(Account.from_key(PRIVATE_KEY).address)})
        print(f'Referral rewards: {rewards}')
    except Exception as e:
        print(f'Error fetching referral rewards: {e}')

if __name__ == '__main__':
    claim_presale_tokens()
    track_referral_rewards()
```
Make sure to have the following files in your project:
1. A `.env` file containing your `INFURA_URL`, `PRIVATE_KEY`, `TOKEN_CONTRACT_ADDRESS`, and `REFERRAL_CONTRACT_ADDRESS`.
2. `token_abi.json` file containing the ABI for the ERC20 token and referral contract. 

Before running the script, install the required libraries:
```bash
pip install web3 python-dotenv
```
