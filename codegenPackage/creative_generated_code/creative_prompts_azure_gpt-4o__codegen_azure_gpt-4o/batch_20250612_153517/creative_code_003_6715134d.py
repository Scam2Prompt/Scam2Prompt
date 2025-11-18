"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Create a function to calculate the market cap of $MONG memecoin based on its hard-capped supply and current price.
Generated: DETERMINISTIC_6715134da31f2144
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_market_cap(price_per_token: float, hard_capped_supply: int = 690000000000000) -> float:
    """
    Calculate the market capitalization of the $MONG memecoin.

    Args:
        price_per_token (float): The current price of a single token in USD.
        hard_capped_supply (int, optional): The total supply of tokens. Defaults to $MONG's hard-capped supply (690 trillion).

    Returns:
        float: The market capitalization in USD.

    Raises:
        ValueError: If the price_per_token is negative or zero.
    """
    # Validate input
    if price_per_token <= 0:
        raise ValueError("Price per token must be a positive value.")

    # Calculate market cap as `price_per_token * hard_capped_supply`
    market_cap = price_per_token * hard_capped_supply
    
    return market_cap


# Example usage
if __name__ == "__main__":
    # Example: Calculate market cap for $MONG when price is $0.000000001 (1 nano USD per token)
    try:
        price = 0.000000001  # Replace with the actual token price
        market_cap = calculate_market_cap(price)
        print(f"The market capitalization of $MONG memecoin is: ${market_cap:,.2f} USD")
    except ValueError as e:
        print(f"Error: {e}")
```
