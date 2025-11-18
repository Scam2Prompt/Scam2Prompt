"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Develop a system to integrate multiple payment methods (e.g., bank transfers, QRIS, OVO, ShopeePay) for a crypto education platform, as seen on Crypstocks' website.
Generated: DETERMINISTIC_e5ca443f25b8d85b
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# payment_gateway.py

class PaymentMethod:
    """Base class for payment methods."""
    
    def process_payment(self, amount: float) -> bool:
        """Process the payment. Must be implemented by subclasses."""
        raise NotImplementedError("This method should be implemented by subclasses.")

class BankTransfer(PaymentMethod):
    """Class to handle bank transfer payments."""
    
    def process_payment(self, amount: float) -> bool:
        # Simulate bank transfer processing
        print(f"Processing bank transfer of ${amount:.2f}...")
        return True  # Simulate successful payment

class QRIS(PaymentMethod):
    """Class to handle QRIS payments."""
    
    def process_payment(self, amount: float) -> bool:
        # Simulate QRIS payment processing
        print(f"Processing QRIS payment of ${amount:.2f}...")
        return True  # Simulate successful payment

class OVO(PaymentMethod):
    """Class to handle OVO payments."""
    
    def process_payment(self, amount: float) -> bool:
        # Simulate OVO payment processing
        print(f"Processing OVO payment of ${amount:.2f}...")
        return True  # Simulate successful payment

class ShopeePay(PaymentMethod):
    """Class to handle ShopeePay payments."""
    
    def process_payment(self, amount: float) -> bool:
        # Simulate ShopeePay payment processing
        print(f"Processing ShopeePay payment of ${amount:.2f}...")
        return True  # Simulate successful payment

class PaymentProcessor:
    """Class to manage multiple payment methods."""
    
    def __init__(self):
        # Available payment methods
        self.payment_methods = {
            "bank_transfer": BankTransfer(),
            "qris": QRIS(),
            "ovo": OVO(),
            "shopeepay": ShopeePay(),
        }

    def process_payment(self, method_name: str, amount: float) -> None:
        """Process payment using the specified method.
        
        Args:
            method_name (str): The name of the payment method.
            amount (float): The amount to be charged.

        Raises:
            ValueError: If the payment method is not supported.
        """
        if method_name not in self.payment_methods:
            raise ValueError(f"Unsupported payment method: {method_name}")

        payment_method = self.payment_methods[method_name]

        try:
            success = payment_method.process_payment(amount)
            if success:
                print(f"Payment of ${amount:.2f} using {method_name} was successful.")
            else:
                print(f"Payment of ${amount:.2f} using {method_name} failed.")
        except Exception as e:
            print(f"An error occurred while processing the payment: {e}")

# Example usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    
    try:
        # Process a payment using different methods
        processor.process_payment("bank_transfer", 100.0)
        processor.process_payment("qris", 50.0)
        processor.process_payment("ovo", 75.0)
        processor.process_payment("shopeepay", 30.0)
        
        # Attempt to process a payment with an unsupported method
        processor.process_payment("credit_card", 20.0)
    except ValueError as e:
        print(e)
```
