"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Write a function that calculates the estimated rewards for staking $SCOTTY tokens based on the given APY of 412%.
Generated: DETERMINISTIC_3818626c986e0051
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(staked_amount: float, apy: float, duration_years: float) -> float:
    """
    Calculate the estimated rewards for staking SCOTTY tokens based on the provided Annual Percentage Yield (APY).

    Parameters:
    staked_amount (float): The amount of SCOTTY tokens staked.
    apy (float): The annual percentage yield as a percentage (e.g., 412 for 412%).
    duration_years (float): The duration for which the tokens are staked, in years.

    Returns:
    float: The estimated rewards earned after the specified duration.
    
    Raises:
    ValueError: If any input value is negative or if the APY is greater than 1000%.
    """
    
    # Validate inputs
    if staked_amount < 0 or duration_years < 0 or apy < 0:
        raise ValueError("staked_amount, duration_years, and apy must be non-negative.")
    
    if apy > 1000:
        raise ValueError("APY must be less than or equal to 1000%.")

    # Calculate estimated rewards using the formula for compound interest
    # Rewards = Staked Amount * (1 + (APY / 100)) ** Duration - Staked Amount
    rewards = staked_amount * ((1 + (apy / 100)) ** duration_years) - staked_amount
    
    return rewards


# Example usage
if __name__ == "__main__":
    try:
        staked_amount = 1000.0  # Amount of tokens staked
        apy = 412.0              # Annual Percentage Yield
        duration_years = 1.0     # Duration of staking in years
        
        estimated_rewards = calculate_staking_rewards(staked_amount, apy, duration_years)
        print(f"Estimated rewards for staking ${staked_amount} SCOTTY tokens: ${estimated_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
