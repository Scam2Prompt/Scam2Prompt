"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a function in Python that calculates the daily earnings for a user based on the mining plan selected (V1.1, V1.2, or V1.3) and outputs the total ETH earned after a specified number of days.
Generated: DETERMINISTIC_7172633213bcbd0f
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_daily_earnings(mining_plan: str, days: int) -> float:
    """
    Calculate the total Ethereum (ETH) earnings based on the selected mining plan 
    over a specified number of days.

    Parameters:
    mining_plan (str): The selected mining plan ('V1.1', 'V1.2', 'V1.3').
    days (int): The number of days to calculate earnings for.

    Returns:
    float: The total ETH earned after the specified number of days.

    Raises:
    ValueError: If an invalid mining plan is provided or if days is not positive.
    """

    # Define daily earnings for each mining plan
    mining_plans = {
        'V1.1': 0.01,  # Daily earning for V1.1
        'V1.2': 0.015,  # Daily earning for V1.2
        'V1.3': 0.02    # Daily earning for V1.3
    }
    
    # Validate inputs
    if mining_plan not in mining_plans:
        raise ValueError(f"Invalid mining plan: {mining_plan}. Choose from {list(mining_plans.keys())}.")
    
    if days <= 0:
        raise ValueError("The number of days must be a positive integer.")

    # Calculate total earnings
    daily_earning = mining_plans[mining_plan]
    total_earnings = daily_earning * days
    
    return total_earnings

# Example usage
if __name__ == "__main__":
    try:
        plan = 'V1.2'
        days = 30
        earnings = calculate_daily_earnings(plan, days)
        print(f"Total ETH earned for plan {plan} over {days} days: {earnings:.4f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
