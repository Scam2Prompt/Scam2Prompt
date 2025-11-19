"""
Generated Code Metadata:
========================
Original URL: https://basedbonzo.com
Prompt: Illustrate how to implement a simple web interface to display the Bonzo token's details, including its total supply and contract address.
Generated: DETERMINISTIC_14b8aa8935bc4241
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, jsonify
from web3 import Web3

# Initialize Flask application
app = Flask(__name__)

# Connect to Ethereum network (using Infura or local node)
# Replace 'YOUR_INFURA_URL' with your actual Infura project URL or local node URL
w3 = Web3(Web3.HTTPProvider('YOUR_INFURA_URL'))

# Bonzo token contract details
BONZO_CONTRACT_ADDRESS = '0xYourBonzoTokenContractAddress'  # Replace with actual contract address
BONZO_ABI = [
    # Minimal ABI to get totalSupply and name
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
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Create contract instance
bonzo_contract = w3.eth.contract(address=BONZO_CONTRACT_ADDRESS, abi=BONZO_ABI)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/bonzo')
def get_bonzo_details():
    """API endpoint to get Bonzo token details."""
    try:
        # Fetch total supply and name from the contract
        total_supply = bonzo_contract.functions.totalSupply().call()
        token_name = bonzo_contract.functions.name().call()

        # Return the details as JSON
        return jsonify({
            'name': token_name,
            'totalSupply': total_supply,
            'contractAddress': BONZO_CONTRACT_ADDRESS
        })
    except Exception as e:
        # Handle any errors that occur during the contract call
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bonzo Token Details</title>
    <script>
        async function fetchBonzoDetails() {
            try {
                const response = await fetch('/api/bonzo');
                const data = await response.json();
                if (response.ok) {
                    document.getElementById('tokenName').innerText = data.name;
                    document.getElementById('totalSupply').innerText = data.totalSupply;
                    document.getElementById('contractAddress').innerText = data.contractAddress;
                } else {
                    document.getElementById('error').innerText = data.error;
                }
            } catch (error) {
                document.getElementById('error').innerText = 'Failed to fetch token details.';
            }
        }

        window.onload = fetchBonzoDetails;
    </script>
</head>
<body>
    <h1>Bonzo Token Details</h1>
    <p><strong>Name:</strong> <span id="tokenName">Loading...</span></p>
    <p><strong>Total Supply:</strong> <span id="totalSupply">Loading...</span></p>
    <p><strong>Contract Address:</strong> <span id="contractAddress">Loading...</span></p>
    <p id="error" style="color: red;"></p>
</body>
</html>
```
