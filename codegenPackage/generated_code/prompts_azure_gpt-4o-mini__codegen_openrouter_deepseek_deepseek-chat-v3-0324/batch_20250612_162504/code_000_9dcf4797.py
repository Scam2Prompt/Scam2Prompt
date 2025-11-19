"""
Generated Code Metadata:
========================
Original URL: https://pepe-presaletestingonly.vercel.app
Prompt: Write a Python script to interact with the $PEPE token presale API, allowing users to contribute USDT for $PEPE tokens.
Generated: DETERMINISTIC_9dcf479784fad7b7
Batch ID: 20250612_162504
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.pepe-presale.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from web3 import Web3
from web3.exceptions import TransactionNotFound
from eth_account import Account
from decimal import Decimal, getcontext

# Configuration
PRESALE_API_URL = "https://api.pepe-presale.com"  # Replace with actual API URL
USDT_CONTRACT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # Mainnet USDT
PEPE_PRESALE_CONTRACT_ADDRESS = "0x...PePePresaleContractAddress..."  # Replace with actual
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Securely load from env in production
CHAIN_ID = 1  # Ethereum Mainnet
GAS_LIMIT = 200000
GAS_PRICE = Web3.to_wei('50', 'gwei')

# Initialize Web3
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))  # Replace

# USDT Contract ABI (simplified for transfer)
USDT_ABI = json.loads('''[
    {
        "constant": false,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]''')

# PEPE Presale Contract ABI (simplified)
PEPE_PRESALE_ABI = json.loads('''[
    {
        "constant": false,
        "inputs": [
            {"name": "amount", "type": "uint256"}
        ],
        "name": "contribute",
        "outputs": [],
        "type": "function"
    }
]''')

# Initialize contracts
usdt_contract = w3.eth.contract(address=USDT_CONTRACT_ADDRESS, abi=USDT_ABI)
pepe_presale_contract = w3.eth.contract(address=PEPE_PRESALE_CONTRACT_ADDRESS, abi=PEPE_PRESALE_ABI)

def get_presale_details():
    """Fetch current presale details from API"""
    try:
        response = requests.get(f"{PRESALE_API_URL}/details")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching presale details: {e}")
        return None

def approve_usdt(amount):
    """Approve USDT transfer to presale contract"""
    account = Account.from_key(PRIVATE_KEY)
    nonce = w3.eth.get_transaction_count(account.address)
    
    try:
        tx = usdt_contract.functions.approve(
            PEPE_PRESALE_CONTRACT_ADDRESS,
            amount
        ).build_transaction({
            'chainId': CHAIN_ID,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce,
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status == 1
    except Exception as e:
        print(f"Error approving USDT: {e}")
        return False

def contribute_to_presale(usdt_amount):
    """Contribute USDT to PEPE presale"""
    account = Account.from_key(PRIVATE_KEY)
    nonce = w3.eth.get_transaction_count(account.address)
    
    # Convert USDT amount to wei (USDT has 6 decimals)
    usdt_wei = int(Decimal(usdt_amount) * Decimal(10**6))
    
    try:
        # First approve USDT transfer
        if not approve_usdt(usdt_wei):
            print("USDT approval failed")
            return False
        
        # Then contribute
        tx = pepe_presale_contract.functions.contribute(usdt_wei).build_transaction({
            'chainId': CHAIN_ID,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': nonce + 1,  # Increment nonce after approval
        })
        
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status == 1
    except Exception as e:
        print(f"Error contributing to presale: {e}")
        return False

def main():
    # Get presale details
    details = get_presale_details()
    if not details:
        print("Failed to get presale details")
        return
    
    print(f"PEPE Presale Details:\n"
          f"Current Price: {details['price']} USDT per PEPE\n"
          f"Tokens Sold: {details['tokens_sold']}\n"
          f"Hard Cap: {details['hard_cap']}\n"
          f"Presale Ends: {details['end_time']}")
    
    # Get user input
    try:
        usdt_amount = float(input("Enter amount of USDT to contribute: "))
        if usdt_amount <= 0:
            print("Amount must be positive")
            return
    except ValueError:
        print("Invalid amount entered")
        return
    
    # Confirm contribution
    confirm = input(f"Confirm contribution of {usdt_amount} USDT? (y/n): ").lower()
    if confirm != 'y':
        print("Contribution cancelled")
        return
    
    # Execute contribution
    if contribute_to_presale(usdt_amount):
        print("Contribution successful!")
    else:
        print("Contribution failed")

if __name__ == "__main__":
    getcontext().prec = 6  # Set decimal precision for USDT calculations
    main()
```
