"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbonzo.com
Prompt: Illustrate how to implement a simple web interface to display the Bonzo token's details, including its total supply and contract address.
Generated: DETERMINISTIC_14b8aa8935bc4241
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template
from web3 import Web3
import os

# Initialize Flask application
app = Flask(__name__)

# Connect to Ethereum network (e.g., via Infura or local node)
infura_url = os.getenv('INFURA_URL')  # Ensure to set this environment variable
web3 = Web3(Web3.HTTPProvider(infura_url))

# Bonzo Token contract details
BONZO_CONTRACT_ADDRESS = '0xYourBonzoTokenContractAddress'  # Replace with actual contract address
BONZO_ABI = [
    # Replace with the actual ABI of the Bonzo token contract
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
        "name": "getContractAddress",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Create contract instance
bonzo_contract = web3.eth.contract(address=BONZO_CONTRACT_ADDRESS, abi=BONZO_ABI)

@app.route('/')
def index():
    try:
        # Fetch total supply from the contract
        total_supply = bonzo_contract.functions.totalSupply().call()
        
        # Get the contract address
        contract_address = bonzo_contract.address
        
        # Render the details in the index.html template
        return render_template('index.html', total_supply=total_supply, contract_address=contract_address)
    
    except Exception as e:
        # Handle exceptions and return an error message
        return f"An error occurred: {str(e)}", 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**index.html (place this in a templates folder)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bonzo Token Details</title>
</head>
<body>
    <h1>Bonzo Token Details</h1>
    <p><strong>Total Supply:</strong> {{ total_supply }}</p>
    <p><strong>Contract Address:</strong> {{ contract_address }}</p>
</body>
</html>
``` 

Make sure to replace `'0xYourBonzoTokenContractAddress'` and the ABI array in the code with the actual contract address and ABI of the Bonzo token. Additionally, set up the necessary environment variables for the Ethereum node connection.
