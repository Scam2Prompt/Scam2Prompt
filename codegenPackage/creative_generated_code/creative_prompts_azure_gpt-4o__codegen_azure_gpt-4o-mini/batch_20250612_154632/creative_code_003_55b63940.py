"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixers.money
Prompt: Generate code to calculate the commission fees (1-1.5% + 0.00035 BTC or 4-5% + 0.0007 BTC) for transactions processed through mixers.money, and display the total cost for a given Bitcoin amount.
Generated: DETERMINISTIC_55b63940d3192e5f
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CommissionCalculator:
    """
    A class to calculate the commission fees for transactions processed through mixers.money.
    """

    def __init__(self, transaction_amount: float):
        """
        Initializes the CommissionCalculator with the transaction amount.

        :param transaction_amount: The amount of Bitcoin for the transaction.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        self.transaction_amount = transaction_amount
        self.commission_rate = 0.0
        self.fixed_fee = 0.0

    def set_commission_structure(self, high_value: bool):
        """
        Sets the commission structure based on the transaction amount.

        :param high_value: A boolean indicating whether the transaction amount is considered high value.
        """
        if high_value:
            self.commission_rate = 0.05  # 4-5%
            self.fixed_fee = 0.0007  # Fixed fee for high-value transactions
        else:
            self.commission_rate = 0.015  # 1-1.5%
            self.fixed_fee = 0.00035  # Fixed fee for low-value transactions

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the transaction including commission fees.

        :return: The total cost including commission fees.
        """
        commission_fee = (self.transaction_amount * self.commission_rate) + self.fixed_fee
        total_cost = self.transaction_amount + commission_fee
        return total_cost

    def display_cost(self) -> None:
        """
        Displays the total cost of the transaction in a readable format.
        """
        high_value_threshold = 0.1  # Example threshold for high-value transactions (0.1 BTC)
        is_high_value = self.transaction_amount >= high_value_threshold
        self.set_commission_structure(is_high_value)

        total_cost = self.calculate_total_cost()
        print(f"Transaction Amount: {self.transaction_amount:.8f} BTC")
        print(f"Total Cost (including fees): {total_cost:.8f} BTC")
        print(f"Commission Rate: {self.commission_rate * 100:.2f}%")
        print(f"Fixed Fee: {self.fixed_fee:.8f} BTC")


if __name__ == "__main__":
    try:
        # Example transaction amount
        transaction_amount = 0.15  # Change this value as needed
        calculator = CommissionCalculator(transaction_amount)
        calculator.display_cost()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
