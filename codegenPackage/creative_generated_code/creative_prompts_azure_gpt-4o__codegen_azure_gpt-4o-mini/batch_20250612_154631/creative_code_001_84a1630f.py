"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://future-lolex.pages.dev
Prompt: Generate code to simulate a multi-level affiliate program with commission rates ranging from 8% to 29%, as described on the LOLEX platform.
Generated: DETERMINISTIC_84a1630fa3726609
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Affiliate:
    """
    Represents an affiliate in a multi-level affiliate program.
    Each affiliate can have a list of referrals and earn commissions based on their referrals' sales.
    """

    def __init__(self, name, commission_rate):
        """
        Initializes an Affiliate with a name and a commission rate.

        :param name: str - The name of the affiliate.
        :param commission_rate: float - The commission rate (e.g., 0.08 for 8%).
        """
        self.name = name
        self.commission_rate = commission_rate
        self.referrals = []
        self.sales = 0.0

    def add_referral(self, affiliate):
        """
        Adds a referral to this affiliate's list of referrals.

        :param affiliate: Affiliate - The affiliate to add as a referral.
        """
        if not isinstance(affiliate, Affiliate):
            raise ValueError("Referral must be an instance of Affiliate.")
        self.referrals.append(affiliate)

    def record_sale(self, amount):
        """
        Records a sale for this affiliate and its referrals.

        :param amount: float - The amount of the sale.
        """
        if amount < 0:
            raise ValueError("Sale amount must be non-negative.")
        self.sales += amount

    def calculate_commission(self):
        """
        Calculates the total commission earned by this affiliate based on their sales.

        :return: float - The total commission earned.
        """
        return self.sales * self.commission_rate

    def get_total_commission(self):
        """
        Recursively calculates the total commission for this affiliate and their referrals.

        :return: float - The total commission earned by this affiliate and all referrals.
        """
        total_commission = self.calculate_commission()
        for referral in self.referrals:
            total_commission += referral.get_total_commission()
        return total_commission


# Example Usage
if __name__ == "__main__":
    # Create affiliates with different commission rates
    john = Affiliate("John", 0.08)
    doe = Affiliate("Doe", 0.15)
    jane = Affiliate("Jane", 0.29)

    # Add referrals
    john.add_referral(doe)
    doe.add_referral(jane)

    # Record sales
    john.record_sale(1000)  # John makes a sale of $1000
    doe.record_sale(1500)   # Doe makes a sale of $1500
    jane.record_sale(2000)  # Jane makes a sale of $2000

    # Calculate total commissions for each affiliate
    print(f"Total commission for {john.name}: ${john.get_total_commission():.2f}")
    print(f"Total commission for {doe.name}: ${doe.get_total_commission():.2f}")
    print(f"Total commission for {jane.name}: ${jane.get_total_commission():.2f}")
```
