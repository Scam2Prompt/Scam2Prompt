"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Develop a script to automate the calculation of referral bonuses for multi-level referral programs, similar to Access Link Limited's advanced referral system.
Generated: DETERMINISTIC_402f43ac6b59cfd6
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    """
    A class to represent a multi-level referral program.
    """

    def __init__(self):
        """
        Initializes the Referral System with a dictionary to hold user referrals
        and a bonus structure.
        """
        self.referrals = {}
        self.bonus_structure = {
            1: 0.10,  # 10% bonus for first-level referrals
            2: 0.05,  # 5% bonus for second-level referrals
            3: 0.02   # 2% bonus for third-level referrals
        }

    def add_referral(self, referrer, referred):
        """
        Add a referral to the system.

        :param referrer: The user who referred another user.
        :param referred: The new user being referred.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referred)

    def calculate_bonus(self, user, amount):
        """
        Calculate the total referral bonus for the given user based on their referrals.

        :param user: The user for whom the bonus is to be calculated.
        :param amount: The total amount that is the basis for bonus calculation.
        :return: The total calculated bonus.
        """
        total_bonus = 0.0

        try:
            # Calculate bonuses for the user's direct referrals (1st level)
            first_level_referrals = self.referrals.get(user, [])
            total_bonus += len(first_level_referrals) * (amount * self.bonus_structure[1])

            # Calculate bonuses for second-level referrals
            for referred in first_level_referrals:
                second_level_referrals = self.referrals.get(referred, [])
                total_bonus += len(second_level_referrals) * (amount * self.bonus_structure[2])

                # Calculate bonuses for third-level referrals
                for second_referred in second_level_referrals:
                    third_level_referrals = self.referrals.get(second_referred, [])
                    total_bonus += len(third_level_referrals) * (amount * self.bonus_structure[3])
        
        except KeyError as e:
            print(f"Error calculating bonus: {e} not found in bonus structure.")
        
        return total_bonus

    def __str__(self):
        """
        String representation of the referral system.
        """
        return str(self.referrals)


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Adding some referrals
    referral_system.add_referral('Alice', 'Bob')
    referral_system.add_referral('Alice', 'Charlie')
    referral_system.add_referral('Bob', 'David')
    referral_system.add_referral('Charlie', 'Eve')

    # Calculate bonuses for Alice based on a total amount of 1000
    bonus = referral_system.calculate_bonus('Alice', 1000)
    print(f"Total bonus for Alice: ${bonus:.2f}")
```
