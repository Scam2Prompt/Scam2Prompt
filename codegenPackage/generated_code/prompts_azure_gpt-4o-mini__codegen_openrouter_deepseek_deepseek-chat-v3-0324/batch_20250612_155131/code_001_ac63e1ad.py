"""
Generated Code Metadata:
========================
Original URL: https://pepeunchaineden.pages.dev
Prompt: Write a Python script that calculates potential staking rewards for $PEPU tokens based on the double staking rewards mentioned on the Pepe Unchained website.
Generated: DETERMINISTIC_ac63e1adb6b235b7
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_staking_rewards(
    principal: float,
    apy: float,
    duration_days: int,
    compounding_frequency: int = 365,
    double_rewards: bool = False
) -> dict:
    """
    Calculate staking rewards for PEPU tokens with optional double rewards.

    Args:
        principal: Initial amount of tokens staked
        apy: Annual Percentage Yield (as decimal, e.g., 0.1 for 10%)
        duration_days: Staking duration in days
        compounding_frequency: Number of compounding periods per year (default: daily)
        double_rewards: Whether to apply double rewards (default: False)

    Returns:
        Dictionary containing:
        - total_rewards: Total rewards earned
        - total_value: Principal + rewards
        - effective_apy: Effective APY considering compounding
    """
    try:
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if apy <= 0:
            raise ValueError("APY must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be positive")

        # Apply double rewards if enabled
        effective_apy = apy * 2 if double_rewards else apy

        # Calculate compounding periods
        n = compounding_frequency
        t = duration_days / 365  # Convert days to years

        # Compound interest formula
        total_value = principal * (1 + (effective_apy / n)) ** (n * t)
        total_rewards = total_value - principal

        return {
            "total_rewards": total_rewards,
            "total_value": total_value,
            "effective_apy": effective_apy,
        }

    except ValueError as e:
        print(f"Error in input parameters: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """Main function to demonstrate staking rewards calculation."""
    try:
        # Example parameters
        principal = float(input("Enter the amount of PEPU tokens to stake: "))
        apy = float(input("Enter the APY (as decimal, e.g., 0.1 for 10%): "))
        duration = int(input("Enter staking duration in days: "))
        double = input("Double rewards enabled? (y/n): ").lower() == 'y'

        result = calculate_staking_rewards(
            principal=principal,
            apy=apy,
            duration_days=duration,
            double_rewards=double
        )

        if result:
            print("\nStaking Rewards Calculation:")
            print(f"Principal: {principal:.2f} PEPU")
            print(f"APY: {apy * 100:.2f}% {'(Double Rewards)' if double else ''}")
            print(f"Duration: {duration} days")
            print(f"Total Rewards: {result['total_rewards']:.2f} PEPU")
            print(f"Total Value: {result['total_value']:.2f} PEPU")
            print(f"Effective APY: {result['effective_apy'] * 100:.2f}%")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
