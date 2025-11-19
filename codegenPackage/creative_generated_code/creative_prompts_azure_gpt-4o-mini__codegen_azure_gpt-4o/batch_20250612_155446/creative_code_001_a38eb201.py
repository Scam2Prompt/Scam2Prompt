"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Write a Python script to calculate the staking power for the Polyhedra Network token based on the amount staked and the lock duration.
Generated: DETERMINISTIC_a38eb2010543311b
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_power(amount_staked, lock_duration):
    """
    Calculate staking power for the Polyhedra Network token.
    
    Staking power is calculated as:
    staking_power = amount_staked * (1 + lock_multiplier)
    
    The lock_multiplier increases with the lock duration:
    - For lock duration < 6 months: lock_multiplier = 0.1
    - For lock duration >= 6 months and < 12 months: lock_multiplier = 0.25
    - For lock duration >= 12 months: lock_multiplier = 0.5
    
    Parameters:
        amount_staked (float): Amount of tokens staked.
        lock_duration (int): Lock duration in months.
    
    Returns:
        float: Calculated staking power.
    """
    try:
        # Validate inputs
        if amount_staked < 0:
            raise ValueError("Amount staked must be non-negative.")
        if lock_duration < 0:
            raise ValueError("Lock duration must be non-negative.")

        # Determine lock multiplier based on lock duration
        if lock_duration < 6:
            lock_multiplier = 0.1
        elif 6 <= lock_duration < 12:
            lock_multiplier = 0.25
        else:  # lock_duration >= 12
            lock_multiplier = 0.5

        # Calculate staking power
        staking_power = amount_staked * (1 + lock_multiplier)
        return staking_power

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interactively calculate staking power based on user input.
    """
    try:
        print("=== Polyhedra Network Staking Power Calculator ===")
        
        # Get input from the user
        amount_staked = float(input("Enter the amount staked (tokens): "))
        lock_duration = int(input("Enter the lock duration (months): "))
        
        # Calculate staking power
        staking_power = calculate_staking_power(amount_staked, lock_duration)
        
        print(f"Calculated Staking Power: {staking_power:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers for amount staked and lock duration.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for script execution
    main()
```
