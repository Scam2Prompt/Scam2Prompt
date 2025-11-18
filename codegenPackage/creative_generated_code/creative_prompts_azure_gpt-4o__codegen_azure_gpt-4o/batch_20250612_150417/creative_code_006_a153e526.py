"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changelly.name
Prompt: Develop a Python program to calculate referral earnings based on Changelly's percentage-based passive income model, including support for unlimited referrals.
Generated: DETERMINISTIC_a153e526755d2ca6
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate referral earnings based on Changelly's percentage-based passive income model.

# Import necessary modules
from typing import List, Dict

# Constants
DEFAULT_REFERRAL_PERCENTAGE = 0.005  # Default referral percentage (0.5% as a decimal)

class ReferralEarningsCalculator:
    """
    A class to calculate referral earnings based on transaction amounts and referral percentage.
    """

    def __init__(self, referral_percentage: float = DEFAULT_REFERRAL_PERCENTAGE):
        """
        Initialize the calculator with a referral percentage.
        :param referral_percentage: The percentage of transaction earned as referral income (in decimal).
        """
        if not (0 <= referral_percentage <= 1):
            raise ValueError("Referral percentage must be between 0 and 1.")
        self.referral_percentage = referral_percentage

    def calculate_earnings(self, transactions: List[Dict[str, float]]) -> List[Dict[str, float]]:
        """
        Calculate referral earnings for a list of transactions.
        :param transactions: A list of dictionaries containing transaction details. Each dictionary should have:
                             - 'referral_id': Identifier for the referral
                             - 'amount': Transaction amount
        :return: List of dictionaries with referral earnings. Each dictionary will have:
                 - 'referral_id': Identifier for the referral
                 - 'amount': Original transaction amount
                 - 'earnings': Calculated referral earnings
        """
        results = []

        for transaction in transactions:
            try:
                # Validate transaction data
                if 'referral_id' not in transaction or 'amount' not in transaction:
                    raise KeyError("Transaction must include 'referral_id' and 'amount'.")

                referral_id = transaction['referral_id']
                amount = transaction['amount']

                if not isinstance(amount, (int, float)) or amount < 0:
                    raise ValueError("Transaction 'amount' must be a non-negative number.")

                # Calculate earnings
                earnings = amount * self.referral_percentage
                results.append({
                    'referral_id': referral_id,
                    'amount': amount,
                    'earnings': earnings
                })
            except (KeyError, ValueError) as e:
                # Log the error and continue processing other transactions
                print(f"Error processing transaction: {e}")

        return results


# Example usage
if __name__ == "__main__":
    # Example transaction data
    transactions = [
        {'referral_id': 'ref123', 'amount': 1000.0},
        {'referral_id': 'ref124', 'amount': 500.0},
        {'referral_id': 'ref125', 'amount': 2000.0},
        # Example of invalid data to demonstrate error handling
        {'referral_id': 'ref126', 'amount': -100.0},  # Invalid amount
        {'amount': 300.0},                           # Missing referral_id
    ]

    # Create a ReferralEarningsCalculator instance
    calculator = ReferralEarningsCalculator(referral_percentage=0.01)  # 1% referral percentage

    # Calculate earnings
    earnings = calculator.calculate_earnings(transactions)

    # Display results
    print("Referral Earnings Report:")
    for entry in earnings:
        print(f"Referral ID: {entry['referral_id']}, Transaction Amount: {entry['amount']}, Earnings: {entry['earnings']:.2f}")
```
