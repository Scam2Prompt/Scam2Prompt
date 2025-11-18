"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payapayments.com
Prompt: Generate a script to calculate merchant pricing models, including interchange and credit card fees, using Paya's resources.
Generated: DETERMINISTIC_6c3d694a28916407
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MerchantPricingCalculator:
    """
    A class to calculate merchant pricing models including interchange and credit card fees.
    """

    def __init__(self, base_rate, interchange_rate, per_transaction_fee):
        """
        Initialize the calculator with base rate, interchange rate, and transaction fee.

        :param base_rate: The base rate charged by the merchant (percentage, e.g., 0.02 for 2%)
        :param interchange_rate: The interchange rate (percentage, e.g., 0.015 for 1.5%)
        :param per_transaction_fee: Flat fee per transaction (e.g., $0.10)
        """
        self.base_rate = base_rate
        self.interchange_rate = interchange_rate
        self.per_transaction_fee = per_transaction_fee

    def calculate_fee(self, transaction_amount):
        """
        Calculate total fees for a given transaction amount.

        :param transaction_amount: The amount of the transaction (e.g., $100)
        :return: Total fee for the transaction
        """
        try:
            if transaction_amount <= 0:
                raise ValueError("Transaction amount must be greater than zero.")
            
            # Calculate the interchange fee
            interchange_fee = transaction_amount * self.interchange_rate
            
            # Calculate the base rate fee
            base_rate_fee = transaction_amount * self.base_rate
            
            # Calculate the total fee
            total_fee = interchange_fee + base_rate_fee + self.per_transaction_fee
            
            logging.info(f"Transaction Amount: ${transaction_amount:.2f}")
            logging.info(f"Interchange Fee: ${interchange_fee:.2f}")
            logging.info(f"Base Rate Fee: ${base_rate_fee:.2f}")
            logging.info(f"Per Transaction Fee: ${self.per_transaction_fee:.2f}")
            logging.info(f"Total Fee: ${total_fee:.2f}")
            
            return total_fee

        except Exception as e:
            logging.error(f"Error calculating fees: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Configure merchant pricing model with example rates
        base_rate = 0.02  # 2%
        interchange_rate = 0.015  # 1.5%
        per_transaction_fee = 0.10  # $0.10 per transaction

        calculator = MerchantPricingCalculator(base_rate, interchange_rate, per_transaction_fee)
        
        # Example transaction amount
        transaction_amount = 100.00  # $100 transaction
        
        # Calculate fees
        total_fee = calculator.calculate_fee(transaction_amount)
        print(f"Total Fee for ${transaction_amount:.2f} transaction: ${total_fee:.2f}")

    except Exception as e:
        logging.error(f"Failed to execute script: {e}")
```
