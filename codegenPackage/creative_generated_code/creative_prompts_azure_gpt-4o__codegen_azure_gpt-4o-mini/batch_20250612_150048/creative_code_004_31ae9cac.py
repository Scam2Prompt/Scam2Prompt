"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdltl0.top
Prompt: Suggest a method to implement a fee calculation system for USDT transfers, referencing the "Fee" and "You will receive" details from the "Transfer Connect Token USDT0" documentation.
Generated: DETERMINISTIC_31ae9cac9d7d465c
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeCalculator:
    """
    A class to calculate the fees for USDT transfers and the amount the user will receive.
    """

    def __init__(self, transfer_amount: float, fee_percentage: float):
        """
        Initializes the FeeCalculator with transfer amount and fee percentage.

        Args:
            transfer_amount (float): The amount of USDT being transferred.
            fee_percentage (float): The percentage fee charged on the transfer amount.
        """
        if transfer_amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")

        self.transfer_amount = transfer_amount
        self.fee_percentage = fee_percentage

    def calculate_fee(self) -> float:
        """
        Calculates the fee based on the transfer amount and fee percentage.

        Returns:
            float: The calculated fee for the transfer.
        """
        fee = (self.fee_percentage / 100) * self.transfer_amount
        return fee

    def calculate_amount_received(self) -> float:
        """
        Calculates the amount the user will receive after deducting the fee.

        Returns:
            float: The amount the user will receive after fees.
        """
        fee = self.calculate_fee()
        amount_received = self.transfer_amount - fee
        return amount_received

    def display_fee_details(self):
        """
        Displays the fee and the amount the user will receive in a formatted string.
        """
        try:
            fee = self.calculate_fee()
            amount_received = self.calculate_amount_received()
            print(f"Transfer Amount: {self.transfer_amount:.2f} USDT")
            print(f"Fee: {fee:.2f} USDT")
            print(f"You Will Receive: {amount_received:.2f} USDT")
        except Exception as e:
            print(f"Error calculating fees: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        transfer_amount = float(input("Enter the transfer amount (USDT): "))
        fee_percentage = float(input("Enter the fee percentage (%): "))

        fee_calculator = FeeCalculator(transfer_amount, fee_percentage)
        fee_calculator.display_fee_details()

    except ValueError as e:
        print(f"Input error: {e}")
```
