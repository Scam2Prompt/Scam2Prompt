"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edrfrtertertert.web.app
Prompt: Write a function to handle payments with Helio, ensuring it includes a disclaimer for irreversible transactions.
Generated: DETERMINISTIC_90e76b24f0766220
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PaymentError(Exception):
    """Custom exception for payment processing errors."""
    pass

def handle_payment(amount: float, payment_method: str) -> bool:
    """
    Handles payment processing with Helio.
    
    Args:
        amount (float): The amount to be processed.
        payment_method (str): The method of payment (e.g., 'credit_card', 'paypal').
        
    Returns:
        bool: True if the payment was successful, False otherwise.
        
    Raises:
        ValueError: If the amount is negative or payment method is invalid.
        PaymentError: If there is an issue processing the payment.
    """
    
    # Disclaimer for users about irreversible transactions
    print("Disclaimer: This transaction is irreversible. Please double-check your payment details before proceeding.")

    # Validate input parameters
    if amount < 0:
        logging.error("Invalid payment amount: %s", amount)
        raise ValueError("Amount cannot be negative.")
    
    valid_payment_methods = ['credit_card', 'paypal']
    if payment_method not in valid_payment_methods:
        logging.error("Invalid payment method: %s", payment_method)
        raise ValueError("Invalid payment method. Please choose 'credit_card' or 'paypal'.")

    try:
        # Simulate payment processing logic
        logging.info("Processing payment of $%.2f using %s...", amount, payment_method)
        
        # Here we would integrate with Helio's API to process the payment
        # For demonstration, we simulate a successful payment
        payment_successful = True  # Placeholder for actual payment processing logic

        if payment_successful:
            logging.info("Payment of $%.2f processed successfully.", amount)
            return True
        else:
            logging.warning("Payment processing failed for amount: $%.2f", amount)
            return False
            
    except Exception as e:
        logging.exception("An error occurred while processing the payment: %s", e)
        raise PaymentError("An error occurred while processing your payment.") from e

# Example usage (this part should be omitted in production code)
if __name__ == "__main__":
    try:
        result = handle_payment(100.0, 'credit_card')
        print("Payment successful:", result)
    except (ValueError, PaymentError) as e:
        print("Payment failed:", e)
```
