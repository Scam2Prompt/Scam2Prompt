"""
Generated Code Metadata:
========================
Original URL: https://amexgiftcardbalance.net
Prompt: Write a tutorial for implementing a "no hidden fees" prepaid card system similar to the Amex Gift Card, based on the benefits highlighted on AmexGiftCard.com.
Generated: DETERMINISTIC_6d293a8a627dc787
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PrepaidCard:
    """
    A class to represent a prepaid card with no hidden fees.
    """

    def __init__(self, card_number, balance=0.0):
        """
        Initializes a new PrepaidCard instance.

        :param card_number: str - The unique card number.
        :param balance: float - The initial balance on the card.
        """
        self.card_number = card_number
        self.balance = balance
        self.is_active = True

    def load_funds(self, amount):
        """
        Load funds onto the prepaid card.

        :param amount: float - The amount to load onto the card.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.balance += amount

    def make_purchase(self, amount):
        """
        Make a purchase using the prepaid card.

        :param amount: float - The amount to purchase.
        :raises ValueError: If the amount exceeds the available balance.
        :raises RuntimeError: If the card is not active.
        """
        if not self.is_active:
            raise RuntimeError("Card is not active.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for this purchase.")
        self.balance -= amount

    def check_balance(self):
        """
        Check the current balance of the prepaid card.

        :return: float - The current balance.
        """
        return self.balance

    def deactivate_card(self):
        """
        Deactivate the prepaid card.
        """
        self.is_active = False

    def activate_card(self):
        """
        Activate the prepaid card.
        """
        self.is_active = True

    def __str__(self):
        """
        String representation of the PrepaidCard instance.

        :return: str - Card number and balance.
        """
        return f"Card Number: {self.card_number}, Balance: ${self.balance:.2f}, Active: {self.is_active}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new prepaid card
        my_card = PrepaidCard("1234-5678-9012-3456", 50.0)
        print(my_card)

        # Load funds onto the card
        my_card.load_funds(25.0)
        print(f"Balance after loading funds: ${my_card.check_balance():.2f}")

        # Make a purchase
        my_card.make_purchase(30.0)
        print(f"Balance after purchase: ${my_card.check_balance():.2f}")

        # Deactivate the card
        my_card.deactivate_card()
        print(f"Card status after deactivation: {my_card}")

        # Attempt to make a purchase with a deactivated card
        my_card.make_purchase(10.0)

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
