"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.tax
Prompt: What features does Sui Tax offer for managing cryptocurrency tax reporting?
Generated: DETERMINISTIC_346e9c161e7d25ea
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sui_tax_features.py

class SuiTax:
    """
    SuiTax class provides features for managing cryptocurrency tax reporting.
    """

    def __init__(self):
        """
        Initializes a SuiTax instance with an empty list for transactions.
        """
        self.transactions = []  # Stores cryptocurrency transactions

    def add_transaction(self, date, transaction_type, amount, currency, price_per_unit, fee):
        """
        Adds a cryptocurrency transaction to the record.

        Args:
            date (str): The date of the transaction in 'YYYY-MM-DD' format.
            transaction_type (str): Type of transaction ('buy', 'sell', 'transfer').
            amount (float): Amount of cryptocurrency involved in the transaction.
            currency (str): Type of cryptocurrency (e.g., 'BTC', 'ETH').
            price_per_unit (float): Price per unit of the cryptocurrency.
            fee (float): Transaction fee.

        Raises:
            ValueError: If any of the inputs have invalid values.
        """
        if transaction_type not in ['buy', 'sell', 'transfer']:
            raise ValueError("Invalid transaction type. Must be 'buy', 'sell', or 'transfer'.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if price_per_unit < 0:
            raise ValueError("Price per unit cannot be negative.")
        if fee < 0:
            raise ValueError("Fee cannot be negative.")

        transaction = {
            "date": date,
            "type": transaction_type,
            "amount": amount,
            "currency": currency,
            "price_per_unit": price_per_unit,
            "fee": fee
        }
        self.transactions.append(transaction)

    def calculate_taxable_gains(self):
        """
        Calculates taxable gains based on recorded transactions.

        Returns:
            float: The total taxable gains.
        """
        taxable_gains = 0.0
        for transaction in self.transactions:
            if transaction["type"] == "sell":
                taxable_gains += (transaction["amount"] * transaction["price_per_unit"]) - transaction["fee"]
        return taxable_gains

    def generate_tax_report(self):
        """
        Generates a tax report based on recorded transactions.

        Returns:
            dict: A summary of the tax report including total transactions and taxable gains.
        """
        report = {
            "total_transactions": len(self.transactions),
            "taxable_gains": self.calculate_taxable_gains(),
            "transactions": self.transactions
        }
        return report

    def save_report_to_file(self, filename):
        """
        Saves the tax report to a file in JSON format.

        Args:
            filename (str): The name of the file to save the report.

        Raises:
            IOError: If there is an issue with file writing.
        """
        import json
        report = self.generate_tax_report()
        try:
            with open(filename, 'w') as file:
                json.dump(report, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving report to file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize SuiTax
        sui_tax = SuiTax()

        # Add transactions
        sui_tax.add_transaction("2023-01-01", "buy", 0.5, "BTC", 30000, 10)
        sui_tax.add_transaction("2023-02-15", "sell", 0.2, "BTC", 32000, 5)
        sui_tax.add_transaction("2023-03-10", "transfer", 0.1, "ETH", 1500, 2)

        # Generate tax report
        report = sui_tax.generate_tax_report()
        print("Tax Report:")
        print(report)

        # Save report to file
        sui_tax.save_report_to_file("tax_report.json")
        print("Tax report saved successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
