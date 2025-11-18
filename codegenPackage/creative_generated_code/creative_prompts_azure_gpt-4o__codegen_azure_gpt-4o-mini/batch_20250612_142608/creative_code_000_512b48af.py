"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Write a Python script to integrate the MetaMask wallet into a web application for managing ERC-20 tokens, referencing the installation process for the MetaMask browser extension described on the website.
Generated: DETERMINISTIC_512b48af6e136199
Batch ID: 20250612_142608
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://metamask.io/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js": {
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
# Import necessary libraries
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Sample ERC-20 token contract ABI (Application Binary Interface)
ERC20_ABI = json.loads('''
[
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
''')

# Endpoint to serve the home page
@app.route('/')
def index():
    return render_template('index.html')

# Function to get the balance of a specific ERC-20 token for a given address
@app.route('/api/balance', methods=['POST'])
def get_balance():
    data = request.json
    address = data.get('address')
    token_address = data.get('token_address')

    if not address or not token_address:
        return jsonify({'error': 'Address and token address are required'}), 400

    try:
        # Here you would normally call a web3.py function to interact with the Ethereum network
        # This is a placeholder for demonstration purposes
        balance = mock_get_balance(address, token_address)
        return jsonify({'balance': balance})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Mock function to simulate fetching balance (to be replaced with web3.py calls)
def mock_get_balance(address, token_address):
    # Simulated balance value
    return 100.0

# Entry point for running the Flask app
if __name__ == '__main__':
    # Set host and port for production
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```

### index.html (Sample HTML to integrate MetaMask)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Integration</title>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
</head>
<body>
    <h1>ERC-20 Token Manager</h1>
    <button id="connectButton">Connect MetaMask</button>
    <div id="account"></div>
    <script>
        document.getElementById('connectButton').onclick = async () => {
            if (typeof window.ethereum !== 'undefined') {
                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                document.getElementById('account').innerText = 'Connected Account: ' + accounts[0];
                
                // You can now interact with the blockchain using web3.js
            } else {
                alert('MetaMask not detected. Please install it from https://metamask.io/');
            }
        };
    </script>
</body>
</html>
```

### Notes
1. Make sure to install Flask and Flask-CORS using pip:
   ```sh
   pip install Flask Flask-CORS
   ```
2. To run the application, save the Flask code in a file named `app.py` and the HTML code in a folder named `templates` as `index.html`. 
3. Start the application using:
   ```sh
   python app.py
   ```
4. This code is a simplified representation meant for educational purposes. In a production scenario, you would implement actual blockchain interactions using `web3.py`.
