"""
Generated Code Metadata:
========================
Original URL: https://fornm.network
Prompt: Write a code snippet that facilitates a lease-to-own payment option for domain names, inspired by the features on fornm.network.
Generated: DETERMINISTIC_f5bbf55b746b56b2
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, Dict, List

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class LeaseToOwnOption:
    def __init__(
        self,
        domain_name: str,
        total_price: float,
        down_payment: float,
        installment_count: int,
        installment_frequency_days: int,
        lease_duration_days: int
    ):
        """
        Initialize a lease-to-own option for a domain name.
        
        Args:
            domain_name: The domain name being leased
            total_price: Total price to own the domain
            down_payment: Initial down payment amount
            installment_count: Number of installment payments
            installment_frequency_days: Days between installments
            lease_duration_days: Total lease duration in days
        """
        self.domain_name = domain_name
        self.total_price = total_price
        self.down_payment = down_payment
        self.installment_count = installment_count
        self.installment_frequency_days = installment_frequency_days
        self.lease_duration_days = lease_duration_days
        self.installment_amount = (total_price - down_payment) / installment_count
        self.start_date = None
        self.payments = []
        
    def start_lease(self) -> None:
        """Mark the lease as started with current date as start date."""
        self.start_date = datetime.date.today()
        
    def add_payment(
        self,
        amount: float,
        payment_date: datetime.date,
        transaction_id: str,
        status: PaymentStatus = PaymentStatus.PENDING
    ) -> Dict:
        """
        Record a payment made towards the lease.
        
        Args:
            amount: Payment amount
            payment_date: Date of payment
            transaction_id: Unique transaction ID
            status: Payment status
            
        Returns:
            Dictionary containing payment details
            
        Raises:
            ValueError: If lease hasn't started or invalid payment amount
        """
        if not self.start_date:
            raise ValueError("Lease has not started yet")
            
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
            
        payment = {
            "amount": amount,
            "date": payment_date,
            "transaction_id": transaction_id,
            "status": status
        }
        
        self.payments.append(payment)
        return payment
        
    def get_next_payment_due_date(self) -> Optional[datetime.date]:
        """Calculate the next payment due date based on lease terms."""
        if not self.start_date or not self.payments:
            return self.start_date
            
        last_payment_date = max(payment["date"] for payment in self.payments)
        return last_payment_date + datetime.timedelta(days=self.installment_frequency_days)
        
    def get_remaining_payments(self) -> List[Dict]:
        """Get list of remaining payments with due dates and amounts."""
        if not self.start_date:
            return []
            
        payments_made = len([p for p in self.payments if p["status"] == PaymentStatus.COMPLETED])
        remaining_payments = self.installment_count - payments_made
        
        if remaining_payments <= 0:
            return []
            
        next_due_date = self.get_next_payment_due_date()
        payment_schedule = []
        
        for i in range(remaining_payments):
            payment_schedule.append({
                "due_date": next_due_date + datetime.timedelta(days=i * self.installment_frequency_days),
                "amount": self.installment_amount,
                "payment_number": payments_made + i + 1
            })
            
        return payment_schedule
        
    def is_lease_completed(self) -> bool:
        """Check if all payments have been completed."""
        completed_payments = len([p for p in self.payments if p["status"] == PaymentStatus.COMPLETED])
        return completed_payments >= self.installment_count
        
    def get_remaining_balance(self) -> float:
        """Calculate the remaining balance to own the domain."""
        paid_amount = sum(p["amount"] for p in self.payments if p["status"] == PaymentStatus.COMPLETED)
        return max(0, self.total_price - paid_amount)

class DomainLeaseManager:
    def __init__(self):
        self.leases = {}
        
    def create_lease(
        self,
        domain_name: str,
        total_price: float,
        down_payment: float,
        installment_count: int,
        installment_frequency_days: int,
        lease_duration_days: int
    ) -> LeaseToOwnOption:
        """
        Create a new lease-to-own option for a domain.
        
        Args:
            domain_name: The domain name
            total_price: Total price to own
            down_payment: Initial payment
            installment_count: Number of installments
            installment_frequency_days: Days between payments
            lease_duration_days: Total lease duration
            
        Returns:
            LeaseToOwnOption instance
            
        Raises:
            ValueError: If invalid parameters provided
        """
        if domain_name in self.leases:
            raise ValueError("Lease already exists for this domain")
            
        if down_payment >= total_price:
            raise ValueError("Down payment must be less than total price")
            
        if installment_count <= 0:
            raise ValueError("Installment count must be positive")
            
        lease = LeaseToOwnOption(
            domain_name,
            total_price,
            down_payment,
            installment_count,
            installment_frequency_days,
            lease_duration_days
        )
        
        self.leases[domain_name] = lease
        return lease
        
    def get_lease(self, domain_name: str) -> Optional[LeaseToOwnOption]:
        """Retrieve a lease by domain name."""
        return self.leases.get(domain_name)
        
    def process_payment(
        self,
        domain_name: str,
        amount: float,
        transaction_id: str,
        payment_date: Optional[datetime.date] = None
    ) -> Dict:
        """
        Process a payment for a domain lease.
        
        Args:
            domain_name: The domain name
            amount: Payment amount
            transaction_id: Unique transaction ID
            payment_date: Date of payment (defaults to today)
            
        Returns:
            Dictionary containing payment details
            
        Raises:
            ValueError: If lease not found or invalid payment
        """
        lease = self.get_lease(domain_name)
        if not lease:
            raise ValueError("Lease not found")
            
        if not payment_date:
            payment_date = datetime.date.today()
            
        return lease.add_payment(
            amount=amount,
            payment_date=payment_date,
            transaction_id=transaction_id,
            status=PaymentStatus.COMPLETED
        )
```
