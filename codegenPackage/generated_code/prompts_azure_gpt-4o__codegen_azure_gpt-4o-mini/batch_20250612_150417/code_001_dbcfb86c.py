"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: Generate Python code for a referral program that calculates commission earnings based on LongTradeGroup's referral structure, where Level A referrals earn 0.50% of deposits.
Generated: DETERMINISTIC_dbcfb86c25f81879
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralProgram:
    """
    A class to represent a referral program for LongTradeGroup.
    
    Attributes
    ----------
    commission_rate : float
        The commission rate for Level A referrals (0.50%).
    referrals : dict
        A dictionary to store referral deposits keyed by user ID.
    """

    def __init__(self):
        """
        Initializes the ReferralProgram with a commission rate and an empty referrals dictionary.
        """
        self.commission_rate = 0.005  # 0.50% commission
        self.referrals = {}

    def add_referral(self, user_id: str, deposit: float) -> None:
        """
        Adds a referral deposit for a given user.

        Parameters
        ----------
        user_id : str
            The unique identifier for the user making the deposit.
        deposit : float
            The amount deposited by the user.

        Raises
        ------
        ValueError
            If the deposit amount is negative.
        """
        if deposit < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        self.referrals[user_id] = self.referrals.get(user_id, 0) + deposit

    def calculate_commission(self, user_id: str) -> float:
        """
        Calculates the commission earnings for a given user based on their deposits.

        Parameters
        ----------
        user_id : str
            The unique identifier for the user whose commission is to be calculated.

        Returns
        -------
        float
            The commission earned by the user.

        Raises
        ------
        KeyError
            If the user ID does not exist in the referrals.
        """
        if user_id not in self.referrals:
            raise KeyError(f"No deposits found for user ID: {user_id}")

        total_deposit = self.referrals[user_id]
        commission = total_deposit * self.commission_rate
        return commission

    def get_all_commissions(self) -> dict:
        """
        Retrieves the commission earnings for all users in the referral program.

        Returns
        -------
        dict
            A dictionary with user IDs as keys and their respective commissions as values.
        """
        commissions = {}
        for user_id in self.referrals:
            commissions[user_id] = self.calculate_commission(user_id)
        return commissions


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Adding referrals
    try:
        referral_program.add_referral("user123", 1000.0)
        referral_program.add_referral("user456", 2000.0)
    except ValueError as e:
        print(f"Error adding referral: {e}")

    # Calculating commissions
    try:
        commission_user123 = referral_program.calculate_commission("user123")
        print(f"Commission for user123: ${commission_user123:.2f}")

        commission_user456 = referral_program.calculate_commission("user456")
        print(f"Commission for user456: ${commission_user456:.2f}")

        # Attempting to calculate commission for a non-existent user
        commission_user789 = referral_program.calculate_commission("user789")
    except KeyError as e:
        print(f"Error calculating commission: {e}")

    # Getting all commissions
    all_commissions = referral_program.get_all_commissions()
    print("All commissions:", all_commissions)
```
