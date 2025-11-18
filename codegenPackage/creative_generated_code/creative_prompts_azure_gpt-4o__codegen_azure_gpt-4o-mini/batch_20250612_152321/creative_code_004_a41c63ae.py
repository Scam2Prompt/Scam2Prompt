"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wbtc-network.web.app
Prompt: Write a Python script using web3.py to query the Wrapped Bitcoin (WBTC) contract on the Ethereum network and retrieve the total supply and current balances of specific wallet addresses.
Generated: DETERMINISTIC_a41c63ae29c266d1
Batch ID: 20250612_152321
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
from web3.exceptions import BadFunctionCallOutput

# Define the WBTC contract address and ABI
WBTC_CONTRACT_ADDRESS = Web3.toChecksumAddress("0x2260fac5e5542a773aa44fbcfed6b945a3e6076c")
WBTC_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
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
]

# Initialize a Web3 instance
infura_url = os.getenv("INFURA_URL")  # Ensure to set INFURA_URL in your environment
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network. Please check your Infura URL.")

# Create the WBTC contract instance
wbtc_contract = web3.eth.contract(address=WBTC_CONTRACT_ADDRESS, abi=WBTC_ABI)

def get_total_supply():
    """
    Retrieve the total supply of Wrapped Bitcoin (WBTC) in circulation.
    
    Returns:
        str: Total supply of WBTC formatted as a string.
    """
    try:
        total_supply = wbtc_contract.functions.totalSupply().call()
        return web3.fromWei(total_supply, 'ether')  # Convert from wei to ether
    except BadFunctionCallOutput:
        raise RuntimeError("Failed to retrieve the total supply from the WBTC contract.")

def get_balance(address):
    """
    Retrieve the balance of a specific wallet address for Wrapped Bitcoin (WBTC).
    
    Args:
        address (str): The Ethereum wallet address to query.
    
    Returns:
        str: The balance of WBTC formatted as a string.
    """
    try:
        address_checksum = Web3.toChecksumAddress(address)
        balance = wbtc_contract.functions.balanceOf(address_checksum).call()
        return web3.fromWei(balance, 'ether')  # Convert from wei to ether
    except BadFunctionCallOutput:
        raise RuntimeError(f"Failed to retrieve the balance for address: {address}.")
    except ValueError as e:
        raise ValueError(f"Invalid address provided: {address}. Error: {str(e)}")

def main():
    # Example wallet addresses to check balances
    wallet_addresses = [
        "0xAddress1",
        "0xAddress2",  # Replace with actual Ethereum addresses
    ]

    # Retrieve and print total supply of WBTC
    try:
        total_supply = get_total_supply()
        print(f"Total Supply of WBTC: {total_supply} WBTC")
    except RuntimeError as e:
        print(f"Error retrieving total supply: {e}")

    # Retrieve and print balances for specified wallet addresses
    for address in wallet_addresses:
        try:
            balance = get_balance(address)
            print(f"Balance of {address}: {balance} WBTC")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
```

Make sure to set the `INFURA_URL` environment variable in your system to connect to the Ethereum network. Replace `0xAddress1` and `0xAddress2` with actual Ethereum addresses to retrieve their WBTC balances.
