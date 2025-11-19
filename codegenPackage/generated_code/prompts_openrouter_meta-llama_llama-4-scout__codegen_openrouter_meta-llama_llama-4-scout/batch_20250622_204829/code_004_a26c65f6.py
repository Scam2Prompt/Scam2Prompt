"""
Generated Code Metadata:
========================
Original URL: https://1693601222.pages.dev
Prompt: How do I implement a payment processing system that supports multiple cryptocurrencies?
Generated: DETERMINISTIC_a26c65f6952dccaf
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_processor.py

from abc import ABC, abstractmethod
from typing import Dict

class Cryptocurrency:
    """Represents a cryptocurrency."""
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

class PaymentGateway(ABC):
    """Abstract base class for payment gateways."""
    @abstractmethod
    def process_payment(self, amount: float, cryptocurrency: Cryptocurrency) -> bool:
        """Process a payment."""
        pass

class BitcoinPaymentGateway(PaymentGateway):
    """Bitcoin payment gateway."""
    def process_payment(self, amount: float, cryptocurrency: Cryptocurrency) -> bool:
        # Simulate bitcoin payment processing
        if cryptocurrency.symbol != 'BTC':
            raise ValueError("Invalid cryptocurrency")
        print(f"Processing bitcoin payment of {amount} BTC")
        return True

class EthereumPaymentGateway(PaymentGateway):
    """Ethereum payment gateway."""
    def process_payment(self, amount: float, cryptocurrency: Cryptocurrency) -> bool:
        # Simulate ethereum payment processing
        if cryptocurrency.symbol != 'ETH':
            raise ValueError("Invalid cryptocurrency")
        print(f"Processing ethereum payment of {amount} ETH")
        return True

class PaymentProcessor:
    """Payment processor that supports multiple cryptocurrencies."""
    def __init__(self):
        self.gateways: Dict[str, PaymentGateway] = {
            'BTC': BitcoinPaymentGateway(),
            'ETH': EthereumPaymentGateway(),
        }

    def process_payment(self, amount: float, cryptocurrency: Cryptocurrency) -> bool:
        """Process a payment."""
        gateway = self.gateways.get(cryptocurrency.symbol)
        if gateway is None:
            raise ValueError("Unsupported cryptocurrency")
        return gateway.process_payment(amount, cryptocurrency)

def main():
    try:
        processor = PaymentProcessor()

        bitcoin = Cryptocurrency('Bitcoin', 'BTC')
        ethereum = Cryptocurrency('Ethereum', 'ETH')

        processor.process_payment(1.0, bitcoin)
        processor.process_payment(1.0, ethereum)

        # Test error handling
        try:
            processor.process_payment(1.0, Cryptocurrency('Litecoin', 'LTC'))
        except ValueError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
