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
class ReferralProgram:
    """
    A class to represent a referral program earnings simulator.

    Attributes:
        referral_percentage (float): The percentage of earnings from referrals.
    """

    def __init__(self, referral_percentage=0.05):
        """
        Initializes the ReferralProgram with a given referral percentage.

        Parameters:
            referral_percentage (float): The percentage of earnings from referrals.
        """
        self.referral_percentage = referral_percentage

    def calculate_earnings(self, referrals):
        """
        Calculate total earnings based on referrals and their deposit amounts.

        Parameters:
            referrals (list): A list of tuples where each tuple contains 
                              (referral deposit amount, number of referrals).

        Returns:
            float: Total earnings from referrals.
        """
        total_earnings = 0.0
        
        for deposit, count in referrals:
            if deposit < 0 or count < 0:
                raise ValueError("Deposit amounts and referral counts must be non-negative.")
            earnings = deposit * count * self.referral_percentage
            total_earnings += earnings
        
        return total_earnings

def main():
    """
    Main function to run the Referral Program earnings simulation.
    """
    referral_program = ReferralProgram()

    print("Welcome to the MFX-Online Trade Referral Program Earnings Calculator!")
    referrals = []
    
    while True:
        try:
            # Input number of referrals
            num_referrals = int(input("Enter the number of different referral deposits (or -1 to finish): "))
            if num_referrals == -1:
                break
            
            # Input referral deposit amounts and counts
            for _ in range(num_referrals):
                deposit = float(input("Enter referral deposit amount: "))
                count = int(input("Enter number of referrals: "))
                
                referrals.append((deposit, count))
        
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
            continue

    try:
        total_earnings = referral_program.calculate_earnings(referrals)
        print(f"Total earnings from referrals: ${total_earnings:.2f}")
    except Exception as e:
        print(f"Error calculating earnings: {e}")

if __name__ == "__main__":
    main()
```
