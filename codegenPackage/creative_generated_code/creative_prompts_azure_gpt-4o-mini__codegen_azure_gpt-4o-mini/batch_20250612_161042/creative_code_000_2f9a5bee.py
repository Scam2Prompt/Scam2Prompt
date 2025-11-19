"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Generate a code snippet for a ticket purchasing system for the Celestia 2025 festival that includes event details and user registration.
Generated: DETERMINISTIC_2f9a5bee3b21e1da
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Event:
    """Class to represent an Event for the festival."""
    
    def __init__(self, name, date, location, total_tickets):
        self.name = name
        self.date = date
        self.location = location
        self.total_tickets = total_tickets
        self.tickets_sold = 0

    def sell_ticket(self, quantity):
        """Sell tickets for the event."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if self.tickets_sold + quantity > self.total_tickets:
            raise ValueError("Not enough tickets available.")
        
        self.tickets_sold += quantity
        return f"{quantity} tickets sold for {self.name}."

class User:
    """Class to represent a User in the ticket purchasing system."""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.purchased_tickets = []

    def purchase_ticket(self, event, quantity):
        """Purchase tickets for a given event."""
        try:
            confirmation = event.sell_ticket(quantity)
            self.purchased_tickets.append((event.name, quantity))
            return confirmation
        except ValueError as e:
            return str(e)

def main():
    """Main function to run the ticket purchasing system."""
    # Create a sample event for the festival
    event_date = datetime.datetime(2025, 7, 20)
    celestia_festival = Event("Celestia 2025", event_date, "Celestial Park", 5000)

    # User registration
    user = User(username="festival_lover", email="user@example.com")

    # User attempts to purchase tickets
    try:
        print(user.purchase_ticket(celestia_festival, 5))  # Successful purchase
        print(user.purchase_ticket(celestia_festival, 5000))  # Exceeds available tickets
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
