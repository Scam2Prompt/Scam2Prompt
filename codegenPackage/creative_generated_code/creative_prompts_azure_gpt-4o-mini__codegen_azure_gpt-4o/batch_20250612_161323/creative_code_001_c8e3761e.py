"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a Python function that calculates the total cost of purchasing Bitcoin on Coinbase, factoring in the 1.49% fee and the 0.5% spread mentioned on the webpage.
Generated: DETERMINISTIC_c8e3761e236a9792
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_bitcoin_cost(usd_amount: float, bitcoin_price: float) -> float:
    """
    Calculate the total cost of purchasing Bitcoin on Coinbase, factoring in the fee and spread.

    Args:
        usd_amount (float): The dollar amount the user wants to spend on Bitcoin.
        bitcoin_price (float): The current price of Bitcoin in USD.

    Returns:
        float: The total cost in USD after factoring in Coinbase's fees and spread.
    """
    try:
        # Validate inputs
        if usd_amount <= 0:
            raise ValueError("USD amount must be greater than 0.")
        if bitcoin_price <= 0:
            raise ValueError("Bitcoin price must be greater than 0.")

        # Coinbase fee (1.49%)
        fee = usd_amount * 0.0149

        # Spread (0.5%)
        adjusted_bitcoin_price = bitcoin_price * 1.005

        # Total Bitcoin cost after fees and spread
        total_cost = usd_amount + fee

        # Return the calculated cost
        return total_cost, adjusted_bitcoin_price
    except ValueError as e:
        raise
