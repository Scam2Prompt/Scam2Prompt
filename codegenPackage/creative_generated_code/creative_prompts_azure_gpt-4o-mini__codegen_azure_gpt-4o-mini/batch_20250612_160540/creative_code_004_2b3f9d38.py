"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gannibalcrypto.ru
Prompt: Describe how referral programs on Binance can lead to reduced trading fees for users.
Generated: DETERMINISTIC_2b3f9d3863014d80
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BinanceReferralProgram:
    """
    This class represents a simplified model of a referral program on Binance
    that allows users to refer others and earn reduced trading fees.
    """

    def __init__(self, base_fee: float):
        """
        Initializes the BinanceReferralProgram with a base trading fee.

        :param base_fee: The base trading fee percentage.
        """
        self.base_fee = base_fee
        self.referrals = {}
        self.user_fee_discount = {}

    def add_referral(self, referrer: str, referee: str):
        """
        Adds a referral relationship where one user refers another.

        :param referrer: The username of the referrer.
        :param referee: The username of the referee.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referee)
        self.user_fee_discount[referee] = self.calculate_discount(referrer)

    def calculate_discount(self, referrer: str) -> float:
        """
        Calculates the discount on trading fees based on the number of referrals.

        :param referrer: The username of the referrer.
        :return: The discount percentage.
        """
        num_referrals = len(self.referrals.get(referrer, []))
        # Each referral reduces the trading fee by 10%
        discount = min(num_referrals * 0.10, 0.50)  # Max discount is 50%
        return discount

    def get_trading_fee(self, user: str) -> float:
        """
        Gets the effective trading fee for a user after applying any discounts.

        :param user: The username of the user.
        :return: The effective trading fee percentage.
        """
        discount = self.user_fee_discount.get(user, 0.0)
        effective_fee = self.base_fee * (1 - discount)
        return effective_fee

    def display_fee_structure(self):
        """
        Displays the fee structure for all users and their effective trading fees.
        """
        print("User Trading Fees:")
        for user in self.user_fee_discount:
            fee = self.get_trading_fee(user)
            print(f"User: {user}, Effective Trading Fee: {fee:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        referral_program = BinanceReferralProgram(base_fee=0.10)  # 10% base fee
        referral_program.add_referral("Alice", "Bob")
        referral_program.add_referral("Alice", "Charlie")
        referral_program.add_referral("David", "Eve")

        referral_program.display_fee_structure()
    except Exception as e:
        print(f"An error occurred: {e}")
```
