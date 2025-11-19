"""
Generated Code Metadata:
========================
Original URL: https://musdt.xyz
Prompt: Write a program to calculate the total USDT received after applying the platform's exchange rate and discount policies for both QR code and bank account transactions.
Generated: DETERMINISTIC_39849de3a7898fe1
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# usdt_calculator.py

class Transaction:
    def __init__(self, amount, transaction_type):
        """
        Initialize a Transaction object.

        Args:
        - amount (float): The transaction amount.
        - transaction_type (str): The type of transaction ('qr_code' or 'bank_account').
        """
        self.amount = amount
        self.transaction_type = transaction_type

class ExchangeRate:
    def __init__(self, rate):
        """
        Initialize an ExchangeRate object.

        Args:
        - rate (float): The exchange rate.
        """
        self.rate = rate

class DiscountPolicy:
    def __init__(self, discount_percentage):
        """
        Initialize a DiscountPolicy object.

        Args:
        - discount_percentage (float): The discount percentage.
        """
        self.discount_percentage = discount_percentage

class USDTCalculator:
    def __init__(self, exchange_rate, qr_code_discount_policy, bank_account_discount_policy):
        """
        Initialize a USDTCalculator object.

        Args:
        - exchange_rate (ExchangeRate): The exchange rate.
        - qr_code_discount_policy (DiscountPolicy): The discount policy for QR code transactions.
        - bank_account_discount_policy (DiscountPolicy): The discount policy for bank account transactions.
        """
        self.exchange_rate = exchange_rate
        self.qr_code_discount_policy = qr_code_discount_policy
        self.bank_account_discount_policy = bank_account_discount_policy

    def calculate_usdt(self, transaction):
        """
        Calculate the total USDT received after applying the platform's exchange rate and discount policies.

        Args:
        - transaction (Transaction): The transaction.

        Returns:
        - float: The total USDT received.

        Raises:
        - ValueError: If the transaction type is invalid.
        """
        if transaction.transaction_type not in ['qr_code', 'bank_account']:
            raise ValueError("Invalid transaction type")

        # Apply exchange rate
        usdt_before_discount = transaction.amount * self.exchange_rate.rate

        # Apply discount policy
        if transaction.transaction_type == 'qr_code':
            discount_policy = self.qr_code_discount_policy
        else:
            discount_policy = self.bank_account_discount_policy

        discount_amount = usdt_before_discount * (discount_policy.discount_percentage / 100)
        usdt_after_discount = usdt_before_discount - discount_amount

        return usdt_after_discount

def main():
    try:
        # Define exchange rate
        exchange_rate = ExchangeRate(0.95)

        # Define discount policies
        qr_code_discount_policy = DiscountPolicy(5)
        bank_account_discount_policy = DiscountPolicy(3)

        # Create USDT calculator
        usdt_calculator = USDTCalculator(exchange_rate, qr_code_discount_policy, bank_account_discount_policy)

        # Create transactions
        qr_code_transaction = Transaction(1000, 'qr_code')
        bank_account_transaction = Transaction(500, 'bank_account')

        # Calculate USDT
        qr_code_usdt = usdt_calculator.calculate_usdt(qr_code_transaction)
        bank_account_usdt = usdt_calculator.calculate_usdt(bank_account_transaction)

        print(f"USDT received for QR code transaction: {qr_code_usdt:.2f}")
        print(f"USDT received for bank account transaction: {bank_account_usdt:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
