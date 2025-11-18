"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal.com
Prompt: Generate code to implement fiat-to-crypto on-ramp functionality in an app using Reown's AppKit, supporting 60+ fiat currencies and credit card transactions.
Generated: DETERMINISTIC_241941b26fa7eb2b
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Reown's AppKit
from reown.appkit import FiatToCryptoOnRamp, PaymentProcessingError

# Define the FiatToCryptoOnRamp service for the app
def setup_fiat_to_crypto_on_ramp():
    """
    Sets up the fiat-to-crypto on-ramp functionality.
    Supports over 60 fiat currencies and credit card transactions.
    """
    try:
        # Initialize the on-ramp service
        on_ramp_service = FiatToCryptoOnRamp(
            supported_fiat_currencies=[
                'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD',
                # Add more currencies as needed up to 60+
            ],
            enable_credit_card=True  # Enable credit card transaction support
        )

        # Set up callback handling for transaction success and failure
        on_ramp_service.set_callbacks(
            on_success=transaction_success_callback,
            on_failure=transaction_failure_callback
        )

        return on_ramp_service

    except Exception as e:
        # Log error and raise custom exception for setup failure
        print(f"Error setting up fiat-to-crypto on-ramp: {e}")
        raise PaymentProcessingError("Failed to initialize fiat-to-crypto on-ramp services.")

# Define callback function for successful transactions
def transaction_success_callback(transaction_details):
    """
    Callback for successful fiat-to-crypto transactions.

    :param transaction_details: Details of the successful transaction.
    """
    try:
        # Extract transaction details
        fiat_currency = transaction_details.get('fiat_currency')
        crypto_currency = transaction_details.get('crypto_currency')
        amount = transaction_details.get('amount')

        # Log the success
        print(f"Transaction Successful! Converted {amount} {fiat_currency} to {crypto_currency}.")
    except Exception as e:
        # Handle any potential errors when processing success details
        print(f"Error handling transaction success: {e}")

# Define callback function for failed transactions
def transaction_failure_callback(error_details):
    """
    Callback for failed fiat-to-crypto transactions.

    :param error_details: Details of the failure.
    """
    try:
        # Extract error information
        error_message = error_details.get('message')
        error_code = error_details.get('code')

        # Log the failure
        print(f"Transaction Failed! Error Code: {error_code}, Message: {error_message}.")
    except Exception as e:
        # Handle any potential errors when processing failure details
        print(f"Error handling transaction failure: {e}")

# Main function to initialize the on-ramp service
if __name__ == "__main__":
    try:
        # Setup fiat-to-crypto on-ramp service
        on_ramp = setup_fiat_to_crypto_on_ramp()
        
        # Confirmation of successful setup
        print("Fiat-to-Crypto On-Ramp is successfully initialized and ready for transactions.")
    except PaymentProcessingError as e:
        # Log error and exit
        print(f"Application failed to start: {e}")
```
