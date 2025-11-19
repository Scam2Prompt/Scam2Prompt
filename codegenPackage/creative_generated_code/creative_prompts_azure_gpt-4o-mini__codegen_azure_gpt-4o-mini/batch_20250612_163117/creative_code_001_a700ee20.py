"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link.sxdev.io
Prompt: Write a Python function that calculates the cashback earned from transactions made with the NAGA Pay card, considering different account plans.
Generated: DETERMINISTIC_a700ee2026267891
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackCalculator:
    """Class to calculate cashback earned from transactions with NAGA Pay card."""

    def __init__(self, account_plan: str):
        """
        Initializes the CashbackCalculator with a specified account plan.

        Args:
            account_plan (str): The account plan type (e.g., 'basic', 'premium', 'vip').
        """
        self.account_plan = account_plan.lower()
        self.cashback_rates = {
            'basic': 0.01,  # 1% cashback for basic plan
            'premium': 0.02,  # 2% cashback for premium plan
            'vip': 0.03  # 3% cashback for VIP plan
        }

    def validate_account_plan(self):
        """Validates the account plan to ensure it is recognized."""
        if self.account_plan not in self.cashback_rates:
            raise ValueError(f"Invalid account plan: {self.account_plan}. "
                             "Must be one of: 'basic', 'premium', 'vip'.")

    def calculate_cashback(self, transaction_amount: float) -> float:
        """
        Calculates the cashback earned from a transaction.

        Args:
            transaction_amount (float): The amount of the transaction.

        Returns:
            float: The cashback amount earned.

        Raises:
            ValueError: If the transaction amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")

        self.validate_account_plan()
        
        cashback_rate = self.cashback_rates[self.account_plan]
        cashback_earned = transaction_amount * cashback_rate
        return cashback_earned

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the CashbackCalculator with the desired account plan
        calculator = CashbackCalculator(account_plan='premium')
        
        # Calculate cashback for a given transaction amount
        transaction = 100.00  # Example transaction amount
        cashback = calculator.calculate_cashback(transaction)
        
        print(f"Cashback earned for a transaction of ${transaction}: ${cashback:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
