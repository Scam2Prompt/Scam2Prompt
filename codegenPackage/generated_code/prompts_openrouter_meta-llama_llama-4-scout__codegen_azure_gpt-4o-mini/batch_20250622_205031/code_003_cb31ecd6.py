"""
Generated Code Metadata:
========================
Original URL: https://fin-flix.me
Prompt: What are the advantages of using a credit card without Schufa-Prüfung, and how can it benefit individuals with poor credit history?
Generated: DETERMINISTIC_cb31ecd6d66c1344
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CreditCard:
    """
    A class to represent a credit card without Schufa-Prüfung (credit check).
    This class simulates the advantages of using such a credit card for individuals
    with poor credit history.
    """

    def __init__(self, cardholder_name, credit_limit):
        """
        Initializes a new CreditCard instance.

        :param cardholder_name: Name of the cardholder
        :param credit_limit: Credit limit for the card
        """
        self.cardholder_name = cardholder_name
        self.credit_limit = credit_limit
        self.balance = 0.0

    def make_purchase(self, amount):
        """
        Simulates making a purchase with the credit card.

        :param amount: Amount to be charged to the credit card
        :raises ValueError: If the purchase amount exceeds the credit limit
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")
        if self.balance + amount > self.credit_limit:
            raise ValueError("Purchase exceeds credit limit.")
        
        self.balance += amount
        print(f"Purchase of {amount} made. New balance: {self.balance}")

    def make_payment(self, amount):
        """
        Simulates making a payment towards the credit card balance.

        :param amount: Amount to be paid
        :raises ValueError: If the payment amount is invalid
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        
        self.balance -= amount
        if self.balance < 0:
            self.balance = 0  # Prevent negative balance
        print(f"Payment of {amount} made. New balance: {self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the credit card.

        :return: Current balance
        """
        return self.balance

    def get_credit_limit(self):
        """
        Returns the credit limit of the credit card.

        :return: Credit limit
        """
        return self.credit_limit

    def __str__(self):
        """
        Returns a string representation of the credit card details.

        :return: String representation
        """
        return f"Credit Card for {self.cardholder_name}, Credit Limit: {self.credit_limit}, Current Balance: {self.balance}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a credit card for a user with a poor credit history
        user_card = CreditCard("John Doe", 1000.0)

        # Make a purchase
        user_card.make_purchase(200.0)

        # Make a payment
        user_card.make_payment(50.0)

        # Display current balance and credit limit
        print(user_card)
    except ValueError as e:
        print(f"Error: {e}")
```
