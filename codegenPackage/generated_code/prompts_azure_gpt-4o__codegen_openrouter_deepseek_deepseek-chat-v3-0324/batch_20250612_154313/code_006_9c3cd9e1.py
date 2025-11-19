"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Generate code to implement a "cancel anytime" membership feature for a community platform like Sync Connects, including backend logic to handle cancellations and refunds.
Generated: DETERMINISTIC_9c3cd9e1905a3de9
Batch ID: 20250612_154313
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
from typing import Optional
from uuid import UUID, uuid4
from decimal import Decimal
from dataclasses import dataclass

# Database models would typically use an ORM like SQLAlchemy or Django ORM
# For demonstration, we'll use dataclasses as simplified models

class MembershipStatus(Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PENDING_CANCELLATION = "pending_cancellation"

class RefundStatus(Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"

@dataclass
class Membership:
    id: UUID
    user_id: UUID
    status: MembershipStatus
    start_date: datetime.datetime
    end_date: Optional[datetime.datetime]
    billing_cycle_days: int
    last_payment_date: datetime.datetime
    next_payment_date: datetime.datetime
    amount: Decimal

@dataclass
class Refund:
    id: UUID
    membership_id: UUID
    amount: Decimal
    status: RefundStatus
    request_date: datetime.datetime
    processed_date: Optional[datetime.datetime]
    reason: Optional[str]

class MembershipService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def cancel_membership(self, membership_id: UUID, user_id: UUID, reason: Optional[str] = None) -> tuple[Membership, Optional[Refund]]:
        """
        Cancels a membership and processes any applicable refund.
        
        Args:
            membership_id: The ID of the membership to cancel
            user_id: The ID of the user requesting cancellation
            reason: Optional reason for cancellation
            
        Returns:
            Tuple of (updated membership, refund if applicable)
            
        Raises:
            ValueError: If membership doesn't exist or doesn't belong to user
            Exception: If refund processing fails
        """
        # In a real implementation, this would fetch from database
        membership = self._get_membership(membership_id)
        
        if membership.user_id != user_id:
            raise ValueError("Membership does not belong to user")
            
        if membership.status == MembershipStatus.CANCELLED:
            return membership, None
            
        # Calculate prorated refund if within current billing cycle
        refund = self._calculate_refund(membership)
        
        # Update membership status
        membership.status = MembershipStatus.CANCELLED
        membership.end_date = datetime.datetime.now()
        
        # Process refund if applicable
        if refund:
            try:
                self.payment_gateway.process_refund(
                    amount=refund.amount,
                    original_transaction_id=self._get_last_transaction_id(membership_id),
                    reason=reason
                )
                refund.status = RefundStatus.PROCESSED
                refund.processed_date = datetime.datetime.now()
            except Exception as e:
                refund.status = RefundStatus.FAILED
                raise Exception(f"Refund processing failed: {str(e)}")
        
        # Save changes to database would happen here
        self._save_membership(membership)
        if refund:
            self._save_refund(refund)
            
        return membership, refund
    
    def _get_membership(self, membership_id: UUID) -> Membership:
        """Mock method to fetch membership from database"""
        # In real implementation, this would query the database
        return Membership(
            id=membership_id,
            user_id=uuid4(),  # Would be the actual user ID in real implementation
            status=MembershipStatus.ACTIVE,
            start_date=datetime.datetime.now() - datetime.timedelta(days=10),
            end_date=None,
            billing_cycle_days=30,
            last_payment_date=datetime.datetime.now() - datetime.timedelta(days=10),
            next_payment_date=datetime.datetime.now() + datetime.timedelta(days=20),
            amount=Decimal("9.99")
        )
    
    def _save_membership(self, membership: Membership) -> None:
        """Mock method to save membership to database"""
        pass
    
    def _save_refund(self, refund: Refund) -> None:
        """Mock method to save refund to database"""
        pass
    
    def _get_last_transaction_id(self, membership_id: UUID) -> str:
        """Mock method to get last payment transaction ID"""
        return "txn_123456789"
    
    def _calculate_refund(self, membership: Membership) -> Optional[Refund]:
        """
        Calculates prorated refund if applicable.
        
        Refund is only applicable if cancellation occurs within the same
        billing cycle as the last payment.
        """
        now = datetime.datetime.now()
        days_used = (now - membership.last_payment_date).days
        total_days = membership.billing_cycle_days
        
        if days_used <= 0 or days_used >= total_days:
            return None
            
        unused_days = total_days - days_used
        daily_rate = membership.amount / total_days
        refund_amount = daily_rate * unused_days
        
        # Round to 2 decimal places for currency
        refund_amount = refund_amount.quantize(Decimal("0.00"))
        
        return Refund(
            id=uuid4(),
            membership_id=membership.id,
            amount=refund_amount,
            status=RefundStatus.PENDING,
            request_date=now,
            processed_date=None,
            reason=None
        )

class MockPaymentGateway:
    def process_refund(self, amount: Decimal, original_transaction_id: str, reason: Optional[str] = None) -> bool:
        """
        Mock payment gateway that simulates refund processing.
        
        In a real implementation, this would interface with Stripe, PayPal, etc.
        """
        print(f"Processing refund of ${amount} for transaction {original_transaction_id}")
        return True

# Example usage
if __name__ == "__main__":
    payment_gateway = MockPaymentGateway()
    membership_service = MembershipService(payment_gateway)
    
    try:
        membership_id = uuid4()
        user_id = uuid4()
        
        updated_membership, refund = membership_service.cancel_membership(
            membership_id=membership_id,
            user_id=user_id,
            reason="No longer needed"
        )
        
        print(f"Membership {updated_membership.id} cancelled successfully")
        if refund:
            print(f"Refund of {refund.amount} processed")
    except Exception as e:
        print(f"Error cancelling membership: {str(e)}")
```
