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
import datetime
from typing import List, Dict
import json

class BillableHour:
    """Class to represent a billable hour entry."""
    
    def __init__(self, description: str, hours: float, date: datetime.date):
        self.description = description
        self.hours = hours
        self.date = date

    def total_cost(self, hourly_rate: float) -> float:
        """Calculate total cost for this billable hour based on hourly rate."""
        return self.hours * hourly_rate

class Invoice:
    """Class to represent an invoice."""
    
    def __init__(self, lawyer_name: str, hourly_rate: float):
        self.lawyer_name = lawyer_name
        self.hourly_rate = hourly_rate
        self.billable_hours: List[BillableHour] = []
        self.invoice_date = datetime.date.today()
    
    def add_billable_hour(self, description: str, hours: float, date: datetime.date):
        """Add a billable hour to the invoice."""
        if hours <= 0:
            raise ValueError("Hours must be greater than zero.")
        self.billable_hours.append(BillableHour(description, hours, date))
    
    def total_amount(self) -> float:
        """Calculate total invoice amount based on billable hours."""
        return sum(hour.total_cost(self.hourly_rate) for hour in self.billable_hours)
    
    def generate_invoice(self) -> Dict:
        """Generate a structured invoice representation."""
        return {
            "lawyer_name": self.lawyer_name,
            "invoice_date": str(self.invoice_date),
            "billable_hours": [
                {
                    "description": hour.description,
                    "hours": hour.hours,
                    "date": str(hour.date),
                    "cost": hour.total_cost(self.hourly_rate)
                } for hour in self.billable_hours
            ],
            "total_amount": self.total_amount()
        }

def save_invoice(invoice: Invoice, filename: str):
    """Save the invoice to a JSON file."""
    invoice_data = invoice.generate_invoice()
    try:
        with open(filename, 'w') as json_file:
            json.dump(invoice_data, json_file, indent=4)
    except IOError as e:
        raise RuntimeError(f"Error writing to file {filename}: {e}")

# Example usage
def main():
    try:
        lawyer_invoice = Invoice("John Doe", hourly_rate=250.00)
        lawyer_invoice.add_billable_hour("Client Consultation", 3.5, datetime.date(2023, 10, 1))
        lawyer_invoice.add_billable_hour("Draft Contract", 4.0, datetime.date(2023, 10, 2))
        
        # Save the invoice to a JSON file
        save_invoice(lawyer_invoice, 'invoice.json')

        print("Invoice generated and saved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
