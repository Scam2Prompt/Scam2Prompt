"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a Python function that calculates the total cost of purchasing Bitcoin on Coinbase, factoring in the 1.49% fee and the 0.5% spread mentioned on the webpage.
Generated: DETERMINISTIC_c8e3761e236a9792
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bitcoin_purchase_cost(usd_amount: float) -> dict:
    """
    Calculate the total cost of purchasing Bitcoin on Coinbase, including fees and spread.
    
    Args:
        usd_amount (float): The amount in USD to be used for purchasing Bitcoin.
        
    Returns:
        dict: A dictionary containing:
            - 'usd_amount': Original USD amount
            - 'fee': Coinbase fee (1.49% of usd_amount)
            - 'spread_cost': Spread cost (0.5% of usd_amount)
            - 'total_cost': Total cost including fees and spread
            - 'bitcoin_amount': Estimated BTC amount after fees and spread
            
    Raises:
        ValueError: If usd_amount is not positive
    """
    if usd_amount <= 0:
        raise ValueError("USD amount must be positive")
    
    # Calculate fees and spread
    fee = usd_amount * 0.0149
    spread_cost = usd_amount * 0.005
    
    # Calculate total cost (amount after fees and spread)
    total_cost = usd_amount - fee - spread_cost
    
    # For demonstration, we'll assume current BTC price is $1 (actual implementation would fetch current price)
    # In practice, you would get the current BTC price from Coinbase API
    btc_price = 1.0  # This should be replaced with actual price lookup
    bitcoin_amount = total_cost / btc_price
    
    return {
        'usd_amount': usd_amount,
        'fee': fee,
        'spread_cost': spread_cost,
        'total_cost': total_cost,
        'bitcoin_amount': bitcoin_amount
    }
```
