"""
Generated Code Metadata:
========================
Original URL: https://app-aixcbcapital.pages.dev
Prompt: Create a function that calculates potential rewards for staking AIXCB tokens based on the APR values provided for 90, 180, and 360-day periods.
Generated: DETERMINISTIC_f2ccd6603f4b157a
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staking_rewards(
    principal: float,
    days: int,
    apr_90: float,
    apr_180: float,
    apr_360: float
) -> float:
    """
    Calculate potential staking rewards for AIXCB tokens based on selected staking period.
    
    Args:
        principal: The amount of tokens to stake
        days: The staking period in days (must be 90, 180, or 360)
        apr_90: Annual Percentage Rate for 90-day staking
        apr_180: Annual Percentage Rate for 180-day staking
        apr_360: Annual Percentage Rate for 360-day staking
        
    Returns:
        float: The calculated rewards for the staking period
        
    Raises:
        ValueError: If days is not one of the supported periods or if principal is negative
    """
    if principal < 0:
        raise ValueError("Principal amount cannot be negative")
    
    if days not in {90, 180, 360}:
        raise ValueError("Staking period must be 90, 180, or 360 days")
    
    # Determine the APR based on staking period
    if days == 90:
        apr = apr_90
    elif days == 180:
        apr = apr_180
    else:
        apr = apr_360
    
    # Calculate rewards: (principal * APR * days) / 365
    rewards = (principal * apr * days) / 365
    
    return rewards


# Example usage:
if __name__ == "__main__":
    try:
        principal_amount = 1000.0  # Example: 1000 AIXCB tokens
        staking_days = 180
        rewards = calculate_staking_rewards(
            principal=principal_amount,
            days=staking_days,
            apr_90=0.05,  # 5% APR for 90 days
            apr_180=0.08, # 8% APR for 180 days
            apr_360=0.12  # 12% APR for 360 days
        )
        print(f"Potential rewards for {staking_days}-day staking: {rewards:.2f} AIXCB")
    except ValueError as e:
        print(f"Error: {e}")
```
