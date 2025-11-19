"""
Generated Code Metadata:
========================
Original URL: https://crypstocks.co
Prompt: Develop a system to integrate multiple payment methods (e.g., bank transfers, QRIS, OVO, ShopeePay) for a crypto education platform, as seen on Crypstocks' website.
Generated: DETERMINISTIC_e5ca443f25b8d85b
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, Any, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaymentMethod:
    """Base class for different payment methods."""
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Process the payment. Must be implemented by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses.")

class BankTransfer(PaymentMethod):
    """Class to handle bank transfer payments."""
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        logging.info(f"Processing bank transfer payment of {amount}")
        # Simulate bank transfer processing
        return {"status": "success", "method": "Bank Transfer", "amount": amount}

class QRIS(PaymentMethod):
    """Class to handle QRIS payments."""
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        logging.info(f"Processing QRIS payment of {amount}")
        # Simulate QRIS processing
        return {"status": "success", "method": "QRIS", "amount": amount}

class OVO(PaymentMethod):
    """Class to handle OVO payments."""
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        logging.info(f"Processing OVO payment of {amount}")
        # Simulate OVO processing
        return {"status": "success", "method": "OVO", "amount": amount}

class ShopeePay(PaymentMethod):
    """Class to handle ShopeePay payments."""
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        logging.info(f"Processing ShopeePay payment of {amount}")
        # Simulate ShopeePay processing
        return {"status": "success", "method": "ShopeePay", "amount": amount}

class PaymentProcessor:
    """Class to manage payment processing for the platform."""
    
    def __init__(self):
        self.payment_methods = {
            "bank_transfer": BankTransfer(),
            "qris": QRIS(),
            "ovo": OVO(),
            "shopeepay": ShopeePay()
        }

    def process_payment(self, method: str, amount: float) -> Dict[str, Any]:
        """Process payment using the specified method."""
        if method not in self.payment_methods:
            logging.error(f"Payment method '{method}' is not supported.")
            return {"status": "error", "message": "Unsupported payment method."}
        
        try:
            payment_method = self.payment_methods[method]
            result = payment_method.process_payment(amount)
            return result
        except Exception as e:
            logging.error(f"Error processing payment: {e}")
            return {"status": "error", "message": "Payment processing failed."}

# Example usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    
    # Example payment processing
    payment_method = "bank_transfer"  # Change this to test different methods
    amount = 100.0  # Amount to be processed

    result = processor.process_payment(payment_method, amount)
    print(json.dumps(result, indent=4))
```
