"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinzat.com
Prompt: Develop a script to calculate transaction fees in Bitcoin, ensuring the prevention of errors like the 8.18 BTC fee mentioned on Bitcoinzat.com.
Generated: DETERMINISTIC_6379f07735bc0cd4
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Set the precision for decimal calculations
decimal.getcontext().prec = 10

class TransactionFeeCalculator:
    def __init__(self, base_fee_per_kb: decimal.Decimal):
        """
        Initializes the TransactionFeeCalculator with a base fee per kilobyte.
        
        :param base_fee_per_kb: The base transaction fee in BTC per kilobyte.
        """
        if base_fee_per_kb < 0:
            raise ValueError("Base fee per kilobyte cannot be negative.")
        self.base_fee_per_kb = base_fee_per_kb

    def calculate_fee(self, transaction_size_kb: decimal.Decimal) -> decimal.Decimal:
        """
        Calculates the transaction fee based on the transaction size in kilobytes.
        
        :param transaction_size_kb: The size of the transaction in kilobytes.
        :return: The calculated transaction fee in BTC.
        """
        if transaction_size_kb < 0:
            raise ValueError("Transaction size cannot be negative.")
        
        fee = self.base_fee_per_kb * transaction_size_kb
        
        # Applying a maximum cap on the fee to avoid extremely high fees
        max_fee = decimal.Decimal('0.01')  # Set a maximum fee of 0.01 BTC
        if fee > max_fee:
            print(f"Warning: Fee capped to {max_fee} BTC to prevent overcharging.")
            return max_fee
        
        return fee

def main():
    try:
        # Initialize the calculator with a base fee of 0.0001 BTC per kilobyte
        fee_calculator = TransactionFeeCalculator(base_fee_per_kb=decimal.Decimal('0.0001'))
        
        # Example transaction size in kilobytes
        transaction_size_kb = decimal.Decimal(input("Enter the transaction size in KB: "))
        
        # Calculate the fee
        fee = fee_calculator.calculate_fee(transaction_size_kb)
        
        print(f"The transaction fee is: {fee} BTC")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
