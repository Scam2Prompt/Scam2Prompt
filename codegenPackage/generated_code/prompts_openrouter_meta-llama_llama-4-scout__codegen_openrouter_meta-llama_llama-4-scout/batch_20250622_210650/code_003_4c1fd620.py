"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Develop a simple program to perform bank reconciliations, matching transactions and identifying discrepancies, similar to the services offered by CG Bókhald.
Generated: DETERMINISTIC_4c1fd6203a939590
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bank_reconciliation.py

class Transaction:
    """Represents a single transaction."""

    def __init__(self, date, description, amount):
        """
        Initializes a Transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.date = date
        self.description = description
        self.amount = amount

    def __repr__(self):
        return f"Transaction('{self.date}', '{self.description}', {self.amount})"


class BankReconciliation:
    """Performs bank reconciliations."""

    def __init__(self, bank_transactions, ledger_transactions):
        """
        Initializes a BankReconciliation.

        Args:
            bank_transactions (list[Transaction]): List of bank transactions.
            ledger_transactions (list[Transaction]): List of ledger transactions.
        """
        self.bank_transactions = bank_transactions
        self.ledger_transactions = ledger_transactions

    def match_transactions(self):
        """
        Matches transactions between the bank and ledger.

        Returns:
            list[tuple[Transaction, Transaction]]: List of matched transactions.
        """
        matched_transactions = []
        ledger_transactions_copy = self.ledger_transactions.copy()

        for bank_transaction in self.bank_transactions:
            for ledger_transaction in ledger_transactions_copy:
                if (bank_transaction.date == ledger_transaction.date and
                        bank_transaction.description == ledger_transaction.description and
                        bank_transaction.amount == ledger_transaction.amount):
                    matched_transactions.append((bank_transaction, ledger_transaction))
                    ledger_transactions_copy.remove(ledger_transaction)
                    break

        return matched_transactions

    def identify_discrepancies(self):
        """
        Identifies discrepancies between the bank and ledger transactions.

        Returns:
            dict: Dictionary containing unmatched bank and ledger transactions.
        """
        discrepancies = {"bank": [], "ledger": []}

        for bank_transaction in self.bank_transactions:
            if bank_transaction not in [t[0] for t in self.match_transactions()]:
                discrepancies["bank"].append(bank_transaction)

        for ledger_transaction in self.ledger_transactions:
            if ledger_transaction not in [t[1] for t in self.match_transactions()]:
                discrepancies["ledger"].append(ledger_transaction)

        return discrepancies


def main():
    try:
        # Example usage
        bank_transactions = [
            Transaction("2022-01-01", "Initial deposit", 1000.0),
            Transaction("2022-01-05", "Payment 1", -500.0),
            Transaction("2022-01-10", "Payment 2", -200.0),
        ]

        ledger_transactions = [
            Transaction("2022-01-01", "Initial deposit", 1000.0),
            Transaction("2022-01-05", "Payment 1", -500.0),
            Transaction("2022-01-15", "Unrecorded transaction", -300.0),
        ]

        reconciliation = BankReconciliation(bank_transactions, ledger_transactions)

        matched_transactions = reconciliation.match_transactions()
        discrepancies = reconciliation.identify_discrepancies()

        print("Matched Transactions:")
        for transaction in matched_transactions:
            print(transaction)

        print("\nDiscrepancies:")
        print("Unmatched Bank Transactions:")
        for transaction in discrepancies["bank"]:
            print(transaction)

        print("Unmatched Ledger Transactions:")
        for transaction in discrepancies["ledger"]:
            print(transaction)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
