"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Write a Python function that calculates the total rewards earned from staking DCB based on the provided APY and lock term.
Generated: DETERMINISTIC_b47fe1f997d9e4d4
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(principal: float, apy: float, lock_term_years: int) -> float:
    """
    Calculate the total rewards earned from staking DCB.

    Args:
        principal (float): The amount of DCB staked (in currency units).
        apy (float): The annual percentage yield (as a decimal, e.g., 0.05 for 5%).
        lock_term_years (int): The duration for which the DCB is staked (in years).

    Returns:
        float: The total rewards earned from staking.
    
    Raises:
        ValueError: If the principal is negative, APY is less than 0, or lock term is negative.
    """
    
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if apy < 0:
        raise ValueError("APY must be non-negative.")
    if lock_term_years < 0:
        raise ValueError("Lock term must be non-negative.")

    # Calculate total rewards using compound interest formula
    total_rewards = principal * ((1 + apy) ** lock_term_years - 1)
    
    return total_rewards

# Example usage (uncomment to run):
# principal_amount = 1000  # Stake amount in currency units
# annual_percentage_yield = 0.05  # 5% APY
# lock_duration_years = 3  # Stake duration in years
# rewards = calculate_staking_rewards(principal_amount, annual_percentage_yield, lock_duration_years)
# print(f"Total rewards earned from staking: {rewards:.2f}")
```
