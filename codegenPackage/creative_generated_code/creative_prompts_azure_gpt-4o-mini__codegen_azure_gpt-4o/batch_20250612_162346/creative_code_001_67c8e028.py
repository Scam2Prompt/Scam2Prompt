"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdstation-revshare.pages.dev
Prompt: Write a function that calculates the estimated gas fees for a trade on Holdstation, considering the refund policy for unused gas fees.
Generated: DETERMINISTIC_67c8e02846307c9b
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_gas_fees(trade_amount, gas_price, gas_limit, refund_policy_percentage):
    """
    Calculate the estimated gas fees for a trade on Holdstation, factoring in the refund policy for unused gas fees.
    
    Parameters:
    - trade_amount (float): The amount of the trade in cryptocurrency.
    - gas_price (float): The current gas price per unit in Gwei.
    - gas_limit (int): The maximum amount of gas units allowed for the trade.
    - refund_policy_percentage (float): The percentage of unused gas fees refunded (between 0 and 100).
    
    Returns:
    - estimated_gas_fee (float): The net gas fee for the trade after considering the refund policy.
    
    Raises:
    - ValueError: If any input parameter is invalid.
    """
    try:
        # Validate inputs
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than 0.")
        if gas_price <= 0:
            raise ValueError("Gas price must be greater than 0.")
        if gas_limit <= 0:
            raise ValueError("Gas limit must be greater than 0.")
        if not (0 <= refund_policy_percentage <= 100):
            raise ValueError("Refund policy percentage must be between 0 and 100.")
        
        # Calculate the gross gas fee (before refund)
        gross_gas_fee = gas_price * gas_limit / 1_000_000_000  # Convert from Gwei to Ether
        
        # Assuming Holdstation refunds unused gas fees based on the refund policy percentage
        refund_amount = gross_gas_fee * (refund_policy_percentage / 100)
        
        # Net gas fee after refund
        estimated_gas_fee = gross_gas_fee - refund_amount
        
        return estimated_gas_fee
    
    except ValueError as e:
        # Catch and raise any validation errors
        raise ValueError(f"Input validation error: {e}")
    except Exception as e:
        # Catch and raise unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")
```

This function ensures clean, maintainable code with robust error handling mechanisms.
