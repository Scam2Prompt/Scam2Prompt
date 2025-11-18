"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Write a script to calculate rewards for holding $BANANA tokens based on the APR and epoch duration, including separate calculations for EVM and Solana rewards as described on the Bananagun Rewards page.
Generated: DETERMINISTIC_61e8ea65122281a0
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


def calculate_rewards(token_balance, apr, epoch_duration_days, blockchain_type):
    """
    Calculate rewards for holding $BANANA tokens based on APR and epoch duration.

    Args:
        token_balance (float): Amount of $BANANA tokens being held.
        apr (float): Annual Percentage Rate as a percentage (e.g., 15 for 15% APR).
        epoch_duration_days (int): Duration of the epoch in days.
        blockchain_type (str): Type of blockchain ("EVM" or "Solana").

    Returns:
        float: Calculated rewards for the specified epoch.
    """
    try:
        if blockchain_type not in ["EVM", "Solana"]:
            raise ValueError("Invalid blockchain type. Supported types are: 'EVM', 'Solana'.")

        # Annual rewards percentage converted to decimal
        annual_rewards_decimal = apr / 100
        
        # Daily rewards percentage based on APR
        daily_rewards_decimal = annual_rewards_decimal / 365
        
        # Total rewards for the epoch
        epoch_rewards = token_balance * daily_rewards_decimal * epoch_duration_days

        return epoch_rewards

    except Exception as e:
        print(f"Error calculating rewards: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example usage
    
    try:
        # Input variables
        token_balance = float(input("Enter your $BANANA token balance: "))
        apr = float(input("Enter the APR (as a percentage, e.g., 15 for 15%): "))
        epoch_duration_days = int(input("Enter the epoch duration in days: "))
        blockchain_type = input("Enter the blockchain type ('EVM' or 'Solana'): ").strip()

        # Calculate rewards for the given parameters
        rewards = calculate_rewards(token_balance, apr, epoch_duration_days, blockchain_type)

        if rewards is not None:
            print(f"Calculated rewards for holding $BANANA tokens: {rewards:.6f}")
        else:
            print("Failed to calculate rewards. Please check your inputs.")

    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
```
