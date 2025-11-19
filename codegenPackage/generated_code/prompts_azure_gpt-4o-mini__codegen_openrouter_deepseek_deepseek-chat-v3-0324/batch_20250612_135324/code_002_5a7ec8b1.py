"""
Generated Code Metadata:
========================
Original URL: https://zerolend.omc.zone
Prompt: Generate a function that calculates the vesting amount for a user based on a 12-month linear vesting period after a 1-month cliff.
Generated: DETERMINISTIC_5a7ec8b1b8b4ed73
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_vesting_amount(total_grant: float, months_since_grant: int) -> float:
    """
    Calculate the vested amount based on a 12-month linear vesting schedule with a 1-month cliff.
    
    Args:
        total_grant (float): The total grant amount to be vested
        months_since_grant (int): Number of months since the grant date
        
    Returns:
        float: The vested amount as of the specified month
        
    Raises:
        ValueError: If total_grant is negative or months_since_grant is negative
    """
    # Validate inputs
    if total_grant < 0:
        raise ValueError("Total grant amount cannot be negative")
    if months_since_grant < 0:
        raise ValueError("Months since grant cannot be negative")
    
    # Handle cliff period (no vesting before 1 month)
    if months_since_grant < 1:
        return 0.0
    
    # Calculate vested amount after cliff
    vested_months = min(months_since_grant, 12)
    vested_amount = (vested_months / 12) * total_grant
    
    # Ensure we don't return more than the total grant
    return min(vested_amount, total_grant)
```
