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
def calculate_bitcoin_cost(amount_in_usd):
    """
    Calculate the total cost of purchasing Bitcoin on Coinbase including fees and spread.

    Parameters:
    amount_in_usd (float): The amount in USD to purchase Bitcoin.

    Returns:
    float: The total cost including the Coinbase fee and spread.
    
    Raises:
    ValueError: If the amount_in_usd is negative or not a number.
    """

    # Validate input
    if not isinstance(amount_in_usd, (int, float)):
        raise ValueError("amount_in_usd must be a number.")
    if amount_in_usd < 0:
        raise ValueError("amount_in_usd cannot be negative.")
    
    # Define the fee and spread percentages
    fee_percentage = 1.49 / 100
    spread_percentage = 0.5 / 100
    
    # Calculate fees and total cost
    fee = amount_in_usd * fee_percentage
    spread = amount_in_usd * spread_percentage
    total_cost = amount_in_usd + fee + spread
    
    return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        amount = 1000  # Example amount in USD
        total_cost = calculate_bitcoin_cost(amount)
        print(f"Total cost for purchasing ${amount} of Bitcoin: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
