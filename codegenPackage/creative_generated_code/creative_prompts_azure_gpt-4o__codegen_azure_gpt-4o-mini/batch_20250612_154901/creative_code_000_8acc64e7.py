"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write Python code to calculate cryptocurrency transaction fees on Coinbase, factoring in a 1.49% card payment fee and a 0.5% spread for a given transaction amount.
Generated: DETERMINISTIC_8acc64e7d99e828f
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoTransactionFeeCalculator:
    """
    A class to calculate cryptocurrency transaction fees on Coinbase.
    """

    def __init__(self, transaction_amount: float):
        """
        Initializes the calculator with the transaction amount.

        Args:
            transaction_amount (float): The amount for which the transaction fee is to be calculated.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be a non-negative value.")
        self.transaction_amount = transaction_amount
        self.card_payment_fee_rate = 0.0149  # 1.49% card payment fee
        self.spread_fee_rate = 0.005  # 0.5% spread

    def calculate_card_payment_fee(self) -> float:
        """
        Calculates the card payment fee based on the transaction amount.

        Returns:
            float: The card payment fee.
        """
        card_fee = self.transaction_amount * self.card_payment_fee_rate
        return card_fee

    def calculate_spread_fee(self) -> float:
        """
        Calculates the spread fee based on the transaction amount.

        Returns:
            float: The spread fee.
        """
        spread_fee = self.transaction_amount * self.spread_fee_rate
        return spread_fee

    def calculate_total_fee(self) -> float:
        """
        Calculates the total transaction fee, including both card payment and spread fees.

        Returns:
            float: The total transaction fee.
        """
        total_fee = self.calculate_card_payment_fee() + self.calculate_spread_fee()
        return total_fee

    def calculate_final_amount(self) -> float:
        """
        Calculates the final amount after deducting the total fees from the transaction amount.

        Returns:
            float: The final amount after fees.
        """
        total_fee = self.calculate_total_fee()
        final_amount = self.transaction_amount - total_fee
        return final_amount


if __name__ == "__main__":
    # Example usage:
    try:
        transaction_amount = float(input("Enter the transaction amount in USD: "))
        calculator = CryptoTransactionFeeCalculator(transaction_amount)
        
        print(f"Transaction Amount: ${transaction_amount:.2f}")
        print(f"Card Payment Fee: ${calculator.calculate_card_payment_fee():.2f}")
        print(f"Spread Fee: ${calculator.calculate_spread_fee():.2f}")
        print(f"Total Fee: ${calculator.calculate_total_fee():.2f}")
        print(f"Final Amount After Fees: ${calculator.calculate_final_amount():.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
