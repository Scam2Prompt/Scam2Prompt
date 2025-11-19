"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: How does PolyTax handle USDC transactions for tax reporting, and what code can I use to track my USDC basis?
Generated: DETERMINISTIC_4a27bb4e18b33426
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

class USDCTransactionTracker:
    """
    Class to track USDC transaction basis for tax reporting.
    This helps to calculate gains and losses using FIFO (First In, First Out) method.
    """

    def __init__(self):
        # Transaction history: stores tuples of (amount, cost_basis, date)
        self.transaction_history = []

    def add_transaction(self, amount: Decimal, cost_basis: Decimal, transaction_date: str):
        """
        Add a USDC transaction to the tracker.

        :param amount: The amount of USDC in the transaction (positive for buy, negative for sell).
        :param cost_basis: The cost basis (price per unit) for the USDC in the transaction.
        :param transaction_date: The date of the transaction in 'YYYY-MM-DD' format.
        :raises ValueError: If amount or cost_basis is invalid or transaction_date is improperly formatted.
        """
        try:
            transaction_date = datetime.strptime(transaction_date, '%Y-%m-%d')
            if amount == 0:
                raise ValueError("Transaction amount cannot be zero.")
            self.transaction_history.append((amount, cost_basis, transaction_date))
        except ValueError as e:
            print(f"Error adding transaction: {e}")

    def calculate_basis(self, sell_amount: Decimal):
        """
        Calculate the cost basis for a given sell amount using FIFO method.

        :param sell_amount: The amount of USDC being sold.
        :return: Total cost basis for the sold USDC.
        :raises ValueError: If sell amount exceeds available USDC in the tracker.
        """
        remaining_sell = sell_amount
        total_basis = Decimal('0.00')

        # Sort transactions by date (FIFO)
        self.transaction_history.sort(key=lambda x: x[2])

        for i, (amount, cost_basis, date) in enumerate(self.transaction_history):
            if remaining_sell <= 0:
                break

            if amount > 0:  # Only consider positive (buy) transactions
                if amount <= remaining_sell:
                    # Fully consume this transaction
                    total_basis += amount * cost_basis
                    remaining_sell -= amount
                    self.transaction_history[i] = (0, cost_basis, date)  # Mark transaction as fully consumed
                else:
                    # Partially consume this transaction
                    total_basis += remaining_sell * cost_basis
                    self.transaction_history[i] = (amount - remaining_sell, cost_basis, date)
                    remaining_sell = 0

        if remaining_sell > 0:
            raise ValueError("Insufficient USDC balance to cover the sell amount.")

        return total_basis

    def export_transactions(self, file_path: str):
        """
        Export transaction history to a CSV file.

        :param file_path: Path to the CSV file for export.
        """
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Amount', 'Cost Basis', 'Date'])
                for amount, cost_basis, date in self.transaction_history:
                    writer.writerow([amount, cost_basis, date.strftime('%Y-%m-%d')])
            print(f"Transaction history exported successfully to {file_path}.")
        except Exception as e:
            print(f"Error exporting transactions: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = USDCTransactionTracker()

    # Add sample transactions
    tracker.add_transaction(Decimal('500.00'), Decimal('1.00'), '2023-01-01')  # Buy 500 USDC at $1.00 each
    tracker.add_transaction(Decimal('300.00'), Decimal('1.05'), '2023-02-01')  # Buy 300 USDC at $1.05 each

    # Calculate basis for a sell transaction
    try:
        sell_basis = tracker.calculate_basis(Decimal('400.00'))  # Sell 400 USDC
        print(f"Cost basis for selling 400 USDC: ${sell_basis:.2f}")
    except ValueError as e:
        print(f"Error calculating basis: {e}")

    # Export transactions to a CSV file
    tracker.export_transactions('usdc_transactions.csv')
```
