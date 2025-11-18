"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto4rex360.com
Prompt: Generate a Python script to simulate the referral program earnings described on Crypto 4Rex 360, based on user referrals and their respective investment amounts.
Generated: DETERMINISTIC_43f60e16bfd1907d
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys


class ReferralProgram:
    """
    A class to simulate the referral program earnings on Crypto 4Rex 360.
    """

    def __init__(self):
        """
        Initializes the ReferralProgram with an empty dictionary to store user referrals and investments.
        """
        self.referrals = {}  # Dictionary to store referral data

    def add_referral(self, referrer, referee, investment):
        """
        Adds a referral relationship and investment amount to the program.

        Args:
            referrer (str): The username of the referrer.
            referee (str): The username of the referee.
            investment (float): The investment amount of the referee.

        Returns:
            None
        """
        if investment < 0:
            raise ValueError("Investment amount must be non-negative")

        if referrer not in self.referrals:
            self.referrals[referrer] = []  # Initialize list of referees for the referrer

        self.referrals[referrer].append({"referee": referee, "investment": investment})

    def calculate_earnings(self, referrer):
        """
        Calculates the total earnings for a referrer based on their referees' investments.

        Args:
            referrer (str): The username of the referrer.

        Returns:
            float: Total earnings for the referrer.
        """
        if referrer not in self.referrals:
            return 0.0

        total_earnings = 0.0
        for referral in self.referrals[referrer]:
            investment = referral["investment"]
            total_earnings += investment * 0.1  # Earnings are 10% of the referee's investment

        return total_earnings

    def display_referrals(self):
        """
        Displays all referral relationships and their investments.

        Returns:
            None
        """
        if not self.referrals:
            print("No referrals found.")
            return

        print("Referral Data:")
        for referrer, referees in self.referrals.items():
            print(f"Referrer: {referrer}")
            for referral in referees:
                print(f"  Referee: {referral['referee']}, Investment: ${referral['investment']:.2f}")
            print()

    def display_earnings(self):
        """
        Displays the earnings for each referrer.

        Returns:
            None
        """
        if not self.referrals:
            print("No referrals found.")
            return

        print("Earnings Data:")
        for referrer in self.referrals:
            earnings = self.calculate_earnings(referrer)
            print(f"Referrer: {referrer}, Total Earnings: ${earnings:.2f}")
        print()


def main():
    """
    Main function to simulate the referral program.
    """
    referral_program = ReferralProgram()

    try:
        # Sample data
        referral_program.add_referral("Alice", "Bob", 1000.0)
        referral_program.add_referral("Alice", "Charlie", 2000.0)
        referral_program.add_referral("Alice", "David", 1500.0)

        referral_program.add_referral("Eve", "Frank", 800.0)
        referral_program.add_referral("Eve", "Grace", 1200.0)

        # Display referral relationships
        referral_program.display_referrals()

        # Display earnings for each referrer
        referral_program.display_earnings()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
