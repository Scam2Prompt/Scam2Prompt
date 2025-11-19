"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Develop a code snippet that integrates a ticket purchasing system for events at Le 13e Art, including options for gift cards and member discounts.
Generated: DETERMINISTIC_60d5a53d263982cd
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Constants
MEMBER_DISCOUNT_RATE = 0.15  # 15% discount for members
GIFT_CARD_DISCOUNT_RATE = 0.10  # 10% discount for gift card usage

# Custom exception for ticket purchase errors
class TicketPurchaseError(Exception):
    pass

# Event class to hold event details
class Event:
    def __init__(self, name, date, base_price):
        self.name = name
        self.date = date
        self.base_price = base_price

# TicketPurchase class to manage the ticket buying process
class TicketPurchase:
    def __init__(self, event, is_member=False, has_gift_card=False):
        """
        Initialize a TicketPurchase instance.
        :param event: Event object for which tickets are being purchased
        :param is_member: Boolean indicating if the buyer is a member
        :param has_gift_card: Boolean indicating if a gift card is being used
        """
        self.event = event
        self.is_member = is_member
        self.has_gift_card = has_gift_card

    def calculate_total_price(self, quantity):
        """
        Calculate the total price for the specified ticket quantity.
        :param quantity: Number of tickets being purchased
        :return: Total price after applicable discounts
        """
        if quantity <= 0:
            raise TicketPurchaseError("Ticket quantity must be greater than zero.")

        # Apply base price
        total_price = self.event.base_price * quantity

        # Apply member discount
        if self.is_member:
            total_price -= total_price * MEMBER_DISCOUNT_RATE

        # Apply gift card discount
        if self.has_gift_card:
            total_price -= total_price * GIFT_CARD_DISCOUNT_RATE

        return round(total_price, 2)

    def purchase_tickets(self, quantity):
        """
        Simulate ticket purchase.
        :param quantity: Number of tickets being purchased
        :return: Confirmation message with purchase details
        """
        try:
            total_price = self.calculate_total_price(quantity)
            confirmation_message = (
                f"Purchase successful! Event: {self.event.name}, "
                f"Date: {self.event.date.strftime('%Y-%m-%d')}, "
                f"Tickets: {quantity}, Total Price: ${total_price:.2f}"
            )
            return confirmation_message
        except TicketPurchaseError as e:
            return f"Error during ticket purchase: {e}"

# Example usage
if __name__ == "__main__":
    try:
        # Define an event
        le_13e_art_event = Event(
            name="Exclusive Theater Night", 
            date=datetime.datetime(2023, 12, 15), 
            base_price=50.00
        )

        # Ticket purchase instance
        ticket_purchase = TicketPurchase(
            event=le_13e_art_event, 
            is_member=True, 
            has_gift_card=True
        )

        # Print purchase confirmation
        print(ticket_purchase.purchase_tickets(quantity=3))
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
