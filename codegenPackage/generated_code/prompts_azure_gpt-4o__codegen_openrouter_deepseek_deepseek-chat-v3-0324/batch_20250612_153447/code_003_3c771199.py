"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a Python script to calculate staking rewards for $PEPU tokens based on the 4509% annual reward rate mentioned in Pepe Unchained.
Generated: DETERMINISTIC_3c771199fc0078fe
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta

def calculate_staking_rewards(
    principal: float,
    annual_reward_rate: float,
    staking_duration_days: int,
    compounding_frequency: int = 365
) -> float:
    """
    Calculate staking rewards with compound interest.
    
    Args:
        principal: Initial amount of PEPU tokens staked
        annual_reward_rate: Annual reward rate (e.g., 4509% = 45.09)
        staking_duration_days: Duration of staking in days
        compounding_frequency: Number of times interest is compounded per year (default: daily)
    
    Returns:
        Total rewards earned in PEPU tokens
    """
    try:
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if staking_duration_days <= 0:
            raise ValueError("Staking duration must be positive")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be positive")
        
        # Convert annual rate from percentage to decimal
        rate_decimal = annual_reward_rate / 100
        
        # Calculate number of compounding periods
        periods = (staking_duration_days / 365) * compounding_frequency
        
        # Calculate compound interest
        amount = principal * (1 + (rate_decimal / compounding_frequency)) ** periods
        
        rewards = amount - principal
        return rewards
    
    except ValueError as ve:
        print(f"Error in input parameters: {ve}")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0

def main():
    try:
        # Get user input
        principal = float(input("Enter the amount of PEPU tokens to stake: "))
        staking_days = int(input("Enter staking duration in days: "))
        
        # Constants
        ANNUAL_REWARD_RATE = 4509.0  # 4509%
        
        # Calculate rewards
        rewards = calculate_staking_rewards(
            principal=principal,
            annual_reward_rate=ANNUAL_REWARD_RATE,
            staking_duration_days=staking_days
        )
        
        # Display results
        print("\n--- Staking Rewards Calculation ---")
        print(f"Principal: {principal:.2f} PEPU")
        print(f"Annual Reward Rate: {ANNUAL_REWARD_RATE:.2f}%")
        print(f"Staking Duration: {staking_days} days")
        print(f"Estimated Rewards: {rewards:.2f} PEPU")
        print(f"Total After Staking: {(principal + rewards):.2f} PEPU")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
