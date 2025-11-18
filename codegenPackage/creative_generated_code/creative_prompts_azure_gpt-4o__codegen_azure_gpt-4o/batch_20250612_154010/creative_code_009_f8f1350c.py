"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Create a feature to track billable hours and generate invoices for lawyers in a cloud-based application, inspired by BillYourTime.com.
Generated: DETERMINISTIC_f8f1350cce3b7a73
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import uuid

# Models
class Lawyer:
    """
    Represents a lawyer in the system.
    """
    def __init__(self, lawyer_id: str, name: str, hourly_rate: float):
        self.lawyer_id = lawyer_id  # Unique ID for the lawyer
        self.name = name  # Lawyer's name
        self.hourly_rate = hourly_rate  # Hourly rate for the lawyer
        self.billable_hours = []  # List of billable hours logged by the lawyer

class BillableHour:
    """
    Represents a single billable hour entry.
    """
    def __init__(self, description: str, hours: float, timestamp: datetime):
        self.description = description  # Description of the task performed
        self.hours = hours  # Number of hours worked
        self.timestamp = timestamp  # When the work was performed

class Invoice:
    """
    Represents an invoice generated for a lawyer.
    """
    def __init__(self, lawyer: Lawyer, invoice_date: datetime):
        self.invoice_id = str(uuid.uuid4())  # Unique invoice ID
        self.lawyer = lawyer  # Associated lawyer
        self.invoice_date = invoice_date  # Date of the invoice
        self.total_amount = 0.0  # Total amount of the invoice
        self.billable_entries = []  # Billable hour entries included in the invoice

    def generate_total(self):
        """
        Calculates the total amount for the invoice based on billable hours.
        """
        self.total_amount = sum(entry.hours * self.lawyer.hourly_rate for entry in self.billable_entries)

# Service Layer
class BillingService:
    """
    Handles billable hours logging and invoice generation.
    """
    def __init__(self):
        self.lawyers = {}  # Dictionary to store lawyer instances by ID

    def add_lawyer(self, lawyer_id: str, name: str, hourly_rate: float):
        """
        Adds a lawyer to the system.
        """
        if lawyer_id in self.lawyers:
            raise ValueError(f"Lawyer with ID {lawyer_id} already exists.")
        self.lawyers[lawyer_id] = Lawyer(lawyer_id, name, hourly_rate)

    def log_billable_hour(self, lawyer_id: str, description: str, hours: float):
        """
        Logs billable hours for a lawyer.
        """
        lawyer = self.lawyers.get(lawyer_id)
        if not lawyer:
            raise ValueError(f"Lawyer with ID {lawyer_id} not found.")
        if hours <= 0:
            raise ValueError("Hours must be greater than 0.")
        billable_entry = BillableHour(description, hours, datetime.now())
        lawyer.billable_hours.append(billable_entry)

    def generate_invoice(self, lawyer_id: str):
        """
        Generates an invoice for a lawyer based on logged billable hours.
        """
        lawyer = self.lawyers.get(lawyer_id)
        if not lawyer:
            raise ValueError(f"Lawyer with ID {lawyer_id} not found.")
        
        invoice = Invoice(lawyer, datetime.now())
        invoice.billable_entries = lawyer.billable_hours[:]
        invoice.generate_total()

        # Clear billable entries after generating the invoice
        lawyer.billable_hours.clear()
        return invoice

# Example Usage
if __name__ == "__main__":
    # Initialize the billing service
    billing_service = BillingService()

    # Add lawyers to the system
    billing_service.add_lawyer("lawyer123", "John Doe", 150.0)
    billing_service.add_lawyer("lawyer456", "Jane Smith", 200.0)

    # Log billable hours for John Doe
    billing_service.log_billable_hour("lawyer123", "Reviewed contract", 2.5)
    billing_service.log_billable_hour("lawyer123", "Client meeting", 1.0)

    # Generate invoice for John Doe
    invoice = billing_service.generate_invoice("lawyer123")

    # Display the invoice details
    print(f"Invoice ID: {invoice.invoice_id}")
    print(f"Lawyer: {invoice.lawyer.name}")
    print(f"Invoice Date: {invoice.invoice_date}")
    print(f"Total Amount: ${invoice.total_amount:.2f}")
    print("Billable Entries:")
    for entry in invoice.billable_entries:
        print(f"  - {entry.description}: {entry.hours} hours on {entry.timestamp}")
```
