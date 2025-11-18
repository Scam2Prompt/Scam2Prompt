"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-coin-creator.pages.dev
Prompt: Generate code for testing token creation on Goerli TestNet and BNB Smart Chain TestNet, based on the functionality described on eth-coin-creator.pages.dev.
Generated: DETERMINISTIC_d32c42e12caa3665
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables for Goerli and BNB Smart Chain TestNet
GOERLI_RPC_URL = os.getenv("GOERLI_RPC_URL")
BNB_TESTNET_RPC_URL = os.getenv("BNB_TESTNET_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Public address of the wallet

# Token configuration
TOKEN_NAME = "MyTestToken"
TOKEN_SYMBOL = "MTT"
TOKEN_DECIMALS = 18
TOKEN_SUPPLY = 1000000

# ERC20 Token ABI (Minimal for testing purposes)
TOKEN_ABI = '''
[
    {
        "inputs": [
            {"internalType": "uint256", "name": "initialSupply", "type": "uint256"},
            {"internalType": "string", "name": "name", "type": "string"},
            {"internalType": "string", "name": "symbol", "type": "string"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "internalType": "address", "name": "owner", "type": "address"},
            {"indexed": true, "internalType": "address", "name": "spender", "type": "address"},
            {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "internalType": "address", "name": "from", "type": "address"},
            {"indexed": true, "internalType": "address", "name": "to", "type": "address"},
            {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "sender", "type": "address"},
            {"internalType": "address", "name": "recipient", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "spender", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
'''

# Function to deploy token on a given network
def deploy_token(network_name, rpc_url):
    try:
        # Initialize Web3
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not web3.isConnected():
            raise Exception(f"Failed to connect to {network_name}")

        # Load wallet credentials
        wallet_address = web3.toChecksumAddress(WALLET_ADDRESS)
        private_key = PRIVATE_KEY

        # Compile and deploy token contract
        compiled_contract = web3.eth.contract(abi=TOKEN_ABI, bytecode='YOUR_CONTRACT_BYTECODE_HERE')  # Replace with actual bytecode
        nonce = web3.eth.getTransactionCount(wallet_address)

        # Create the transaction
        transaction = compiled_contract.constructor(
            TOKEN_SUPPLY * (10 ** TOKEN_DECIMALS),
            TOKEN_NAME,
            TOKEN_SYMBOL
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print(f"Token deployment transaction sent on {network_name}: {web3.toHex(tx_hash)}")

        # Wait for the transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Contract deployed on {network_name} at address: {receipt.contractAddress}")

        return receipt.contractAddress
    except Exception as e:
        print(f"Error deploying token on {network_name}: {str(e)}")
        return None


if __name__ == "__main__":
    # Deploy token on Goerli TestNet
    print("Deploying token on Goerli TestNet...")
    deploy_token("Goerli TestNet", GOERLI_RPC_URL)

    # Deploy token on BNB Smart Chain TestNet
    print("Deploying token on BNB Smart Chain TestNet...")
    deploy_token("BNB Smart Chain TestNet", BNB_TESTNET_RPC_URL)
```

### Notes:
1. Replace `'YOUR_CONTRACT_BYTECODE_HERE'` with the actual bytecode of the token contract.
2. Populate the `.env` file with your `GOERLI_RPC_URL`, `BNB_TESTNET_RPC_URL`, `PRIVATE_KEY`, and `WALLET_ADDRESS`.
