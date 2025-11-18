"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakelayerai.pages.dev
Prompt: Generate code to calculate rewards from staking $LAI, including computation credits, fractionalized NFTs, and AI Capsule NFTs, based on the roadmap milestones described on the LayerAI platform.
Generated: DETERMINISTIC_9edd3bf50a0737e6
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Constants
LAI_STAKING_RATE = 0.05  # Percentage reward rate for $LAI staked annually
COMPUTATION_CREDIT_RATE = 10  # Computation credits earned per $LAI staked monthly
FRAC_NFT_THRESHOLD = 1000  # $LAI staked required for fractionalized NFT rewards
AI_CAPSULE_THRESHOLD = 5000  # $LAI staked required for AI Capsule NFT rewards

def calculate_staking_rewards(staked_amount, staking_duration_months):
    """
    Calculate rewards from staking $LAI.

    Args:
        staked_amount (float): The amount of $LAI staked.
        staking_duration_months (int): Duration of staking in months.

    Returns:
        dict: A dictionary containing rewards information including computation credits,
              fractionalized NFT eligibility, and AI Capsule NFT eligibility.
    """
    # Validate inputs
    if staked_amount <= 0 or staking_duration_months <= 0:
        raise ValueError("Staked amount and staking duration must be positive values.")

    # Calculate annual staking rewards based on percentage rate
    annual_rewards = staked_amount * LAI_STAKING_RATE
    monthly_rewards = annual_rewards / 12

    # Calculate computation credits based on staking duration
    computation_credits = staked_amount * COMPUTATION_CREDIT_RATE * staking_duration_months

    # Determine fractionalized NFT eligibility
    frac_nft_eligible = staked_amount >= FRAC_NFT_THRESHOLD

    # Determine AI Capsule NFT eligibility
    ai_capsule_eligible = staked_amount >= AI_CAPSULE_THRESHOLD

    return {
        "total_staked": staked_amount,
        "staking_duration_months": staking_duration_months,
        "monthly_rewards": monthly_rewards,
        "total_rewards": monthly_rewards * staking_duration_months,
        "computation_credits": computation_credits,
        "frac_nft_eligible": frac_nft_eligible,
        "ai_capsule_eligible": ai_capsule_eligible,
    }

def main():
    """
    Main function to interact with the staking reward calculation.
    """
    print("Welcome to $LAI Staking Rewards Calculator!")
    try:
        # Input: Amount of $LAI staked
        staked_amount = float(input("Enter the amount of $LAI staked: "))
        staking_duration_months = int(input("Enter the staking duration in months: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, staking_duration_months)

        # Display rewards summary
        print("\nRewards Summary:")
        print(f"Total $LAI Staked: {rewards['total_staked']}")
        print(f"Staking Duration: {rewards['staking_duration_months']} months")
        print(f"Monthly Rewards: {rewards['monthly_rewards']:.2f} $LAI")
        print(f"Total Rewards: {rewards['total_rewards']:.2f} $LAI")
        print(f"Computation Credits: {rewards['computation_credits']}")
        print(f"Fractionalized NFT Eligibility: {'Yes' if rewards['frac_nft_eligible'] else 'No'}")
        print(f"AI Capsule NFT Eligibility: {'Yes' if rewards['ai_capsule_eligible'] else 'No'}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
