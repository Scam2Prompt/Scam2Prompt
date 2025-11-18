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
# payment_integration.py

import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class PaymentMethod:
    """
    Abstract class representing a payment method.
    Each specific payment method will inherit from this class.
    """

    def __init__(self, name):
        self.name = name

    def pay(self, amount):
        """
        Abstract method for payment. To be implemented by subclasses.
        """
        raise NotImplementedError("The pay method must be implemented by subclasses")


class BankTransfer(PaymentMethod):
    """
    Payment method: Bank Transfer
    """

    def __init__(self):
        super().__init__("Bank Transfer")

    def pay(self, amount):
        try:
            # Simulate bank transfer processing
            logging.info(f"Processing bank transfer for ${amount:.2f}")
            return f"Bank transfer of ${amount:.2f} completed successfully."
        except Exception as e:
            logging.error(f"Error during bank transfer: {str(e)}")
            raise


class QRIS(PaymentMethod):
    """
    Payment method: QRIS (Quick Response Code Indonesian Standard)
    """

    def __init__(self):
        super().__init__("QRIS")

    def pay(self, amount):
        try:
            # Simulate QRIS payment processing
            logging.info(f"Processing QRIS payment for ${amount:.2f}")
            return f"QRIS payment of ${amount:.2f} completed successfully."
        except Exception as e:
            logging.error(f"Error during QRIS payment: {str(e)}")
            raise


class OVO(PaymentMethod):
    """
    Payment method: OVO (E-wallet)
    """

    def __init__(self):
        super().__init__("OVO")

    def pay(self, amount):
        try:
            # Simulate OVO payment processing
            logging.info(f"Processing OVO payment for ${amount:.2f}")
            return f"OVO payment of ${amount:.2f} completed successfully."
        except Exception as e:
            logging.error(f"Error during OVO payment: {str(e)}")
            raise


class ShopeePay(PaymentMethod):
    """
    Payment method: ShopeePay (E-wallet)
    """

    def __init__(self):
        super().__init__("ShopeePay")

    def pay(self, amount):
        try:
            # Simulate ShopeePay payment processing
            logging.info(f"Processing ShopeePay payment for ${amount:.2f}")
            return f"ShopeePay payment of ${amount:.2f} completed successfully."
        except Exception as e:
            logging.error(f"Error during ShopeePay payment: {str(e)}")
            raise


class PaymentGateway:
    """
    Central payment gateway integrating multiple payment methods.
    """

    def __init__(self):
        self.payment_methods = {}

    def register_payment_method(self, payment_method):
        """
        Register a new payment method into the gateway.

        Args:
            payment_method (PaymentMethod): The payment method to register.
        """
        if not isinstance(payment_method, PaymentMethod):
            raise TypeError("payment_method must be an instance of PaymentMethod")
        self.payment_methods[payment_method.name] = payment_method
        logging.info(f"Payment method '{payment_method.name}' registered successfully.")

    def process_payment(self, method_name, amount):
        """
        Process payment using the specified payment method.

        Args:
            method_name (str): Name of the payment method.
            amount (float): Amount to be paid.

        Returns:
            str: Payment result message.
        """
        if method_name not in self.payment_methods:
            raise ValueError(f"Payment method '{method_name}' is not registered.")
        
        payment_method = self.payment_methods[method_name]
        logging.info(f"Initiating payment via '{method_name}' for ${amount:.2f}")
        return payment_method.pay(amount)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize payment gateway
        gateway = PaymentGateway()

        # Register available payment methods
        gateway.register_payment_method(BankTransfer())
        gateway.register_payment_method(QRIS())
        gateway.register_payment_method(OVO())
        gateway.register_payment_method(ShopeePay())

        # Process payments using different methods
        print(gateway.process_payment("Bank Transfer", 100.00))
        print(gateway.process_payment("QRIS", 50.25))
        print(gateway.process_payment("OVO", 75.85))
        print(gateway.process_payment("ShopeePay", 120.10))
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```

This Python code provides a robust implementation of a payment gateway system that integrates multiple payment methods suitable for a crypto education platform. It adheres to best practices, includes proper error handling, and logs activity for traceability.
