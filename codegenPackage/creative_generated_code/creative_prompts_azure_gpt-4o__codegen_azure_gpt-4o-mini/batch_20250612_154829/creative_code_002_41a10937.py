"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophonnow.io
Prompt: Develop a Python program using the Web3 library to retrieve the current $SOPH presale price and calculate the total cost for purchasing a specified number of tokens.
Generated: DETERMINISTIC_41a10937b6b2f21a
Batch ID: 20250612_154829
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

# Define constants
INFURA_URL = os.getenv("INFURA_URL")  # URL for the Infura node
TOKEN_CONTRACT_ADDRESS = "0xYourTokenContractAddress"  # Replace with the actual token contract address
TOKEN_DECIMALS = 18  # Decimals used by the token
PRESALE_PRICE_METHOD = 'presalePrice'  # Replace with actual method name for getting presale price
TOKENS_TO_PURCHASE = 10  # Number of tokens to purchase

def get_presale_price(web3, contract_address):
    """
    Retrieves the current presale price of the token.

    Args:
        web3 (Web3): An instance of the Web3 class.
        contract_address (str): The address of the token contract.

    Returns:
        float: The presale price in ETH.
    """
    try:
        # Load the contract
        contract = web3.eth.contract(address=contract_address, abi=ABI)  # ABI needs to be defined
        # Call the presale price method
        presale_price_wei = contract.functions[PRESALE_PRICE_METHOD]().call()
        # Convert Wei to ETH
        return web3.fromWei(presale_price_wei, 'ether')
    except Exception as e:
        print(f"Error retrieving presale price: {e}")
        return None

def calculate_total_cost(presale_price, tokens_to_purchase):
    """
    Calculates the total cost for purchasing a specified number of tokens.

    Args:
        presale_price (float): The presale price of a single token in ETH.
        tokens_to_purchase (int): The number of tokens to purchase.

    Returns:
        float: Total cost in ETH.
    """
    return presale_price * tokens_to_purchase

def main():
    """
    Main function to execute the script.
    """
    # Initialize Web3
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    if not web3.isConnected():
        print("Error: Unable to connect to the Ethereum network.")
        return

    # Get the presale price
    presale_price = get_presale_price(web3, TOKEN_CONTRACT_ADDRESS)
    
    if presale_price is None:
        print("Failed to get presale price.")
        return

    # Calculate the total cost
    total_cost = calculate_total_cost(presale_price, TOKENS_TO_PURCHASE)

    # Output the results
    print(f"Current presale price of $SOPH: {presale_price} ETH")
    print(f"Total cost for purchasing {TOKENS_TO_PURCHASE} tokens: {total_cost} ETH")

if __name__ == "__main__":
    main()
```

**Note**: Ensure to replace `"0xYourTokenContractAddress"` with the actual token contract address and provide the appropriate ABI for the contract in the `get_presale_price` function.
