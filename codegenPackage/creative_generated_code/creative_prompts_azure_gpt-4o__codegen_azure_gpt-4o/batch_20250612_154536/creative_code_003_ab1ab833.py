"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Develop a program in Python that calculates refund eligibility based on the cancellation policies for refundable and non-refundable tickets provided on Airlines Manage Booking.
Generated: DETERMINISTIC_ab1ab833c2922532
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime, timedelta

# Define the Ticket class
class Ticket:
    """
    Represents an airline ticket with its properties.
    """
    def __init__(self, ticket_id, is_refundable, booking_date, travel_date, cancellation_date=None):
        self.ticket_id = ticket_id
        self.is_refundable = is_refundable  # True for refundable ticket, False for non-refundable
        self.booking_date = datetime.strptime(booking_date, "%Y-%m-%d")
        self.travel_date = datetime.strptime(travel_date, "%Y-%m-%d")
        self.cancellation_date = (
            datetime.strptime(cancellation_date, "%Y-%m-%d") if cancellation_date else None
        )

# Define the function to calculate refund eligibility
def calculate_refund(ticket):
    """
    Determines refund eligibility based on ticket properties and cancellation policies.
    
    Refund Policy:
    1. Refundable Tickets:
       - Full refund if canceled at least 24 hours before travel date.
       - No refund if canceled within 24 hours of travel.
    2. Non-refundable Tickets:
       - No refund under any circumstances.

    Args:
        ticket (Ticket): A Ticket object representing booking details.

    Returns:
        str: A message indicating refund eligibility.
    """
    try:
        if not ticket.cancellation_date:
            return "Cancellation date is not provided."

        if ticket.cancellation_date >= ticket.travel_date:
            return "Cancellation denied. Travel date has already passed."

        if ticket.is_refundable:
            # Refundable ticket logic
            if ticket.travel_date - ticket.cancellation_date >= timedelta(hours=24):
                return f"Ticket ID {ticket.ticket_id}: Full refund eligible."
            else:
                return f"Ticket ID {ticket.ticket_id}: No refund eligible (canceled within 24 hours of travel)."
        else:
            # Non-refundable ticket logic
            return f"Ticket ID {ticket.ticket_id}: No refund eligible (ticket is non-refundable)."

    except Exception as e:
        return f"An error occurred while processing refund eligibility: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Create test tickets
    refundable_ticket = Ticket(
        ticket_id="R123", is_refundable=True, booking_date="2023-10-01", travel_date="2023-10-10", cancellation_date="2023-10-08"
    )
    non_refundable_ticket = Ticket(
        ticket_id="NR456", is_refundable=False, booking_date="2023-10-01", travel_date="2023-10-10", cancellation_date="2023-10-08"
    )
    late_cancellation_ticket = Ticket(
        ticket_id="R789", is_refundable=True, booking_date="2023-10-01", travel_date="2023-10-10", cancellation_date="2023-10-09"
    )

    # Calculate refund eligibility for each ticket
    print(calculate_refund(refundable_ticket))
    print(calculate_refund(non_refundable_ticket))
    print(calculate_refund(late_cancellation_ticket))
```
