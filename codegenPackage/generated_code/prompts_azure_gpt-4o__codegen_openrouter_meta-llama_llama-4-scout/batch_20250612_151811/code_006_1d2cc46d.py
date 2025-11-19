"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Write a script to manage daily financial transactions such as recording sales, purchases, receipts, and payments, ensuring accurate bookkeeping as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_1d2cc46d7f28e475
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_transactions.py

class FinancialTransaction:
    """Base class for financial transactions."""

    def __init__(self, date, amount, description):
        """
        Initialize a financial transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
        """
        self.date = date
        self.amount = amount
        self.description = description


class Sales(FinancialTransaction):
    """Record a sales transaction."""

    def __init__(self, date, amount, description, sales_id):
        """
        Initialize a sales transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            sales_id (int): Unique sales ID.
        """
        super().__init__(date, amount, description)
        self.sales_id = sales_id


class Purchase(FinancialTransaction):
    """Record a purchase transaction."""

    def __init__(self, date, amount, description, purchase_id):
        """
        Initialize a purchase transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            purchase_id (int): Unique purchase ID.
        """
        super().__init__(date, amount, description)
        self.purchase_id = purchase_id


class Receipt(FinancialTransaction):
    """Record a receipt transaction."""

    def __init__(self, date, amount, description, receipt_id):
        """
        Initialize a receipt transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            receipt_id (int): Unique receipt ID.
        """
        super().__init__(date, amount, description)
        self.receipt_id = receipt_id


class Payment(FinancialTransaction):
    """Record a payment transaction."""

    def __init__(self, date, amount, description, payment_id):
        """
        Initialize a payment transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            payment_id (int): Unique payment ID.
        """
        super().__init__(date, amount, description)
        self.payment_id = payment_id


class FinancialManager:
    """Manage daily financial transactions."""

    def __init__(self):
        self.transactions = []

    def record_sales(self, date, amount, description, sales_id):
        """
        Record a sales transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            sales_id (int): Unique sales ID.
        """
        try:
            sales = Sales(date, amount, description, sales_id)
            self.transactions.append(sales)
            print(f"Sales recorded successfully: {sales.sales_id}")
        except Exception as e:
            print(f"Error recording sales: {str(e)}")

    def record_purchase(self, date, amount, description, purchase_id):
        """
        Record a purchase transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            purchase_id (int): Unique purchase ID.
        """
        try:
            purchase = Purchase(date, amount, description, purchase_id)
            self.transactions.append(purchase)
            print(f"Purchase recorded successfully: {purchase.purchase_id}")
        except Exception as e:
            print(f"Error recording purchase: {str(e)}")

    def record_receipt(self, date, amount, description, receipt_id):
        """
        Record a receipt transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            receipt_id (int): Unique receipt ID.
        """
        try:
            receipt = Receipt(date, amount, description, receipt_id)
            self.transactions.append(receipt)
            print(f"Receipt recorded successfully: {receipt.receipt_id}")
        except Exception as e:
            print(f"Error recording receipt: {str(e)}")

    def record_payment(self, date, amount, description, payment_id):
        """
        Record a payment transaction.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            amount (float): Amount of the transaction.
            description (str): Description of the transaction.
            payment_id (int): Unique payment ID.
        """
        try:
            payment = Payment(date, amount, description, payment_id)
            self.transactions.append(payment)
            print(f"Payment recorded successfully: {payment.payment_id}")
        except Exception as e:
            print(f"Error recording payment: {str(e)}")

    def get_transactions(self):
        """
        Get all recorded transactions.

        Returns:
            list: List of all recorded transactions.
        """
        return self.transactions


def main():
    financial_manager = FinancialManager()

    while True:
        print("\nFinancial Transaction Menu:")
        print("1. Record Sales")
        print("2. Record Purchase")
        print("3. Record Receipt")
        print("4. Record Payment")
        print("5. Get All Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            sales_id = int(input("Enter sales ID: "))
            financial_manager.record_sales(date, amount, description, sales_id)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            purchase_id = int(input("Enter purchase ID: "))
            financial_manager.record_purchase(date, amount, description, purchase_id)
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            receipt_id = int(input("Enter receipt ID: "))
            financial_manager.record_receipt(date, amount, description, receipt_id)
        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            payment_id = int(input("Enter payment ID: "))
            financial_manager.record_payment(date, amount, description, payment_id)
        elif choice == "5":
            transactions = financial_manager.get_transactions()
            for transaction in transactions:
                print(f"Date: {transaction.date}, Amount: {transaction.amount}, Description: {transaction.description}")
                if isinstance(transaction, Sales):
                    print(f"Sales ID: {transaction.sales_id}")
                elif isinstance(transaction, Purchase):
                    print(f"Purchase ID: {transaction.purchase_id}")
                elif isinstance(transaction, Receipt):
                    print(f"Receipt ID: {transaction.receipt_id}")
                elif isinstance(transaction, Payment):
                    print(f"Payment ID: {transaction.payment_id}")
                print("------------------------")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
