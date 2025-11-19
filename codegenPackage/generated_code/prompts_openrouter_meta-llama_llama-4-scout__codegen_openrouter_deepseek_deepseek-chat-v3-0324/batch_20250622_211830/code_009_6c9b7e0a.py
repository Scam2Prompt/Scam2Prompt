"""
Generated Code Metadata:
========================
Original URL: https://digielearning.in
Prompt: "Design a secure payment gateway for processing transactions related to e-book purchases and subscriptions on a platform like Digielearning, considering multiple payment options."
Generated: DETERMINISTIC_6c9b7e0a35fbb96f
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Union
import stripe
from paypalrestsdk import Payment
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Payment providers
class PaymentProvider(Enum):
    STRIPE = "stripe"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

# Payment statuses
class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

# Initialize payment providers
stripe.api_key = os.getenv("STRIPE_API_KEY")
paypalrestsdk.configure({
    "mode": os.getenv("PAYPAL_MODE", "sandbox"),
    "client_id": os.getenv("PAYPAL_CLIENT_ID"),
    "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
})

# Encryption setup for sensitive data
ENCRYPTION_KEY = os.getenv("PAYMENT_ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("Payment encryption key not configured")
cipher_suite = Fernet(ENCRYPTION_KEY)

class PaymentGateway:
    """Secure payment gateway for processing e-book transactions."""
    
    def __init__(self):
        self._validate_environment()
    
    def _validate_environment(self):
        """Validate required environment variables."""
        required_vars = [
            "STRIPE_API_KEY",
            "PAYPAL_CLIENT_ID",
            "PAYPAL_CLIENT_SECRET",
            "PAYMENT_ENCRYPTION_KEY"
        ]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
    
    def _encrypt_data(self, data: str) -> str:
        """Encrypt sensitive payment data."""
        return cipher_suite.encrypt(data.encode()).decode()
    
    def _decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive payment data."""
        return cipher_suite.decrypt(encrypted_data.encode()).decode()
    
    def process_payment(
        self,
        amount: float,
        currency: str,
        payment_method: PaymentProvider,
        payment_details: Dict,
        user_id: str,
        description: str = "E-book purchase"
    ) -> Dict[str, Union[str, PaymentStatus]]:
        """
        Process a payment transaction.
        
        Args:
            amount: Transaction amount
            currency: Currency code (e.g., 'USD')
            payment_method: Payment provider
            payment_details: Payment method details
            user_id: User ID making the payment
            description: Transaction description
            
        Returns:
            Dictionary containing payment status and transaction details
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            if payment_method == PaymentProvider.STRIPE:
                return self._process_stripe_payment(
                    amount, currency, payment_details, user_id, description
                )
            elif payment_method == PaymentProvider.PAYPAL:
                return self._process_paypal_payment(
                    amount, currency, payment_details, user_id, description
                )
            elif payment_method == PaymentProvider.BANK_TRANSFER:
                return self._process_bank_transfer(
                    amount, currency, payment_details, user_id, description
                )
            else:
                raise ValueError("Unsupported payment method")
                
        except Exception as e:
            logger.error(f"Payment processing failed: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "transaction_id": None,
                "error": str(e)
            }
    
    def _process_stripe_payment(
        self,
        amount: float,
        currency: str,
        payment_details: Dict,
        user_id: str,
        description: str
    ) -> Dict[str, Union[str, PaymentStatus]]:
        """Process payment using Stripe."""
        try:
            # Encrypt sensitive card details
            encrypted_card = {
                "number": self._encrypt_data(payment_details["card_number"]),
                "exp_month": payment_details["exp_month"],
                "exp_year": payment_details["exp_year"],
                "cvc": self._encrypt_data(payment_details["cvc"])
            }
            
            # Create payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency.lower(),
                payment_method_types=["card"],
                description=description,
                metadata={"user_id": user_id}
            )
            
            # Confirm payment
            confirmed_intent = stripe.PaymentIntent.confirm(
                payment_intent.id,
                payment_method={
                    "card": {
                        "number": self._decrypt_data(encrypted_card["number"]),
                        "exp_month": encrypted_card["exp_month"],
                        "exp_year": encrypted_card["exp_year"],
                        "cvc": self._decrypt_data(encrypted_card["cvc"])
                    }
                }
            )
            
            if confirmed_intent.status == "succeeded":
                return {
                    "status": PaymentStatus.COMPLETED,
                    "transaction_id": confirmed_intent.id,
                    "provider": PaymentProvider.STRIPE.value
                }
            else:
                return {
                    "status": PaymentStatus.FAILED,
                    "transaction_id": confirmed_intent.id,
                    "error": confirmed_intent.last_payment_error or "Payment failed"
                }
                
        except stripe.error.StripeError as e:
            logger.error(f"Stripe payment failed: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "transaction_id": None,
                "error": str(e)
            }
    
    def _process_paypal_payment(
        self,
        amount: float,
        currency: str,
        payment_details: Dict,
        user_id: str,
        description: str
    ) -> Dict[str, Union[str, PaymentStatus]]:
        """Process payment using PayPal."""
        try:
            payment = Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "transactions": [{
                    "amount": {
                        "total": str(amount),
                        "currency": currency
                    },
                    "description": description,
                    "custom": user_id
                }],
                "redirect_urls": {
                    "return_url": os.getenv("PAYPAL_RETURN_URL"),
                    "cancel_url": os.getenv("PAYPAL_CANCEL_URL")
                }
            })
            
            if payment.create():
                return {
                    "status": PaymentStatus.PENDING,
                    "transaction_id": payment.id,
                    "approval_url": next(
                        link.href for link in payment.links if link.rel == "approval_url"
                    ),
                    "provider": PaymentProvider.PAYPAL.value
                }
            else:
                return {
                    "status": PaymentStatus.FAILED,
                    "transaction_id": None,
                    "error": payment.error or "PayPal payment creation failed"
                }
                
        except Exception as e:
            logger.error(f"PayPal payment failed: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "transaction_id": None,
                "error": str(e)
            }
    
    def _process_bank_transfer(
        self,
        amount: float,
        currency: str,
        payment_details: Dict,
        user_id: str,
        description: str
    ) -> Dict[str, Union[str, PaymentStatus]]:
        """Process bank transfer payment."""
        try:
            # Validate bank details
            required_fields = ["account_number", "routing_number", "account_name"]
            for field in required_fields:
                if field not in payment_details:
                    raise ValueError(f"Missing required field: {field}")
            
            # Encrypt sensitive bank details
            encrypted_details = {
                "account_number": self._encrypt_data(payment_details["account_number"]),
                "routing_number": self._encrypt_data(payment_details["routing_number"]),
                "account_name": self._encrypt_data(payment_details["account_name"])
            }
            
            # In a real implementation, this would interface with a bank API
            # For demo purposes, we'll simulate a successful transfer
            transaction_id = f"BANK-{datetime.now().strftime('%Y%m%d%H%M%S')}-{user_id}"
            
            return {
                "status": PaymentStatus.PENDING,  # Bank transfers often take time to clear
                "transaction_id": transaction_id,
                "provider": PaymentProvider.BANK_TRANSFER.value
            }
            
        except Exception as e:
            logger.error(f"Bank transfer failed: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "transaction_id": None
