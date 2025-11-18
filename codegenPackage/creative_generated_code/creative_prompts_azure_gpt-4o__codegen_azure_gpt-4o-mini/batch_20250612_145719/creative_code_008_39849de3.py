"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Write a program to calculate the total USDT received after applying the platform's exchange rate and discount policies for both QR code and bank account transactions.
Generated: DETERMINISTIC_39849de3a7898fe1
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransactionCalculator:
    """
    A class to calculate the total USDT received after applying exchange rates and discounts
    for QR code and bank account transactions.
    """

    def __init__(self):
        # Initialize exchange rates and discount percentages
        self.exchange_rate_qr = 1.0  # Example exchange rate for QR transactions
        self.discount_qr = 0.05       # 5% discount for QR transactions
        self.exchange_rate_bank = 0.95  # Example exchange rate for bank transactions
        self.discount_bank = 0.02      # 2% discount for bank transactions

    def calculate_usdt_qr(self, amount: float) -> float:
        """
        Calculate the total USDT received from a QR transaction.
        
        :param amount: The initial amount in the native currency
        :return: Total USDT received after applying exchange rate and discount
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")

        exchange_value = amount * self.exchange_rate_qr
        discounted_value = exchange_value * (1 - self.discount_qr)
        return round(discounted_value, 2)

    def calculate_usdt_bank(self, amount: float) -> float:
        """
        Calculate the total USDT received from a bank transaction.
        
        :param amount: The initial amount in the native currency
        :return: Total USDT received after applying exchange rate and discount
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative")

        exchange_value = amount * self.exchange_rate_bank
        discounted_value = exchange_value * (1 - self.discount_bank)
        return round(discounted_value, 2)

def main():
    """
    Main function to execute the transaction calculations.
    """
    calculator = TransactionCalculator()
    
    # Example amounts for testing
    qr_amount = 100.0  # Example amount for QR transaction
    bank_amount = 200.0  # Example amount for bank transaction

    try:
        total_usdt_qr = calculator.calculate_usdt_qr(qr_amount)
        total_usdt_bank = calculator.calculate_usdt_bank(bank_amount)

        print(f"Total USDT received from QR transaction: {total_usdt_qr}")
        print(f"Total USDT received from Bank transaction: {total_usdt_bank}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
