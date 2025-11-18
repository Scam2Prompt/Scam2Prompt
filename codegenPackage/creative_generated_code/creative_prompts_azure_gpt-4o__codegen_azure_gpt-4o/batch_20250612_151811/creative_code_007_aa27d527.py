"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Create a Python program to simulate the referral program earnings described on MFX-Online Trade, allowing users to input the number of referrals and their deposit amounts.
Generated: DETERMINISTIC_aa27d527582b368b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Program to Simulate Referral Program Earnings for MFX-Online Trade

# Constants representing referral earnings percentages at each level
REFERRAL_LEVEL_PERCENTAGES = {
    1: 0.07,  # Level 1: 7%
    2: 0.02,  # Level 2: 2%
    3: 0.01   # Level 3: 1%
}

def calculate_referral_earnings(referrals):
    """
    Calculate referral earnings based on the number of referrals and their deposit amounts.
    
    Args:
        referrals (dict): A dictionary where keys are referral levels (1, 2, 3) and 
                          values are lists of deposit amounts from referrals at that level.
    
    Returns:
        float: Total earnings from all referral levels.
    """
    total_earnings = 0.0

    for level, deposits in referrals.items():
        if level not in REFERRAL_LEVEL_PERCENTAGES:
            print(f"Warning: Level {level} is not recognized. Skipping...")
            continue
        
        # Calculate earnings for each deposit in the current level
        level_percentage = REFERRAL_LEVEL_PERCENTAGES[level]
        for deposit in deposits:
            # Validate deposit amount
            if deposit < 0:
                print(f"Error: Negative deposit amount ({deposit}) encountered. Skipping...")
                continue
            
            total_earnings += deposit * level_percentage
    
    return total_earnings


def main():
    """
    Main function to simulate the referral program earnings.
    Allows user input for referral data.
    """
    print("Welcome to the MFX-Online Trade Referral Program Earnings Simulator!")
    print("Provide the referral data for each level.")
    
    referrals = {}

    try:
        for level in REFERRAL_LEVEL_PERCENTAGES.keys():
            deposits = []
            num_referrals = int(input(f"Enter the number of referrals at Level {level}: "))
            
            for i in range(num_referrals):
                deposit = float(input(f"  Enter deposit amount for referral {i + 1} at Level {level}: "))
                deposits.append(deposit)
            
            referrals[level] = deposits
        
        # Calculate total earnings
        total_earnings = calculate_referral_earnings(referrals)
        print(f"\nTotal Referral Earnings: ${total_earnings:.2f}")
    
    except ValueError as e:
        print(f"Error: Invalid input encountered. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
