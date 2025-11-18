"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9ias90dia90sdi9asidasdk.pages.dev
Prompt: Generate an example of integrating THORChain into a decentralized exchange to enable native cross-chain swaps for Bitcoin, Ethereum, and Avalanche. Include affiliate fee collection logic.
Generated: DETERMINISTIC_5a5b9e4143ed5db6
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://thornode.thorchain.info/v1": {
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
# Import required libraries
import requests
import json

# Constants
THORCHAIN_API_BASE = "https://thornode.thorchain.info/v1"
AFFILIATE_ADDRESS = "affiliate-address"  # Replace with your affiliate address
AFFILIATE_FEE_PERCENT = 0.003  # Affiliate fee, 0.3%
SUPPORTED_CHAINS = ["BTC", "ETH", "AVAX"]  # Supported chains for swaps

# Exception for handling THORChain errors
class THORChainError(Exception):
    pass

# Function to retrieve pool information from THORChain
def get_pool_info():
    try:
        response = requests.get(f"{THORCHAIN_API_BASE}/pools")
        response.raise_for_status()
        pools = response.json()
        return pools
    except requests.exceptions.RequestException as e:
        raise THORChainError(f"Failed to fetch pool information: {str(e)}")

# Function to validate whether a chain is supported
def validate_chain(chain: str):
    if chain not in SUPPORTED_CHAINS:
        raise ValueError(f"Unsupported chain: {chain}")

# Function to calculate affiliate fee
def calculate_affiliate_fee(amount: float) -> float:
    return amount * AFFILIATE_FEE_PERCENT

# Function to create a swap request
def create_swap(chain_in: str, chain_out: str, amount: float, recipient: str):
    # Validate input chains
    validate_chain(chain_in)
    validate_chain(chain_out)

    try:
        # Fetch pool information to ensure liquidity is available
        pools = get_pool_info()
        if chain_in not in [pool["asset"] for pool in pools]:
            raise THORChainError(f"No liquidity available for {chain_in}")
        if chain_out not in [pool["asset"] for pool in pools]:
            raise THORChainError(f"No liquidity available for {chain_out}")

        # Calculate affiliate fee
        affiliate_fee = calculate_affiliate_fee(amount)
        amount_after_fee = amount - affiliate_fee

        # Prepare swap request payload
        payload = {
            "asset_in": chain_in,
            "asset_out": chain_out,
            "amount": amount_after_fee,
            "recipient": recipient,
            "affiliate_address": AFFILIATE_ADDRESS,
            "affiliate_fee": affiliate_fee
        }

        # Post the swap request to THORChain
        response = requests.post(f"{THORCHAIN_API_BASE}/swap", json=payload)
        response.raise_for_status()
        return response.json()  # Return swap transaction details

    except requests.exceptions.RequestException as e:
        raise THORChainError(f"Failed to execute swap: {str(e)}")

# Example usage: Swap 0.1 BTC to ETH
if __name__ == "__main__":
    try:
        swap_details = create_swap(
            chain_in="BTC",
            chain_out="ETH",
            amount=0.1,
            recipient="recipient-eth-address"  # Replace with actual recipient address
        )
        print("Swap executed successfully:")
        print(json.dumps(swap_details, indent=2))
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
