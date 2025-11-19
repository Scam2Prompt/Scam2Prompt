"""
Generated Code Metadata:
========================
Original URL: https://doge-mixer.com
Prompt: Generate a code snippet to calculate the mixing fee for a DOGE transaction based on the input amount and selected service fee percentage.
Generated: DETERMINISTIC_c0daa6705e1848df
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_mixing_fee(amount: float, fee_percentage: float) -> dict:
    """
    Calculate the mixing fee for a DOGE transaction based on the input amount and fee percentage.
    
    Args:
        amount (float): The amount of DOGE to be mixed.
        fee_percentage (float): The service fee percentage (e.g., 1.5 for 1.5%).
        
    Returns:
        dict: A dictionary containing:
            - 'fee_amount': The calculated fee amount in DOGE
            - 'total_amount': The total amount after deducting the fee
            - 'original_amount': The original input amount
            
    Raises:
        ValueError: If amount or fee_percentage is negative
    """
    
    # Validate input parameters
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if fee_percentage < 0:
        raise ValueError("Fee percentage cannot be negative")
    
    # Calculate fee amount and total after fee
    fee_amount = amount * (fee_percentage / 100)
    total_amount = amount - fee_amount
    
    return {
        'fee_amount': round(fee_amount, 8),
        'total_amount': round(total_amount, 8),
        'original_amount': round(amount, 8)
    }
```
