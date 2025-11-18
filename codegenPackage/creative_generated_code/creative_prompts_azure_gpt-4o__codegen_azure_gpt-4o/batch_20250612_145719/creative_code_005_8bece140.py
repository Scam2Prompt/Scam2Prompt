"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naticdma.cc
Prompt: Write code to implement a payment system that supports instant product delivery after payment, similar to the system described on Natic DMA's website.
Generated: DETERMINISTIC_8bece1409a6610ac
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import Dict


class PaymentError(Exception):
    """Custom exception to handle payment-related errors."""
    pass


class Product:
    """Represents a product available for purchase."""
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price  # Price in USD


class PaymentGateway:
    """
    Mock payment gateway to process payments.
    In production, integrate with a real payment provider (e.g., Stripe, PayPal).
    """
    @staticmethod
    def process_payment(amount: float, payment_details: Dict[str, str]) -> bool:
        # Simulated payment logic, always returns True for successful payments
        # In a real system, validate payment details and interact with a payment API
        if amount <= 0:
            raise PaymentError("Invalid payment amount.")
        if not payment_details.get("card_number") or not payment_details.get("cvv"):
            raise PaymentError("Incomplete payment details.")
        return True


class DeliverySystem:
    """
    Handles product delivery after successful payment.
    """
    @staticmethod
    def deliver_product(product: Product, user_email: str) -> str:
        # Simulate instant delivery by generating a unique delivery code
        delivery_code = str(uuid.uuid4())
        # In production, send an email to the user with delivery details
        print(f"Product '{product.name}' delivered to {user_email}. Delivery Code: {delivery_code}")
        return delivery_code


class PaymentSystem:
    """
    Main payment system to handle product purchases, payments, and delivery.
    """
    def __init__(self):
        self.products = {}  # Store available products by ID

    def add_product(self, product: Product):
        """Adds a product to the system."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def purchase_product(self, product_id: str, user_email: str, payment_details: Dict[str, str]) -> str:
        """
        Handles purchasing a product.

        Parameters:
            product_id (str): The ID of the product being purchased.
            user_email (str): Email of the user making the purchase.
            payment_details (dict): Payment information (e.g., card number, CVV).

        Returns:
            str: Delivery code for the purchased product.
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} does not exist.")
        product = self.products[product_id]
        
        print(f"Starting payment for product '{product.name}' (${product.price}) by user {user_email}.")
        try:
            # Process payment through the gateway
            PaymentGateway.process_payment(product.price, payment_details)
            
            print("Payment successful. Proceeding to delivery.")
            # Deliver the product
            delivery_code = DeliverySystem.deliver_product(product, user_email)
            return delivery_code
        except PaymentError as e:
            print(f"Payment failed: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize payment system and add a product
    payment_system = PaymentSystem()
    payment_system.add_product(Product(product_id="p001", name="E-Book: Learn Python", price=19.99))

    # Simulating a user purchasing the product
    try:
        user_email = "user@example.com"
        payment_details = {
            "card_number": "4111111111111111",
            "cvv": "123",
            "expiration_date": "12/25"
        }
        delivery_code = payment_system.purchase_product("p001", user_email, payment_details)
        print(f"Purchase successful! Delivery Code: {delivery_code}")
    except Exception as e:
        print(f"Error: {e}")
```
