"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-trias-one.pages.dev
Prompt: Create a Python script that calculates TAS rewards based on the migration amount of TRIAS tokens, as outlined in the migration rewards section of the webpage.
Generated: DETERMINISTIC_555b33efffb3598e
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate TAS rewards based on the migration amount of TRIAS tokens.

This script assumes the TAS reward calculation formula is based on the following parameters:
- Migration Amount: Number of TRIAS tokens migrated
- Reward Rate: Percentage corresponding to the reward tier (defined by the migration amount)

Ensure to replace `reward_rate_tiers` with accurate reward rate data from the official source.
"""

# Import necessary libraries
import sys

# Function to calculate TAS rewards
def calculate_tas_rewards(migration_amount):
    """
    Calculate TAS rewards based on the migration amount of TRIAS tokens.
    
    Parameters:
        migration_amount (float): The number of TRIAS tokens migrated.

    Returns:
        float: TAS rewards earned.
    """
    try:
        # Define reward tiers (replace with official rates as per the webpage)
        reward_rate_tiers = [
            (0, 100, 0.05),      # Tier 1: 0-100 TRIAS tokens → 5% reward
            (101, 500, 0.10),    # Tier 2: 101-500 TRIAS tokens → 10% reward
            (501, 1000, 0.15),   # Tier 3: 501-1000 TRIAS tokens → 15% reward
            (1001, float('inf'), 0.20)  # Tier 4: >1000 TRIAS tokens → 20% reward
        ]

        # Validate input
        if migration_amount < 0:
            raise ValueError("Migration amount cannot be negative.")

        # Determine reward rate based on tiers
        for tier in reward_rate_tiers:
            lower_bound, upper_bound, rate = tier
            if lower_bound <= migration_amount <= upper_bound:
                reward_rate = rate
                break
        else:
            raise ValueError("No reward rate found for the given migration amount.")

        # Calculate rewards
        rewards = migration_amount * reward_rate
        return rewards

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main function to execute the script
def main():
    """
    Main function to run the TAS reward calculation script.
    """
    try:
        # Input the migration amount
        migration_amount = float(input("Enter the migration amount of TRIAS tokens: "))

        # Calculate rewards
        rewards = calculate_tas_rewards(migration_amount)

        # Display the result
        if rewards is not None:
            print(f"TAS rewards for migrating {migration_amount} TRIAS tokens: {rewards:.2f}")
        else:
            print("Could not calculate rewards due to an error.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for migration amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
