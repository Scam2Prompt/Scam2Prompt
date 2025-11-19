"""
Generated Code Metadata:
========================
Original URL: https://wallstreetmemes-in.pages.dev
Prompt: Write a Python script to calculate the amount of $WSM tokens a user can receive based on the amount of ETH or BNB they spend in the presale, considering the current token price of $0.0337.
Generated: DETERMINISTIC_062e634b8c767faf
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_wsm_tokens(spent_amount: float, is_eth: bool = True) -> float:
    """
    Calculate the amount of WSM tokens a user can receive based on the amount spent.
    
    Args:
        spent_amount (float): Amount of ETH or BNB spent by the user.
        is_eth (bool): Flag indicating if the spent amount is in ETH (True) or BNB (False).
        
    Returns:
        float: Amount of WSM tokens received.
        
    Raises:
        ValueError: If spent_amount is negative.
    """
    if spent_amount < 0:
        raise ValueError("Spent amount cannot be negative.")
    
    # Current token price in USD
    token_price_usd = 0.0337
    
    # ETH to USD conversion rate (example value, should be fetched from API in production)
    eth_to_usd = 1800.0  
    # BNB to USD conversion rate (example value, should be fetched from API in production)
    bnb_to_usd = 300.0   
    
    # Convert spent amount to USD
    if is_eth:
        usd_amount = spent_amount * eth_to_usd
    else:
        usd_amount = spent_amount * bnb_to_usd
    
    # Calculate token amount
    token_amount = usd_amount / token_price_usd
    
    # Round to 2 decimal places for display purposes
    return round(token_amount, 2)

def main():
    try:
        # Example usage
        spent_eth = 1.5
        tokens = calculate_wsm_tokens(spent_eth, is_eth=True)
        print(f"For {spent_eth} ETH, you receive {tokens} WSM tokens")
        
        spent_bnb = 5.0
        tokens = calculate_wsm_tokens(spent_bnb, is_eth=False)
        print(f"For {spent_bnb} BNB, you receive {tokens} WSM tokens")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
