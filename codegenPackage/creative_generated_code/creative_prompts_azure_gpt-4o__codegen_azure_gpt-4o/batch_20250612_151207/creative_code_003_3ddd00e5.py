"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbfour-meme.pages.dev
Prompt: Write a Python script using Web3.py to query the balance of $FOUR tokens for a given wallet address, referencing the contract address provided on the webpage.
Generated: DETERMINISTIC_3ddd00e503ea0184
Batch ID: 20250612_151207
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
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
TOKEN_CONTRACT_ADDRESS = "0xYourFOURTokenContractAddressHere"  # Replace with the $FOUR token contract address
WALLET_ADDRESS = "0xYourWalletAddressHere"  # Replace with the desired wallet address
ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]  # Minimal ABI required to interact with the balanceOf function

def get_token_balance(web3, contract_address, wallet_address):
    """
    Queries the balance of $FOUR tokens for a given wallet address.

    Args:
        web3 (Web3): An instance of the Web3 library connected to the Ethereum blockchain.
        contract_address (str): The contract address of the $FOUR token.
        wallet_address (str): The wallet address to query the token balance for.

    Returns:
        int: The balance of $FOUR tokens in the wallet.
    """
    try:
        # Initialize the token contract
        contract = web3.eth.contract(address=contract_address, abi=ABI)

        # Call the balanceOf function from the contract
        balance = contract.functions.balanceOf(wallet_address).call()

        return balance
    except ContractLogicError:
        print("Error: Unable to fetch balance. Check the wallet or contract address.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

def main():
    # Connect to Ethereum blockchain using Infura
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    if not web3.isConnected():
        print("Error: Unable to connect to the Ethereum network. Check your Infura URL.")
        return

    if not web3.isAddress(TOKEN_CONTRACT_ADDRESS):
        print("Error: Invalid token contract address.")
        return

    if not web3.isAddress(WALLET_ADDRESS):
        print("Error: Invalid wallet address.")
        return

    # Fetch token balance
    balance = get_token_balance(web3, TOKEN_CONTRACT_ADDRESS, WALLET_ADDRESS)

    if balance is not None:
        print(f"The balance of $FOUR tokens for wallet {WALLET_ADDRESS} is: {balance}")
    else:
        print("Failed to retrieve token balance.")

if __name__ == "__main__":
    main()
```
