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
# Custom checkout process for Vanilla Gift Cards

class GiftCard:
    """
    Represents a Vanilla Gift Card with a balance.
    """

    def __init__(self, card_number: str, pin: str, balance: float):
        """
        Initializes a GiftCard instance.

        :param card_number: The gift card number (as a string)
        :param pin: The pin associated with the gift card (as a string)
        :param balance: The current balance on the gift card (as a float)
        """
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def apply_payment(self, amount: float) -> bool:
        """
        Applies payment to the gift card, reducing the balance.

        :param amount: The amount to be deducted (as a float)
        :return: True if the payment was successful, False otherwise
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds on the gift card.")
        
        self.balance -= amount
        return True


class Checkout:
    """
    Handles the checkout process using a gift card.
    """

    def __init__(self):
        """
        Initializes the Checkout instance.
        """
        self.cart_total = 0.0

    def add_to_cart(self, amount: float):
        """
        Adds an item price to the cart total.

        :param amount: The price of the item to add (as a float)
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.cart_total += amount

    def process_payment(self, gift_card: GiftCard):
        """
        Processes the payment using the provided gift card.

        :param gift_card: The GiftCard instance to be used for payment
        """
        try:
            if gift_card.apply_payment(self.cart_total):
                print("Payment successful. Thank you for your purchase!")
                print(f"Remaining balance: ${gift_card.balance:.2f}")
        except ValueError as e:
            print(f"Payment failed: {e}")

# Example usage
if __name__ == "__main__":
    # Create a gift card instance
    my_gift_card = GiftCard(card_number="1234567890123456", pin="1234", balance=100.0)

    # Initialize the checkout process
    checkout = Checkout()
    
    # Add items to the cart
    checkout.add_to_cart(30.0)  # Item 1
    checkout.add_to_cart(20.0)  # Item 2
    
    # Process payment with the gift card
    checkout.process_payment(my_gift_card)

    # Output the remaining balance
    print(f"Final Gift Card Balance: ${my_gift_card.balance:.2f}")
```
