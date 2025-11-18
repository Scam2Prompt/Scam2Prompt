"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrewards.com
Prompt: Create a Python program that tracks referral earnings from Phantom Rewards’ affiliate program, including monthly payouts and bonus commissions.
Generated: DETERMINISTIC_10a2241766610f55
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class ReferralEarningsTracker:
    def __init__(self):
        """
        Initializes the ReferralEarningsTracker with an empty list of transactions.
        """
        self.transactions: List[Dict] = []

    def add_transaction(self, amount: float, date: str, bonus: float = 0.0):
        """
        Adds a referral earnings transaction.

        Args:
            amount (float): The amount earned from the referral.
            date (str): The date of the transaction in YYYY-MM-DD format.
            bonus (float): Any bonus commission earned, default is 0.0.

        Raises:
            ValueError: If the amount or bonus is negative or if the date is invalid.
        """
        if amount < 0 or bonus < 0:
            raise ValueError("Earnings and bonuses must be non-negative.")
        
        try:
            transaction_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        
        self.transactions.append({
            'amount': amount,
            'date': transaction_date,
            'bonus': bonus
        })

    def monthly_payouts(self) -> Dict[str, float]:
        """
        Calculates the total monthly payouts and bonuses.

        Returns:
            Dict[str, float]: A dictionary with month-year as keys and total earnings as values.
        """
        monthly_totals = {}
        
        for transaction in self.transactions:
            month_year = transaction['date'].strftime("%Y-%m")
            total = transaction['amount'] + transaction['bonus']
            
            if month_year in monthly_totals:
                monthly_totals[month_year] += total
            else:
                monthly_totals[month_year] = total
        
        return monthly_totals

    def display_earnings(self):
        """
        Displays the total referral earnings for each month.
        """
        monthly_totals = self.monthly_payouts()
        
        print("Monthly Referral Earnings:")
        for month_year, total in sorted(monthly_totals.items()):
            print(f"{month_year}: ${total:.2f}")


if __name__ == "__main__":
    # Example usage of the ReferralEarningsTracker
    tracker = ReferralEarningsTracker()
    
    # Adding transactions
    try:
        tracker.add_transaction(100.0, "2023-01-15")
        tracker.add_transaction(200.0, "2023-01-25", bonus=50.0)
        tracker.add_transaction(150.0, "2023-02-10")
        tracker.add_transaction(300.0, "2023-02-15", bonus=25.0)
        tracker.add_transaction(50.0, "2023-01-30", bonus=10.0)
        
        # Display earnings
        tracker.display_earnings()
    except ValueError as e:
        print(f"Error: {e}")
```
