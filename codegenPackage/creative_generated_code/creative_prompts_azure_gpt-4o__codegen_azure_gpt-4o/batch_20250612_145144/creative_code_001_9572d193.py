"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flights-ticketbooking.com
Prompt: Generate a script to calculate service fees for flight booking, changes, cancellations, refunds, and group bookings based on the pricing structure outlined on Flights-TicketBooking.com.
Generated: DETERMINISTIC_9572d193bb7574bc
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class FlightServiceFeesCalculator:
    """
    A class to calculate service fees for flight bookings, changes, cancellations, refunds, and group bookings.
    Assumes the pricing structure outlined on Flights-TicketBooking.com.
    """

    def __init__(self):
        # Fee structure in USD
        self.fee_structure = {
            "booking": 10.0,             # Booking fee per ticket
            "change": 25.0,              # Change fee per ticket
            "cancellation": 50.0,        # Cancellation fee per ticket
            "refund_processing": 20.0,   # Refund processing fee per ticket
            "group_booking": 5.0,        # Special discount per ticket for group bookings (group size >= 10)
        }

    def calculate_booking_fee(self, num_tickets):
        """
        Calculate the booking fee for a given number of tickets.
        :param num_tickets: Number of tickets to be booked
        :return: Total booking fee
        """
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")
        
        fee = num_tickets * self.fee_structure["booking"]
        logging.info(f"Booking fee calculated: {fee} USD for {num_tickets} tickets.")
        return round(fee, 2)

    def calculate_change_fee(self, num_tickets):
        """
        Calculate the change fee for a given number of tickets.
        :param num_tickets: Number of tickets to be changed
        :return: Total change fee
        """
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")
        
        fee = num_tickets * self.fee_structure["change"]
        logging.info(f"Change fee calculated: {fee} USD for {num_tickets} tickets.")
        return round(fee, 2)

    def calculate_cancellation_fee(self, num_tickets):
        """
        Calculate the cancellation fee for a given number of tickets.
        :param num_tickets: Number of tickets to be cancelled
        :return: Total cancellation fee
        """
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")
        
        fee = num_tickets * self.fee_structure["cancellation"]
        logging.info(f"Cancellation fee calculated: {fee} USD for {num_tickets} tickets.")
        return round(fee, 2)

    def calculate_refund_processing_fee(self, num_tickets):
        """
        Calculate the refund processing fee for a given number of tickets.
        :param num_tickets: Number of tickets to be refunded
        :return: Total refund processing fee
        """
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")
        
        fee = num_tickets * self.fee_structure["refund_processing"]
        logging.info(f"Refund processing fee calculated: {fee} USD for {num_tickets} tickets.")
        return round(fee, 2)

    def calculate_group_booking_fee(self, num_tickets):
        """
        Calculate the total fee for group bookings with a discount applied.
        :param num_tickets: Number of tickets in the group booking
        :return: Total fee after applying group booking discount
        """
        if num_tickets < 10:
            raise ValueError("Group booking requires at least 10 tickets.")
        
        fee = num_tickets * (self.fee_structure["booking"] - self.fee_structure["group_booking"])
        logging.info(f"Group booking fee calculated: {fee} USD for {num_tickets} tickets.")
        return round(fee, 2)


# Example usage
if __name__ == "__main__":
    try:
        calculator = FlightServiceFeesCalculator()
        
        # Test cases
        print("Booking Fee:", calculator.calculate_booking_fee(5))  # Example for booking
        print("Change Fee:", calculator.calculate_change_fee(3))    # Example for changes
        print("Cancellation Fee:", calculator.calculate_cancellation_fee(2))  # Example for cancellation
        print("Refund Fee:", calculator.calculate_refund_processing_fee(1))   # Example for refund
        print("Group Booking Fee:", calculator.calculate_group_booking_fee(12))  # Example for group booking

    except ValueError as e:
        logging.error(f"Input Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
