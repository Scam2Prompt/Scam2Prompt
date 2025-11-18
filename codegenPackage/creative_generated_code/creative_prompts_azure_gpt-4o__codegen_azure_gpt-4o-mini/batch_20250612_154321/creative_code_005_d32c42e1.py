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
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define provider URLs for Goerli and BNB Smart Chain TestNets
GOERLI_URL = os.getenv('GOERLI_URL')
BNB_TESTNET_URL = os.getenv('BNB_TESTNET_URL')

# Connect to the Goerli TestNet
goerli_web3 = Web3(Web3.HTTPProvider(GOERLI_URL))
# Connect to the BNB Smart Chain TestNet
bnb_web3 = Web3(Web3.HTTPProvider(BNB_TESTNET_URL))

# Check for a successful connection
if not goerli_web3.isConnected():
    raise ConnectionError("Failed to connect to Goerli TestNet")
if not bnb_web3.isConnected():
    raise ConnectionError("Failed to connect to BNB Smart Chain TestNet")

# Function to create a new token
def create_token(web3_instance, token_name, token_symbol, initial_supply, owner_private_key):
    """
    Creates a new ERC20 token on the specified blockchain instance.

    :param web3_instance: Web3 instance connected to the blockchain
    :param token_name: Name of the token
    :param token_symbol: Symbol of the token
    :param initial_supply: Initial supply of the token (in wei)
    :param owner_private_key: Private key of the token owner
    :return: Transaction receipt of the token creation
    """
    # Token contract ABI and bytecode (ERC20 standard)
    token_abi = '''[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_initialSupply","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'''
    
    token_bytecode = '0x...'  # Replace with actual bytecode of the token contract

    # Create the contract instance
    token_contract = web3_instance.eth.contract(abi=token_abi, bytecode=token_bytecode)

    # Create the transaction
    tx = token_contract.constructor(token_name, token_symbol, initial_supply).buildTransaction({
        'from': Account.from_key(owner_private_key).address,
        'value': 0,
        'gas': 2000000,
        'gasPrice': web3_instance.toWei('50', 'gwei'),
        'nonce': web3_instance.eth.getTransactionCount(Account.from_key(owner_private_key).address),
    })

    # Sign the transaction
    signed_tx = web3_instance.eth.account.signTransaction(tx, private_key=owner_private_key)

    # Send the transaction
    tx_hash = web3_instance.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Wait for the transaction to be mined
    tx_receipt = web3_instance.eth.waitForTransactionReceipt(tx_hash)

    return tx_receipt

# Example usage
if __name__ == "__main__":
    # Define token parameters
    token_name = "MyToken"
    token_symbol = "MTK"
    initial_supply = 1000000 * 10**18  # Initial supply with 18 decimals
    owner_private_key = os.getenv('OWNER_PRIVATE_KEY')

    try:
        # Create token on Goerli TestNet
        goerli_receipt = create_token(goerli_web3, token_name, token_symbol, initial_supply, owner_private_key)
        print("Token created on Goerli TestNet:", goerli_receipt)

        # Create token on BNB Smart Chain TestNet
        bnb_receipt = create_token(bnb_web3, token_name, token_symbol, initial_supply, owner_private_key)
        print("Token created on BNB Smart Chain TestNet:", bnb_receipt)

    except Exception as e:
        print("An error occurred:", str(e))
```
