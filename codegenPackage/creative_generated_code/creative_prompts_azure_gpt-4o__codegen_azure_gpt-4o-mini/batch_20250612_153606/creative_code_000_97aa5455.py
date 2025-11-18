"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokss.pages.dev
Prompt: Write a Python script using the web3.py library to interact with the GROK Token smart contract and check the balance of a given wallet address.
Generated: DETERMINISTIC_97aa5455928dc6dc
Batch ID: 20250612_153606
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

# Load environment variables for configuration
INFURA_URL = os.getenv('INFURA_URL')  # The URL to the Ethereum node
GROK_CONTRACT_ADDRESS = os.getenv('GROK_CONTRACT_ADDRESS')  # The deployed GROK Token contract address

# ABI for the GROK Token contract
GROK_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

def main(wallet_address):
    """
    Main function to check the balance of the specified wallet address.
    
    :param wallet_address: The Ethereum wallet address to check the GROK Token balance for.
    :raises ValueError: If the wallet address is invalid or balance retrieval fails.
    """
    
    # Validate the wallet address
    if not Web3.isChecksumAddress(wallet_address):
        raise ValueError("Invalid Ethereum address format.")

    # Initialize a Web3 instance
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    # Check if the connection to the Ethereum node is successful
    if not web3.isConnected():
        raise ConnectionError("Unable to connect to the Ethereum node.")

    # Create a contract instance
    grok_contract = web3.eth.contract(address=GROK_CONTRACT_ADDRESS, abi=GROK_ABI)

    try:
        # Fetch the balance of the specified wallet address
        balance = grok_contract.functions.balanceOf(wallet_address).call()
        # Convert the balance from Wei (or the smallest token unit) to a human-readable format
        balance_readable = web3.fromWei(balance, 'ether')  # Adjust conversion as per token's decimal

        print(f"Balance of wallet {wallet_address}: {balance_readable} GROK")
    except Exception as e:
        raise RuntimeError(f"An error occurred while retrieving the balance: {str(e)}")

if __name__ == "__main__":
    # Specify the wallet address to check (replace with a valid address)
    wallet_address = "0xYourWalletAddressHere"  # Replace with the actual wallet address
    main(wallet_address)
```

### Note:
- The user should set their Infura API URL and the GROK Token contract address as environment variables (`INFURA_URL` and `GROK_CONTRACT_ADDRESS`).
- The wallet address should be replaced in the `if __name__ == "__main__":` block with a valid Ethereum address.
- The balance conversion assumes the GROK token uses 18 decimals. Adjust `web3.fromWei` conversion accordingly if necessary.
