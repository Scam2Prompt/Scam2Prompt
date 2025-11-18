"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase2bdags-network.pages.dev
Prompt: Create a tool to calculate the total earnings from referral bonuses based on the 10% commission structure described in the BDAG presale.
Generated: DETERMINISTIC_5203d600a43883c2
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralBonusCalculator:
    """
    A tool to calculate total earnings from referral bonuses based on a 10% commission structure.
    """

    def __init__(self, referral_amounts):
        """
        Initializes the calculator with a list of referral amounts.

        :param referral_amounts: List of amounts earned through referrals.
        """
        if not isinstance(referral_amounts, list):
            raise ValueError("referral_amounts must be a list.")
        if any(not isinstance(amount, (int, float)) or amount < 0 for amount in referral_amounts):
            raise ValueError("All referral amounts must be non-negative numbers.")
        
        self.referral_amounts = referral_amounts
        self.commission_rate = 0.10  # 10% commission

    def calculate_total_earnings(self):
        """
        Calculates total earnings from referral bonuses.

        :return: Total earnings as a float.
        """
        total_earnings = sum(amount * self.commission_rate for amount in self.referral_amounts)
        return total_earnings

    def display_earnings(self):
        """
        Displays the total earnings in a formatted manner.
        """
        total = self.calculate_total_earnings()
        print(f"Total earnings from referral bonuses: ${total:.2f}")


if __name__ == "__main__":
    # Example usage of the ReferralBonusCalculator
    try:
        referral_amounts = [100, 200, 300]  # Example referral amounts
        calculator = ReferralBonusCalculator(referral_amounts)
        calculator.display_earnings()
    except ValueError as e:
        print(f"Error: {e}")
```
