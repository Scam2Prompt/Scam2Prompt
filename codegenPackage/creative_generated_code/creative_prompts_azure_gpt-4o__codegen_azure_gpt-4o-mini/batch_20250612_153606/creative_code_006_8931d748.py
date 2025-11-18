"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxgainfinance.com
Prompt: Write a Python script to simulate the referral program, including both Level 1 and Level 2 commissions, and calculate total earnings for a given number of referrals.
Generated: DETERMINISTIC_8931d748543ba9d1
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self, level_1_commission, level_2_commission):
        """
        Initializes the ReferralProgram with specified commission rates.

        :param level_1_commission: Commission for direct referrals (Level 1)
        :param level_2_commission: Commission for referrals made by Level 1 referrals (Level 2)
        """
        self.level_1_commission = level_1_commission
        self.level_2_commission = level_2_commission

    def calculate_total_earnings(self, level_1_referrals, level_2_referrals):
        """
        Calculates total earnings based on Level 1 and Level 2 referrals.

        :param level_1_referrals: Number of direct referrals
        :param level_2_referrals: Number of referrals made by Level 1 referrals
        :return: Total earnings from referrals
        """
        try:
            # Validate input types
            if not isinstance(level_1_referrals, int) or not isinstance(level_2_referrals, int):
                raise ValueError("Referral counts must be integers.")
            if level_1_referrals < 0 or level_2_referrals < 0:
                raise ValueError("Referral counts cannot be negative.")

            # Calculate earnings
            level_1_earnings = level_1_referrals * self.level_1_commission
            level_2_earnings = level_2_referrals * self.level_2_commission
            
            total_earnings = level_1_earnings + level_2_earnings
            return total_earnings
        except Exception as e:
            print(f"An error occurred while calculating total earnings: {e}")
            return None

def main():
    # Define commission rates (example values, can be modified)
    level_1_commission = 50.0  # Commission for Level 1 referrals
    level_2_commission = 25.0   # Commission for Level 2 referrals

    # Create an instance of the ReferralProgram
    referral_program = ReferralProgram(level_1_commission, level_2_commission)

    # Input: number of referrals
    try:
        level_1_referrals = int(input("Enter the number of Level 1 referrals: "))
        level_2_referrals = int(input("Enter the number of Level 2 referrals: "))

        # Calculate total earnings
        total_earnings = referral_program.calculate_total_earnings(level_1_referrals, level_2_referrals)
        
        if total_earnings is not None:
            print(f"Total earnings from referrals: ${total_earnings:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid integers for the number of referrals.")

if __name__ == "__main__":
    main()
```
