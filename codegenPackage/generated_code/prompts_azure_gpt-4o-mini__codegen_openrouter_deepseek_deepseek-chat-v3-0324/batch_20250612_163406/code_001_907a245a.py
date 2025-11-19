"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: How can I implement a payment plan feature in a web application for selling automotive products, similar to the one described on Itamarati Online?
Generated: DETERMINISTIC_907a245a8cfede28
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation of a payment plan feature for an automotive e-commerce application:

```python
# payment_plan.py
from datetime import datetime, timedelta
from decimal import Decimal
from enum import Enum, auto
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


class PaymentPlanStatus(Enum):
    ACTIVE = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    DEFAULTED = auto()


class PaymentPlan:
    def __init__(
        self,
        plan_id: str,
        total_amount: Decimal,
        installment_count: int,
        start_date: datetime,
        interval_days: int = 30,
        down_payment: Decimal = Decimal("0"),
    ):
        """
        Initialize a payment plan for automotive products.
        
        Args:
            plan_id: Unique identifier for the payment plan
            total_amount: Total amount to be paid (including any interest)
            installment_count: Number of installments
            start_date: Date when the first payment is due
            interval_days: Days between installments (default 30)
            down_payment: Optional upfront payment amount
        """
        if installment_count < 1:
            raise ValueError("Installment count must be at least 1")
        if total_amount <= 0:
            raise ValueError("Total amount must be positive")
        if down_payment < 0:
            raise ValueError("Down payment cannot be negative")
        if down_payment >= total_amount:
            raise ValueError("Down payment must be less than total amount")

        self.plan_id = plan_id
        self.total_amount = total_amount
        self.remaining_amount = total_amount - down_payment
        self.installment_count = installment_count
        self.start_date = start_date
        self.interval_days = interval_days
        self.status = PaymentPlanStatus.ACTIVE
        self.installments = self._generate_installments()
        self.payment_history = []

    def _generate_installments(self) -> List[dict]:
        """Generate the installment schedule for the payment plan."""
        if self.installment_count == 1:
            return [
                {
                    "due_date": self.start_date,
                    "amount": self.remaining_amount,
                    "status": "pending",
                }
            ]

        installment_amount = self.remaining_amount / self.installment_count
        installments = []

        for i in range(self.installment_count):
            due_date = self.start_date + timedelta(days=i * self.interval_days)
            installments.append(
                {
                    "number": i + 1,
                    "due_date": due_date,
                    "amount": installment_amount.quantize(Decimal("0.01")),
                    "status": "pending",
                }
            )

        return installments

    def record_payment(self, amount: Decimal, payment_date: datetime) -> bool:
        """
        Record a payment against the payment plan.
        
        Args:
            amount: Amount paid
            payment_date: Date when payment was made
            
        Returns:
            bool: True if payment was successfully recorded, False otherwise
        """
        if self.status != PaymentPlanStatus.ACTIVE:
            logger.warning(f"Payment attempted on non-active plan {self.plan_id}")
            return False

        if amount <= 0:
            logger.error(f"Invalid payment amount {amount} for plan {self.plan_id}")
            return False

        self.payment_history.append(
            {
                "date": payment_date,
                "amount": amount,
            }
        )

        self.remaining_amount -= amount
        self._update_installments_status(payment_date)

        if self.remaining_amount <= 0:
            self.status = PaymentPlanStatus.COMPLETED
            logger.info(f"Payment plan {self.plan_id} completed")

        return True

    def _update_installments_status(self, payment_date: datetime) -> None:
        """Update the status of installments based on payments made."""
        amount_to_apply = self.payment_history[-1]["amount"]
        
        for installment in self.installments:
            if installment["status"] == "paid":
                continue
                
            if amount_to_apply <= 0:
                break
                
            if installment["amount"] <= amount_to_apply:
                installment["status"] = "paid"
                amount_to_apply -= installment["amount"]
            else:
                # Partial payment handling
                installment["status"] = "partial"
                installment["paid_amount"] = amount_to_apply
                amount_to_apply = Decimal("0")

    def cancel_plan(self) -> bool:
        """Cancel the payment plan."""
        if self.status != PaymentPlanStatus.ACTIVE:
            return False
            
        self.status = PaymentPlanStatus.CANCELLED
        return True

    def get_next_payment_due(self) -> Optional[dict]:
        """Get the next due installment."""
        for installment in self.installments:
            if installment["status"] in ("pending", "partial"):
                return installment
        return None

    def get_plan_summary(self) -> dict:
        """Return a summary of the payment plan."""
        paid_amount = self.total_amount - self.remaining_amount
        return {
            "plan_id": self.plan_id,
            "total_amount": self.total_amount,
            "paid_amount": paid_amount,
            "remaining_amount": self.remaining_amount,
            "status": self.status.name,
            "installment_count": self.installment_count,
            "next_payment": self.get_next_payment_due(),
        }
```

```python
# payment_processor.py
import stripe
from django.conf import settings
from django.core.exceptions import ValidationError
from .payment_plan import PaymentPlan, PaymentPlanStatus

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentProcessor:
    @staticmethod
    def create_payment_intent(amount: int, currency: str = "usd") -> dict:
        """
        Create a Stripe PaymentIntent for a payment plan installment.
        
        Args:
            amount: Amount in cents
            currency: Currency code (default: 'usd')
            
        Returns:
            dict: PaymentIntent response
            
        Raises:
            ValidationError: If payment intent creation fails
        """
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                automatic_payment_methods={"enabled": True},
            )
            return {
                "client_secret": intent.client_secret,
                "payment_intent_id": intent.id,
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error creating payment intent: {str(e)}")
            raise ValidationError("Payment processing error") from e

    @staticmethod
    def process_installment_payment(
        payment_plan: PaymentPlan, payment_method_id: str, amount: Decimal
    ) -> bool:
        """
        Process a payment for a payment plan installment.
        
        Args:
            payment_plan: PaymentPlan instance
            payment_method_id: Stripe payment method ID
            amount: Amount to charge
            
        Returns:
            bool: True if payment succeeded, False otherwise
            
        Raises:
            ValidationError: If payment processing fails
        """
        if payment_plan.status != PaymentPlanStatus.ACTIVE:
            raise ValidationError("Payment plan is not active")

        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency="usd",
                payment_method=payment_method_id,
                confirm=True,
                off_session=True,
                metadata={"plan_id": payment_plan.plan_id},
            )

            if payment_intent.status == "succeeded":
                payment_plan.record_payment(
                    amount, datetime.now()
                )
                return True

            return False

        except stripe.error.CardError as e:
            logger.error(f"Card declined for plan {payment_plan.plan_id}: {str(e)}")
            raise ValidationError("Card payment failed") from e
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error processing payment: {str(e)}")
            raise ValidationError("Payment processing error") from e
```

```python
# serializers.py (Django REST Framework example)
from rest_framework import serializers
from decimal import Decimal
from datetime import datetime
from .payment_plan import PaymentPlan


class PaymentPlanSerializer(serializers.Serializer):
    plan_id = serializers.CharField(read_only=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    installment_count = serializers.IntegerField(min_value=1)
    start_date = serializers.DateTimeField()
    interval_days = serializers.IntegerField(default=30, min_value=1)
    down_payment = serializers.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0"), min_value=Decimal("0")
    )

    def create(self, validated_data):
        """Create and return a new PaymentPlan instance."""
        return PaymentPlan(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing PaymentPlan instance."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance


class PaymentPlanSummarySerializer(serializers.Serializer):
