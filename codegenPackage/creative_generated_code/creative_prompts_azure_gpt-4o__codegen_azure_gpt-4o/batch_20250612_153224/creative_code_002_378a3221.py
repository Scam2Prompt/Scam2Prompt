"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-share.pages.dev
Prompt: Create a function to calculate the estimated rewards in stETH based on the APY (3.3%) and program duration (24.1 days) for a given deposit amount.
Generated: DETERMINISTIC_378a32212574a5fa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import timedelta

def calculate_steth_rewards(deposit_amount, apy, duration_days):
    """
    Calculate estimated rewards in stETH based on APY and program duration.

    Args:
        deposit_amount (float): The amount deposited in stETH.
        apy (float): Annual percentage yield (e.g., 3.3 for 3.3%).
        duration_days (float): The duration of the program in days.

    Returns:
        float: Estimated rewards earned in stETH.
    """
    try:
        # Validate input types
        if not isinstance(deposit_amount, (int, float)) or deposit_amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        if not isinstance(apy, (int, float)) or apy <= 0:
            raise ValueError("APY must be a positive number.")
        if not isinstance(duration_days, (int, float)) or duration_days <= 0:
            raise ValueError("Duration days must be a positive number.")

        # Convert APY from percentage to decimal (e.g., 3.3% => 0.033)
        annual_yield = apy / 100

        # Calculate daily yield rate (assuming 365 days in a year)
        daily_yield_rate = annual_yield / 365

        # Calculate rewards based on the duration
        rewards = deposit_amount * daily_yield_rate * duration_days

        return round(rewards, 8)  # Return rounded result for precision

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating rewards: {e}")
        return None


# Example usage
if __name__ == "__main__":
    deposit = 1000  # Example deposit amount in stETH
    annual_percentage_yield = 3.3  # APY in percentage
    program_duration = 24.1  # Duration in days

    estimated_rewards = calculate_steth_rewards(deposit, annual_percentage_yield, program_duration)
    if estimated_rewards is not None:
        print(f"Estimated rewards: {estimated_rewards} stETH")
```
