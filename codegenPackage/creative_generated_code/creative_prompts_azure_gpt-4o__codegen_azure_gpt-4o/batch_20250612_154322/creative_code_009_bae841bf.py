"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-creator.pages.dev
Prompt: Generate code for a web interface that allows users to input new currency data and initiate the ERC-20 token creation process, similar to the interface described on https://erc20-creator.pages.dev.
Generated: DETERMINISTIC_bae841bf1435c9bf
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py
# Description: A web interface for creating ERC-20 tokens based on user input.

from flask import Flask, render_template, request, jsonify
from web3 import Web3
import os

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
INFURA_URL = os.getenv('INFURA_URL')  # URL for connecting to Ethereum network
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Wallet private key for signing transactions
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')  # Your Ethereum wallet address

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure we're connected to the Ethereum network
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network.")

# Load ERC-20 Token Solidity code
ERC20_CONTRACT = """
pragma solidity ^0.8.0;

contract ERC20Token {
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;
    address public owner;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        owner = msg.sender;
        balanceOf[owner] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");
        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}
"""

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/create-token', methods=['POST'])
def create_token():
    # Extract user inputs
    token_name = request.form.get('name')
    token_symbol = request.form.get('symbol')
    token_decimals = int(request.form.get('decimals'))
    token_supply = int(request.form.get('supply'))

    if not token_name or not token_symbol or not token_decimals or not token_supply:
        return jsonify({'error': 'All fields are required'}), 400

    # Compile the Solidity contract
    compiled_contract = web3.eth.compile_source(ERC20_CONTRACT)
    contract_interface = compiled_contract['<stdin>:ERC20Token']

    # Create the transaction
    ERC20 = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)

    transaction = ERC20.constructor(token_name, token_symbol, token_decimals, token_supply).build_transaction({
        'chainId': 1,  # Ethereum Mainnet
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction using the private key
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    # Send the transaction to the Ethereum network
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return jsonify({'success': True, 'transaction_hash': web3.toHex(tx_hash)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Filename: templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERC-20 Token Creator</title>
</head>
<body>
    <h1>Create Your ERC-20 Token</h1>
    <form action="/create-token" method="POST">
        <label for="name">Token Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="symbol">Token Symbol:</label><br>
        <input type="text" id="symbol" name="symbol" required><br><br>

        <label for="decimals">Decimals:</label><br>
        <input type="number" id="decimals" name="decimals" required><br><br>

        <label for="supply">Initial Supply:</label><br>
        <input type="number" id="supply" name="supply" required><br><br>

        <button type="submit">Create Token</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure you have installed Flask and Web3 libraries (`pip install Flask web3`).
- Replace the environment variable placeholders (`INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`) with actual values.
- This app is configured for Ethereum Mainnet (`chainId: 1`). Adjust `chainId` for test networks.
- Consider using Flask-Env or dotenv to manage environment variables securely in production.
