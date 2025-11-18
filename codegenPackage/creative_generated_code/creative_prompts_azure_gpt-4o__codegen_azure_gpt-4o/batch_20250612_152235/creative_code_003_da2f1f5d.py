"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://humanxpert.com
Prompt: Provide a Python script for tracking and collecting unpaid medical accounts receivable, inspired by Human Xpert's specialized services.
Generated: DETERMINISTIC_da2f1f5d74d25a51
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime


class MedicalAccountsReceivableTracker:
    """
    A class for tracking unpaid medical accounts receivable.
    """

    def __init__(self):
        """
        Initialize an empty list to store unpaid accounts.
        """
        self.unpaid_accounts = []

    def add_account(self, account_id, patient_name, amount_due, due_date):
        """
        Add a new unpaid account.

        :param account_id: Unique identifier for the account
        :param patient_name: Name of the patient
        :param amount_due: Amount of money owed
        :param due_date: Due date for the payment (YYYY-MM-DD format)
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            account = {
                "Account ID": account_id,
                "Patient Name": patient_name,
                "Amount Due": float(amount_due),
                "Due Date": due_date_obj,
                "Status": "Unpaid",
            }
            self.unpaid_accounts.append(account)
        except ValueError as e:
            print(f"Error: Invalid date format or amount. Details: {e}")

    def mark_as_paid(self, account_id):
        """
        Mark an unpaid account as paid.

        :param account_id: Unique identifier for the account to be updated
        """
        for account in self.unpaid_accounts:
            if account["Account ID"] == account_id:
                account["Status"] = "Paid"
                print(f"Account {account_id} marked as paid.")
                return

        print(f"Error: Account with ID {account_id} not found.")

    def generate_report(self, file_name="account_receivable_report.csv"):
        """
        Generate a CSV report of all unpaid accounts.

        :param file_name: Name of the file to save the report
        """
        try:
            with open(file_name, mode="w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Account ID", "Patient Name", "Amount Due", "Due Date", "Status"],
                )
                writer.writeheader()
                writer.writerows(self.unpaid_accounts)
            print(f"Report successfully generated: {file_name}")
        except Exception as e:
            print(f"Error: Unable to generate report. Details: {e}")

    def get_overdue_accounts(self):
        """
        Retrieve a list of accounts that are overdue.

        :return: A list of overdue accounts
        """
        today = datetime.date.today()
        overdue_accounts = [
            account
            for account in self.unpaid_accounts
            if account["Due Date"] < today and account["Status"] == "Unpaid"
        ]
        return overdue_accounts

    def display_overdue_accounts(self):
        """
        Display the overdue accounts in the console.
        """
        overdue_accounts = self.get_overdue_accounts()
        if overdue_accounts:
            print("Overdue Accounts:")
            for account in overdue_accounts:
                print(
                    f"- Account ID: {account['Account ID']}, Patient: {account['Patient Name']}, "
                    f"Amount Due: {account['Amount Due']:.2f}, Due Date: {account['Due Date']}"
                )
        else:
            print("No overdue accounts found.")


# Example usage:
if __name__ == "__main__":
    tracker = MedicalAccountsReceivableTracker()

    # Add accounts
    tracker.add_account("001", "John Doe", 1500.75, "2023-10-01")
    tracker.add_account("002", "Jane Smith", 2500.50, "2023-10-15")
    tracker.add_account("003", "Alice Johnson", 1000.00, "2023-09-20")

    # Display overdue accounts
    tracker.display_overdue_accounts()

    # Mark an account as paid
    tracker.mark_as_paid("001")

    # Generate report
    tracker.generate_report()

    # Display overdue accounts again
    tracker.display_overdue_accounts()
```
