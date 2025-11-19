"""
Generated Code Metadata:
========================
Original URL: https://bake-4kd.pages.dev
Prompt: Generate a code snippet that calculates potential rewards from staking various cryptocurrencies on Bake, considering the commission fees mentioned.
Generated: DETERMINISTIC_e677915b62018aed
Batch ID: 20250612_163902
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
    annual_interest_rate: float,
    days_staked: int,
    commission_fee: float = 0.0
) -> dict:
    """
    Calculate potential staking rewards after considering commission fees.

    Args:
        principal: Initial amount of cryptocurrency staked.
        annual_interest_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%).
        days_staked: Number of days the cryptocurrency is staked.
        commission_fee: Commission fee taken by platform (as a decimal, e.g., 0.1 for 10%).

    Returns:
        dict: Dictionary containing gross rewards, commission, and net rewards.

    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal must be a positive number.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if days_staked <= 0:
        raise ValueError("Days staked must be a positive number.")
    if commission_fee < 0 or commission_fee >= 1:
        raise ValueError("Commission fee must be between 0 and 1 (exclusive).")

    # Calculate daily interest rate
    daily_interest_rate = annual_interest_rate / 365

    # Calculate gross rewards (before commission)
    gross_rewards = principal * daily_interest_rate * days_staked

    # Calculate commission
    commission = gross_rewards * commission_fee

    # Calculate net rewards (after commission)
    net_rewards = gross_rewards - commission

    return {
        "gross_rewards": round(gross_rewards, 8),
        "commission": round(commission, 8),
        "net_rewards": round(net_rewards, 8),
        "principal": principal,
        "days_staked": days_staked
    }


# Example usage
if __name__ == "__main__":
    try:
        result = calculate_staking_rewards(
            principal=1000.0,
            annual_interest_rate=0.1,  # 10% annual interest
            days_staked=30,
            commission_fee=0.15  # 15% commission
        )
        print("Staking Rewards Calculation:")
        print(f"Principal: {result['principal']}")
        print(f"Days Staked: {result['days_staked']}")
        print(f"Gross Rewards: {result['gross_rewards']}")
        print(f"Commission: {result['commission']}")
        print(f"Net Rewards: {result['net_rewards']}")
    except ValueError as e:
        print(f"Error: {e}")
```
