"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Write a Python script to calculate EGLD staking rewards using the formula provided on the MultiversX website: `[EGLD reward] = [Current EGLD holdings] * [ (EGLD Staked / Users Staking) * 775 ] * [Delegate Factor] * [Stake Factor]`.
Generated: DETERMINISTIC_29699f575157b181
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_egld_staking_rewards(
    current_egld_holdings: float,
    egld_staked: float,
    users_staking: float,
    delegate_factor: float,
    stake_factor: float,
) -> float:
    """
    Calculate EGLD staking rewards based on the MultiversX formula.

    Args:
        current_egld_holdings: Current amount of EGLD held by the user
        egld_staked: Total EGLD staked in the network
        users_staking: Total number of users staking
        delegate_factor: Delegate factor (between 0 and 1)
        stake_factor: Stake factor (between 0 and 1)

    Returns:
        float: Calculated EGLD staking rewards

    Raises:
        ValueError: If any input is negative or invalid
    """
    # Validate inputs
    if any(arg < 0 for arg in [current_egld_holdings, egld_staked, users_staking, delegate_factor, stake_factor]):
        raise ValueError("All input values must be non-negative")
    
    if users_staking == 0:
        raise ValueError("Users staking cannot be zero")
    
    if delegate_factor < 0 or delegate_factor > 1:
        raise ValueError("Delegate factor must be between 0 and 1")
    
    if stake_factor < 0 or stake_factor > 1:
        raise ValueError("Stake factor must be between 0 and 1")

    # Calculate rewards using the formula
    try:
        rewards = current_egld_holdings * ((egld_staked / users_staking) * 775) * delegate_factor * stake_factor
        return rewards
    except Exception as e:
        raise ValueError(f"Error calculating rewards: {str(e)}")


if __name__ == "__main__":
    try:
        # Example usage
        current_holdings = float(input("Enter your current EGLD holdings: "))
        total_staked = float(input("Enter total EGLD staked in network: "))
        total_users = float(input("Enter total number of users staking: "))
        delegate_fact = float(input("Enter delegate factor (0-1): "))
        stake_fact = float(input("Enter stake factor (0-1): "))

        result = calculate_egld_staking_rewards(
            current_holdings,
            total_staked,
            total_users,
            delegate_fact,
            stake_fact
        )
        
        print(f"Estimated EGLD staking rewards: {result:.6f} EGLD")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
