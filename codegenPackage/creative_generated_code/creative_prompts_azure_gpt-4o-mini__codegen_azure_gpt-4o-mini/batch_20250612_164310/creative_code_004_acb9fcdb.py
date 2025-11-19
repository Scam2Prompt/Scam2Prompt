"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Implement a payment processing function that supports multiple installment options for beauty product purchases, reflecting the payment plans available on aquarelaesmalte.
Generated: DETERMINISTIC_acb9fcdb6664b21d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaymentProcessor:
    def __init__(self):
        # Supported installment plans
        self.installment_plans = {
            "1x": 1.0,    # Full payment
            "2x": 0.5,    # 50% in 2 installments
            "3x": 0.33,   # 33% in 3 installments
            "4x": 0.25,   # 25% in 4 installments
            "6x": 0.1667, # 16.67% in 6 installments
            "12x": 0.0833 # 8.33% in 12 installments
        }

    def process_payment(self, total_amount: float, installment_option: str) -> Union[str, Dict[str, float]]:
        """
        Process a payment based on the total amount and selected installment option.

        :param total_amount: Total amount to be paid for the beauty product.
        :param installment_option: Selected installment option (e.g., '1x', '2x', '3x', etc.).
        :return: A confirmation message or a dictionary with installment details.
        """
        try:
            if total_amount <= 0:
                raise ValueError("Total amount must be greater than zero.")

            if installment_option not in self.installment_plans:
                raise ValueError(f"Invalid installment option: {installment_option}. Supported options: {list(self.installment_plans.keys())}")

            # Calculate installment amount
            num_installments = int(installment_option[0])  # Extract the number of installments
            installment_amount = total_amount * self.installment_plans[installment_option]

            logging.info(f"Processing payment for {total_amount} with {installment_option} option.")
            installments = {
                "total_amount": total_amount,
                "installment_option": installment_option,
                "installment_amount": round(installment_amount, 2),
                "number_of_installments": num_installments,
            }

            return installments

        except ValueError as ve:
            logging.error(f"Value error occurred: {ve}")
            return str(ve)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred while processing the payment."

# Example usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    result = processor.process_payment(100.0, '3x')
    print(result)
```
