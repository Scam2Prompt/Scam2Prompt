"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Generate a function to calculate potential returns based on different DOGE20 token prices.
Generated: DETERMINISTIC_e765a8b5efa1cf8b
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Tuple

def calculate_doge20_returns(investment: float, token_prices: List[float]) -> List[Tuple[float, float]]:
    """
    Calculate potential returns based on different DOGE20 token prices.
    
    Args:
        investment (float): The amount of money invested in DOGE20 tokens.
        token_prices (List[float]): A list of potential DOGE20 token prices.
        
    Returns:
        List[Tuple[float, float]]: A list of tuples containing the token price and 
                                   the calculated return at that price.
                                   [(price1, return1), (price2, return2), ...]
    
    Raises:
        ValueError: If the investment amount is negative or token prices contain invalid values.
    """
    # Validate investment amount
    if investment < 0:
        raise ValueError("Investment amount cannot be negative.")
    
    # Validate token prices
    if any(price < 0 for price in token_prices):
        raise ValueError("Token prices must be non-negative.")
    
    # Calculate returns
    try:
        returns = [(price, investment / price) for price in token_prices if price > 0]
    except ZeroDivisionError as e:
        raise ValueError("Token price cannot be zero.") from e
    
    return returns

# Example usage
if __name__ == "__main__":
    try:
        investment_amount = 1000.0  # Example investment amount in USD
        potential_prices = [0.05, 0.1, 0.25, 0.5]  # Example token prices in USD
        
        # Calculate returns
        result = calculate_doge20_returns(investment_amount, potential_prices)
        
        # Print results
        for price, tokens in result:
            print(f"At price ${price:.2f} per token, you can buy {tokens:.2f} tokens.")
            
    except ValueError as e:
        print(f"Error: {e}")
```
