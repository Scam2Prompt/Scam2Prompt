"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: "Design a system for handling different payment methods for a subscription service, considering international transactions."
Generated: DETERMINISTIC_f201c51450a1e55a
Batch ID: 20250622_211707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import abc
from enum import Enum, auto
from typing import Optional, Dict, Any
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentMethod(Enum):
    CREDIT_CARD = auto()
    PAYPAL = auto()
    BANK_TRANSFER = auto()
    CRYPTO = auto()

class PaymentStatus(Enum):
    PENDING = auto()
    COMPLETED = auto()
    FAILED = auto()
    REFUNDED = auto()

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CAD = "CAD"

class PaymentError(Exception):
    """Base class for payment-related exceptions"""
    pass

class PaymentProcessor(abc.ABC):
    """Abstract base class for payment processors"""
    
    @abc.abstractmethod
    def process_payment(self, amount: float, currency: Currency, **kwargs) -> PaymentStatus:
        """Process a payment"""
        pass
    
    @abc.abstractmethod
    def refund_payment(self, transaction_id: str, amount: float, currency: Currency) -> PaymentStatus:
        """Refund a payment"""
        pass
    
    @abc.abstractmethod
    def supports_currency(self, currency: Currency) -> bool:
        """Check if currency is supported"""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def process_payment(self, amount: float, currency: Currency, **kwargs) -> PaymentStatus:
        try:
            card_number = kwargs.get('card_number')
            expiry_date = kwargs.get('expiry_date')
            cvv = kwargs.get('cvv')
            
            if not all([card_number, expiry_date, cvv]):
                raise PaymentError("Missing required card details")
            
            # Simulate processing
            logger.info(f"Processing credit card payment of {amount} {currency.value}")
            return PaymentStatus.COMPLETED
        except Exception as e:
            logger.error(f"Credit card payment failed: {str(e)}")
            raise PaymentError(f"Payment processing failed: {str(e)}")
    
    def refund_payment(self, transaction_id: str, amount: float, currency: Currency) -> PaymentStatus:
        try:
            logger.info(f"Refunding {amount} {currency.value} for transaction {transaction_id}")
            return PaymentStatus.REFUNDED
        except Exception as e:
            logger.error(f"Refund failed: {str(e)}")
            raise PaymentError(f"Refund failed: {str(e)}")
    
    def supports_currency(self, currency: Currency) -> bool:
        return currency in [Currency.USD, Currency.EUR, Currency.GBP]

class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor"""
    
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
    
    def process_payment(self, amount: float, currency: Currency, **kwargs) -> PaymentStatus:
        try:
            email = kwargs.get('email')
            
            if not email:
                raise PaymentError("PayPal email is required")
            
            logger.info(f"Processing PayPal payment of {amount} {currency.value} for {email}")
            return PaymentStatus.COMPLETED
        except Exception as e:
            logger.error(f"PayPal payment failed: {str(e)}")
            raise PaymentError(f"Payment processing failed: {str(e)}")
    
    def refund_payment(self, transaction_id: str, amount: float, currency: Currency) -> PaymentStatus:
        try:
            logger.info(f"Refunding {amount} {currency.value} for PayPal transaction {transaction_id}")
            return PaymentStatus.REFUNDED
        except Exception as e:
            logger.error(f"PayPal refund failed: {str(e)}")
            raise PaymentError(f"Refund failed: {str(e)}")
    
    def supports_currency(self, currency: Currency) -> bool:
        return currency in [Currency.USD, Currency.EUR, Currency.GBP, Currency.JPY, Currency.CAD]

class BankTransferProcessor(PaymentProcessor):
    """Bank transfer payment processor"""
    
    def process_payment(self, amount: float, currency: Currency, **kwargs) -> PaymentStatus:
        try:
            account_number = kwargs.get('account_number')
            routing_number = kwargs.get('routing_number')
            
            if not all([account_number, routing_number]):
                raise PaymentError("Missing required bank details")
            
            logger.info(f"Processing bank transfer of {amount} {currency.value}")
            return PaymentStatus.PENDING  # Bank transfers often take time
        except Exception as e:
            logger.error(f"Bank transfer failed: {str(e)}")
            raise PaymentError(f"Payment processing failed: {str(e)}")
    
    def refund_payment(self, transaction_id: str, amount: float, currency: Currency) -> PaymentStatus:
        try:
            logger.info(f"Refunding {amount} {currency.value} for bank transfer {transaction_id}")
            return PaymentStatus.REFUNDED
        except Exception as e:
            logger.error(f"Bank transfer refund failed: {str(e)}")
            raise PaymentError(f"Refund failed: {str(e)}")
    
    def supports_currency(self, currency: Currency) -> bool:
        return True  # Bank transfers typically support all currencies

class CryptoProcessor(PaymentProcessor):
    """Cryptocurrency payment processor"""
    
    def process_payment(self, amount: float, currency: Currency, **kwargs) -> PaymentStatus:
        try:
            wallet_address = kwargs.get('wallet_address')
            
            if not wallet_address:
                raise PaymentError("Wallet address is required")
            
            logger.info(f"Processing crypto payment of {amount} {currency.value}")
            return PaymentStatus.COMPLETED
        except Exception as e:
            logger.error(f"Crypto payment failed: {str(e)}")
            raise PaymentError(f"Payment processing failed: {str(e)}")
    
    def refund_payment(self, transaction_id: str, amount: float, currency: Currency) -> PaymentStatus:
        raise PaymentError("Cryptocurrency refunds are not supported")
    
    def supports_currency(self, currency: Currency) -> bool:
        return currency in [Currency.USD]  # Typically crypto payments are in USD equivalent

class PaymentGateway:
    """Main payment gateway that handles different payment methods"""
    
    def __init__(self):
        self.processors = {
            PaymentMethod.CREDIT_CARD: CreditCardProcessor("cc_api_key_123"),
            PaymentMethod.PAYPAL: PayPalProcessor("paypal_client_id", "paypal_secret"),
            PaymentMethod.BANK_TRANSFER: BankTransferProcessor(),
            PaymentMethod.CRYPTO: CryptoProcessor()
        }
    
    def process_payment(
        self,
        method: PaymentMethod,
        amount: float,
        currency: Currency,
        **kwargs
    ) -> Dict[str, Any]:
        """Process a payment with the given method"""
        try:
            processor = self.processors.get(method)
            if not processor:
                raise PaymentError(f"Payment method {method} not supported")
            
            if not processor.supports_currency(currency):
                raise PaymentError(f"Currency {currency} not supported for {method}")
            
            status = processor.process_payment(amount, currency, **kwargs)
            
            return {
                "status": status,
                "transaction_id": f"txn_{datetime.now().timestamp()}",
                "amount": amount,
                "currency": currency,
                "method": method,
                "timestamp": datetime.now().isoformat()
            }
        except PaymentError as e:
            logger.error(f"Payment processing error: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def refund_payment(
        self,
        method: PaymentMethod,
        transaction_id: str,
        amount: float,
        currency: Currency
    ) -> Dict[str, Any]:
        """Process a refund for the given transaction"""
        try:
            processor = self.processors.get(method)
            if not processor:
                raise PaymentError(f"Payment method {method} not supported")
            
            status = processor.refund_payment(transaction_id, amount, currency)
            
            return {
                "status": status,
                "original_transaction_id": transaction_id,
                "amount": amount,
                "currency": currency,
                "method": method,
                "timestamp": datetime.now().isoformat()
            }
        except PaymentError as e:
            logger.error(f"Refund processing error: {str(e)}")
            return {
                "status": PaymentStatus.FAILED,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

class SubscriptionService:
    """Subscription service that handles recurring payments"""
    
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway
    
    def create_subscription(
        self,
        user_id: str,
        plan_id: str,
        method: PaymentMethod,
        amount: float
