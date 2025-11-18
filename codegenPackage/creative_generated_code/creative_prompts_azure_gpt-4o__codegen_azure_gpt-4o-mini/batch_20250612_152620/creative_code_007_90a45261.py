"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Generate code in Python using the `web3.py` library to retrieve and display the total number of $QUBE tokens sold and remaining during the presale stage on InQubeta.
Generated: DETERMINISTIC_90a4526110f3ee25
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3

# Connect to Ethereum node (Infura, Alchemy, etc.)
INFURA_URL = 'YOUR_INFURA_URL_HERE'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the Ethereum node
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum node.")

# Contract address for InQubeta presale (replace with actual contract address)
PRESALE_CONTRACT_ADDRESS = 'YOUR_PRESALE_CONTRACT_ADDRESS_HERE'

# ABI for the presale contract (replace with actual ABI)
PRESALE_CONTRACT_ABI = json.loads('''
[
    {
        "constant": true,
        "inputs": [],
        "name": "totalSold",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
''')

# Create a contract instance
try:
    presale_contract = web3.eth.contract(address=PRESALE_CONTRACT_ADDRESS, abi=PRESALE_CONTRACT_ABI)
except Exception as e:
    raise RuntimeError(f"Failed to create contract instance: {e}")

# Function to retrieve total tokens sold and remaining
def get_presale_info():
    try:
        # Retrieve total tokens sold
        total_sold = presale_contract.functions.totalSold().call()
        
        # Retrieve total supply (presale cap)
        total_supply = presale_contract.functions.totalSupply().call()
        
        # Calculate remaining tokens
        remaining_tokens = total_supply - total_sold
        
        return total_sold, remaining_tokens
    except Exception as e:
        raise RuntimeError(f"Error retrieving presale information: {e}")

# Main execution
if __name__ == "__main__":
    try:
        sold, remaining = get_presale_info()
        print(f"Total $QUBE Tokens Sold: {sold}")
        print(f"Remaining $QUBE Tokens in Presale: {remaining}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
