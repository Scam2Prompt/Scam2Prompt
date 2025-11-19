"""
Generated Code Metadata:
========================
Original URL: https://megaetlh.com
Prompt: Write a code snippet for a domain leasing feature that allows users to pay monthly, as mentioned on the megaetlh.com site.
Generated: DETERMINISTIC_f95fed4471ef2565
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# domain_leasing.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class PaymentFrequency(Enum):
    """Payment frequency enumeration"""
    MONTHLY = 1

class DomainLeasingService:
    """Domain leasing service class"""

    def __init__(self, domain_name: str, lease_duration: int, payment_frequency: PaymentFrequency, monthly_fee: float):
        """
        Initialize the domain leasing service

        Args:
        - domain_name (str): The name of the domain
        - lease_duration (int): The duration of the lease in months
        - payment_frequency (PaymentFrequency): The payment frequency
        - monthly_fee (float): The monthly fee
        """
        self.domain_name = domain_name
        self.lease_duration = lease_duration
        self.payment_frequency = payment_frequency
        self.monthly_fee = monthly_fee
        self.lease_start_date = None

    def lease_domain(self) -> Dict:
        """
        Lease the domain and return the lease details

        Returns:
        - A dictionary containing the lease details
        """
        try:
            # Validate input parameters
            if not self.domain_name:
                raise ValueError("Domain name is required")
            if self.lease_duration <= 0:
                raise ValueError("Lease duration must be greater than 0")
            if self.payment_frequency != PaymentFrequency.MONTHLY:
                raise ValueError("Only monthly payment frequency is supported")
            if self.monthly_fee <= 0:
                raise ValueError("Monthly fee must be greater than 0")

            # Initialize lease start date
            self.lease_start_date = datetime.now()

            # Calculate lease end date
            lease_end_date = self.lease_start_date + timedelta(days=self.lease_duration * 30)

            # Calculate total cost
            total_cost = self.monthly_fee * self.lease_duration

            # Return lease details
            return {
                "domain_name": self.domain_name,
                "lease_start_date": self.lease_start_date.strftime("%Y-%m-%d"),
                "lease_end_date": lease_end_date.strftime("%Y-%m-%d"),
                "payment_frequency": self.payment_frequency.name,
                "monthly_fee": self.monthly_fee,
                "total_cost": total_cost
            }

        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}

    def pay_monthly(self, payment_date: datetime) -> Dict:
        """
        Pay the monthly fee

        Args:
        - payment_date (datetime): The date of payment

        Returns:
        - A dictionary containing the payment result
        """
        try:
            # Validate payment date
            if not self.lease_start_date:
                raise ValueError("Lease has not started yet")
            if payment_date < self.lease_start_date:
                raise ValueError("Payment date is before lease start date")

            # Calculate number of months paid
            months_paid = (payment_date - self.lease_start_date).days // 30

            # Return payment result
            return {
                "domain_name": self.domain_name,
                "payment_date": payment_date.strftime("%Y-%m-%d"),
                "months_paid": months_paid,
                "monthly_fee": self.monthly_fee,
                "total_paid": self.monthly_fee * months_paid
            }

        except Exception as e:
            # Handle any exceptions
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    domain_leasing_service = DomainLeasingService(
        domain_name="example.com",
        lease_duration=12,
        payment_frequency=PaymentFrequency.MONTHLY,
        monthly_fee=10.99
    )

    lease_details = domain_leasing_service.lease_domain()
    print(lease_details)

    payment_date = datetime.now()
    payment_result = domain_leasing_service.pay_monthly(payment_date)
    print(payment_result)
```
