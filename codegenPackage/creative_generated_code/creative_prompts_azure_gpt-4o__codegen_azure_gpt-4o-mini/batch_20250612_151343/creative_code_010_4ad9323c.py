"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-8bz.pages.dev
Prompt: Write code to implement referral bonuses for investors as part of BlockDAG's marketing strategy described in the launch phase.
Generated: DETERMINISTIC_4ad9323cfc8d7843
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investor:
    """
    Represents an investor in the BlockDAG system.
    Each investor can refer other investors and potentially earn bonuses.
    """
    def __init__(self, investor_id, name):
        """
        Initializes an Investor instance.

        :param investor_id: Unique identifier for the investor.
        :param name: Name of the investor.
        """
        self.investor_id = investor_id
        self.name = name
        self.referrals = []  # List to store referrals
        self.bonus_balance = 0.0  # Track referral bonuses

    def refer(self, referred_investor):
        """
        Refers a new investor and adds them to the referral list.
        
        :param referred_investor: An instance of Investor that is being referred.
        :raises ValueError: If the referred_investor is already a referral of this investor.
        """
        if referred_investor in self.referrals:
            raise ValueError("This investor has already been referred.")
        self.referrals.append(referred_investor)

    def add_bonus(self, amount):
        """
        Adds a bonus amount to the investor's bonus balance.

        :param amount: The amount to add to the bonus balance.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Bonus amount cannot be negative.")
        self.bonus_balance += amount

    def get_bonus_balance(self):
        """
        Returns the current bonus balance of the investor.
        
        :return: Current bonus balance.
        """
        return self.bonus_balance


class ReferralProgram:
    """
    Manages the referral program for investors.
    """
    def __init__(self, bonus_per_referral):
        """
        Initializes the ReferralProgram instance.

        :param bonus_per_referral: The bonus amount awarded for each successful referral.
        """
        self.bonus_per_referral = bonus_per_referral
        self.investors = {}  # Dictionary to store Investors by their ID

    def register_investor(self, investor_id, name):
        """
        Registers a new investor in the referral program.

        :param investor_id: Unique identifier for the investor.
        :param name: Name of the investor.
        :raises ValueError: If the investor_id already exists.
        """
        if investor_id in self.investors:
            raise ValueError("Investor ID already exists.")
        self.investors[investor_id] = Investor(investor_id, name)

    def refer_investor(self, referrer_id, referred_id, referred_name):
        """
        Processes the referral of a new investor.

        :param referrer_id: The ID of the investor making the referral.
        :param referred_id: The ID of the investor being referred.
        :param referred_name: Name of the investor being referred.
        :raises KeyError: If referrer_id or referred_id does not exist.
        """
        if referrer_id not in self.investors:
            raise KeyError("Referrer ID not found.")
        
        if referred_id in self.investors:
            raise ValueError("Referred investor ID already exists.")

        # Register the referred investor
        self.register_investor(referred_id, referred_name)

        # Refer the new investor to the referrer
        referrer = self.investors[referrer_id]
        referred_investor = self.investors[referred_id]
        referrer.refer(referred_investor)

        # Add bonus to the referrer
        referrer.add_bonus(self.bonus_per_referral)

    def get_investor_bonus(self, investor_id):
        """
        Returns the bonus balance of a specified investor.

        :param investor_id: The ID of the investor.
        :raises KeyError: If the investor_id does not exist.
        :return: The current bonus balance of the investor.
        """
        if investor_id not in self.investors:
            raise KeyError("Investor ID not found.")
        return self.investors[investor_id].get_bonus_balance()


# Example usage:
if __name__ == "__main__":
    # Initialize the referral program with a bonus of $50 per referral
    referral_program = ReferralProgram(bonus_per_referral=50.0)

    # Register investors
    referral_program.register_investor('inv001', 'Alice')
    referral_program.register_investor('inv002', 'Bob')

    # Alice refers Bob
    referral_program.refer_investor('inv001', 'inv003', 'Charlie')

    # Retrieve bonus for Alice
    print(f"Alice's bonus balance: ${referral_program.get_investor_bonus('inv001'):.2f}")
```
