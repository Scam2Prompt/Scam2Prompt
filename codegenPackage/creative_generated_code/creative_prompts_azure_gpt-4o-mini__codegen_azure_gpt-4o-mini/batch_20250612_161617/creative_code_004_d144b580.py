"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins.pages.dev
Prompt: Create a function that calculates the potential rewards for staking $GBTC based on varying amounts staked and the current annual percentage yield (APY) of 435%.
Generated: DETERMINISTIC_d144b580ff736495
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(staked_amount: float, apy: float, years: float) -> float:
    """
    Calculate the potential rewards for staking a cryptocurrency.

    :param staked_amount: The amount of $GBTC staked (in USD).
    :param apy: The annual percentage yield (as a decimal, e.g., 4.35 for 435%).
    :param years: The number of years the amount is staked for.
    :return: The total rewards earned after the specified number of years.
    
    :raises ValueError: If staked_amount, apy, or years are negative.
    """
    
    # Input validation
    if staked_amount < 0:
        raise ValueError("Staked amount must be non-negative.")
    if apy < 0:
        raise ValueError("Annual Percentage Yield (APY) must be non-negative.")
    if years < 0:
        raise ValueError("Years must be non-negative.")
    
    # Calculate the total rewards using compound interest formula
    total_rewards = staked_amount * ((1 + apy) ** years - 1)
    
    return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        staked = 1000.0  # Example amount in USD
        annual_yield = 4.35  # 435% expressed as a decimal
        staking_years = 5  # Number of years to stake
        
        rewards = calculate_staking_rewards(staked, annual_yield, staking_years)
        print(f"Total rewards for staking ${staked} for {staking_years} years: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
