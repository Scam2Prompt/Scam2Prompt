"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Generate a guide on how to integrate a payment gateway with a charitable donation feature, similar to UniSwop's system, which donates a percentage of transactions to the Irish Cancer Society.
Generated: DETERMINISTIC_2ef9c34b1922eb9e
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_gateway_integrator.py

import os
import logging
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaymentGatewayIntegrator:
    """
    Integrates a payment gateway with a charitable donation feature.

    Attributes:
    - gateway_url (str): The URL of the payment gateway.
    - api_key (str): The API key for the payment gateway.
    - charity_name (str): The name of the charity.
    - charity_account_number (str): The account number of the charity.
    - donation_percentage (float): The percentage of transactions to donate.
    """

    def __init__(self, 
                 gateway_url: str, 
                 api_key: str, 
                 charity_name: str, 
                 charity_account_number: str, 
                 donation_percentage: float):
        """
        Initializes the PaymentGatewayIntegrator.

        Args:
        - gateway_url (str): The URL of the payment gateway.
        - api_key (str): The API key for the payment gateway.
        - charity_name (str): The name of the charity.
        - charity_account_number (str): The account number of the charity.
        - donation_percentage (float): The percentage of transactions to donate.
        """
        self.gateway_url = gateway_url
        self.api_key = api_key
        self.charity_name = charity_name
        self.charity_account_number = charity_account_number
        self.donation_percentage = donation_percentage

    def process_transaction(self, amount: float, payment_method: str) -> Dict:
        """
        Processes a transaction and donates a percentage to the charity.

        Args:
        - amount (float): The amount of the transaction.
        - payment_method (str): The payment method used.

        Returns:
        - A dictionary containing the transaction result and donation details.
        """
        try:
            # Validate input parameters
            if amount <= 0:
                raise ValueError("Invalid transaction amount")

            # Calculate donation amount
            donation_amount = amount * (self.donation_percentage / 100)

            # Process transaction through payment gateway
            transaction_result = self._process_transaction_through_gateway(amount, payment_method)

            # Make donation to charity
            donation_result = self._make_donation(donation_amount)

            # Return transaction result and donation details
            return {
                "transaction_result": transaction_result,
                "donation_amount": donation_amount,
                "donation_result": donation_result
            }

        except Exception as e:
            logger.error(f"Error processing transaction: {str(e)}")
            return {
                "error": str(e)
            }

    def _process_transaction_through_gateway(self, amount: float, payment_method: str) -> Dict:
        """
        Processes a transaction through the payment gateway.

        Args:
        - amount (float): The amount of the transaction.
        - payment_method (str): The payment method used.

        Returns:
        - A dictionary containing the transaction result.
        """
        # Implement payment gateway API call here
        # For demonstration purposes, assume a successful transaction
        return {
            "transaction_id": "12345",
            "payment_method": payment_method,
            "amount": amount,
            "status": "success"
        }

    def _make_donation(self, amount: float) -> Dict:
        """
        Makes a donation to the charity.

        Args:
        - amount (float): The amount to donate.

        Returns:
        - A dictionary containing the donation result.
        """
        # Implement charity donation API call here
        # For demonstration purposes, assume a successful donation
        return {
            "donation_id": "67890",
            "charity_name": self.charity_name,
            "amount": amount,
            "status": "success"
        }

def main():
    # Example usage
    gateway_url = os.environ.get("PAYMENT_GATEWAY_URL")
    api_key = os.environ.get("PAYMENT_GATEWAY_API_KEY")
    charity_name = "Irish Cancer Society"
    charity_account_number = "123456789"
    donation_percentage = 1.0  # 1%

    integrator = PaymentGatewayIntegrator(gateway_url, api_key, charity_name, charity_account_number, donation_percentage)

    amount = 100.0
    payment_method = "credit_card"

    result = integrator.process_transaction(amount, payment_method)
    logger.info(result)

if __name__ == "__main__":
    main()
```
