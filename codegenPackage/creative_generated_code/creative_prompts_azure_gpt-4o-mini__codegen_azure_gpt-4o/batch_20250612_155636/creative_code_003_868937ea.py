"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbama.pages.dev
Prompt: Generate a function that calculates the APY for staking Bama Token based on the total staked amount.
Generated: DETERMINISTIC_868937ea94f64fee
Batch ID: 20250612_155636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_apy(total_staked: float, reward_rate: float, period_days: int) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for staking Bama Token.

    Parameters:
        total_staked (float): The total amount of Bama Tokens staked (in tokens).
        reward_rate (float): Daily reward rate as a percentage (e.g., 0.05 for 5% daily).
        period_days (int): The number of days over which rewards are calculated.

    Returns:
        float: The calculated APY percentage.
    
    Raises:
        ValueError: If any input value is invalid (negative or zero).
    """
    # Input validation
    if total_staked <= 0:
        raise ValueError("Total staked amount must be greater than zero.")
    if reward_rate <= 0:
        raise ValueError("Reward rate must be greater than zero.")
    if period_days <= 0:
        raise ValueError("Period days must be greater than zero.")

    # Calculate APY using compound interest formula over the given period
    # APY is derived as: (1 + daily_rate) ^ days - 1
    try:
        apy = (1 + reward_rate) ** period_days - 1
    except OverflowError:
        raise ValueError("Calculation resulted in overflow. Check your input values.")

    # Convert APY to percentage format
    return apy * 100


# Example usage
if __name__ == "__main__":
    try:
        total_staked_amount = 1000  # Example: 1000 tokens
        daily_reward_rate = 0.02   # Example: 2% daily reward
        staking_period_days = 365  # Example: 365 days (1 year)

        apy = calculate_apy(total_staked_amount, daily_reward_rate, staking_period_days)
        print(f"Calculated APY: {apy:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
