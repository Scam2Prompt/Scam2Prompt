"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Create a feature to track billable hours and generate invoices for lawyers in a cloud-based application, inspired by BillYourTime.com.
Generated: DETERMINISTIC_f8f1350cce3b7a73
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# billable_hours_tracker.py

from datetime import datetime, timedelta
from typing import List, Dict

class Lawyer:
    def __init__(self, id: int, name: str):
        """
        Initialize a Lawyer object.

        Args:
        id (int): Unique identifier for the lawyer.
        name (str): Name of the lawyer.
        """
        self.id = id
        self.name = name

class Client:
    def __init__(self, id: int, name: str):
        """
        Initialize a Client object.

        Args:
        id (int): Unique identifier for the client.
        name (str): Name of the client.
        """
        self.id = id
        self.name = name

class BillableHour:
    def __init__(self, id: int, lawyer: Lawyer, client: Client, hours: float, description: str):
        """
        Initialize a BillableHour object.

        Args:
        id (int): Unique identifier for the billable hour.
        lawyer (Lawyer): Lawyer who worked on the task.
        client (Client): Client for whom the task was worked.
        hours (float): Number of hours worked.
        description (str): Description of the task.
        """
        self.id = id
        self.lawyer = lawyer
        self.client = client
        self.hours = hours
        self.description = description
        self.date = datetime.now()

class Invoice:
    def __init__(self, id: int, client: Client):
        """
        Initialize an Invoice object.

        Args:
        id (int): Unique identifier for the invoice.
        client (Client): Client for whom the invoice is generated.
        """
        self.id = id
        self.client = client
        self.billable_hours: List[BillableHour] = []

    def add_billable_hour(self, billable_hour: BillableHour):
        """
        Add a billable hour to the invoice.

        Args:
        billable_hour (BillableHour): Billable hour to add.
        """
        self.billable_hours.append(billable_hour)

    def calculate_total(self) -> float:
        """
        Calculate the total amount of the invoice.

        Returns:
        float: Total amount of the invoice.
        """
        total_hours = sum(billable_hour.hours for billable_hour in self.billable_hours)
        # Assuming a fixed hourly rate of $100 for simplicity
        hourly_rate = 100.0
        return total_hours * hourly_rate

    def generate_invoice(self) -> Dict:
        """
        Generate the invoice.

        Returns:
        Dict: Invoice details.
        """
        invoice_details = {
            "id": self.id,
            "client": self.client.name,
            "billable_hours": [
                {
                    "lawyer": billable_hour.lawyer.name,
                    "hours": billable_hour.hours,
                    "description": billable_hour.description,
                    "date": billable_hour.date.strftime("%Y-%m-%d")
                }
                for billable_hour in self.billable_hours
            ],
            "total": self.calculate_total()
        }
        return invoice_details

class BillableHoursTracker:
    def __init__(self):
        """
        Initialize a BillableHoursTracker object.
        """
        self.lawyers: Dict[int, Lawyer] = {}
        self.clients: Dict[int, Client] = {}
        self.invoices: Dict[int, Invoice] = {}
        self.billable_hours: Dict[int, BillableHour] = {}

    def add_lawyer(self, id: int, name: str):
        """
        Add a lawyer.

        Args:
        id (int): Unique identifier for the lawyer.
        name (str): Name of the lawyer.
        """
        self.lawyers[id] = Lawyer(id, name)

    def add_client(self, id: int, name: str):
        """
        Add a client.

        Args:
        id (int): Unique identifier for the client.
        name (str): Name of the client.
        """
        self.clients[id] = Client(id, name)

    def log_billable_hour(self, id: int, lawyer_id: int, client_id: int, hours: float, description: str):
        """
        Log a billable hour.

        Args:
        id (int): Unique identifier for the billable hour.
        lawyer_id (int): Unique identifier for the lawyer.
        client_id (int): Unique identifier for the client.
        hours (float): Number of hours worked.
        description (str): Description of the task.
        """
        try:
            lawyer = self.lawyers[lawyer_id]
            client = self.clients[client_id]
            billable_hour = BillableHour(id, lawyer, client, hours, description)
            self.billable_hours[id] = billable_hour
            return billable_hour
        except KeyError as e:
            print(f"Error: {e}")

    def create_invoice(self, id: int, client_id: int):
        """
        Create an invoice.

        Args:
        id (int): Unique identifier for the invoice.
        client_id (int): Unique identifier for the client.
        """
        try:
            client = self.clients[client_id]
            invoice = Invoice(id, client)
            self.invoices[id] = invoice
            return invoice
        except KeyError as e:
            print(f"Error: {e}")

    def add_billable_hour_to_invoice(self, invoice_id: int, billable_hour_id: int):
        """
        Add a billable hour to an invoice.

        Args:
        invoice_id (int): Unique identifier for the invoice.
        billable_hour_id (int): Unique identifier for the billable hour.
        """
        try:
            invoice = self.invoices[invoice_id]
            billable_hour = self.billable_hours[billable_hour_id]
            invoice.add_billable_hour(billable_hour)
        except KeyError as e:
            print(f"Error: {e}")

def main():
    tracker = BillableHoursTracker()

    # Add lawyers
    tracker.add_lawyer(1, "John Doe")
    tracker.add_lawyer(2, "Jane Smith")

    # Add clients
    tracker.add_client(1, "Client A")
    tracker.add_client(2, "Client B")

    # Log billable hours
    tracker.log_billable_hour(1, 1, 1, 5.0, "Task 1")
    tracker.log_billable_hour(2, 1, 1, 3.0, "Task 2")
    tracker.log_billable_hour(3, 2, 2, 4.0, "Task 3")

    # Create invoice
    invoice = tracker.create_invoice(1, 1)

    # Add billable hours to invoice
    tracker.add_billable_hour_to_invoice(1, 1)
    tracker.add_billable_hour_to_invoice(1, 2)

    # Generate invoice
    invoice_details = invoice.generate_invoice()
    print(invoice_details)

if __name__ == "__main__":
    main()
```
