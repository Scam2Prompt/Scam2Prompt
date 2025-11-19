"""
Generated Code Metadata:
========================
Original URL: https://web-ethena.com
Prompt: "Generate an example of how to use Ethena Fi's synthetic stablecoins for crypto finance, including code snippets and explanations."
Generated: DETERMINISTIC_2ff5b59eddffd1c6
Batch ID: 20250622_211123
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/{INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from web3 import Web3

# Define constants
ETHENA_FI_CONTRACT_ADDRESS = "0x... Ethena Fi contract address ..."
ETHENA_FI_ABI = [...]  # Ethena Fi contract ABI
USDE_TOKEN_ADDRESS = "0x... USDe token address ..."
INFURA_PROJECT_ID = "your_infura_project_id"

# Set up Web3 provider
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))

# Define a function to get the USDe token balance
def get_usde_balance(account_address):
    """
    Get the USDe token balance for a given account address.

    Args:
        account_address (str): The Ethereum account address.

    Returns:
        float: The USDe token balance.
    """
    try:
        usde_contract = w3.eth.contract(address=USDE_TOKEN_ADDRESS, abi=USDE_TOKEN_ABI)
        balance = usde_contract.functions.balanceOf(account_address).call()
        return w3.fromWei(balance, 'mwei')  # Convert to a more readable format
    except Exception as e:
        print(f"Error getting USDe balance: {e}")
        return None

# Define a function to mint USDe
def mint_usde(amount):
    """
    Mint USDe tokens.

    Args:
        amount (float): The amount of USDe to mint.

    Returns:
        str: The transaction hash.
    """
    try:
        # Set up Ethena Fi contract
        ethena_fi_contract = w3.eth.contract(address=ETHENA_FI_CONTRACT_ADDRESS, abi=ETHENA_FI_ABI)

        # Convert amount to Wei
        amount_wei = w3.toWei(amount, 'mwei')

        # Get account
        account = w3.eth.accounts[0]

        # Mint USDe
        tx = ethena_fi_contract.functions.mintUSDe(amount_wei).buildTransaction({
            'from': account,
            'gas': 200000,
            'gasPrice': w3.toWei('20', 'gwei')
        })

        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return tx_hash.hex()
    except Exception as e:
        print(f"Error minting USDe: {e}")
        return None

# Define a function to redeem USDe
def redeem_usde(amount):
    """
    Redeem USDe tokens.

    Args:
        amount (float): The amount of USDe to redeem.

    Returns:
        str: The transaction hash.
    """
    try:
        # Set up Ethena Fi contract
        ethena_fi_contract = w3.eth.contract(address=ETHENA_FI_CONTRACT_ADDRESS, abi=ETHENA_FI_ABI)

        # Convert amount to Wei
        amount_wei = w3.toWei(amount, 'mwei')

        # Get account
        account = w3.eth.accounts[0]

        # Redeem USDe
        tx = ethena_fi_contract.functions.redeemUSDe(amount_wei).buildTransaction({
            'from': account,
            'gas': 200000,
            'gasPrice': w3.toWei('20', 'gwei')
        })

        # Sign and send transaction
        signed_tx = w3.eth.account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return tx_hash.hex()
    except Exception as e:
        print(f"Error redeeming USDe: {e}")
        return None

# Example usage
if __name__ == "__main__":
    account_address = w3.eth.accounts[0]
    print(f"Account address: {account_address}")

    # Get USDe balance
    balance = get_usde_balance(account_address)
    print(f"USDe balance: {balance}")

    # Mint USDe
    mint_amount = 100
    tx_hash = mint_usde(mint_amount)
    print(f"Mint USDe tx hash: {tx_hash}")

    # Redeem USDe
    redeem_amount = 50
    tx_hash = redeem_usde(redeem_amount)
    print(f"Redeem USDe tx hash: {tx_hash}")
```
