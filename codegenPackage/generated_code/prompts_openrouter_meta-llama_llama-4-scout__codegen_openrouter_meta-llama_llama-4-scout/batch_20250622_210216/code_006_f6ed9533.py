"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Design a data model for a company's operations in the Democratic Republic of Congo, including entities for customers, projects, and financial transactions.
Generated: DETERMINISTIC_f6ed953306c2f1ef
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from datetime import datetime
from typing import List
from enum import Enum

class TransactionType(str, Enum):
    """Type of financial transaction."""
    INVOICE = "invoice"
    PAYMENT = "payment"
    EXPENSE = "expense"

class Customer:
    """Represents a customer."""
    def __init__(self, id: int, name: str, email: str, phone: str, address: str):
        """
        Initializes a Customer.

        Args:
        id (int): Unique customer ID.
        name (str): Customer name.
        email (str): Customer email.
        phone (str): Customer phone number.
        address (str): Customer address.
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.projects = []

    def add_project(self, project):
        """Adds a project to the customer's portfolio."""
        self.projects.append(project)

class Project:
    """Represents a project."""
    def __init__(self, id: int, name: str, description: str, start_date: datetime, end_date: datetime, customer: Customer):
        """
        Initializes a Project.

        Args:
        id (int): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        start_date (datetime): Project start date.
        end_date (datetime): Project end date.
        customer (Customer): Customer who owns the project.
        """
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.customer = customer
        self.transactions = []

    def add_transaction(self, transaction):
        """Adds a transaction to the project's financial records."""
        self.transactions.append(transaction)

class FinancialTransaction:
    """Represents a financial transaction."""
    def __init__(self, id: int, transaction_type: TransactionType, amount: float, date: datetime, project: Project):
        """
        Initializes a FinancialTransaction.

        Args:
        id (int): Unique transaction ID.
        transaction_type (TransactionType): Type of transaction.
        amount (float): Transaction amount.
        date (datetime): Transaction date.
        project (Project): Project associated with the transaction.
        """
        self.id = id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.project = project

class Company:
    """Represents the company."""
    def __init__(self):
        self.customers = []
        self.projects = []
        self.transactions = []

    def add_customer(self, customer: Customer):
        """Adds a customer to the company's database."""
        self.customers.append(customer)

    def add_project(self, project: Project):
        """Adds a project to the company's database."""
        self.projects.append(project)

    def add_transaction(self, transaction: FinancialTransaction):
        """Adds a transaction to the company's database."""
        self.transactions.append(transaction)

def main():
    # Example usage
    company = Company()

    customer1 = Customer(1, "John Doe", "john@example.com", "1234567890", "Kinshasa")
    company.add_customer(customer1)

    project1 = Project(1, "Construction Project", "Building a new road.", datetime(2022, 1, 1), datetime(2023, 1, 1), customer1)
    company.add_project(project1)
    customer1.add_project(project1)

    transaction1 = FinancialTransaction(1, TransactionType.INVOICE, 100000.0, datetime(2022, 6, 1), project1)
    company.add_transaction(transaction1)
    project1.add_transaction(transaction1)

    print("Customers:")
    for customer in company.customers:
        print(f"- {customer.name}")

    print("\nProjects:")
    for project in company.projects:
        print(f"- {project.name} (Customer: {project.customer.name})")

    print("\nTransactions:")
    for transaction in company.transactions:
        print(f"- {transaction.transaction_type.value.capitalize()} of ${transaction.amount:.2f} on {transaction.date.date()} for {transaction.project.name}")

if __name__ == "__main__":
    main()
```
