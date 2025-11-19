"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a Python script to handle ticket booking form submissions, including validation for ticket quantity and communication method.
Generated: DETERMINISTIC_0ddc66285b2b5f68
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class TicketBookingError(Exception):
    """Custom exception for ticket booking errors."""
    pass

class TicketBooking:
    def __init__(self):
        self.max_tickets = 10  # Maximum tickets allowed per booking

    def validate_ticket_quantity(self, quantity):
        """Validate the ticket quantity."""
        if not isinstance(quantity, int):
            raise TicketBookingError("Ticket quantity must be an integer.")
        if quantity <= 0:
            raise TicketBookingError("Ticket quantity must be greater than zero.")
        if quantity > self.max_tickets:
            raise TicketBookingError(f"Cannot book more than {self.max_tickets} tickets.")

    def validate_communication_method(self, method):
        """Validate the communication method."""
        valid_methods = ['email', 'phone', 'sms']
        if method not in valid_methods:
            raise TicketBookingError(f"Invalid communication method. Choose from: {', '.join(valid_methods)}.")

    def book_tickets(self, quantity, communication_method):
        """Handle the ticket booking process."""
        try:
            self.validate_ticket_quantity(quantity)
            self.validate_communication_method(communication_method)
            # Simulate ticket booking process
            print(f"Successfully booked {quantity} tickets. Communication method: {communication_method}.")
        except TicketBookingError as e:
            print(f"Error: {e}")

def main():
    """Main function to run the ticket booking process."""
    booking = TicketBooking()
    
    # Example input (in a real application, this would come from a form submission)
    ticket_quantity = 5  # Example ticket quantity
    communication_method = 'email'  # Example communication method

    # Attempt to book tickets
    booking.book_tickets(ticket_quantity, communication_method)

if __name__ == "__main__":
    main()
```
