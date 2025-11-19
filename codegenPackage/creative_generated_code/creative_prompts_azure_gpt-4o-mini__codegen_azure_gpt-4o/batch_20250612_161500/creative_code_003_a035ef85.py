"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Generate code to calculate the total rewards earned from staking AITECH tokens over different lock periods, as mentioned in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_a035ef85412f78d0
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate total rewards earned from staking AITECH tokens
# based on the Solidus AI Tech staking tiers.
# Assumes staking tiers are defined with lock periods and reward rates.

# Constants for staking tiers (lock period in months and reward rate per year)
STAKING_TIERS = {
    "bronze": {"lock_period_months": 3, "annual_reward_rate": 0.06},  # 6% annual reward
    "silver": {"lock_period_months": 6, "annual_reward_rate": 0.08},  # 8% annual reward
    "gold": {"lock_period_months": 12, "annual_reward_rate": 0.12},  # 12% annual reward
    "platinum": {"lock_period_months": 24, "annual_reward_rate": 0.20},  # 20% annual reward
}

def calculate_rewards(staked_amount, staking_tier):
    """
    Calculate the total rewards earned from staking AITECH tokens.

    Parameters:
        staked_amount (float): The amount of AITECH tokens staked.
        staking_tier (str): The staking tier ('bronze', 'silver', 'gold', 'platinum').

    Returns:
        float: Total rewards earned over the lock period.
    Raises:
        ValueError: If the staking tier is invalid or staked amount is negative.
    """
    if staking_tier not in STAKING_TIERS:
        raise ValueError(f"Invalid staking tier: {staking_tier}. Must be one of {', '.join(STAKING_TIERS.keys())}")
    if staked_amount < 0:
        raise ValueError("Staked amount cannot be negative.")

    # Get lock period and annual reward rate for the specified staking tier
    tier_data = STAKING_TIERS[staking_tier]
    lock_period_months = tier_data["lock_period_months"]
    annual_reward_rate = tier_data["annual_reward_rate"]

    # Calculate rewards
    lock_period_years = lock_period_months / 12  # Convert lock period to years
    total_rewards = staked_amount * annual_reward_rate * lock_period_years
    
    return total_rewards

def main():
    """
    Main function to interactively calculate staking rewards based on user input.
    """
    try:
        # Get user inputs
        staked_amount = float(input("Enter the amount of AITECH tokens staked: "))
        staking_tier = input("Enter the staking tier (bronze, silver, gold, platinum): ").strip().lower()

        # Calculate rewards
        total_rewards = calculate_rewards(staked_amount, staking_tier)
        print(f"Total rewards earned from staking {staked_amount} AITECH tokens in the {staking_tier} tier: {total_rewards:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
