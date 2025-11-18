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

# Configure logging
logging.basicConfig(
    filename="agency_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class OutOfHoursAgencyOperations:
    """
    Class to manage out-of-hours agency operations, including handling 
    last-minute bookings, cancellations, and escalations.
    """

    def __init__(self):
        self.bookings = {}  # Store bookings in a dictionary: {booking_id: booking_info}

    def create_booking(self, client_name, service_type, booking_time):
        """
        Creates a new booking.
        :param client_name: Name of the client requesting the service.
        :param service_type: Type of service requested.
        :param booking_time: Time of the booking (datetime object).
        :return: Booking ID (string).
        """
        try:
            # Generate a unique booking ID based on datetime and client name
            booking_id = f"{client_name[:3].upper()}_{int(datetime.datetime.now().timestamp())}"
            
            # Store booking information
            self.bookings[booking_id] = {
                "client_name": client_name,
                "service_type": service_type,
                "booking_time": booking_time,
                "status": "confirmed",
            }
            
            logging.info(f"Booking created: {booking_id} for {client_name}")
            return booking_id
        except Exception as e:
            logging.error(f"Error creating booking: {e}")
            raise

    def cancel_booking(self, booking_id):
        """
        Cancels an existing booking.
        :param booking_id: ID of the booking to cancel.
        """
        try:
            if booking_id not in self.bookings:
                raise ValueError("Booking ID not found.")

            # Update booking status to cancelled
            self.bookings[booking_id]["status"] = "cancelled"
            logging.info(f"Booking cancelled: {booking_id}")
        except Exception as e:
            logging.error(f"Error cancelling booking {booking_id}: {e}")
            raise

    def escalate_issue(self, booking_id, issue_description):
        """
        Escalates an issue related to a booking.
        :param booking_id: ID of the booking related to the issue.
        :param issue_description: Description of the issue to escalate.
        """
        try:
            if booking_id not in self.bookings:
                raise ValueError("Booking ID not found.")

            escalation_details = {
                "booking_id": booking_id,
                "issue_description": issue_description,
                "escalation_time": datetime.datetime.now(),
            }

            # Log escalation details
            logging.warning(f"Issue escalated: {escalation_details}")
            return escalation_details
        except Exception as e:
            logging.error(f"Error escalating issue for booking {booking_id}: {e}")
            raise

    def get_booking_details(self, booking_id):
        """
        Retrieves details of a specific booking.
        :param booking_id: ID of the booking to retrieve details for.
        :return: Dictionary containing booking details.
        """
        try:
            if booking_id not in self.bookings:
                raise ValueError("Booking ID not found.")

            return self.bookings[booking_id]
        except Exception as e:
            logging.error(f"Error retrieving booking details for {booking_id}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the service
    agency_operations = OutOfHoursAgencyOperations()

    try:
        # Create a booking
        booking_id = agency_operations.create_booking(
            client_name="John Doe",
            service_type="Transport",
            booking_time=datetime.datetime.now() + datetime.timedelta(hours=2)
        )
        print(f"Booking created: {booking_id}")

        # Retrieve booking details
        booking_details = agency_operations.get_booking_details(booking_id)
        print(f"Booking Details: {booking_details}")

        # Cancel the booking
        agency_operations.cancel_booking(booking_id)
        print(f"Booking {booking_id} cancelled.")

        # Escalate an issue
        escalation = agency_operations.escalate_issue(booking_id, "Driver unavailable")
        print(f"Issue escalated: {escalation}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
