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
def calculate_market_cap(hard_capped_supply: float, current_price: float) -> float:
    """
    Calculate the market capitalization of the $MONG memecoin.

    Parameters:
    hard_capped_supply (float): The total supply of the memecoin that is hard-capped.
    current_price (float): The current price of one unit of the memecoin.

    Returns:
    float: The market capitalization of the memecoin.
    
    Raises:
    ValueError: If hard_capped_supply or current_price is negative.
    """
    # Validate inputs
    if hard_capped_supply < 0:
        raise ValueError("Hard-capped supply must be a non-negative value.")
    if current_price < 0:
        raise ValueError("Current price must be a non-negative value.")

    # Calculate market cap
    market_cap = hard_capped_supply * current_price
    return market_cap

# Example usage
if __name__ == "__main__":
    try:
        hard_capped_supply = 1000000  # Example hard-capped supply
        current_price = 0.05  # Example current price in USD
        market_cap = calculate_market_cap(hard_capped_supply, current_price)
        print(f"The market cap of $MONG is: ${market_cap:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
