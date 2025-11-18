"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeianm7lllm6v2rpyuah5gzsh22gxfikab5ie3xei6f2n3ngfvsx524.ipfs.dweb.link
Prompt: How can I use the 1inch API to aggregate liquidity from multiple DEXs on Binance Smart Chain? Provide code examples.
Generated: DETERMINISTIC_350b1ea8961ebcbd
Batch ID: 20250612_151547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.1inch.io/v5.0/": {
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

# Constants
BASE_URL = "https://api.1inch.io/v5.0/"  # Base URL for the 1inch API
CHAIN_ID = 56  # Binance Smart Chain ID

# Function to get swap quote from 1inch API
def get_swap_quote(from_token_address, to_token_address, amount, slippage=1):
    """
    Fetches a swap quote from the 1inch API.

    :param from_token_address: Address of the token being swapped (input token).
    :param to_token_address: Address of the token being received (output token).
    :param amount: Amount of input token to swap (in smallest token units).
    :param slippage: Slippage tolerance percentage (default: 1%).
    :return: Swap quote data (dict) or None if an error occurs.
    """
    url = f"{BASE_URL}{CHAIN_ID}/quote"
    params = {
        "fromTokenAddress": from_token_address,
        "toTokenAddress": to_token_address,
        "amount": amount,
        "slippage": slippage
    }
    
    try:
        # Send GET request to the 1inch API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP failures
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    # Return None in case of an error
    return None


# Example usage
if __name__ == "__main__":
    # Example token addresses on Binance Smart Chain
    BNB_ADDRESS = "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"  # Native BNB token
    USDT_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"  # USDT token

    # Example amount (1 BNB in wei)
    AMOUNT_IN_WEI = 1000000000000000000  # 1 BNB

    # Fetch swap quote
    quote = get_swap_quote(BNB_ADDRESS, USDT_ADDRESS, AMOUNT_IN_WEI)

    if quote:
        print("Swap Quote:")
        print("-----------------------------")
        print(f"From Token: {quote['fromToken']['symbol']}")
        print(f"To Token: {quote['toToken']['symbol']}")
        print(f"Amount to Receive: {quote['toTokenAmount']}")
        print(f"Estimated Gas: {quote['estimatedGas']}")
    else:
        print("Failed to retrieve swap quote.")
```

### Notes:
1. Install the `requests` library if not already installed:
   ```bash
   pip install requests
   ```
2. Replace token addresses and amounts as needed.
3. Ensure slippage tolerance is appropriately set for your use case.
4. Always verify token addresses and make sure they are valid for the Binance Smart Chain network.
