"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amexgiftcardbalance.net
Prompt: Write a tutorial for implementing a "no hidden fees" prepaid card system similar to the Amex Gift Card, based on the benefits highlighted on AmexGiftCard.com.
Generated: DETERMINISTIC_6d293a8a627dc787
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Prepaid Card System Implementation
# This code simulates a "No Hidden Fees" prepaid card system

class PrepaidCard:
    def __init__(self, card_number: str, balance: float):
        """
        Initializes a prepaid card with a card number and initial balance.
        
        :param card_number: Unique identifier for the prepaid card
        :param balance: Initial balance on the card
        """
        self.card_number = card_number  # Unique card number
        self.balance = balance  # Balance in the card
        self.is_active = True  # Card status

    def load_money(self, amount: float) -> None:
        """
        Load money onto the prepaid card.
        
        :param amount: Amount to be loaded onto the card
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.balance += amount
        print(f"Loaded ${amount:.2f} onto card {self.card_number}. New balance: ${self.balance:.2f}")

    def make_purchase(self, amount: float) -> None:
        """
        Makes a purchase using the prepaid card.
        
        :param amount: Amount to be deducted from the card balance
        """
        if not self.is_active:
            raise Exception("Card is not active.")
        
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        
        if amount > self.balance:
            raise ValueError("Insufficient balance for the purchase.")
        
        self.balance -= amount
        print(f"Purchase of ${amount:.2f} made with card {self.card_number}. Remaining balance: ${self.balance:.2f}")

    def check_balance(self) -> float:
        """
        Returns the current balance on the prepaid card.
        
        :return: Current card balance
        """
        return self.balance

    def deactivate_card(self) -> None:
        """
        Deactivates the prepaid card.
        """
        self.is_active = False
        print(f"Card {self.card_number} has been deactivated.")

    def activate_card(self) -> None:
        """
        Activates the prepaid card.
        """
        self.is_active = True
        print(f"Card {self.card_number} has been activated.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a prepaid card with a balance of $100
        card = PrepaidCard("1234-5678-9012-3456", 100.00)

        # Load additional money onto the card
        card.load_money(50.00)

        # Make a purchase
        card.make_purchase(30.00)

        # Check current balance
        current_balance = card.check_balance()
        print(f"Current balance is: ${current_balance:.2f}")

        # Deactivate the card
        card.deactivate_card()

        # Attempt to make a purchase with a deactivated card
        card.make_purchase(20.00)  # This will raise an exception

    except Exception as e:
        print(f"Error: {e}")
```
