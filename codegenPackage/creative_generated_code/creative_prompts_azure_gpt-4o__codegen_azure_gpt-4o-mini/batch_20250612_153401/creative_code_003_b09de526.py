"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbot-io.web.app
Prompt: Write a script to implement a referral system that calculates fees earned based on BONKbot's referral structure: 30% in the first month, 20% in the second month, and 10% thereafter.
Generated: DETERMINISTIC_b09de526b0f0fc61
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    def __init__(self):
        """Initialize the referral system with a fee structure."""
        self.fee_structure = {
            1: 0.30,  # 30% for the first month
            2: 0.20,  # 20% for the second month
            3: 0.10   # 10% for the third month and beyond
        }

    def calculate_fee(self, amount, month):
        """Calculate the referral fee based on the amount and month.

        Args:
            amount (float): The total amount for which the fee is to be calculated.
            month (int): The month number for which the fee is calculated.

        Returns:
            float: The calculated referral fee.

        Raises:
            ValueError: If the amount is negative or month is less than 1.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if month < 1:
            raise ValueError("Month must be greater than or equal to 1.")

        # Determine the fee percentage based on the month
        if month in self.fee_structure:
            fee_percentage = self.fee_structure[month]
        else:
            fee_percentage = self.fee_structure[3]  # 10% for months 3 and beyond

        # Calculate the fee
        fee = amount * fee_percentage
        return fee

    def get_total_fee(self, amount, months):
        """Calculate total referral fee over multiple months.

        Args:
            amount (float): The total amount for which the fee is calculated.
            months (list of int): List containing the month numbers.

        Returns:
            float: Total calculated referral fee over the specified months.
        """
        total_fee = 0.0
        for month in months:
            total_fee += self.calculate_fee(amount, month)
        return total_fee


if __name__ == "__main__":
    # Example usage of the ReferralSystem
    referral_system = ReferralSystem()

    try:
        amount = 1000.0  # Example amount
        months = [1, 2, 3, 4]  # Example months

        # Calculate total fees earned
        total_fees = referral_system.get_total_fee(amount, months)
        print(f"Total fees earned for amount ${amount} over months {months}: ${total_fees:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
