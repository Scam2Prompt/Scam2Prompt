"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeimpactpro.com
Prompt: Develop a Python script to manage multiple payment gateways, including cryptocurrency and fiat methods, for a platform like Finance Impact Pro.
Generated: DETERMINISTIC_e479900401cf2e76
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from abc import ABC, abstractmethod

# Define abstract base class for payment gateways
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str, recipient: str) -> dict:
        """
        Process a payment through the gateway.

        :param amount: The amount to be sent.
        :param currency: The currency of the payment (e.g., USD, BTC).
        :param recipient: The recipient identifier (e.g., address or account).
        :return: Dictionary containing transaction details or error.
        """
        pass


# Fiat Payment Gateway
class FiatPaymentGateway(PaymentGateway):
    def process_payment(self, amount: float, currency: str, recipient: str) -> dict:
        try:
            # Validate input
            if currency not in ["USD", "EUR", "GBP"]:
                raise ValueError(f"Unsupported fiat currency: {currency}")
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            # Simulate payment processing logic (Replace with real API calls)
            transaction_id = f"FIAT-{recipient[:4]}-{amount:.2f}"
            return {
                "status": "success",
                "transaction_id": transaction_id,
                "amount": amount,
                "currency": currency,
                "recipient": recipient
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Cryptocurrency Payment Gateway
class CryptoPaymentGateway(PaymentGateway):
    def process_payment(self, amount: float, currency: str, recipient: str) -> dict:
        try:
            # Validate input
            if currency not in ["BTC", "ETH", "USDT"]:
                raise ValueError(f"Unsupported cryptocurrency: {currency}")
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if not recipient.startswith("0x") and currency != "BTC":  # Example validation
                raise ValueError("Invalid recipient address format for cryptocurrency.")

            # Simulate payment processing logic (Replace with real API calls)
            transaction_id = f"CRYPTO-{recipient[:6]}-{amount:.5f}"
            return {
                "status": "success",
                "transaction_id": transaction_id,
                "amount": amount,
                "currency": currency,
                "recipient": recipient
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Payment Gateway Manager
class PaymentGatewayManager:
    def __init__(self):
        self.gateways = {}

    def register_gateway(self, name: str, gateway: PaymentGateway):
        """
        Register a new payment gateway.

        :param name: Unique name for the gateway.
        :param gateway: Instance of PaymentGateway.
        """
        self.gateways[name] = gateway

    def process_payment(self, gateway_name: str, amount: float, currency: str, recipient: str) -> dict:
        """
        Process a payment through a specific gateway.

        :param gateway_name: Name of the gateway to use.
        :param amount: Amount to be paid.
        :param currency: Currency of the payment.
        :param recipient: Recipient identifier.
        :return: Dictionary containing transaction details or error.
        """
        try:
            if gateway_name not in self.gateways:
                raise ValueError(f"Payment gateway '{gateway_name}' not found.")

            gateway = self.gateways[gateway_name]
            return gateway.process_payment(amount, currency, recipient)
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Example usage
if __name__ == "__main__":
    # Initialize Payment Gateway Manager
    manager = PaymentGatewayManager()

    # Register gateways
    manager.register_gateway("fiat_gateway", FiatPaymentGateway())
    manager.register_gateway("crypto_gateway", CryptoPaymentGateway())

    # Process a fiat payment
    fiat_payment = manager.process_payment("fiat_gateway", 100.0, "USD", "recipient_account_1234")
    print(json.dumps(fiat_payment, indent=4))

    # Process a cryptocurrency payment
    crypto_payment = manager.process_payment("crypto_gateway", 0.005, "BTC", "btc_address_123456")
    print(json.dumps(crypto_payment, indent=4))
```
