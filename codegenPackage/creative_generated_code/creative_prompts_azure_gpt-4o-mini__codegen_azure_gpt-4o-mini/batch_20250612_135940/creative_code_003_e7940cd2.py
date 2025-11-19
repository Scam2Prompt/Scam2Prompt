"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Generate a sample code to handle the charging of '단골머니' in a prepayment discount application.
Generated: DETERMINISTIC_e7940cd2af2d1aed
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrepaymentDiscountApplication:
    """
    A class to manage the charging of '단골머니' (loyalty money) 
    in a prepayment discount application.
    """

    def __init__(self):
        self.balance = 0.0  # Initialize balance to 0

    def charge_loyalty_money(self, amount: float) -> None:
        """
        Charge an amount to the loyalty money balance.

        :param amount: The amount to charge (must be positive)
        :raises ValueError: If the amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive value.")
        
        self.balance += amount
        print(f"Charged {amount:.2f} to loyalty money. New balance: {self.balance:.2f}")

    def get_balance(self) -> float:
        """
        Retrieve the current balance of loyalty money.

        :return: The current balance
        """
        return self.balance

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Apply a discount based on the current loyalty money balance.

        :param discount_percentage: The percentage discount to apply (0 to 100)
        :raises ValueError: If the discount percentage is out of valid range
        :return: The discount amount
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        discount_amount = (discount_percentage / 100) * self.balance
        print(f"Applying a discount of {discount_percentage}%: {discount_amount:.2f}")
        return discount_amount

    def reset_balance(self) -> None:
        """
        Resets the loyalty money balance to zero.
        """
        self.balance = 0.0
        print("Loyalty money balance has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        app = PrepaymentDiscountApplication()
        app.charge_loyalty_money(100.0)  # Charge loyalty money
        print(f"Current balance: {app.get_balance():.2f}")

        discount = app.apply_discount(10)  # Apply a 10% discount
        print(f"Discount applied: {discount:.2f}")

        app.reset_balance()  # Reset the balance
    except ValueError as e:
        print(f"Error: {e}")
```
