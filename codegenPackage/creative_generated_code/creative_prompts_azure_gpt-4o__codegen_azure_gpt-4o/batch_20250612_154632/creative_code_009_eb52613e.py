"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindexe.fx-inc.us
Prompt: Write a script to implement Coindexe FX's "Referral Level System," where users can earn up to $500 based on their referrals.
Generated: DETERMINISTIC_eb52613e05e9c5fe
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_referral_bonus(referrals):
    """
    Calculates the referral bonus based on the number of referrals.
    
    Referral levels:
        1-5 referrals: $50
        6-10 referrals: $150
        11-20 referrals: $300
        21+ referrals: $500
        
    Parameters:
        referrals (int): The number of referrals made by the user.
        
    Returns:
        int: The referral bonus in USD.
    """
    if referrals < 1:
        return 0
    elif 1 <= referrals <= 5:
        return 50
    elif 6 <= referrals <= 10:
        return 150
    elif 11 <= referrals <= 20:
        return 300
    else:  # referrals >= 21
        return 500

def main():
    """
    Main function to execute the referral level system script.
    Prompts the user for the number of referrals and calculates the bonus.
    """
    try:
        # Prompt the user to enter the number of referrals
        referrals = int(input("Enter the number of referrals you've made: "))
        
        if referrals < 0:
            print("Error: Number of referrals cannot be negative.")
            return
        
        # Calculate referral bonus
        bonus = calculate_referral_bonus(referrals)
        
        # Display the bonus
        print(f"Based on your {referrals} referrals, your bonus is ${bonus}.")
    except ValueError:
        # Handle invalid input errors
        print("Error: Please enter a valid integer for the number of referrals.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
