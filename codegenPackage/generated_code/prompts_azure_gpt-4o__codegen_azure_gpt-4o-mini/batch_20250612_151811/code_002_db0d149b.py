"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Generate a script to manage out-of-hours agency operations, including handling last-minute bookings, cancellations, and escalations, as outlined by Eximious Global's OOH services.
Generated: DETERMINISTIC_db0d149bf8838f5b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Booking:
    """Class to represent a booking."""
    
    def __init__(self, booking_id: str, client_name: str, service_type: str, booking_time: datetime.datetime):
        self.booking_id = booking_id
        self.client_name = client_name
        self.service_type = service_type
        self.booking_time = booking_time
        self.status = 'confirmed'  # Initial status of the booking

    def cancel(self):
        """Cancel the booking."""
        if self.status == 'confirmed':
            self.status = 'cancelled'
            logging.info(f"Booking {self.booking_id} cancelled.")
        else:
            logging.warning(f"Booking {self.booking_id} cannot be cancelled as it is already {self.status}.")

class OOHServiceManager:
    """Class to manage out-of-hours agency operations."""
    
    def __init__(self):
        self.bookings: Dict[str, Booking] = {}  # Store bookings by booking_id

    def add_booking(self, booking_id: str, client_name: str, service_type: str, booking_time: datetime.datetime) -> None:
        """Add a new booking."""
        if booking_id in self.bookings:
            logging.error(f"Booking ID {booking_id} already exists.")
            raise ValueError("Booking ID already exists.")
        
        self.bookings[booking_id] = Booking(booking_id, client_name, service_type, booking_time)
        logging.info(f"Booking {booking_id} added for {client_name}.")

    def cancel_booking(self, booking_id: str) -> None:
        """Cancel an existing booking."""
        if booking_id not in self.bookings:
            logging.error(f"Booking ID {booking_id} not found.")
            raise KeyError("Booking ID not found.")
        
        self.bookings[booking_id].cancel()

    def escalate_issue(self, booking_id: str, issue_description: str) -> None:
        """Escalate an issue related to a booking."""
        if booking_id not in self.bookings:
            logging.error(f"Booking ID {booking_id} not found for escalation.")
            raise KeyError("Booking ID not found.")
        
        logging.warning(f"Issue escalated for Booking ID {booking_id}: {issue_description}")

    def get_bookings(self) -> List[Dict]:
        """Get a list of all bookings."""
        return [{'booking_id': b.booking_id, 'client_name': b.client_name, 'service_type': b.service_type, 
                 'booking_time': b.booking_time, 'status': b.status} for b in self.bookings.values()]

# Example usage
if __name__ == "__main__":
    manager = OOHServiceManager()
    
    try:
        # Adding bookings
        manager.add_booking("001", "Alice Smith", "Transport", datetime.datetime(2023, 10, 15, 18, 0))
        manager.add_booking("002", "Bob Johnson", "Security", datetime.datetime(2023, 10, 15, 19, 0))
        
        # Cancelling a booking
        manager.cancel_booking("001")
        
        # Escalating an issue
        manager.escalate_issue("002", "Client requested additional security personnel.")
        
        # Retrieving all bookings
        bookings = manager.get_bookings()
        logging.info(f"Current bookings: {bookings}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
