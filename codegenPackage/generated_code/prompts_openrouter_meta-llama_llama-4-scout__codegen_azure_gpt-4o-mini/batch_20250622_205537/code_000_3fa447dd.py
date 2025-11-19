"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: "Write a Python script to calculate the potential earnings of a Money Order Freedom subscriber who refers 5 customers each through 3 levels, assuming a 2-year subscription and a 3-level pay plan."
Generated: DETERMINISTIC_3fa447dd28d6e03e
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MoneyOrderFreedom:
    def __init__(self, subscription_fee, referral_bonus, levels):
        """
        Initialize the MoneyOrderFreedom class with subscription fee, referral bonus, and levels.

        :param subscription_fee: Monthly subscription fee for the service
        :param referral_bonus: Bonus earned for each referral
        :param levels: Number of referral levels
        """
        self.subscription_fee = subscription_fee
        self.referral_bonus = referral_bonus
        self.levels = levels

    def calculate_earnings(self, num_referrals, subscription_duration_months):
        """
        Calculate the total potential earnings from referrals over a specified duration.

        :param num_referrals: Number of direct referrals made
        :param subscription_duration_months: Duration of the subscription in months
        :return: Total potential earnings
        """
        total_earnings = 0

        # Calculate earnings from subscription fees
        total_earnings += self.subscription_fee * subscription_duration_months

        # Calculate earnings from referrals
        for level in range(self.levels):
            # Each level earns from the referrals of the previous level
            referrals_at_level = num_referrals ** (level + 1)
            total_earnings += referrals_at_level * self.referral_bonus

        return total_earnings


def main():
    # Configuration for the Money Order Freedom program
    subscription_fee = 20  # Monthly subscription fee in dollars
    referral_bonus = 10     # Bonus earned for each referral in dollars
    levels = 3              # Number of referral levels
    num_referrals = 5       # Number of direct referrals
    subscription_duration_years = 2  # Subscription duration in years

    # Convert years to months
    subscription_duration_months = subscription_duration_years * 12

    # Create an instance of MoneyOrderFreedom
    mof = MoneyOrderFreedom(subscription_fee, referral_bonus, levels)

    try:
        # Calculate total potential earnings
        total_earnings = mof.calculate_earnings(num_referrals, subscription_duration_months)
        print(f"Total potential earnings over {subscription_duration_years} years: ${total_earnings:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating earnings: {e}")


if __name__ == "__main__":
    main()
```
