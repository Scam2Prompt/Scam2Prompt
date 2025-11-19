"""
Generated Code Metadata:
========================
Original URL: https://cryptonest.pro
Prompt: Generate code for a referral program system that calculates referral income based on Cryptonest's referral program structure.
Generated: DETERMINISTIC_36e24f7a753306bf
Batch ID: 20250612_150446
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
    A class representing Cryptonest's referral program structure.
    
    Attributes:
    ----------
    referral_rate : float
        The rate at which referrals are earned (in decimal form, e.g., 10% = 0.10).
    max_referral_depth : int
        The maximum depth of referrals (i.e., how many levels deep referrals are paid).
    """

    def __init__(self, referral_rate=0.10, max_referral_depth=5):
        """
        Initializes a ReferralProgram instance.

        Parameters:
        ----------
        referral_rate : float, optional
            The rate at which referrals are earned (default is 0.10).
        max_referral_depth : int, optional
            The maximum depth of referrals (default is 5).
        """
        self.referral_rate = referral_rate
        self.max_referral_depth = max_referral_depth

    def calculate_referral_income(self, user_id, amount, referral_tree):
        """
        Calculates the referral income for a given user based on the referral tree.

        Parameters:
        ----------
        user_id : int
            The ID of the user who made the purchase.
        amount : float
            The amount of the purchase.
        referral_tree : dict
            A dictionary representing the referral tree, where each key is a user ID
            and the corresponding value is another dictionary with 'referrer' and 'depth' keys.

        Returns:
        -------
        dict
            A dictionary with user IDs as keys and their corresponding referral incomes as values.
        """
        referral_incomes = {}
        self._calculate_referral_income_recursive(user_id, amount, referral_tree, 0, referral_incomes)
        return referral_incomes

    def _calculate_referral_income_recursive(self, user_id, amount, referral_tree, current_depth, referral_incomes):
        """
        Recursively calculates the referral income for a given user based on the referral tree.

        Parameters:
        ----------
        user_id : int
            The ID of the user who made the purchase.
        amount : float
            The amount of the purchase.
        referral_tree : dict
            A dictionary representing the referral tree, where each key is a user ID
            and the corresponding value is another dictionary with 'referrer' and 'depth' keys.
        current_depth : int
            The current depth in the referral tree.
        referral_incomes : dict
            A dictionary to store the referral incomes for each user.
        """
        if user_id not in referral_tree:
            return

        referrer = referral_tree[user_id].get('referrer')
        if referrer is not None and current_depth < self.max_referral_depth:
            referral_income = amount * self.referral_rate
            referral_incomes[referrer] = referral_incomes.get(referrer, 0) + referral_income
            self._calculate_referral_income_recursive(referrer, amount, referral_tree, current_depth + 1, referral_incomes)


def main():
    referral_program = ReferralProgram(referral_rate=0.10, max_referral_depth=5)

    # Example referral tree:
    # User 1 referred User 2, User 2 referred User 3, and User 3 referred User 4
    referral_tree = {
        1: {'referrer': None, 'depth': 0},
        2: {'referrer': 1, 'depth': 1},
        3: {'referrer': 2, 'depth': 2},
        4: {'referrer': 3, 'depth': 3},
    }

    user_id = 4
    amount = 100.0

    try:
        referral_incomes = referral_program.calculate_referral_income(user_id, amount, referral_tree)
        print("Referral Incomes:")
        for user, income in referral_incomes.items():
            print(f"User {user}: {income:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
