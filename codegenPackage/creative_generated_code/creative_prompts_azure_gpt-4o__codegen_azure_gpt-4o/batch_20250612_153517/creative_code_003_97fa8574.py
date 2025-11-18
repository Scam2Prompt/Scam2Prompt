"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Develop a script to automate the selection of vesting bonuses for $MANIA token purchases, ensuring the correct percentage bonus is applied based on the user's spending amount.
Generated: DETERMINISTIC_97fa8574be3c55ea
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vesting_bonus_calculator.py

# Import necessary modules
import sys

def calculate_bonus(spending_amount):
    """
    Calculate the vesting bonus percentage based on the spending amount.
    
    Args:
        spending_amount (float): The amount spent by the user on $MANIA tokens.
    
    Returns:
        float: The bonus percentage based on the spending amount.
    """
    if spending_amount < 0:
        raise ValueError("Spending amount cannot be negative.")
    
    # Define the bonus tiers
    bonus_tiers = [
        (0, 0),         # No bonus for spending less than $0.
        (100, 5),       # 5% bonus for spending $100-$499.
        (500, 10),      # 10% bonus for spending $500-$999.
        (1000, 15),     # 15% bonus for spending $1000-$4999.
        (5000, 20),     # 20% bonus for spending $5000-$9999.
        (10000, 25)     # 25% bonus for spending $10000 and above.
    ]
    
    # Determine the applicable bonus percentage
    for tier_amount, bonus_percentage in reversed(bonus_tiers):
        if spending_amount >= tier_amount:
            return bonus_percentage
    
    return 0  # Default fallback (shouldn't be reached)

def main():
    """
    Main function to execute the vesting bonus calculation for $MANIA token purchases.
    """
    try:
        # Prompt user for spending amount
        spending_amount = float(input("Enter the amount spent on $MANIA tokens: $"))
        
        # Calculate the bonus percentage
        bonus_percentage = calculate_bonus(spending_amount)
        
        # Display the result
        print(f"Spending Amount: ${spending_amount:.2f}")
        print(f"Vesting Bonus Percentage: {bonus_percentage}%")
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
