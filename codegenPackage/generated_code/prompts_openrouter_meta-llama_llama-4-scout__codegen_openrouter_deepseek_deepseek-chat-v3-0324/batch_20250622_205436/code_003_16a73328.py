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
import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Customer:
    """Class representing a customer for utility billing."""
    name: str
    address: str
    account_number: str
    phone: Optional[str] = None
    email: Optional[str] = None

@dataclass
class UtilityBill:
    """Class representing a utility bill."""
    customer: Customer
    billing_period_start: datetime.date
    billing_period_end: datetime.date
    due_date: datetime.date
    previous_reading: float
    current_reading: float
    rate_per_unit: float
    fixed_charges: float = 0.0
    late_fee: float = 0.0
    tax_rate: float = 0.0

    def calculate_consumption(self) -> float:
        """Calculate the units consumed."""
        return self.current_reading - self.previous_reading

    def calculate_subtotal(self) -> float:
        """Calculate subtotal before taxes and fees."""
        return (self.calculate_consumption() * self.rate_per_unit) + self.fixed_charges

    def calculate_tax(self) -> float:
        """Calculate tax amount."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total(self) -> float:
        """Calculate total amount due."""
        return self.calculate_subtotal() + self.calculate_tax() + self.late_fee

    def generate_bill(self) -> str:
        """Generate a formatted utility bill."""
        consumption = self.calculate_consumption()
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        bill_template = f"""
        =============================================
        UTILITY BILL STATEMENT
        =============================================
        Customer Name: {self.customer.name}
        Account Number: {self.customer.account_number}
        Address: {self.customer.address}
        {'Phone: ' + self.customer.phone if self.customer.phone else ''}
        {'Email: ' + self.customer.email if self.customer.email else ''}
        
        Billing Period: {self.billing_period_start.strftime('%Y-%m-%d')} to {self.billing_period_end.strftime('%Y-%m-%d')}
        Due Date: {self.due_date.strftime('%Y-%m-%d')}
        
        =============================================
        USAGE DETAILS
        =============================================
        Previous Reading: {self.previous_reading:.2f} units
        Current Reading: {self.current_reading:.2f} units
        Consumption: {consumption:.2f} units
        Rate per Unit: ${self.rate_per_unit:.2f}
        
        =============================================
        CHARGES
        =============================================
        Consumption Charges: ${consumption * self.rate_per_unit:.2f}
        Fixed Charges: ${self.fixed_charges:.2f}
        Subtotal: ${subtotal:.2f}
        Tax ({self.tax_rate*100:.1f}%): ${tax:.2f}
        Late Fee: ${self.late_fee:.2f}
        
        =============================================
        TOTAL AMOUNT DUE: ${total:.2f}
        =============================================
        
        Please pay by the due date to avoid late fees.
        Thank you for your business!
        """
        return bill_template

def create_sample_bill() -> UtilityBill:
    """Create a sample utility bill for demonstration."""
    customer = Customer(
        name="John Doe",
        address="123 Main St, Anytown, USA",
        account_number="UTIL-2023-001",
        phone="(555) 123-4567",
        email="john.doe@example.com"
    )
    
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=30)
    end_date = today
    due_date = today + datetime.timedelta(days=14)
    
    return UtilityBill(
        customer=customer,
        billing_period_start=start_date,
        billing_period_end=end_date,
        due_date=due_date,
        previous_reading=450.0,
        current_reading=520.5,
        rate_per_unit=0.15,
        fixed_charges=10.0,
        late_fee=0.0,
        tax_rate=0.07
    )

if __name__ == "__main__":
    try:
        bill = create_sample_bill()
        print(bill.generate_bill())
    except Exception as e:
        print(f"Error generating bill: {str(e)}")
```
