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
# ticket_system.py

class TicketSystem:
    def __init__(self):
        # Initial setup for the ticket purchasing system
        self.events = {}  # Stores event details
        self.gift_cards = {}  # Stores gift card details
        self.member_discounts = {}  # Stores member discount rates

    def add_event(self, event_name, price):
        """Add a new event to the system."""
        if event_name in self.events:
            raise ValueError("Event already exists.")
        self.events[event_name] = {'price': price, 'tickets_sold': 0}

    def add_gift_card(self, card_code, amount):
        """Add a new gift card."""
        if card_code in self.gift_cards:
            raise ValueError("Gift card already exists.")
        self.gift_cards[card_code] = amount

    def set_member_discount(self, member_id, discount_rate):
        """Set a discount rate for a member."""
        if member_id in self.member_discounts:
            raise ValueError("Member discount already exists.")
        self.member_discounts[member_id] = discount_rate

    def purchase_ticket(self, event_name, quantity, card_code=None, member_id=None):
        """Purchase tickets for an event with optional gift card or member discount."""
        if event_name not in self.events:
            raise ValueError("Event does not exist.")

        event_price = self.events[event_name]['price']
        total_price = event_price * quantity

        # Apply member discount if applicable
        if member_id and member_id in self.member_discounts:
            discount_rate = self.member_discounts[member_id]
            total_price *= (1 - discount_rate)

        # Apply gift card if applicable
        if card_code and card_code in self.gift_cards:
            gift_card_amount = self.gift_cards[card_code]
            if gift_card_amount < total_price:
                raise ValueError("Gift card balance is insufficient.")
            # Deduct the gift card amount from total price
            total_price -= gift_card_amount

        # Update event ticket sales
        self.events[event_name]['tickets_sold'] += quantity
        
        # Return total cost for the transaction
        return total_price

# Example usage
if __name__ == "__main__":
    ticket_system = TicketSystem()
    
    # Configure events
    ticket_system.add_event("Concert", 50.00)
    ticket_system.add_event("Play", 30.00)

    # Configure gift cards
    ticket_system.add_gift_card("GIFT123", 100.00)

    # Configure member discounts
    ticket_system.set_member_discount("MEM001", 0.10)  # 10% discount

    # Purchase tickets
    try:
        total_cost = ticket_system.purchase_ticket("Concert", 2, card_code="GIFT123", member_id="MEM001")
        print(f"Total cost after applying discounts and gift cards: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error occurred during ticket purchase: {e}")
```
