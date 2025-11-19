"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Develop a function to simulate the compounding rewards for staking AITECH over a 365-day lock term.
Generated: DETERMINISTIC_70d4623204c98b34
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import List


def simulate_staking_rewards(
    principal: float, 
    annual_reward_rate: float, 
    days_locked: int = 365, 
    daily_compounding: bool = True
) -> List[float]:
    """
    Simulate compounding rewards for staking AITECH over a defined lock term.

    Args:
        principal (float): The initial amount of AITECH staked.
        annual_reward_rate (float): Annual reward rate as a percentage (e.g., 10 for 10%).
        days_locked (int): Duration of the lock term in days. Default is 365 days.
        daily_compounding (bool): Whether rewards compound daily. Default is True.

    Returns:
        List[float]: A list containing the balance at each day of the lock term.

    Raises:
        ValueError: If principal or annual_reward_rate is negative.
    """
    # Input validation
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if annual_reward_rate < 0:
        raise ValueError("Annual reward rate cannot be negative.")

    # Convert annual reward rate to daily rate
    daily_rate = (annual_reward_rate / 100) / 365

    # Initialize the daily balances with the starting principal amount
    balances = [principal]

    # Iterate through each day in the lock term and calculate the balance
    for day in range(1, days_locked + 1):
        if daily_compounding:
            # Compound the rewards daily
            updated_balance = balances[-1] * (1 + daily_rate)
        else:
            # Calculate rewards without compounding
            updated_balance = principal + (principal * daily_rate * day)
        
        # Append the updated balance to the list
        balances.append(updated_balance)

    return balances


if __name__ == "__main__":
    # Example usage
    initial_stake = 1000.0  # Initial AITECH staked
    annual_rate = 10.0  # Annual reward rate in percentage
    lock_term = 365  # Lock duration in days

    try:
        # Simulate staking rewards
        results = simulate_staking_rewards(
            principal=initial_stake, 
            annual_reward_rate=annual_rate, 
            days_locked=lock_term
        )
        # Print the balance at the end of the lock term
        print(f"Final balance after {lock_term} days: {results[-1]:.2f} AITECH")
    except ValueError as e:
        print(f"Error: {e}")
```
