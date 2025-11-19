"""
Generated Code Metadata:
========================
Original URL: https://ethminer.world
Prompt: Create a function in Python that calculates the daily earnings for a user based on the mining plan selected (V1.1, V1.2, or V1.3) and outputs the total ETH earned after a specified number of days.
Generated: DETERMINISTIC_7172633213bcbd0f
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_eth_earnings(plan: str, days: int) -> float:
    """
    Calculate the total ETH earnings based on the selected mining plan and number of days.
    
    Args:
        plan (str): The mining plan selected (V1.1, V1.2, or V1.3)
        days (int): Number of days for mining
        
    Returns:
        float: Total ETH earned after specified days
        
    Raises:
        ValueError: If invalid plan is provided or days is negative
    """
    # Validate input parameters
    if days < 0:
        raise ValueError("Days cannot be negative")
    
    # Define daily earnings for each plan (in ETH)
    plan_earnings = {
        "V1.1": 0.001,
        "V1.2": 0.002,
        "V1.3": 0.003
    }
    
    # Check if plan is valid
    if plan not in plan_earnings:
        raise ValueError(f"Invalid plan: {plan}. Must be one of {list(plan_earnings.keys())}")
    
    # Calculate total earnings
    daily_earnings = plan_earnings[plan]
    total_earnings = daily_earnings * days
    
    return round(total_earnings, 6)  # Round to 6 decimal places for ETH precision
```
