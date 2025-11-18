"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Write a Python script to interact with the QiDao protocol and create MAI stablecoins by depositing ERC-20 tokens as collateral. Include functionality for managing collateralized vaults.
Generated: DETERMINISTIC_50a53da06cc9a8ad
Batch ID: 20250612_155037
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
from web3.middleware import geth_poa_middleware
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Environment variables for configuration
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key for the wallet
QI_DAO_CONTRACT_ADDRESS = os.getenv("QI_DAO_CONTRACT_ADDRESS")  # QiDao contract address
ERC20_TOKEN_ADDRESS = os.getenv("ERC20_TOKEN_ADDRESS")  # ERC-20 token address
VAULT_ID = int(os.getenv("VAULT_ID", 0))  # Vault ID (create a new vault if not provided)

# Constants
COLLATERAL_AMOUNT = int(os.getenv("COLLATERAL_AMOUNT", 100 * 10**18))  # Amount to deposit as collateral
MAI_AMOUNT = int(os.getenv("MAI_AMOUNT", 50 * 10**18))  # Amount of MAI to mint

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check connection
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network.")

# Get wallet address
wallet_address = Account.privateKeyToAccount(PRIVATE_KEY).address

# Load contract ABI for QiDao
with open("qi_dao_abi.json", "r") as abi_file:
    qi_dao_abi = json.load(abi_file)

# Load contract ABI for ERC-20 token (standard ABI)
with open("erc20_abi.json", "r") as abi_file:
    erc20_abi = json.load(abi_file)

# Initialize QiDao contract
qi_dao_contract = web3.eth.contract(address=QI_DAO_CONTRACT_ADDRESS, abi=qi_dao_abi)

# Initialize ERC-20 token contract
erc20_contract = web3.eth.contract(address=ERC20_TOKEN_ADDRESS, abi=erc20_abi)

def approve_erc20(amount):
    """Approve the QiDao contract to spend ERC-20 tokens."""
    try:
        tx = erc20_contract.functions.approve(QI_DAO_CONTRACT_ADDRESS, amount).buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 200000,
            'gasPrice': web3.toWei('20', 'gwei')
        })
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"ERC-20 token approved for QiDao contract. Tx Hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error during ERC-20 token approval: {e}")

def create_vault():
    """Create a new vault on the QiDao protocol."""
    try:
        tx = qi_dao_contract.functions.createVault().buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 300000,
            'gasPrice': web3.toWei('20', 'gwei')
        })
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        vault_id = qi_dao_contract.functions.getVaultId(wallet_address).call()
        print(f"Vault created successfully. Vault ID: {vault_id}, Tx Hash: {tx_hash.hex()}")
        return vault_id
    except Exception as e:
        print(f"Error during vault creation: {e}")

def deposit_collateral(vault_id, amount):
    """Deposit collateral into a vault."""
    try:
        tx = qi_dao_contract.functions.depositCollateral(vault_id, amount).buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 300000,
            'gasPrice': web3.toWei('20', 'gwei')
        })
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Collateral deposited successfully. Tx Hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error during collateral deposit: {e}")

def mint_mai(vault_id, amount):
    """Mint MAI stablecoins from a vault."""
    try:
        tx = qi_dao_contract.functions.borrow(vault_id, amount).buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 300000,
            'gasPrice': web3.toWei('20', 'gwei')
        })
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"MAI stablecoins minted successfully. Tx Hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error during MAI minting: {e}")

if __name__ == "__main__":
    # Approve QiDao contract to spend ERC-20 tokens
    approve_erc20(COLLATERAL_AMOUNT)
    
    # Create a new vault if no vault ID is provided
    vault_id = VAULT_ID if VAULT_ID != 0 else create_vault()
    
    # Deposit collateral into the vault
    deposit_collateral(vault_id, COLLATERAL_AMOUNT)
    
    # Mint MAI stablecoins
    mint_mai(vault_id, MAI_AMOUNT)
```

**Dependencies:**
1. Install Web3 library: `pip install web3`
2. Install dotenv library: `pip install python-dotenv`
3. Provide `qi_dao_abi.json` and `erc20_abi.json` ABI files for QiDao and ERC-20 tokens respectively.
4. Set appropriate values in a `.env` file:
   ```
   INFURA_URL=<Your Infura URL>
   PRIVATE_KEY=<Your Private Key>
   QI_DAO_CONTRACT_ADDRESS=<QiDao Contract Address>
   ERC20_TOKEN_ADDRESS=<ERC20 Token Address>
   COLLATERAL_AMOUNT=<Amount of Collateral in Wei>
   MAI_AMOUNT=<Amount of MAI to Mint in Wei>
   VAULT_ID=0
   ```
