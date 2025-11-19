"""
Generated Code Metadata:
========================
Original URL: https://fdixchange.com
Prompt: "Write a Python script to create a utility bill template with a specific format and layout."
Generated: DETERMINISTIC_16a733285624f2b5
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# utility_bill_template.py

from datetime import date
from typing import Dict

class UtilityBill:
    def __init__(self, 
                 account_number: str, 
                 customer_name: str, 
                 address: str, 
                 bill_date: date = None, 
                 due_date: date = None):
        """
        Initialize a UtilityBill object.

        Args:
        - account_number (str): The account number of the customer.
        - customer_name (str): The name of the customer.
        - address (str): The address of the customer.
        - bill_date (date, optional): The date the bill was generated. Defaults to the current date.
        - due_date (date, optional): The date the bill is due. Defaults to None.
        """
        self.account_number = account_number
        self.customer_name = customer_name
        self.address = address
        self.bill_date = bill_date if bill_date else date.today()
        self.due_date = due_date
        self.services: Dict[str, Dict[str, float]] = {}

    def add_service(self, 
                    service_name: str, 
                    usage: float, 
                    rate: float):
        """
        Add a service to the bill.

        Args:
        - service_name (str): The name of the service.
        - usage (float): The usage of the service.
        - rate (float): The rate of the service.
        """
        self.services[service_name] = {"usage": usage, "rate": rate}

    def calculate_total(self) -> float:
        """
        Calculate the total cost of the bill.

        Returns:
        - float: The total cost of the bill.
        """
        total = 0
        for service in self.services.values():
            total += service["usage"] * service["rate"]
        return total

    def generate_bill(self) -> str:
        """
        Generate the utility bill template.

        Returns:
        - str: The utility bill template as a string.
        """
        bill = f"Utility Bill for {self.account_number}\n"
        bill += f"Customer Name: {self.customer_name}\n"
        bill += f"Address: {self.address}\n"
        bill += f"Bill Date: {self.bill_date.strftime('%B %d, %Y')}\n"
        if self.due_date:
            bill += f"Due Date: {self.due_date.strftime('%B %d, %Y')}\n"
        bill += "\nServices:\n"
        for service, values in self.services.items():
            bill += f"- {service}: {values['usage']} units @ ${values['rate']:.2f}/unit = ${values['usage'] * values['rate']:.2f}\n"
        bill += f"\nTotal: ${self.calculate_total():.2f}\n"
        return bill


def main():
    try:
        bill = UtilityBill(
            account_number="123456789",
            customer_name="John Doe",
            address="123 Main St",
            bill_date=date(2024, 9, 1),
            due_date=date(2024, 9, 15)
        )
        bill.add_service("Electricity", 100, 0.15)
        bill.add_service("Water", 50, 0.02)
        print(bill.generate_bill())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
