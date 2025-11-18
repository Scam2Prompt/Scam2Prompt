"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fluff-top.pages.dev
Prompt: Write a Python program to calculate the rewards for staking Seamless (SEAM) and Stablecomp (SCOMP) based on BitMart's APY rates.
Generated: DETERMINISTIC_96cc45da4e6ba822
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(principal, apy_rate, staking_days):
    """
    Calculate the staking rewards based on principal, APY rate, and staking duration in days.

    Args:
        principal (float): The amount staked.
        apy_rate (float): The annual percentage yield (APY) rate as a percentage (e.g., 5 for 5% APY).
        staking_days (int): The number of days the funds are staked.

    Returns:
        float: The calculated staking rewards.
    """
    try:
        # Convert APY rate to a decimal
        annual_rate = apy_rate / 100
        
        # Calculate daily rate
        daily_rate = annual_rate / 365
        
        # Calculate rewards
        rewards = principal * daily_rate * staking_days
        
        return rewards
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating rewards: {e}")
        sys.exit(1)

def main():
    # Define APY rates for SEAM and SCOMP (example values)
    SEAM_APY = 12.5  # 12.5% annual APY
    SCOMP_APY = 8.3  # 8.3% annual APY

    try:
        # Collect user input for staking details
        print("Enter staking details for Seamless (SEAM):")
        seam_principal = float(input("Enter principal amount (SEAM): "))
        seam_days = int(input("Enter number of staking days (SEAM): "))

        print("\nEnter staking details for Stablecomp (SCOMP):")
        scomp_principal = float(input("Enter principal amount (SCOMP): "))
        scomp_days = int(input("Enter number of staking days (SCOMP): "))

        # Calculate rewards
        seam_rewards = calculate_rewards(seam_principal, SEAM_APY, seam_days)
        scomp_rewards = calculate_rewards(scomp_principal, SCOMP_APY, scomp_days)

        # Display results
        print("\nStaking Rewards:")
        print(f"Seamless (SEAM): {seam_rewards:.2f} SEAM")
        print(f"Stablecomp (SCOMP): {scomp_rewards:.2f} SCOMP")
    except ValueError:
        # Handle invalid input errors
        print("Invalid input. Please make sure to enter numeric values for principal and days.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
