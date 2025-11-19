"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanillagift.remadet.com
Prompt: What are the steps to create a custom checkout process using Vanilla Gift cards?
Generated: DETERMINISTIC_89b67cc90f33def0
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Custom Checkout Process using Vanilla Gift Cards

This script demonstrates how to create a basic checkout process 
that validates Vanilla Gift Card payments. It assumes integration 
with a third-party payment processor or API that handles Vanilla Gift Card validation.
"""

import re

class VanillaGiftCardCheckout:
    def __init__(self):
        """
        Initializes the checkout process.
        """
        self.total_amount = 0.0
        self.gift_card_balance = 0.0

    def set_total_amount(self, amount):
        """
        Sets the total amount for checkout.

        Parameters:
        amount (float): The total amount to be paid.
        Raises:
        ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Total amount must be greater than 0.")
        self.total_amount = amount

    def validate_gift_card(self, card_number):
        """
        Validates the Vanilla Gift Card number format.

        Parameters:
        card_number (str): The Vanilla Gift Card number.
        Returns:
        bool: True if the card number is valid, False otherwise.
        """
        # Vanilla Gift Card format (Example: 16-digit numeric format)
        pattern = r"^\d{16}$"
        if re.match(pattern, card_number):
            return True
        return False

    def check_card_balance(self, card_number):
        """
        Mock function to check Vanilla Gift Card balance.
        This is intended to simulate an API call to a payment processor.

        Parameters:
        card_number (str): The Vanilla Gift Card number.
        Returns:
        float: Mock balance of the card.
        """
        # Simulating an API call to retrieve balance
        # Replace this with actual API integration in production
        return 50.00  # Mock balance

    def process_payment(self, card_number):
        """
        Processes the payment via Vanilla Gift Card.

        Parameters:
        card_number (str): The Vanilla Gift Card number.
        Raises:
        ValueError: If the card number is invalid or funds are insufficient.
        """
        if not self.validate_gift_card(card_number):
            raise ValueError("Invalid Vanilla Gift Card number.")

        self.gift_card_balance = self.check_card_balance(card_number)

        if self.gift_card_balance < self.total_amount:
            raise ValueError("Insufficient funds on Vanilla Gift Card.")

        # Deduct the payment from card balance
        self.gift_card_balance -= self.total_amount
        print(f"Payment successful! Remaining card balance: ${self.gift_card_balance:.2f}")

    def run_checkout(self, total_amount, card_number):
        """
        Executes the custom checkout process.

        Parameters:
        total_amount (float): The total amount to be paid.
        card_number (str): The Vanilla Gift Card number.
        """
        try:
            # Step 1: Set the total amount for checkout
            self.set_total_amount(total_amount)

            # Step 2: Process payment using the gift card
            self.process_payment(card_number)

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the checkout process
    checkout = VanillaGiftCardCheckout()

    # Define the total amount and card number for testing
    total_amount = 40.00
    card_number = "1234567812345678"  # Mock 16-digit Vanilla Gift Card number

    # Run the checkout process
    checkout.run_checkout(total_amount, card_number)
```
