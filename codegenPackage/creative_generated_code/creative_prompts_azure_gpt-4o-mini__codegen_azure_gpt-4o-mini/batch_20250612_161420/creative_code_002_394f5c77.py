"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombaten.pages.dev
Prompt: Generate a function that calculates the APY for $MK staked tokens based on the total rewards and stakers mentioned in the Meme Kombat tokenomics.
Generated: DETERMINISTIC_394f5c77aba4ed0c
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(total_rewards: float, stakers: int, stake_amount: float) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for staked $MK tokens.

    Parameters:
    total_rewards (float): The total rewards distributed over the year.
    stakers (int): The total number of stakers participating.
    stake_amount (float): The amount of tokens each staker has staked.

    Returns:
    float: The calculated APY as a percentage.

    Raises:
    ValueError: If any input parameter is negative or if stakers count is zero.
    """
    # Validate input parameters
    if total_rewards < 0:
        raise ValueError("Total rewards must be non-negative.")
    if stakers <= 0:
        raise ValueError("Number of stakers must be greater than zero.")
    if stake_amount < 0:
        raise ValueError("Stake amount must be non-negative.")

    # Calculate total staked value
    total_staked = stakers * stake_amount

    # Check if total staked is zero to avoid division by zero
    if total_staked == 0:
        raise ValueError("Total staked amount must be greater than zero.")

    # Calculate APY
    apy = (total_rewards / total_staked) * 100

    return apy

# Example usage
if __name__ == "__main__":
    try:
        total_rewards = 50000.0  # Example total rewards in dollars
        stakers = 100  # Example number of stakers
        stake_amount = 200.0  # Example stake amount per staker

        apy = calculate_apy(total_rewards, stakers, stake_amount)
        print(f"The calculated APY is: {apy:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
