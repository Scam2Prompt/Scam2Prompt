"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gass-fee.pages.dev
Prompt: What are the criteria for deducting gas fees as business expenses for NFT creators and crypto traders?
Generated: DETERMINISTIC_02ba7d8b4ec4fa87
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script: DeductGasFees.py
Description: This script provides criteria for deducting gas fees as business expenses 
for NFT creators and crypto traders. It calculates whether gas fees are eligible for 
deduction based on the nature of the transaction and the business purpose.

Note: This script is simplified and does not constitute legal or tax advice. 
Consult a tax professional for specific guidance.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class GasFeeDeduction:
    """
    A class to evaluate whether gas fees can be deducted as business expenses.
    """

    def __init__(self, transaction_type: str, is_business_related: bool, gas_fee: float):
        """
        Initialize the GasFeeDeduction with transaction details.
        :param transaction_type: Type of transaction (e.g., 'NFT creation', 'trade', 'transfer').
        :param is_business_related: Whether the transaction is business-related (True/False).
        :param gas_fee: The amount of gas fee incurred (float).
        """
        self.transaction_type = transaction_type
        self.is_business_related = is_business_related
        self.gas_fee = gas_fee

    def is_deductible(self) -> bool:
        """
        Check if the transaction meets criteria for gas fee deduction.
        :return: True if deductible, False otherwise.
        """
        # Criteria for deduction
        if not self.is_business_related:
            logging.warning("Transaction is not business-related. Gas fees are not deductible.")
            return False

        eligible_transaction_types = {"NFT creation", "crypto trading", "staking", "smart contract execution"}
        if self.transaction_type not in eligible_transaction_types:
            logging.warning(f"Transaction type '{self.transaction_type}' is not eligible for deduction.")
            return False

        if self.gas_fee <= 0:
            logging.warning("Invalid gas fee amount. Gas fees must be greater than zero.")
            return False

        logging.info("Gas fees meet all criteria for deduction.")
        return True

    def deduction_summary(self) -> str:
        """
        Return a summary of the deduction evaluation.
        :return: Summary message as a string.
        """
        if self.is_deductible():
            return f"Gas fees of {self.gas_fee} for '{self.transaction_type}' are deductible as business expenses."
        else:
            return f"Gas fees of {self.gas_fee} for '{self.transaction_type}' are NOT deductible as business expenses."


def main():
    """
    Main function to evaluate gas fee deductions.
    """
    try:
        # Example transaction details (these would typically be provided by the user)
        transaction_type = "NFT creation"
        is_business_related = True
        gas_fee = 25.0

        # Create a GasFeeDeduction instance
        deduction = GasFeeDeduction(transaction_type, is_business_related, gas_fee)

        # Evaluate and log deduction summary
        logging.info(deduction.deduction_summary())

    except Exception as e:
        logging.error(f"An error occurred while evaluating gas fee deductions: {e}")


if __name__ == "__main__":
    main()
```
