"""
Generated Code Metadata:
========================
Original URL: https://airlinesmanagebooking.com
Prompt: Develop a program in Python that calculates refund eligibility based on the cancellation policies for refundable and non-refundable tickets provided on Airlines Manage Booking.
Generated: DETERMINISTIC_ab1ab833c2922532
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Ticket:
    """
    A class to represent a flight ticket.

    Attributes:
        ticket_type (str): The type of the ticket ('refundable' or 'non-refundable').
        purchase_date (str): The date the ticket was purchased in 'YYYY-MM-DD' format.
        cancellation_date (str): The date the ticket is canceled in 'YYYY-MM-DD' format.
    """

    def __init__(self, ticket_type, purchase_date, cancellation_date):
        """
        Initializes the Ticket with type, purchase date, and cancellation date.

        Args:
            ticket_type (str): The type of the ticket.
            purchase_date (str): The date the ticket was purchased.
            cancellation_date (str): The date the ticket is canceled.
        """
        self.ticket_type = ticket_type.lower()
        self.purchase_date = purchase_date
        self.cancellation_date = cancellation_date

    def is_refundable(self):
        """Check if the ticket is refundable."""
        return self.ticket_type == 'refundable'

    def calculate_refund(self):
        """
        Calculate refund eligibility based on ticket type and cancellation date.

        Returns:
            str: A message indicating refund eligibility or reason for ineligibility.
        """
        if self.is_refundable():
            return "Refund is eligible for refundable tickets."
        elif self.ticket_type == 'non-refundable':
            return "Refund is not eligible for non-refundable tickets."
        else:
            return "Invalid ticket type."

    def validate_dates(self):
        """
        Validate the purchase and cancellation dates.

        Raises:
            ValueError: If the dates are not in the correct format or if cancellation date is before purchase date.
        """
        from datetime import datetime

        date_format = "%Y-%m-%d"
        try:
            purchase = datetime.strptime(self.purchase_date, date_format)
            cancellation = datetime.strptime(self.cancellation_date, date_format)

            if cancellation < purchase:
                raise ValueError("Cancellation date cannot be before purchase date.")
        except ValueError as e:
            raise ValueError(f"Date validation error: {e}")

def main():
    """
    Main function to execute the refund eligibility check.
    """
    # Example ticket details
    ticket_type = input("Enter ticket type (refundable/non-refundable): ")
    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
    cancellation_date = input("Enter cancellation date (YYYY-MM-DD): ")

    # Create a Ticket instance
    ticket = Ticket(ticket_type, purchase_date, cancellation_date)

    try:
        # Validate dates
        ticket.validate_dates()
        # Calculate and print refund eligibility
        print(ticket.calculate_refund())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
