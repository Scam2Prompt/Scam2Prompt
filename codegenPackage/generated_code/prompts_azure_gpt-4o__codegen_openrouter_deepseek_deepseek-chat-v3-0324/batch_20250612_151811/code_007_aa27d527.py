"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Create a Python program to simulate the referral program earnings described on MFX-Online Trade, allowing users to input the number of referrals and their deposit amounts.
Generated: DETERMINISTIC_aa27d527582b368b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class ReferralProgram:
    """
    Simulates the referral program earnings based on the number of referrals and their deposit amounts.
    """
    
    def __init__(self):
        self.commission_rates = {
            1: 0.05,    # 5% for 1-5 referrals
            6: 0.07,    # 7% for 6-10 referrals
            11: 0.10,   # 10% for 11-20 referrals
            21: 0.15    # 15% for 21+ referrals
        }
    
    def get_commission_rate(self, num_referrals):
        """
        Returns the commission rate based on the number of referrals.
        
        Args:
            num_referrals (int): Number of referrals
            
        Returns:
            float: Commission rate
        """
        if num_referrals >= 21:
            return self.commission_rates[21]
        elif num_referrals >= 11:
            return self.commission_rates[11]
        elif num_referrals >= 6:
            return self.commission_rates[6]
        else:
            return self.commission_rates[1]
    
    def calculate_earnings(self, num_referrals, deposit_amounts):
        """
        Calculates total earnings from referrals.
        
        Args:
            num_referrals (int): Number of referrals
            deposit_amounts (list): List of deposit amounts for each referral
            
        Returns:
            tuple: (total_earnings, commission_rate_used)
        """
        if len(deposit_amounts) != num_referrals:
            raise ValueError("Number of deposit amounts must match number of referrals")
        
        if num_referrals <= 0:
            return (0.0, 0.0)
        
        commission_rate = self.get_commission_rate(num_referrals)
        total_deposits = sum(deposit_amounts)
        total_earnings = total_deposits * commission_rate
        
        return (total_earnings, commission_rate)
    
    def get_user_input(self):
        """
        Gets user input for number of referrals and their deposit amounts.
        
        Returns:
            tuple: (num_referrals, deposit_amounts)
        """
        try:
            num_referrals = int(input("Enter the number of referrals: "))
            if num_referrals < 0:
                raise ValueError("Number of referrals cannot be negative")
            
            deposit_amounts = []
            for i in range(num_referrals):
                while True:
                    try:
                        amount = float(input(f"Enter deposit amount for referral {i+1}: $"))
                        if amount < 0:
                            print("Deposit amount cannot be negative. Please try again.")
                            continue
                        deposit_amounts.append(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            
            return (num_referrals, deposit_amounts)
        
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(1)
    
    def run(self):
        """
        Main program execution.
        """
        print("MFX-Online Trade Referral Program Simulator")
        print("------------------------------------------")
        
        num_referrals, deposit_amounts = self.get_user_input()
        
        try:
            total_earnings, commission_rate = self.calculate_earnings(num_referrals, deposit_amounts)
            
            print("\nResults:")
            print(f"Number of referrals: {num_referrals}")
            print(f"Commission rate applied: {commission_rate * 100:.1f}%")
            print(f"Total deposits from referrals: ${sum(deposit_amounts):,.2f}")
            print(f"Total earnings: ${total_earnings:,.2f}")
            
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    program = ReferralProgram()
    program.run()
```
