"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bingomeme.pages.dev
Prompt: Write a Python script to interact with the $BINGO cryptocurrency contract address `0x230Da48e8d1Baa481aF1Ed7059c7Cd5Da412ACbB` using Web3.py. Include functionality to check the total supply and current buy/sell tax rates.
Generated: DETERMINISTIC_7065f5fb00ac5296
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from web3.exceptions import ContractLogicError

# Define constants
BINGO_CONTRACT_ADDRESS = '0x230Da48e8d1Baa481aF1Ed7059c7Cd5Da412ACbB'
# Replace with the actual ABI for the $BINGO contract
BINGO_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "buyTaxRate",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "sellTaxRate",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Initialize Web3
def init_web3():
    # Connect to an Ethereum node (e.g., Infura, Alchemy, local node)
    infura_url = os.getenv('INFURA_URL')  # Set your Infura URL in an environment variable
    if not infura_url:
        raise ValueError("INFURA_URL environment variable not set.")
    w3 = Web3(Web3.HTTPProvider(infura_url))
    
    if not w3.isConnected():
        raise ConnectionError("Failed to connect to the Ethereum network.")
    
    return w3

# Interact with the $BINGO contract
def get_bingo_contract(w3):
    return w3.eth.contract(address=BINGO_CONTRACT_ADDRESS, abi=BINGO_ABI)

# Fetch total supply of $BINGO
def fetch_total_supply(contract):
    try:
        total_supply = contract.functions.totalSupply().call()
        return total_supply
    except ContractLogicError as e:
        raise Exception(f"Error fetching total supply: {str(e)}")

# Fetch buy and sell tax rates
def fetch_tax_rates(contract):
    try:
        buy_tax = contract.functions.buyTaxRate().call()
        sell_tax = contract.functions.sellTaxRate().call()
        return buy_tax, sell_tax
    except ContractLogicError as e:
        raise Exception(f"Error fetching tax rates: {str(e)}")

def main():
    # Initialize Web3
    w3 = init_web3()
    
    # Get the $BINGO contract
    bingo_contract = get_bingo_contract(w3)
    
    # Fetch and print total supply
    total_supply = fetch_total_supply(bingo_contract)
    print(f"Total Supply of $BINGO: {total_supply}")

    # Fetch and print buy/sell tax rates
    buy_tax, sell_tax = fetch_tax_rates(bingo_contract)
    print(f"Current Buy Tax Rate: {buy_tax}%")
    print(f"Current Sell Tax Rate: {sell_tax}%")

if __name__ == "__main__":
    main()
```
