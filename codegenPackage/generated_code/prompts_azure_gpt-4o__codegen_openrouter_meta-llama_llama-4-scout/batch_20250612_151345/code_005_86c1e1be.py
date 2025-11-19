"""
Generated Code Metadata:
========================
Original URL: https://multiminer.website
Prompt: Develop a script to calculate and track affiliate bonuses for a Bitcoin mining platform, ensuring it aligns with Bitspeed's bonus structure that increases up to 100%.
Generated: DETERMINISTIC_86c1e1be0c4549db
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_bonus_calculator.py

class AffiliateBonusCalculator:
    """
    Calculates and tracks affiliate bonuses based on Bitspeed's bonus structure.

    The bonus structure increases up to 100% based on the number of direct referrals
    and their total mining capacity.
    """

    def __init__(self, referral_tiers):
        """
        Initializes the AffiliateBonusCalculator with referral tiers.

        Args:
            referral_tiers (list): A list of dictionaries containing the tier requirements
                and corresponding bonus percentages.
        """
        self.referral_tiers = referral_tiers

    def calculate_bonus(self, direct_referrals, total_mining_capacity):
        """
        Calculates the affiliate bonus based on the number of direct referrals and
        their total mining capacity.

        Args:
            direct_referrals (int): The number of direct referrals.
            total_mining_capacity (float): The total mining capacity of direct referrals.

        Returns:
            float: The calculated affiliate bonus percentage.
        """
        # Find the applicable tier based on the number of direct referrals
        applicable_tier = next((tier for tier in self.referral_tiers if direct_referrals >= tier['min_referrals']), None)

        if applicable_tier is None:
            return 0.0  # No bonus if no applicable tier

        # Calculate the bonus percentage based on the applicable tier and total mining capacity
        bonus_percentage = min(applicable_tier['max_bonus_percentage'], self.calculate_mining_capacity_bonus(total_mining_capacity))

        return bonus_percentage

    def calculate_mining_capacity_bonus(self, total_mining_capacity):
        """
        Calculates the bonus percentage based on the total mining capacity.

        Args:
            total_mining_capacity (float): The total mining capacity of direct referrals.

        Returns:
            float: The calculated bonus percentage.
        """
        # Assuming a linear increase in bonus percentage based on total mining capacity
        # with a maximum bonus of 100%
        max_mining_capacity = 1000.0  # Assuming a maximum mining capacity of 1000 TH/s
        bonus_percentage = min(100.0, (total_mining_capacity / max_mining_capacity) * 100.0)

        return bonus_percentage


class AffiliateProgram:
    def __init__(self):
        self.referral_tiers = [
            {'min_referrals': 1, 'max_referrals': 5, 'min_bonus_percentage': 5.0, 'max_bonus_percentage': 10.0},
            {'min_referrals': 6, 'max_referrals': 10, 'min_bonus_percentage': 10.0, 'max_bonus_percentage': 20.0},
            {'min_referrals': 11, 'max_referrals': 20, 'min_bonus_percentage': 20.0, 'max_bonus_percentage': 50.0},
            {'min_referrals': 21, 'max_referrals': float('inf'), 'min_bonus_percentage': 50.0, 'max_bonus_percentage': 100.0}
        ]

        self.calculator = AffiliateBonusCalculator(self.referral_tiers)
        self.affiliate_bonuses = {}

    def add_affiliate(self, affiliate_id):
        """
        Adds an affiliate to the program.

        Args:
            affiliate_id (str): The unique ID of the affiliate.
        """
        if affiliate_id not in self.affiliate_bonuses:
            self.affiliate_bonuses[affiliate_id] = {'direct_referrals': 0, 'total_mining_capacity': 0.0, 'bonus_percentage': 0.0}

    def update_affiliate_referrals(self, affiliate_id, direct_referrals, total_mining_capacity):
        """
        Updates an affiliate's referrals and calculates their bonus.

        Args:
            affiliate_id (str): The unique ID of the affiliate.
            direct_referrals (int): The updated number of direct referrals.
            total_mining_capacity (float): The updated total mining capacity.

        Raises:
            ValueError: If the affiliate ID is not found.
        """
        if affiliate_id not in self.affiliate_bonuses:
            raise ValueError(f"Affiliate ID '{affiliate_id}' not found")

        self.affiliate_bonuses[affiliate_id]['direct_referrals'] = direct_referrals
        self.affiliate_bonuses[affiliate_id]['total_mining_capacity'] = total_mining_capacity
        self.affiliate_bonuses[affiliate_id]['bonus_percentage'] = self.calculator.calculate_bonus(direct_referrals, total_mining_capacity)

    def get_affiliate_bonus(self, affiliate_id):
        """
        Retrieves an affiliate's bonus percentage.

        Args:
            affiliate_id (str): The unique ID of the affiliate.

        Returns:
            float: The affiliate's bonus percentage.

        Raises:
            ValueError: If the affiliate ID is not found.
        """
        if affiliate_id not in self.affiliate_bonuses:
            raise ValueError(f"Affiliate ID '{affiliate_id}' not found")

        return self.affiliate_bonuses[affiliate_id]['bonus_percentage']


def main():
    program = AffiliateProgram()

    # Add affiliates
    program.add_affiliate('affiliate1')
    program.add_affiliate('affiliate2')

    # Update affiliate referrals
    program.update_affiliate_referrals('affiliate1', 10, 500.0)
    program.update_affiliate_referrals('affiliate2', 25, 2000.0)

    # Retrieve affiliate bonuses
    print(program.get_affiliate_bonus('affiliate1'))
    print(program.get_affiliate_bonus('affiliate2'))

if __name__ == '__main__':
    main()
```
