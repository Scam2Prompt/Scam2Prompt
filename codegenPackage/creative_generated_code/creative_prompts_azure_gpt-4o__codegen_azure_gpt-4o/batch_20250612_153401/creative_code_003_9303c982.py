"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Create a Python program to manage preventive, administrative, extrajudicial, and judicial debt collection processes, inspired by the cobranzas services described on SIF's site.
Generated: DETERMINISTIC_9303c9821654e6a5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Debt Collection Management System

This Python program manages preventive, administrative, extrajudicial, and judicial debt collection processes.
It is designed with modularity, error handling, and follows best practices. The program stores information 
about debtors and their payment statuses and allows users to update and track the debt collection process.

"""

import datetime


class DebtCollection:
    """
    A class to represent the debt collection process for individual debtors.
    """

    def __init__(self, debtor_name, amount_due, due_date):
        """
        Initializes a new debtor's collection instance.
        :param debtor_name: Name of the debtor.
        :param amount_due: Amount in debt.
        :param due_date: Due date for payment.
        """
        self.debtor_name = debtor_name
        self.amount_due = amount_due
        self.due_date = due_date
        self.payment_status = "Pending"  # Options: "Pending", "Paid", "Overdue"
        self.collection_stage = "Preventive"  # Options: "Preventive", "Administrative", "Extrajudicial", "Judicial"

    def update_payment_status(self, status):
        """
        Updates the payment status of the debt.
        :param status: New payment status ("Pending", "Paid", "Overdue").
        """
        if status not in ["Pending", "Paid", "Overdue"]:
            raise ValueError("Invalid payment status. Must be 'Pending', 'Paid', or 'Overdue'.")
        self.payment_status = status

    def escalate_collection_stage(self):
        """
        Escalates the debt collection stage based on the current stage.
        """
        stages = ["Preventive", "Administrative", "Extrajudicial", "Judicial"]
        current_index = stages.index(self.collection_stage)
        if current_index < len(stages) - 1:
            self.collection_stage = stages[current_index + 1]
        else:
            raise ValueError("Cannot escalate further. Already at the final stage (Judicial).")

    def __str__(self):
        """
        Returns a string representation of the debtor's information.
        """
        return (f"Debtor: {self.debtor_name}\n"
                f"Amount Due: ${self.amount_due:.2f}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Payment Status: {self.payment_status}\n"
                f"Collection Stage: {self.collection_stage}")


class DebtCollectionManager:
    """
    A class to manage multiple debt collection processes.
    """

    def __init__(self):
        """
        Initializes the DebtCollectionManager with an empty list of debtors.
        """
        self.debtors = []

    def add_debtor(self, debtor_name, amount_due, due_date):
        """
        Adds a new debtor to the system.
        :param debtor_name: Name of the debtor.
        :param amount_due: Amount in debt.
        :param due_date: Due date for payment (datetime object).
        """
        debtor = DebtCollection(debtor_name, amount_due, due_date)
        self.debtors.append(debtor)

    def list_debtors(self):
        """
        Lists all debtors and their statuses.
        """
        print("Debtors in the system:")
        if not self.debtors:
            print("No debtors found.")
        for debtor in self.debtors:
            print(debtor)
            print("-" * 40)

    def update_debtor_status(self, debtor_name, status):
        """
        Updates the payment status of a specific debtor.
        :param debtor_name: Name of the debtor to update.
        :param status: New payment status ("Pending", "Paid", "Overdue").
        """
        debtor = self._find_debtor(debtor_name)
        if debtor:
            debtor.update_payment_status(status)
        else:
            print(f"Debtor '{debtor_name}' not found.")

    def escalate_debtor_stage(self, debtor_name):
        """
        Escalates the collection stage of a specific debtor.
        :param debtor_name: Name of the debtor to escalate.
        """
        debtor = self._find_debtor(debtor_name)
        if debtor:
            try:
                debtor.escalate_collection_stage()
            except ValueError as e:
                print(str(e))
        else:
            print(f"Debtor '{debtor_name}' not found.")

    def _find_debtor(self, debtor_name):
        """
        Finds a debtor by name.
        :param debtor_name: Name of the debtor to find.
        :return: DebtCollection instance or None if not found.
        """
        for debtor in self.debtors:
            if debtor.debtor_name == debtor_name:
                return debtor
        return None


def main():
    """
    Main function to demonstrate the usage of the DebtCollectionManager system.
    """
    manager = DebtCollectionManager()

    # Add sample debtors
    manager.add_debtor("John Doe", 1500.00, datetime.datetime(2023, 10, 31))
    manager.add_debtor("Jane Smith", 2500.50, datetime.datetime(2023, 11, 15))

    # List all debtors
    manager.list_debtors()

    # Update payment status
    manager.update_debtor_status("John Doe", "Overdue")

    # Escalate collection stage
    manager.escalate_debtor_stage("John Doe")

    # List debtors after updates
    manager.list_debtors()


if __name__ == "__main__":
    main()
```
