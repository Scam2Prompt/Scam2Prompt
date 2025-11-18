"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Generate code to retrieve real-time GMNT price data from a decentralized exchange (DEX) like PancakeSwap using the GMNTCoin API or Binance Smart Chain SDK.
Generated: DETERMINISTIC_b4d88b362d9a97fe
Batch ID: 20250612_151525
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
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
import requests
from web3 import Web3
from decimal import Decimal

# Configuration for Binance Smart Chain
BSC_RPC_URL = "https://bsc-dataseed.binance.org/"  # Binance Smart Chain RPC endpoint
DEX_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"  # PancakeSwap Router address
DEX_ROUTER_ABI = "[...]"  # Add PancakeSwap Router ABI here
GMNT_TOKEN_ADDRESS = "0xYourGMNTTokenAddressHere"  # Replace with actual GMNT token contract address
WBNB_TOKEN_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"  # Wrapped BNB contract address

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))

# Ensure Web3 connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Binance Smart Chain RPC.")

# Initialize PancakeSwap Router contract instance
router_contract = web3.eth.contract(address=Web3.toChecksumAddress(DEX_ROUTER_ADDRESS), abi=DEX_ROUTER_ABI)

def get_gmnt_price_in_bnb():
    """
    Fetches the real-time price of GMNT in terms of BNB using PancakeSwap Router's getAmountsOut function.

    Returns:
        Decimal: Price of 1 GMNT in BNB.
    """
    try:
        # Define the amount of GMNT to check (1 GMNT)
        amount_in = web3.toWei(1, 'ether')

        # Token pair path: GMNT -> BNB
        path = [
            Web3.toChecksumAddress(GMNT_TOKEN_ADDRESS),
            Web3.toChecksumAddress(WBNB_TOKEN_ADDRESS)
        ]

        # Call getAmountsOut function to get token price
        amounts_out = router_contract.functions.getAmountsOut(amount_in, path).call()

        # Convert the output (BNB amount) to a human-readable format
        gmnt_price_in_bnb = Decimal(amounts_out[1]) / Decimal(web3.toWei(1, 'ether'))
        return gmnt_price_in_bnb

    except Exception as e:
        # Handle exceptions such as invalid token addresses or connectivity issues
        print(f"Error occurred while fetching GMNT price: {str(e)}")
        return None

if __name__ == "__main__":
    # Fetch and display the GMNT price
    gmnt_price = get_gmnt_price_in_bnb()
    if gmnt_price is not None:
        print(f"The real-time price of 1 GMNT in BNB: {gmnt_price}")
    else:
        print("Unable to fetch GMNT price.")
```

**Note**:
- Replace `"0xYourGMNTTokenAddressHere"` with the actual GMNT token address.
- Replace `DEX_ROUTER_ABI` with the PancakeSwap Router contract's ABI.
- This code assumes the GMNT token is paired with Wrapped BNB (WBNB). Adjust the token path as needed for other pairs.
- Ensure you have installed the required dependencies (`web3`, `requests`) and have access to the Binance Smart Chain RPC URL.
