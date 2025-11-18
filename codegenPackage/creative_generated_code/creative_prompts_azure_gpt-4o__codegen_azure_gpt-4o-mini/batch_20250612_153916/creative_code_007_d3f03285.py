"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashai-sushi.top
Prompt: Create a function to calculate the total rewards earned from staking WBTC in the HashAI staking pool with an APY of 136.77%.
Generated: DETERMINISTIC_d3f03285fe6c77a4
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(principal: float, apy: float, years: float) -> float:
    """
    Calculate the total rewards earned from staking.

    Parameters:
    principal (float): The initial amount of WBTC staked.
    apy (float): The annual percentage yield as a decimal (e.g., 136.77% should be passed as 1.3677).
    years (float): The number of years the WBTC is staked.

    Returns:
    float: The total rewards earned from staking.
    
    Raises:
    ValueError: If principal, apy, or years are negative.
    """
    
    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if apy < 0:
        raise ValueError("APY cannot be negative.")
    if years < 0:
        raise ValueError("Years cannot be negative.")
    
    # Calculate total rewards using compound interest formula
    total_rewards = principal * (1 + apy) ** years - principal
    return total_rewards


# Example usage
if __name__ == "__main__":
    try:
        principal_amount = 1000  # Amount of WBTC staked
        apy_value = 1.3677       # 136.77% expressed as a decimal
        staking_years = 1        # Number of years staked

        rewards = calculate_staking_rewards(principal_amount, apy_value, staking_years)
        print(f"Total rewards earned from staking: {rewards:.2f} WBTC")
    except ValueError as e:
        print(f"Error: {e}")
```
