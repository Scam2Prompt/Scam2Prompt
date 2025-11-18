"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Create a program to calculate withdrawal limits and fees for an investment platform, adhering to the constraints mentioned by Brexphil Inc. (e.g., minimum withdrawal amount of $10).
Generated: DETERMINISTIC_a89919ae75e0d67d
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WithdrawalManager:
    """
    A class to manage withdrawal limits and fees for an investment platform.
    """

    def __init__(self, min_withdrawal_amount=10, transaction_fee_rate=0.02):
        """
        Initializes the WithdrawalManager with specified parameters.

        Args:
            min_withdrawal_amount (float): The minimum withdrawal amount allowed. Default is $10.
            transaction_fee_rate (float): The fee rate for processing withdrawals. Default is 2%.
        """
        self.min_withdrawal_amount = min_withdrawal_amount
        self.transaction_fee_rate = transaction_fee_rate

    def calculate_fee(self, withdrawal_amount):
        """
        Calculates the transaction fee based on the withdrawal amount.

        Args:
            withdrawal_amount (float): The amount to withdraw.

        Returns:
            float: The calculated transaction fee.
        """
        return withdrawal_amount * self.transaction_fee_rate

    def validate_withdrawal(self, withdrawal_amount):
        """
        Validates the withdrawal amount against the minimum requirement.

        Args:
            withdrawal_amount (float): The amount to validate.

        Raises:
            ValueError: If the withdrawal amount is less than the minimum withdrawal amount.
        """
        if withdrawal_amount < self.min_withdrawal_amount:
            raise ValueError(f"Withdrawal amount must be at least ${self.min_withdrawal_amount}.")

    def process_withdrawal(self, withdrawal_amount):
        """
        Processes a withdrawal by validating the amount and calculating the fee.

        Args:
            withdrawal_amount (float): The amount to withdraw.

        Returns:
            dict: A dictionary containing the details of the withdrawal, including the total amount, fee, and net amount.
        """
        # Validate the withdrawal amount
        self.validate_withdrawal(withdrawal_amount)

        # Calculate the transaction fee
        fee = self.calculate_fee(withdrawal_amount)
        
        # Calculate the net amount after fee deduction
        net_amount = withdrawal_amount - fee

        return {
            "withdrawal_amount": withdrawal_amount,
            "fee": fee,
            "net_amount": net_amount
        }


if __name__ == "__main__":
    # Example usage of the WithdrawalManager class
    withdrawal_manager = WithdrawalManager()

    try:
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        result = withdrawal_manager.process_withdrawal(withdrawal_amount)

        print("Withdrawal Successful!")
        print(f"Withdrawal Amount: ${result['withdrawal_amount']:.2f}")
        print(f"Transaction Fee: ${result['fee']:.2f}")
        print(f"Net Amount after Fee: ${result['net_amount']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
