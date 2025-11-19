"""
Generated Code Metadata:
========================
Original URL: https://wealthfuned.com
Prompt: Generate code to simulate Wealthfuned.com's referral program, calculating the 5% commission for partners based on the deposit amounts they attract.
Generated: DETERMINISTIC_a741e955e1ab6d3e
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wealthfuned_referral_program.py

class Partner:
    """Represents a partner in the referral program."""

    def __init__(self, partner_id, name):
        """
        Initializes a Partner object.

        Args:
            partner_id (int): Unique identifier for the partner.
            name (str): Name of the partner.
        """
        self.partner_id = partner_id
        self.name = name
        self.referred_deposits = []

    def add_referred_deposit(self, deposit_amount):
        """
        Adds a referred deposit amount.

        Args:
            deposit_amount (float): The deposit amount referred by the partner.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.referred_deposits.append(deposit_amount)

    def calculate_commission(self, commission_rate=0.05):
        """
        Calculates the total commission earned by the partner.

        Args:
            commission_rate (float, optional): The commission rate. Defaults to 0.05 (5%).

        Returns:
            float: The total commission earned.
        """
        total_deposits = sum(self.referred_deposits)
        return total_deposits * commission_rate


class ReferralProgram:
    """Manages the referral program."""

    def __init__(self):
        self.partners = {}

    def add_partner(self, partner_id, name):
        """
        Adds a partner to the referral program.

        Args:
            partner_id (int): Unique identifier for the partner.
            name (str): Name of the partner.

        Raises:
            ValueError: If a partner with the same ID already exists.
        """
        if partner_id in self.partners:
            raise ValueError("Partner with the same ID already exists")
        self.partners[partner_id] = Partner(partner_id, name)

    def get_partner(self, partner_id):
        """
        Retrieves a partner by their ID.

        Args:
            partner_id (int): Unique identifier for the partner.

        Returns:
            Partner: The partner object, or None if not found.
        """
        return self.partners.get(partner_id)

    def add_referred_deposit(self, partner_id, deposit_amount):
        """
        Adds a referred deposit amount for a partner.

        Args:
            partner_id (int): Unique identifier for the partner.
            deposit_amount (float): The deposit amount referred by the partner.

        Raises:
            ValueError: If the partner is not found.
        """
        partner = self.get_partner(partner_id)
        if partner is None:
            raise ValueError("Partner not found")
        partner.add_referred_deposit(deposit_amount)

    def calculate_partner_commission(self, partner_id, commission_rate=0.05):
        """
        Calculates the commission earned by a partner.

        Args:
            partner_id (int): Unique identifier for the partner.
            commission_rate (float, optional): The commission rate. Defaults to 0.05 (5%).

        Returns:
            float: The commission earned by the partner.

        Raises:
            ValueError: If the partner is not found.
        """
        partner = self.get_partner(partner_id)
        if partner is None:
            raise ValueError("Partner not found")
        return partner.calculate_commission(commission_rate)


def main():
    # Example usage:
    referral_program = ReferralProgram()

    # Add partners
    referral_program.add_partner(1, "John Doe")
    referral_program.add_partner(2, "Jane Smith")

    # Add referred deposits
    referral_program.add_referred_deposit(1, 1000.0)
    referral_program.add_referred_deposit(1, 500.0)
    referral_program.add_referred_deposit(2, 2000.0)

    # Calculate commissions
    commission_john = referral_program.calculate_partner_commission(1)
    commission_jane = referral_program.calculate_partner_commission(2)

    print(f"John Doe's commission: ${commission_john:.2f}")
    print(f"Jane Smith's commission: ${commission_jane:.2f}")


if __name__ == "__main__":
    main()
```
