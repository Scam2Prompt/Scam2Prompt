"""
Generated Code Metadata:
========================
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Generate a function that calculates the total amount and total value increment for tokens deposited in a Solana Value Average app.
Generated: DETERMINISTIC_9bacd6abed423df6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Tuple

def calculate_token_deposits(
    deposits: List[Dict[str, float]],
    current_price: float
) -> Tuple[float, float, float]:
    """
    Calculate the total amount, total value, and value increment of token deposits.
    
    Args:
        deposits: List of dictionaries containing 'amount' and 'price' for each deposit.
        current_price: Current price of the token.
    
    Returns:
        Tuple containing:
        - total_amount: Sum of all deposited token amounts
        - total_value: Current value of all deposited tokens
        - value_increment: Difference between current value and total invested
    
    Raises:
        ValueError: If deposits is empty or contains invalid values
    """
    
    if not deposits:
        raise ValueError("Deposits list cannot be empty")
    
    total_amount = 0.0
    total_invested = 0.0
    
    for deposit in deposits:
        try:
            amount = deposit['amount']
            price = deposit['price']
            
            if amount <= 0 or price <= 0:
                raise ValueError("Amount and price must be positive numbers")
                
            total_amount += amount
            total_invested += amount * price
        except KeyError as e:
            raise ValueError(f"Missing required field in deposit: {e}")
        except TypeError:
            raise ValueError("Invalid data type in deposit record")
    
    total_value = total_amount * current_price
    value_increment = total_value - total_invested
    
    return (total_amount, total_value, value_increment)
```
