"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Develop a script using Python and Web3 to query the Oracle Meme presale contract for the current token price and the amount of USDT raised.
Generated: DETERMINISTIC_714b0fe32c1cf6d3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to the Ethereum network (Mainnet, Ropsten, etc.)
INFURA_URL = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection to the Ethereum network is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Oracle Meme presale contract address (replace with the actual address)
PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress"

# ABI for the presale contract (replace with the actual ABI)
PRESALE_CONTRACT_ABI = [
    # Add the relevant ABI JSON here
]

# Create a contract instance
presale_contract = web3.eth.contract(address=PRESALE_CONTRACT_ADDRESS, abi=PRESALE_CONTRACT_ABI)

def get_current_token_price():
    """
    Queries the presale contract for the current token price.
    
    Returns:
        float: The current token price in USDT.
    """
    try:
        token_price = presale_contract.functions.getCurrentTokenPrice().call()
        return web3.fromWei(token_price, 'ether')  # Convert from Wei to Ether
    except Exception as e:
        raise RuntimeError(f"Error fetching token price: {str(e)}")

def get_usdt_raised():
    """
    Queries the presale contract for the total amount of USDT raised.
    
    Returns:
        float: The total amount of USDT raised.
    """
    try:
        usdt_raised = presale_contract.functions.getTotalUSDTRaised().call()
        return web3.fromWei(usdt_raised, 'ether')  # Convert from Wei to Ether
    except Exception as e:
        raise RuntimeError(f"Error fetching USDT raised: {str(e)}")

def main():
    """
    Main function to execute the script.
    """
    try:
        current_price = get_current_token_price()
        total_usdt_raised = get_usdt_raised()
        
        print(f"Current Token Price: {current_price} USDT")
        print(f"Total USDT Raised: {total_usdt_raised} USDT")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

Make sure to replace `0xYourPresaleContractAddress` and the ABI placeholder with the actual contract address and ABI for the Oracle Meme presale contract. Additionally, ensure that you have the `dotenv` and `web3` libraries installed in your Python environment.
