"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Can you provide a code example for bridging tokens between Ethereum and BNB Chain using Dypius tools?
Generated: DETERMINISTIC_b47c3d40184c486d
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import web3
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware

# Constants
ETH_RPC_URL = "<Your Ethereum RPC URL>"  # RPC URL for Ethereum network
BNB_RPC_URL = "<Your BNB Chain RPC URL>"  # RPC URL for BNB Chain network
PRIVATE_KEY = "<Your private key>"  # Private key for the account initiating the bridge transaction
BRIDGE_CONTRACT_ADDRESS = "<Dypius Bridge Contract Address>"  # Address of the Dypius bridge contract
TOKEN_ADDRESS = "<Token Contract Address>"  # Address of the token to be bridged
TO_CHAIN_ID = 56  # Chain ID for BNB Chain
TOKEN_AMOUNT = Web3.toWei(10, 'ether')  # Amount of tokens to bridge (10 tokens in this example)

# Initialize Web3 instances
eth_web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
bnb_web3 = Web3(Web3.HTTPProvider(BNB_RPC_URL))

# Apply middleware for PoA networks if necessary
bnb_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure connections to RPC endpoints are successful
if not eth_web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum RPC")

if not bnb_web3.isConnected():
    raise ConnectionError("Failed to connect to BNB Chain RPC")

# Create account from private key
account = Account.from_key(PRIVATE_KEY)

# Function to build and send a transaction
def send_bridge_transaction():
    # Load Bridge Contract ABI (replace `<ABI>` placeholder with actual ABI of the contract)
    bridge_contract_abi = "<ABI>"
    bridge_contract = eth_web3.eth.contract(address=BRIDGE_CONTRACT_ADDRESS, abi=bridge_contract_abi)

    # Build the transaction
    nonce = eth_web3.eth.getTransactionCount(account.address)
    tx = bridge_contract.functions.bridgeTokens(
        TOKEN_ADDRESS,   # Address of the token to bridge
        TO_CHAIN_ID,     # Destination chain ID
        TOKEN_AMOUNT     # Amount of tokens to bridge
    ).buildTransaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 2000000,  # Estimate gas limit
        'gasPrice': eth_web3.eth.gasPrice,  # Fetch current gas price
    })

    # Sign the transaction
    signed_tx = eth_web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send the transaction
    tx_hash = eth_web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Return the transaction hash
    return tx_hash.hex()

# Main execution flow
if __name__ == "__main__":
    try:
        print("Initiating token bridge...")
        transaction_hash = send_bridge_transaction()
        print(f"Transaction successfully sent. TX Hash: {transaction_hash}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
