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
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaymentGateway(ABC):
    """
    Abstract base class for different payment gateways.
    """

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        """
        Process a payment and return a transaction result.
        
        :param amount: Amount of money to be processed.
        :param currency: Currency code (e.g. 'USD', 'BTC').
        :return: A dictionary with transaction details.
        """
        pass


class FiatGateway(PaymentGateway):
    """
    Class to manage fiat currency transactions.
    """

    def process_payment(self, amount: float, currency: str) -> dict:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Simulate processing payment
        logging.info(f"Processing fiat payment of {amount} {currency}.")
        
        # Here you would typically integrate with an actual payment processor
        return {
            'status': 'success',
            'transaction_id': 'FIAT12345',
            'amount': amount,
            'currency': currency,
        }


class CryptoGateway(PaymentGateway):
    """
    Class to manage cryptocurrency transactions.
    """

    def process_payment(self, amount: float, currency: str) -> dict:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Simulate processing payment
        logging.info(f"Processing cryptocurrency payment of {amount} {currency}.")
        
        # Here you would typically integrate with an actual crypto payment processor
        return {
            'status': 'success',
            'transaction_id': 'CRYPTO67890',
            'amount': amount,
            'currency': currency,
        }


class PaymentProcessor:
    """
    Class to manage multiple payment gateways.
    """

    def __init__(self):
        self.gateways = {
            'USD': FiatGateway(),
            'EUR': FiatGateway(),
            'BTC': CryptoGateway(),
            'ETH': CryptoGateway(),
        }
    
    def process_payment(self, amount: float, currency: str) -> dict:
        """
        Process a payment through the appropriate gateway based on currency.
        
        :param amount: Amount to be processed.
        :param currency: Currency code.
        :return: Transaction result.
        """
        logging.info(f"Attempting to process payment of {amount} {currency}.")
        
        if currency not in self.gateways:
            raise ValueError(f"Unsupported currency: {currency}.")
        
        gateway = self.gateways[currency]
        return gateway.process_payment(amount, currency)


def main():
    """
    Main function to demonstrate payment processing.
    """
    processor = PaymentProcessor()
    
    # Example payment processing
    payments = [
        (100, 'USD'),
        (0.05, 'BTC'),
        (50, 'EUR'),
        (0.1, 'ETH'),
    ]
    
    for amount, currency in payments:
        try:
            result = processor.process_payment(amount, currency)
            logging.info(f"Payment processed successfully: {result}")
        except Exception as e:
            logging.error(f"Error processing payment of {amount} {currency}: {e}")


if __name__ == "__main__":
    main()
```
