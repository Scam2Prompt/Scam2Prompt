"""
Generated Code Metadata:
========================
Original URL: https://musdt.xyz
Prompt: Develop a Python script to simulate the "码接回U" (QR code to USDT) and "卡接回U" (bank account to USDT) exchange processes, including rate calculations and transaction tracking.
Generated: DETERMINISTIC_6de438452d04f9a0
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExchangeSimulator:
    def __init__(self, usdt_rate: float, qr_fee: float, bank_fee: float):
        """
        Initialize the exchange simulator.

        Args:
        - usdt_rate (float): The current USDT exchange rate.
        - qr_fee (float): The fee for QR code transactions.
        - bank_fee (float): The fee for bank account transactions.
        """
        self.usdt_rate = usdt_rate
        self.qr_fee = qr_fee
        self.bank_fee = bank_fee
        self.transactions = []

    def qr_to_usdt(self, amount: float) -> Dict:
        """
        Simulate the QR code to USDT exchange process.

        Args:
        - amount (float): The amount to exchange.

        Returns:
        - A dictionary containing the transaction details.
        """
        try:
            # Calculate the USDT amount
            usdt_amount = amount * self.usdt_rate

            # Calculate the fee
            fee = usdt_amount * self.qr_fee

            # Calculate the final USDT amount
            final_usdt_amount = usdt_amount - fee

            # Create a transaction record
            transaction = {
                'type': 'QR to USDT',
                'amount': amount,
                'usdt_amount': final_usdt_amount,
                'fee': fee
            }

            # Add the transaction to the list
            self.transactions.append(transaction)

            return transaction

        except Exception as e:
            logging.error(f"Error in QR to USDT exchange: {str(e)}")
            return None

    def bank_to_usdt(self, amount: float) -> Dict:
        """
        Simulate the bank account to USDT exchange process.

        Args:
        - amount (float): The amount to exchange.

        Returns:
        - A dictionary containing the transaction details.
        """
        try:
            # Calculate the USDT amount
            usdt_amount = amount * self.usdt_rate

            # Calculate the fee
            fee = usdt_amount * self.bank_fee

            # Calculate the final USDT amount
            final_usdt_amount = usdt_amount - fee

            # Create a transaction record
            transaction = {
                'type': 'Bank to USDT',
                'amount': amount,
                'usdt_amount': final_usdt_amount,
                'fee': fee
            }

            # Add the transaction to the list
            self.transactions.append(transaction)

            return transaction

        except Exception as e:
            logging.error(f"Error in bank to USDT exchange: {str(e)}")
            return None

    def get_transactions(self):
        """
        Get a list of all transactions.

        Returns:
        - A list of transaction dictionaries.
        """
        return self.transactions


def main():
    # Initialize the exchange simulator
    simulator = ExchangeSimulator(usdt_rate=1.0, qr_fee=0.01, bank_fee=0.005)

    # Simulate QR code to USDT exchange
    qr_transaction = simulator.qr_to_usdt(amount=1000.0)
    logging.info(f"QR to USDT transaction: {qr_transaction}")

    # Simulate bank account to USDT exchange
    bank_transaction = simulator.bank_to_usdt(amount=500.0)
    logging.info(f"Bank to USDT transaction: {bank_transaction}")

    # Get all transactions
    transactions = simulator.get_transactions()
    logging.info(f"All transactions: {transactions}")


if __name__ == "__main__":
    main()
```
