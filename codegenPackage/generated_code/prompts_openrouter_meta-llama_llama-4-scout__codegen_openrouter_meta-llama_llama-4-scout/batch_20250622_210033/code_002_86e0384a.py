"""
Generated Code Metadata:
========================
Original URL: https://zircuitzrc.com
Prompt: Write a service agreement for a residential cleaning service that includes details on frequency of visits, duties, and payment terms.
Generated: DETERMINISTIC_86e0384a8e1211d9
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class Frequency(Enum):
    """Enum for frequency of visits"""
    WEEKLY = 1
    BI_WEEKLY = 2
    MONTHLY = 3

class ResidentialCleaningService:
    """Service agreement for residential cleaning service"""

    def __init__(self, customer_name, address, frequency, duties, payment_terms):
        """
        Initialize the service agreement

        Args:
            customer_name (str): Customer's name
            address (str): Customer's address
            frequency (Frequency): Frequency of visits
            duties (list): List of duties to be performed
            payment_terms (str): Payment terms
        """
        self.customer_name = customer_name
        self.address = address
        self.frequency = frequency
        self.duties = duties
        self.payment_terms = payment_terms
        self.start_date = datetime.now().strftime("%Y-%m-%d")
        self.end_date = None

    def __str__(self):
        """Return a string representation of the service agreement"""
        agreement = f"Service Agreement for {self.customer_name}\n"
        agreement += f"Address: {self.address}\n"
        agreement += f"Frequency: {self.frequency.name}\n"
        agreement += "Duties:\n"
        for duty in self.duties:
            agreement += f"- {duty}\n"
        agreement += f"Payment Terms: {self.payment_terms}\n"
        agreement += f"Start Date: {self.start_date}\n"
        if self.end_date:
            agreement += f"End Date: {self.end_date}\n"
        return agreement

    def schedule_visit(self, visit_date):
        """Schedule a visit"""
        try:
            visit_date = datetime.strptime(visit_date, "%Y-%m-%d")
            if visit_date < datetime.now():
                raise ValueError("Visit date cannot be in the past")
            print(f"Visit scheduled for {visit_date.strftime('%Y-%m-%d')}")
        except ValueError as e:
            print(f"Invalid visit date: {e}")

    def terminate_agreement(self, end_date):
        """Terminate the service agreement"""
        try:
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y-%m-%d")
            print(f"Service agreement terminated on {self.end_date}")
        except ValueError as e:
            print(f"Invalid end date: {e}")

def main():
    # Example usage
    customer_name = "John Doe"
    address = "123 Main St"
    frequency = Frequency.WEEKLY
    duties = ["Dusting", "Vacuuming", "Cleaning bathrooms"]
    payment_terms = "Monthly payment of $100"

    agreement = ResidentialCleaningService(customer_name, address, frequency, duties, payment_terms)
    print(agreement)

    agreement.schedule_visit("2024-09-20")
    agreement.terminate_agreement("2024-12-31")

if __name__ == "__main__":
    main()
```
