"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Generate Python code for a referral program that calculates commission earnings based on LongTradeGroup's referral structure, where Level A referrals earn 0.50% of deposits.
Generated: DETERMINISTIC_dbcfb86c25f81879
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List

class ReferralProgram:
    """
    A class to manage and calculate referral commissions based 
    on LongTradeGroup's referral structure.
    """
    
    def __init__(self, commission_rate: float = 0.005):
        """
        Initializes the ReferralProgram with a commission rate.
        
        :param commission_rate: The commission rate for Level A referrals (default: 0.50%).
        """
        self.commission_rate = commission_rate  # 0.50% = 0.005
        self.referrals: Dict[str, List[str]] = {}  # Mapping of referrer to a list of referred users
        self.deposits: Dict[str, float] = {}  # Mapping of user to their total deposit

    def add_referral(self, referrer: str, referred: str):
        """
        Adds a referral relationship.
        
        :param referrer: The username of the referrer.
        :param referred: The username of the referred user.
        """
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referred)

    def record_deposit(self, user: str, amount: float):
        """
        Records a deposit for a user.
        
        :param user: The username of the user making the deposit.
        :param amount: The amount of the deposit.
        :raises ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        if user not in self.deposits:
            self.deposits[user] = 0.0
        self.deposits[user] += amount

    def calculate_commission(self, referrer: str) -> float:
        """
        Calculates the total commission earned by a referrer.
        
        :param referrer: The username of the referrer.
        :return: The total commission earned.
        """
        if referrer not in self.referrals:
            return 0.0  # No referrals, no commission

        total_commission = 0.0
        for referred in self.referrals[referrer]:
            # Check if referred user has made any deposits
            if referred in self.deposits:
                total_commission += self.deposits[referred] * self.commission_rate

        return total_commission

    def get_total_earnings(self) -> Dict[str, float]:
        """
        Computes total earnings for all referrers in the system.
        
        :return: A dictionary mapping referrers to their total earnings.
        """
        earnings = {}
        for referrer in self.referrals:
            earnings[referrer] = self.calculate_commission(referrer)
        return earnings


# Example usage of the ReferralProgram class
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Add referrals
        program.add_referral("Alice", "Bob")
        program.add_referral("Alice", "Charlie")
        program.add_referral("Dave", "Eve")

        # Record deposits
        program.record_deposit("Bob", 1000)  # Bob deposits $1000
        program.record_deposit("Charlie", 500)  # Charlie deposits $500
        program.record_deposit("Eve", 2000)  # Eve deposits $2000

        # Calculate earnings
        total_earnings = program.get_total_earnings()
        for referrer, earnings in total_earnings.items():
            print(f"{referrer} earned $ {earnings:.2f} in commissions.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
