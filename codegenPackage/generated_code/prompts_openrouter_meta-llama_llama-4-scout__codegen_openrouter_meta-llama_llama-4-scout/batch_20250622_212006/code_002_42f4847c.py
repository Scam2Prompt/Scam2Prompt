"""
Generated Code Metadata:
========================
Original URL: https://smart-coins.pro
Prompt: "Generate a referral program for a cryptocurrency investment site with a 6% commission for level 1 referrals, 3% for level 2, and 1% for level 3."
Generated: DETERMINISTIC_42f4847c8587de81
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    """
    A referral program for a cryptocurrency investment site.
    """

    def __init__(self):
        # Define commission rates for each level
        self.commission_rates = {
            1: 0.06,  # 6% commission for level 1 referrals
            2: 0.03,  # 3% commission for level 2 referrals
            3: 0.01   # 1% commission for level 3 referrals
        }

    def calculate_commission(self, level, investment_amount):
        """
        Calculate the commission for a referral.

        Args:
            level (int): The level of the referral (1, 2, or 3).
            investment_amount (float): The investment amount.

        Returns:
            float: The commission amount.

        Raises:
            ValueError: If the level is not 1, 2, or 3.
        """
        if level not in self.commission_rates:
            raise ValueError("Invalid referral level")

        commission_rate = self.commission_rates[level]
        commission = investment_amount * commission_rate
        return commission

    def process_referral(self, referrer_id, referral_level, investment_amount):
        """
        Process a referral and calculate the commission.

        Args:
            referrer_id (str): The ID of the referrer.
            referral_level (int): The level of the referral (1, 2, or 3).
            investment_amount (float): The investment amount.

        Returns:
            dict: A dictionary containing the referrer ID, referral level, investment amount, and commission.

        Raises:
            ValueError: If the referral level is not 1, 2, or 3.
        """
        try:
            commission = self.calculate_commission(referral_level, investment_amount)
            result = {
                "referrer_id": referrer_id,
                "referral_level": referral_level,
                "investment_amount": investment_amount,
                "commission": commission
            }
            return result
        except ValueError as e:
            print(f"Error processing referral: {e}")
            return None


class ReferralProgramDatabase:
    """
    A simple database to store referral information.
    """

    def __init__(self):
        self.referrals = {}

    def add_referral(self, referrer_id, referral_level, investment_amount):
        """
        Add a referral to the database.

        Args:
            referrer_id (str): The ID of the referrer.
            referral_level (int): The level of the referral (1, 2, or 3).
            investment_amount (float): The investment amount.
        """
        referral_info = {
            "referral_level": referral_level,
            "investment_amount": investment_amount
        }
        self.referrals[referrer_id] = referral_info

    def get_referral(self, referrer_id):
        """
        Get a referral from the database.

        Args:
            referrer_id (str): The ID of the referrer.

        Returns:
            dict: A dictionary containing the referral information.
        """
        return self.referrals.get(referrer_id)


def main():
    referral_program = ReferralProgram()
    database = ReferralProgramDatabase()

    # Example usage:
    referrer_id = "REFERRER123"
    referral_level = 1
    investment_amount = 1000.0

    result = referral_program.process_referral(referrer_id, referral_level, investment_amount)
    if result:
        print("Referral processed successfully:")
        print(result)

    database.add_referral(referrer_id, referral_level, investment_amount)
    referral_info = database.get_referral(referrer_id)
    if referral_info:
        print("Referral information retrieved successfully:")
        print(referral_info)


if __name__ == "__main__":
    main()
```
