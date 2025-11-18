"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-is.pages.dev
Prompt: Create a function to calculate gas fees for swapping ETH, BNB, or MATIC for $WAI tokens on the WienerAI platform using the buy widget.
Generated: DETERMINISTIC_9f63394c21346fa0
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_gas_fee(token: str, amount: float, gas_price: float) -> Union[float, str]:
    """
    Calculate the gas fee for swapping ETH, BNB, or MATIC for $WAI tokens
    on the WienerAI platform.

    Parameters:
        token (str): The cryptocurrency being swapped ('ETH', 'BNB', or 'MATIC').
        amount (float): The amount of the token being swapped.
        gas_price (float): Current gas price in Gwei.

    Returns:
        Union[float, str]: The estimated gas fee in the user's token or an error message.
    """
    # Supported tokens
    supported_tokens = {"ETH": 21000, "BNB": 20000, "MATIC": 15000}  # Example gas limits

    # Input validation
    if token.upper() not in supported_tokens:
        return "Error: Unsupported token. Please choose ETH, BNB, or MATIC."

    if amount <= 0:
        return "Error: Amount must be greater than 0."

    if gas_price <= 0:
        return "Error: Gas price must be greater than 0."

    try:
        # Retrieve gas limit for the provided token
        gas_limit = supported_tokens[token.upper()]

        # Calculate gas fee (gas limit * gas price)
        gas_fee = gas_limit * gas_price / 10**9  # Convert Gwei to token unit

        return gas_fee  # Return the gas fee in the token denomination
    except Exception as e:
        # Catch any unexpected errors
        return f"Error: An unexpected error occurred. Details: {str(e)}"

# Example usage
if __name__ == "__main__":
    token = "ETH"  # Token being swapped
    amount = 0.5  # Amount of token being swapped
    gas_price = 50  # Current gas price in Gwei

    gas_fee = calculate_gas_fee(token, amount, gas_price)
    print(f"Gas fee for swapping {amount} {token}: {gas_fee}")
```
