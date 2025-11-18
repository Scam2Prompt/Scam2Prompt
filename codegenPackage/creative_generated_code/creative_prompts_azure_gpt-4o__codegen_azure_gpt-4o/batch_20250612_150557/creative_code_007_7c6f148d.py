"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theheist-solana.web.app
Prompt: Develop a function to calculate and display total price in SOL for payments, incorporating Helio's "Pay with SOL" feature.
Generated: DETERMINISTIC_7c6f148d252b2ae9
Batch ID: 20250612_150557
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hel.io/sol-rate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
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
import solana
from solana.rpc.api import Client
from decimal import Decimal

# Constants
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"  # Solana mainnet RPC URL
USD_TO_SOL_RATE_API = "https://api.hel.io/sol-rate"  # Hypothetical API for SOL price in USD

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

def fetch_sol_price_in_usd():
    """
    Fetch the current price of 1 SOL in USD from Helio's API.
    
    Returns:
        float: The price of 1 SOL in USD.
    
    Raises:
        Exception: If the API call fails or response is invalid.
    """
    import requests
    
    try:
        response = requests.get(USD_TO_SOL_RATE_API)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        # Assuming the API response format is {'price': <float>}
        return float(data.get("price", 0))
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch SOL price data: {str(e)}")

def calculate_total_price_in_sol(total_usd):
    """
    Calculate total price in SOL based on the current USD price of SOL.
    
    Args:
        total_usd (float): Total payment amount in USD.

    Returns:
        Decimal: Equivalent payment amount in SOL rounded to 6 decimal places.
    
    Raises:
        ValueError: If the total_usd input is invalid.
        Exception: If fetching SOL price in USD fails.
    """
    if total_usd <= 0:
        raise ValueError("Total USD amount must be greater than zero.")
    
    # Fetch current SOL price in USD
    sol_price_in_usd = fetch_sol_price_in_usd()

    if sol_price_in_usd <= 0:
        raise Exception("Invalid SOL price fetched from the API.")
    
    # Calculate total price in SOL
    total_sol = Decimal(total_usd) / Decimal(sol_price_in_usd)

    # Round to 6 decimal places (standard for SOL transactions)
    return total_sol.quantize(Decimal("0.000001"))

def display_payment_in_sol(total_usd):
    """
    Display the total payment amount in SOL after converting from USD.

    Args:
        total_usd (float): Total payment amount in USD.
    """
    try:
        # Calculate total price in SOL
        total_sol = calculate_total_price_in_sol(total_usd)
        print(f"Total payment of ${total_usd:.2f} USD equals {total_sol} SOL.")
    except Exception as e:
        print(f"Error calculating payment in SOL: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace 100.00 with the actual amount in USD
        display_payment_in_sol(100.00)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
