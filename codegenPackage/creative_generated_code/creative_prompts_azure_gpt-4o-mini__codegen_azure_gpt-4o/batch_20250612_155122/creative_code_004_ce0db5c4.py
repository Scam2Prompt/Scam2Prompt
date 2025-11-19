"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Describe how to set up a referral system using Renzocash's affiliate marketing program and calculate commissions for new investors.
Generated: DETERMINISTIC_ce0db5c426cb43b0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral System using Renzocash's Affiliate Marketing Program

This script sets up a referral system and calculates commissions for new investors.
The program uses a simple data structure to track referrals and commission payouts.

Requirements:
- Python 3.8 or higher.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ReferralSystem:
    """
    Implements a referral system to manage affiliates and calculate commissions.
    """

    def __init__(self, commission_rate: float):
        """
        Initialize the ReferralSystem.

        :param commission_rate: Percentage commission rate (e.g., 0.10 for 10%)
        """
        self.commission_rate = commission_rate  # Commission percentage
        self.referrals = {}  # Dictionary to store referral data

    def add_referral(self, referrer: str, investor: str, investment_amount: float):
        """
        Add a new referral to the system.

        :param referrer: Affiliate who referred the investor.
        :param investor: Name of the new investor.
        :param investment_amount: Investment made by the investor.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        if referrer not in self.referrals:
            self.referrals[referrer] = []  # Create a new list for the referrer if not exists

        self.referrals[referrer].append({
            "investor": investor,
            "investment_amount": investment_amount,
            "commission": self.calculate_commission(investment_amount)
        })

        logging.info(f"Referral added: {referrer} referred {investor} with an investment of ${investment_amount}")

    def calculate_commission(self, investment_amount: float) -> float:
        """
        Calculate the commission for a given investment.

        :param investment_amount: Investment amount made by the investor.
        :return: Calculated commission.
        """
        return investment_amount * self.commission_rate

    def generate_report(self, referrer: str):
        """
        Generate a report for a specific referrer showing their referral history and total commissions.

        :param referrer: Affiliate whose report is being generated.
        """
        if referrer not in self.referrals:
            logging.warning(f"No referrals found for {referrer}")
            return []

        report = self.referrals[referrer]
        total_commission = sum(item["commission"] for item in report)

        logging.info(f"Report for {referrer}:")
        for entry in report:
            logging.info(f"Investor: {entry['investor']}, Investment: ${entry['investment_amount']}, Commission: ${entry['commission']:.2f}")

        logging.info(f"Total Commission Earned: ${total_commission:.2f}")
        return report, total_commission


# Example Usage
if __name__ == "__main__":
    try:
        # Create an instance of ReferralSystem with a 10% commission rate
        referral_system = ReferralSystem(commission_rate=0.10)

        # Add referrals
        referral_system.add_referral("Affiliate123", "InvestorA", 1000.00)
        referral_system.add_referral("Affiliate123", "InvestorB", 2000.00)
        referral_system.add_referral("Affiliate456", "InvestorC", 3000.00)

        # Generate reports
        referral_system.generate_report("Affiliate123")
        referral_system.generate_report("Affiliate456")
        referral_system.generate_report("NonExistentAffiliate")  # No referrals case

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
