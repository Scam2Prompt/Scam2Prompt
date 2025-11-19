"""
Generated Code Metadata:
========================
Original URL: https://le13emeart.com
Prompt: Develop a code snippet that integrates a ticket purchasing system for events at Le 13e Art, including options for gift cards and member discounts.
Generated: DETERMINISTIC_60d5a53d263982cd
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TicketPurchasingSystem:
    def __init__(self):
        # Initialize the ticket purchasing system with default values
        self.events = {}  # Dictionary to hold event details
        self.gift_cards = {}  # Dictionary to hold gift card values
        self.member_discount_rate = 0.1  # 10% member discount

    def add_event(self, event_name, ticket_price, available_tickets):
        """
        Add a new event to the system.

        :param event_name: Name of the event
        :param ticket_price: Price of a single ticket
        :param available_tickets: Number of tickets available for the event
        """
        if event_name in self.events:
            raise ValueError("Event already exists.")
        self.events[event_name] = {
            'ticket_price': ticket_price,
            'available_tickets': available_tickets
        }

    def purchase_ticket(self, event_name, quantity, is_member=False, gift_card_value=0):
        """
        Purchase tickets for a specified event.

        :param event_name: Name of the event
        :param quantity: Number of tickets to purchase
        :param is_member: Boolean indicating if the purchaser is a member
        :param gift_card_value: Value of the gift card being used (default is 0)
        :return: Total cost of the purchase
        """
        if event_name not in self.events:
            raise ValueError("Event does not exist.")
        
        event = self.events[event_name]
        
        if quantity > event['available_tickets']:
            raise ValueError("Not enough tickets available.")
        
        total_cost = event['ticket_price'] * quantity
        
        # Apply member discount if applicable
        if is_member:
            total_cost *= (1 - self.member_discount_rate)
        
        # Deduct gift card value from total cost
        total_cost -= gift_card_value
        
        if total_cost < 0:
            total_cost = 0  # Ensure total cost does not go negative
        
        # Update available tickets
        event['available_tickets'] -= quantity
        
        return total_cost

    def add_gift_card(self, card_code, value):
        """
        Add a new gift card to the system.

        :param card_code: Unique code for the gift card
        :param value: Value of the gift card
        """
        if card_code in self.gift_cards:
            raise ValueError("Gift card already exists.")
        self.gift_cards[card_code] = value

    def redeem_gift_card(self, card_code):
        """
        Redeem a gift card and return its value.

        :param card_code: Unique code for the gift card
        :return: Value of the gift card
        """
        if card_code not in self.gift_cards:
            raise ValueError("Gift card does not exist.")
        return self.gift_cards.pop(card_code)  # Remove the card after redemption

# Example usage
if __name__ == "__main__":
    system = TicketPurchasingSystem()
    
    # Adding events
    system.add_event("Concert", 50, 100)
    system.add_event("Theater", 30, 50)
    
    # Adding gift cards
    system.add_gift_card("GIFT123", 20)
    
    # Purchasing tickets
    try:
        total_cost = system.purchase_ticket("Concert", 2, is_member=True, gift_card_value=system.redeem_gift_card("GIFT123"))
        print(f"Total cost for tickets: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
