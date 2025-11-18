"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-git-feature-update-history-transactions-venus-protocol.vercel.app
Prompt: Explain how to use the Venus Protocol's features to calculate borrowing limits and collateral ratios programmatically.
Generated: DETERMINISTIC_a1f9c789690f5ccd
Batch ID: 20250612_151626
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
# Import necessary libraries
from web3 import Web3
import json

# Constants
RPC_URL = "https://bsc-dataseed.binance.org/"  # Binance Smart Chain RPC URL
VENUS_COMPTROLLER_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with the actual Comptroller contract address
VENUS_CTOKEN_ABI = "path/to/venus_ctoken_abi.json"  # Replace with the actual path to the Venus cToken ABI JSON
VENUS_COMPTROLLER_ABI = "path/to/venus_comptroller_abi.json"  # Replace with the actual path to the Comptroller ABI JSON

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Binance Smart Chain RPC.")

# Load contract ABIs
with open(VENUS_CTOKEN_ABI, 'r') as f:
    cToken_abi = json.load(f)

with open(VENUS_COMPTROLLER_ABI, 'r') as f:
    comptroller_abi = json.load(f)

# Initialize Comptroller contract
comptroller = web3.eth.contract(address=VENUS_COMPTROLLER_ADDRESS, abi=comptroller_abi)

def get_user_borrowing_limit(user_address):
    """
    Calculate the user's borrowing limit based on their supplied assets and collateral factors.

    Args:
        user_address (str): The user's wallet address.

    Returns:
        float: The maximum borrowing limit in USD.
    """
    try:
        # Get the user's account details
        account_liquidity = comptroller.functions.getAccountLiquidity(user_address).call()
        (_, liquidity, shortfall) = account_liquidity

        if shortfall > 0:
            raise ValueError("User is in shortfall (borrowed more than their limit).")

        # Liquidity is returned in scaled-up USD (18 decimals)
        borrowing_limit = web3.fromWei(liquidity, 'ether')  # Convert to human-readable USD
        return borrowing_limit

    except Exception as e:
        raise RuntimeError(f"Error calculating borrowing limit: {str(e)}")

def get_collateral_ratio(user_address):
    """
    Calculate the user's collateral ratio, which is a measure of how much collateral is being used.

    Args:
        user_address (str): The user's wallet address.

    Returns:
        float: Collateral ratio as a percentage.
    """
    try:
        # Get the user's account details
        account_liquidity = comptroller.functions.getAccountLiquidity(user_address).call()
        (_, liquidity, shortfall) = account_liquidity

        if shortfall > 0:
            raise ValueError("User is in shortfall (borrowed more than their limit).")

        # Get total borrowed value by the user
        total_borrowed = get_total_borrowed_value(user_address)

        if total_borrowed == 0:
            return 0.0  # No borrowing, no ratio to calculate

        # Collateral ratio formula: (Total Borrowed / (Total Borrowed + Liquidity)) * 100
        collateral_ratio = (total_borrowed / (total_borrowed + web3.fromWei(liquidity, 'ether'))) * 100
        return collateral_ratio

    except Exception as e:
        raise RuntimeError(f"Error calculating collateral ratio: {str(e)}")

def get_total_borrowed_value(user_address):
    """
    Helper function to calculate the total borrowed value by the user.

    Args:
        user_address (str): The user's wallet address.

    Returns:
        float: Total borrowed value in USD.
    """
    try:
        # Get the list of assets entered by the user
        assets = comptroller.functions.getAssetsIn(user_address).call()
        total_borrowed = 0

        for asset in assets:
            # Initialize cToken contract
            cToken = web3.eth.contract(address=asset, abi=cToken_abi)

            # Get borrow balance (scaled up by 18 decimals)
            borrow_balance = cToken.functions.borrowBalanceCurrent(user_address).call()

            # Get the asset's underlying price from the price oracle
            price_oracle_address = comptroller.functions.oracle().call()
            price_oracle = web3.eth.contract(address=price_oracle_address, abi=comptroller_abi)
            underlying_price = price_oracle.functions.getUnderlyingPrice(asset).call()  # Scaled by 18 decimals

            # Convert borrow balance to USD
            borrow_balance_in_usd = web3.fromWei(borrow_balance * underlying_price, 'ether')
            total_borrowed += borrow_balance_in_usd

        return total_borrowed

    except Exception as e:
        raise RuntimeError(f"Error calculating total borrowed value: {str(e)}")

# Example Usage
if __name__ == "__main__":
    user_address = "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef"  # Replace with an actual wallet address
    try:
        borrowing_limit = get_user_borrowing_limit(user_address)
        collateral_ratio = get_collateral_ratio(user_address)

        print(f"Borrowing Limit (USD): {borrowing_limit:.2f}")
        print(f"Collateral Ratio (%): {collateral_ratio:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
