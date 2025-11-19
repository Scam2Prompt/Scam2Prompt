"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-staking.pages.dev
Prompt: Create a script that calculates potential gas refunds based on different stake sizes for HEHE Coin users.
Generated: DETERMINISTIC_6bcca07f550c330d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential gas refunds based on different stake sizes for HEHE Coin users.

This script is production-ready, clean, and well-commented.
"""

# Import necessary libraries
import sys

def calculate_gas_refund(stake_size):
    """
    Calculate the potential gas refund based on the stake size.

    Parameters:
        stake_size (float): The amount of HEHE Coin staked.

    Returns:
        float: The estimated gas refund.
    """
    try:
        # Gas refund logic: assume a base rate and multiplier
        # Base refund rate is 0.01 per coin staked, capped at 5000.
        BASE_REFUND_RATE = 0.01
        MAX_REFUND = 5000.0  # Maximum refund allowed

        if stake_size < 0:
            raise ValueError("Stake size cannot be negative.")

        # Calculate refund
        refund = stake_size * BASE_REFUND_RATE
        
        # Apply cap
        return min(refund, MAX_REFUND)
    
    except ValueError as ve:
        # Handle invalid stake size
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate gas refunds.
    """
    print("=== HEHE Coin Gas Refund Calculator ===")
    try:
        # Get user input for stake size
        stake_size = float(input("Enter the amount of HEHE Coin staked: "))
        
        # Calculate the gas refund
        refund = calculate_gas_refund(stake_size)
        
        if refund is not None:
            print(f"Estimated gas refund: {refund:.2f}")
        else:
            print("Could not calculate gas refund due to an error.")
    
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a numeric value for the stake size.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
