"""
Generated Code Metadata:
========================
Original URL: https://binarygoldenoptions.com
Prompt: Create a referral program system in Python that tracks referrals and calculates referral income based on the structure described on Binary Golden Options.
Generated: DETERMINISTIC_2cb335fe51ce9a85
Batch ID: 20250612_150227
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
    A referral program system that tracks referrals and calculates referral income.
    """

    def __init__(self):
        """
        Initializes the referral program with an empty dictionary to store referrals.
        """
        self.referrals = {}

    def add_referral(self, referrer_id, referred_id):
        """
        Adds a new referral to the program.

        Args:
            referrer_id (str): The ID of the user who referred the new user.
            referred_id (str): The ID of the new user.

        Raises:
            ValueError: If the referrer ID or referred ID is empty.
        """
        if not referrer_id or not referred_id:
            raise ValueError("Referrer ID and referred ID cannot be empty")

        if referred_id not in self.referrals:
            self.referrals[referred_id] = {
                "referrer_id": referrer_id,
                "level": 0,
                "income": 0.0
            }

    def calculate_income(self, referred_id, deposit_amount):
        """
        Calculates the referral income based on the deposit amount.

        Args:
            referred_id (str): The ID of the user who made a deposit.
            deposit_amount (float): The amount of the deposit.

        Raises:
            ValueError: If the referred ID is not in the referrals dictionary.
        """
        if referred_id not in self.referrals:
            raise ValueError("Referred ID not found in referrals")

        referrer_id = self.referrals[referred_id]["referrer_id"]
        level = self.referrals[referred_id]["level"]

        # Binary Golden Options structure:
        # Level 0: 5% income
        # Level 1: 3% income
        # Level 2: 2% income
        if level == 0:
            income_percentage = 0.05
        elif level == 1:
            income_percentage = 0.03
        elif level == 2:
            income_percentage = 0.02
        else:
            income_percentage = 0.0

        income = deposit_amount * income_percentage
        self.referrals[referred_id]["income"] += income

        # Update referrer's income
        if referrer_id in self.referrals:
            self.referrals[referrer_id]["income"] += income

    def get_referral_info(self, referred_id):
        """
        Gets the referral information for a given user.

        Args:
            referred_id (str): The ID of the user.

        Returns:
            dict: The referral information, including referrer ID, level, and income.

        Raises:
            ValueError: If the referred ID is not in the referrals dictionary.
        """
        if referred_id not in self.referrals:
            raise ValueError("Referred ID not found in referrals")

        return self.referrals[referred_id]

    def update_level(self, referred_id, level):
        """
        Updates the level of a referred user.

        Args:
            referred_id (str): The ID of the user.
            level (int): The new level.

        Raises:
            ValueError: If the referred ID is not in the referrals dictionary.
        """
        if referred_id not in self.referrals:
            raise ValueError("Referred ID not found in referrals")

        self.referrals[referred_id]["level"] = level


def main():
    referral_program = ReferralProgram()

    # Example usage:
    referral_program.add_referral("referrer1", "referred1")
    referral_program.add_referral("referred1", "referred2")

    referral_program.calculate_income("referred2", 1000.0)

    print(referral_program.get_referral_info("referred1"))
    print(referral_program.get_referral_info("referred2"))


if __name__ == "__main__":
    main()
```
