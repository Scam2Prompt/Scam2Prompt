"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financial-justice.com
Prompt: Generate code to simulate a Ponzi scheme structure for educational purposes, based on the explanation of cryptocurrency pyramid schemes from Financial Justice.
Generated: DETERMINISTIC_c57ba7a9e49287d4
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ponzi Scheme Simulation using Python
This script demonstrates the structure of a Ponzi scheme for educational purposes only.
It simulates how new investors fund payouts of earlier investors in a pyramid-like structure.
This is purely for understanding and does not endorse or promote unethical practices.
"""

import sys

class Investor:
    """
    Represents an investor in the Ponzi scheme.
    Each investor contributes an amount and expects returns based on promised gains.
    """
    def __init__(self, name, contribution):
        self.name = name
        self.contribution = contribution
        self.expected_return = contribution * 1.5  # Example: 50% promised return
        self.payout = 0

    def receive_payout(self, amount):
        """
        Pays the investor an amount. Tracks total payout to detect under/overpayment.
        """
        self.payout += amount

    def is_fully_paid(self):
        """
        Checks if the investor has received their full promised return.
        """
        return self.payout >= self.expected_return

class PonziScheme:
    """
    Represents the Ponzi scheme.
    Tracks investors and simulates the flow of funds.
    """
    def __init__(self):
        self.investors = []  # List of all investors in the scheme
        self.funds = 0       # Total funds in the scheme

    def add_investor(self, name, contribution):
        """
        Adds a new investor to the scheme and updates funds.
        """
        if contribution <= 0:
            raise ValueError("Contribution must be greater than zero.")
        
        self.funds += contribution
        new_investor = Investor(name, contribution)
        self.investors.append(new_investor)
        return new_investor

    def payout_early_investors(self):
        """
        Pays early investors using funds contributed by newer investors.
        """
        for investor in self.investors:
            if not investor.is_fully_paid() and self.funds > 0:
                payout_amount = min(investor.expected_return - investor.payout, self.funds)
                investor.receive_payout(payout_amount)
                self.funds -= payout_amount

    def display_status(self):
        """
        Displays current status of the Ponzi scheme.
        """
        print("\nPonzi Scheme Status:")
        print(f"Total Funds: ${self.funds:.2f}")
        for investor in self.investors:
            print(f"- {investor.name}: Contributed ${investor.contribution:.2f}, "
                  f"Received ${investor.payout:.2f}, "
                  f"Expected ${investor.expected_return:.2f}, "
                  f"{'Fully Paid' if investor.is_fully_paid() else 'Not Fully Paid'}")

def main():
    """
    Main function to simulate the Ponzi scheme.
    """
    try:
        scheme = PonziScheme()

        # Add initial investors
        scheme.add_investor("Alice", 1000)
        scheme.add_investor("Bob", 500)
        
        # Simulate new investors joining and early investors getting paid
        scheme.display_status()
        print("\nAdding new investors...\n")
        scheme.add_investor("Charlie", 2000)
        scheme.add_investor("Dave", 1500)
        
        scheme.payout_early_investors()
        scheme.display_status()
        
        # Add more investors and attempt more payouts
        print("\nAdding more investors...\n")
        scheme.add_investor("Eve", 3000)
        scheme.payout_early_investors()
        scheme.display_status()
        
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
