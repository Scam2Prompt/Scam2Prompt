"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: What are the steps to integrate USDC with Ethereum for DeFi applications?
Generated: DETERMINISTIC_d1e2272651968251
Batch ID: 20250612_155739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import web3
from web3 import Web3

# Define constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'  # Replace with your Infura project ID
USDC_CONTRACT_ADDRESS = '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'  # USDC contract address on Ethereum mainnet
USDC_ABI = [
    # Minimal ABI for USDC, including only the functions we need
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "recipient", "type": "address"},
            {"name": "amount", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Initialize a web3 instance
def init_web3():
    try:
        w3 = Web3(Web3.HTTPProvider(INFURA_URL))
        if not w3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum network.")
        return w3
    except Exception as e:
        print(f"Error initializing Web3: {e}")
        raise

# Get USDC balance for a given address
def get_usdc_balance(w3, address):
    try:
        usdc_contract = w3.eth.contract(address=USDC_CONTRACT_ADDRESS, abi=USDC_ABI)
        balance = usdc_contract.functions.balanceOf(address).call()
        decimals = usdc_contract.functions.decimals().call()
        return balance / (10 ** decimals)  # Convert to human-readable format
    except Exception as e:
        print(f"Error fetching USDC balance: {e}")
        return None

# Transfer USDC to a specified address
def transfer_usdc(w3, from_address, private_key, to_address, amount):
    try:
        usdc_contract = w3.eth.contract(address=USDC_CONTRACT_ADDRESS, abi=USDC_ABI)
        decimals = usdc_contract.functions.decimals().call()
        amount_in_wei = int(amount * (10 ** decimals))  # Convert to Wei

        # Build transaction
        nonce = w3.eth.getTransactionCount(from_address)
        transaction = usdc_contract.functions.transfer(to_address, amount_in_wei).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 200000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return w3.toHex(txn_hash)
    except Exception as e:
        print(f"Error while transferring USDC: {e}")
        return None

# Main function to demonstrate USDC balance retrieval and transfer
def main():
    w3 = init_web3()
    
    # Example addresses and private key (DO NOT USE IN PRODUCTION)
    my_address = 'YOUR_ADDRESS'  # Replace with your Ethereum address
    my_private_key = 'YOUR_PRIVATE_KEY'  # Replace with your Ethereum private key
    recipient_address = 'RECIPIENT_ADDRESS'  # Replace with recipient's address

    # Get USDC balance
    balance = get_usdc_balance(w3, my_address)
    if balance is not None:
        print(f'Your USDC Balance: {balance} USDC')

    # Transfer USDC (optional)
    amount_to_transfer = 10  # Amount of USDC to transfer
    txn_hash = transfer_usdc(w3, my_address, my_private_key, recipient_address, amount_to_transfer)
    if txn_hash:
        print(f'Transaction successful with hash: {txn_hash}')

if __name__ == "__main__":
    main()
```
