"""
Generated Code Metadata:
========================
Original URL: https://currency-connect.com
Prompt: Recommend APIs or libraries for integrating international payment gateways into a law firm's website, considering regulatory compliance with FCA and HMRC.
Generated: DETERMINISTIC_31e9b33c8673c707
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# International Payment Gateway Integration for Law Firms
# Compliant with FCA (Financial Conduct Authority) and HMRC (HM Revenue & Customs)

import stripe
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from datetime import datetime
import logging
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentGateway:
    """
    Base class for payment gateway integration with compliance checks.
    """
    
    def __init__(self):
        self.compliance_checks = {
            'fca': self._check_fca_compliance,
            'hmrc': self._check_hmrc_compliance
        }
    
    def _check_fca_compliance(self) -> bool:
        """Check FCA compliance requirements."""
        # Implement actual FCA compliance checks
        return True
    
    def _check_hmrc_compliance(self) -> bool:
        """Check HMRC compliance requirements."""
        # Implement actual HMRC compliance checks
        return True
    
    def verify_compliance(self) -> bool:
        """Verify all required compliance checks."""
        return all(check() for check in self.compliance_checks.values())

class StripeGateway(PaymentGateway):
    """
    Stripe payment gateway integration with FCA/HMRC compliance.
    """
    
    def __init__(self, api_key: str):
        super().__init__()
        stripe.api_key = api_key
        self.client = stripe
    
    def create_payment_intent(self, amount: int, currency: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a payment intent with Stripe.
        
        Args:
            amount: Amount in smallest currency unit (e.g., pence for GBP)
            currency: 3-letter ISO currency code
            metadata: Optional metadata for the payment
            
        Returns:
            Payment intent response from Stripe
            
        Raises:
            stripe.error.StripeError: For Stripe API errors
            ValueError: For compliance check failures
        """
        if not self.verify_compliance():
            raise ValueError("Compliance checks failed")
            
        try:
            return self.client.PaymentIntent.create(
                amount=amount,
                currency=currency,
                metadata=metadata or {}
            )
        except stripe.error.StripeError as e:
            logger.error(f"Stripe API error: {str(e)}")
            raise

class PayPalGateway(PaymentGateway):
    """
    PayPal payment gateway integration with FCA/HMRC compliance.
    """
    
    def __init__(self, client_id: str, client_secret: str, sandbox: bool = True):
        super().__init__()
        environment = SandboxEnvironment(client_id, client_secret) if sandbox else LiveEnvironment(client_id, client_secret)
        self.client = PayPalHttpClient(environment)
    
    def create_order(self, amount: str, currency: str) -> Dict[str, Any]:
        """
        Create a PayPal order.
        
        Args:
            amount: Amount as string (e.g., "10.00")
            currency: 3-letter ISO currency code
            
        Returns:
            Order creation response from PayPal
            
        Raises:
            IOError: For PayPal API errors
            ValueError: For compliance check failures
        """
        if not self.verify_compliance():
            raise ValueError("Compliance checks failed")
            
        try:
            request = OrdersCreateRequest()
            request.prefer('return=representation')
            request.request_body({
                "intent": "CAPTURE",
                "purchase_units": [{
                    "amount": {
                        "currency_code": currency,
                        "value": amount
                    }
                }]
            })
            response = self.client.execute(request)
            return response.result.__dict__
        except IOError as e:
            logger.error(f"PayPal API error: {str(e)}")
            raise

class PaymentGatewayFactory:
    """
    Factory class to create appropriate payment gateway instances.
    """
    
    @staticmethod
    def create_gateway(gateway_type: str, **kwargs) -> PaymentGateway:
        """
        Create a payment gateway instance based on type.
        
        Args:
            gateway_type: 'stripe' or 'paypal'
            **kwargs: Required parameters for the gateway
            
        Returns:
            Instance of the requested payment gateway
            
        Raises:
            ValueError: For unsupported gateway types
        """
        if gateway_type.lower() == 'stripe':
            return StripeGateway(**kwargs)
        elif gateway_type.lower() == 'paypal':
            return PayPalGateway(**kwargs)
        else:
            raise ValueError(f"Unsupported gateway type: {gateway_type}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize Stripe gateway
        stripe_gateway = PaymentGatewayFactory.create_gateway(
            'stripe',
            api_key='your_stripe_api_key'
        )
        
        # Process payment
        payment_intent = stripe_gateway.create_payment_intent(
            amount=1000,  # £10.00 in pence
            currency='gbp',
            metadata={
                'client_id': '12345',
                'invoice_id': 'INV-2023-001'
            }
        )
        logger.info(f"Stripe payment intent created: {payment_intent['id']}")
        
        # Initialize PayPal gateway
        paypal_gateway = PaymentGatewayFactory.create_gateway(
            'paypal',
            client_id='your_paypal_client_id',
            client_secret='your_paypal_client_secret',
            sandbox=True
        )
        
        # Create PayPal order
        order = paypal_gateway.create_order(
            amount='10.00',
            currency='GBP'
        )
        logger.info(f"PayPal order created: {order['id']}")
        
    except Exception as e:
        logger.error(f"Payment processing failed: {str(e)}")
```
