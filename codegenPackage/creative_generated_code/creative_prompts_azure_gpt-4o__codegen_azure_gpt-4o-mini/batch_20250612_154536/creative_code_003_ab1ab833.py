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
class Ticket:
    """Class representing a flight ticket."""

    def __init__(self, ticket_type: str, purchased_date: str, cancellation_date: str):
        """
        Initializes the Ticket object.

        Args:
            ticket_type (str): Type of the ticket ('refundable' or 'non-refundable').
            purchased_date (str): Date when the ticket was purchased (format: YYYY-MM-DD).
            cancellation_date (str): Date when the ticket was cancelled (format: YYYY-MM-DD).
        """
        self.ticket_type = ticket_type.lower()
        self.purchased_date = self.parse_date(purchased_date)
        self.cancellation_date = self.parse_date(cancellation_date)

    @staticmethod
    def parse_date(date_str: str) -> str:
        """
        Parses a date string into the desired format.

        Args:
            date_str (str): Date string to be parsed.

        Returns:
            str: Parsed date in 'YYYY-MM-DD' format.
        """
        from datetime import datetime

        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.") from e

    def is_refundable(self) -> bool:
        """Checks if the ticket is refundable based on its type."""
        return self.ticket_type == 'refundable'

    def calculate_refund_eligibility(self) -> str:
        """
        Determines refund eligibility based on ticket type and cancellation date.

        Returns:
            str: Refund eligibility message.
        """
        from datetime import timedelta

        if not self.is_valid_dates():
            return "Invalid cancellation process. Please ensure that the cancellation date is after the purchase date."

        if self.is_refundable():
            # Refundable tickets are eligible for refund if canceled at least 24 hours before the flight date
            if self.cancellation_date >= self.purchased_date + timedelta(days=1):
                return "Your refundable ticket is eligible for a full refund."
            else:
                return "Your refundable ticket is NOT eligible for a refund as it was canceled less than 24 hours before the flight."
        else:
            # Non-refundable tickets are generally not eligible for a refund
            return "Your non-refundable ticket is NOT eligible for a refund."

    def is_valid_dates(self) -> bool:
        """Checks if the purchase and cancellation dates are valid."""
        return self.cancellation_date >= self.purchased_date


def main():
    """Main function to demonstrate refund eligibility calculation."""
    try:
        # Example input data for testing
        ticket_type = "refundable"  # Options: 'refundable' or 'non-refundable'
        purchased_date = "2023-10-01"
        cancellation_date = "2023-10-03"

        # Create a Ticket object
        ticket = Ticket(ticket_type, purchased_date, cancellation_date)

        # Calculate and print refund eligibility
        result = ticket.calculate_refund_eligibility()
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
