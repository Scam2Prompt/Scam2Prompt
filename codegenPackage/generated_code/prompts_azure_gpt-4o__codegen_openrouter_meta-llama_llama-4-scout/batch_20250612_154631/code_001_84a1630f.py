"""
Generated Code Metadata:
========================
Original URL: https://future-lolex.pages.dev
Prompt: Generate code to simulate a multi-level affiliate program with commission rates ranging from 8% to 29%, as described on the LOLEX platform.
Generated: DETERMINISTIC_84a1630fa3726609
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_program.py

class Affiliate:
    def __init__(self, name, level):
        """
        Initialize an Affiliate object.

        Args:
        - name (str): Affiliate name
        - level (int): Affiliate level (1-5)
        """
        self.name = name
        self.level = level
        self.commission_rate = self.get_commission_rate()
        self.downline = []

    def get_commission_rate(self):
        """
        Get commission rate based on affiliate level.

        Returns:
        - float: Commission rate
        """
        commission_rates = {
            1: 0.08,  # 8%
            2: 0.10,  # 10%
            3: 0.12,  # 12%
            4: 0.20,  # 20%
            5: 0.29   # 29%
        }
        return commission_rates.get(self.level, 0.0)

    def add_downline(self, affiliate):
        """
        Add affiliate to downline.

        Args:
        - affiliate (Affiliate): Affiliate object
        """
        self.downline.append(affiliate)

    def calculate_commission(self, sale_amount):
        """
        Calculate commission for a sale.

        Args:
        - sale_amount (float): Sale amount

        Returns:
        - float: Commission amount
        """
        return sale_amount * self.commission_rate


class AffiliateProgram:
    def __init__(self):
        """
        Initialize an AffiliateProgram object.
        """
        self.affiliates = {}

    def add_affiliate(self, affiliate):
        """
        Add affiliate to program.

        Args:
        - affiliate (Affiliate): Affiliate object
        """
        self.affiliates[affiliate.name] = affiliate

    def get_affiliate(self, name):
        """
        Get affiliate by name.

        Args:
        - name (str): Affiliate name

        Returns:
        - Affiliate: Affiliate object or None
        """
        return self.affiliates.get(name)

    def simulate_sale(self, affiliate_name, sale_amount):
        """
        Simulate a sale and calculate commissions.

        Args:
        - affiliate_name (str): Affiliate name
        - sale_amount (float): Sale amount

        Returns:
        - dict: Commissions for each affiliate
        """
        affiliate = self.get_affiliate(affiliate_name)
        if not affiliate:
            raise ValueError("Affiliate not found")

        commissions = {}
        current_affiliate = affiliate
        while current_affiliate:
            commission = current_affiliate.calculate_commission(sale_amount)
            commissions[current_affiliate.name] = commission
            current_affiliate = self.get_affiliate_parent(current_affiliate)

        return commissions

    def get_affiliate_parent(self, affiliate):
        """
        Get parent affiliate for a given affiliate.

        Args:
        - affiliate (Affiliate): Affiliate object

        Returns:
        - Affiliate: Parent affiliate or None
        """
        for a in self.affiliates.values():
            if affiliate in a.downline:
                return a
        return None


def main():
    program = AffiliateProgram()

    # Create affiliates
    affiliate1 = Affiliate("John", 1)
    affiliate2 = Affiliate("Jane", 2)
    affiliate3 = Affiliate("Bob", 3)

    # Add affiliates to program
    program.add_affiliate(affiliate1)
    program.add_affiliate(affiliate2)
    program.add_affiliate(affiliate3)

    # Set up downline
    affiliate1.add_downline(affiliate2)
    affiliate2.add_downline(affiliate3)

    # Simulate sale
    sale_amount = 100.0
    commissions = program.simulate_sale("Bob", sale_amount)

    # Print commissions
    for affiliate, commission in commissions.items():
        print(f"{affiliate}: ${commission:.2f}")


if __name__ == "__main__":
    main()
```
