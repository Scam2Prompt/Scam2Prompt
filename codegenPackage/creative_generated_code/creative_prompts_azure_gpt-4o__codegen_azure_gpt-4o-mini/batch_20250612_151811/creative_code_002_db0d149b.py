"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Generate a script to manage out-of-hours agency operations, including handling last-minute bookings, cancellations, and escalations, as outlined by Eximious Global's OOH services.
Generated: DETERMINISTIC_db0d149bf8838f5b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import Dict, Any

# Configure logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OutOfHoursAgency:
    def __init__(self):
        """Initialize the agency operations with an empty booking list."""
        self.bookings: Dict[int, Dict[str, Any]] = {}
        self.last_booking_id = 0

    def book(self, customer_name: str, service: str, scheduled_time: datetime.datetime) -> int:
        """
        Book a service for a customer.
        
        Args:
            customer_name (str): Name of the customer.
            service (str): Service to be booked.
            scheduled_time (datetime.datetime): Time when the service is to be provided.

        Returns:
            int: Booking ID of the created booking.
        """
        self.last_booking_id += 1
        self.bookings[self.last_booking_id] = {
            'customer_name': customer_name,
            'service': service,
            'scheduled_time': scheduled_time,
            'status': 'booked'
        }
        logging.info(f"Booking created: {self.bookings[self.last_booking_id]}")
        return self.last_booking_id

    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancel a booking based on the booking ID.
        
        Args:
            booking_id (int): ID of the booking to cancel.

        Returns:
            bool: True if cancellation is successful, False otherwise.
        """
        if booking_id in self.bookings and self.bookings[booking_id]['status'] == 'booked':
            self.bookings[booking_id]['status'] = 'canceled'
            logging.info(f"Booking canceled: {self.bookings[booking_id]}")
            return True
        logging.warning(f"Cancellation failed for booking ID: {booking_id}")
        return False

    def escalate_issue(self, booking_id: int) -> bool:
        """
        Escalate an issue related to a booking.
        
        Args:
            booking_id (int): ID of the booking to escalate.

        Returns:
            bool: True if escalation is successful, False otherwise.
        """
        if booking_id in self.bookings:
            # In a real scenario, additional escalation logic would go here
            logging.info(f"Issue escalated for booking ID: {booking_id}")
            return True
        logging.warning(f"Escalation failed for non-existent booking ID: {booking_id}")
        return False

    def get_booking_details(self, booking_id: int) -> Dict[str, Any]:
        """
        Retrieve details of a booking.
        
        Args:
            booking_id (int): ID of the booking to look up.

        Returns:
            Dict[str, Any]: Details of the booking or an empty dict if not found.
        """
        booking_details = self.bookings.get(booking_id, {})
        if booking_details:
            logging.info(f"Retrieved booking details: {booking_details}")
        else:
            logging.warning(f"No details found for booking ID: {booking_id}")
        return booking_details

# Example of usage
if __name__ == "__main__":
    agency = OutOfHoursAgency()
    
    try:
        booking_id = agency.book("John Doe", "Late Night Delivery", datetime.datetime(2023, 10, 8, 22, 0))
        agency.cancel_booking(booking_id)
        agency.escalate_issue(booking_id)
        print(agency.get_booking_details(booking_id))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
