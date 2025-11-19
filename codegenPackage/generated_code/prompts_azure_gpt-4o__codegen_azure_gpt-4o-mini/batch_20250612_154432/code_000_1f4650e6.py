"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python script to simulate a plumbing service booking system for Certified Plumbers Graham, TX, including fields for service type (e.g., leak detection, repiping), customer details, and preferred appointment time.
Generated: DETERMINISTIC_1f4650e6e7052d67
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class PlumbingServiceBooking:
    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def add_booking(self, customer_name, customer_phone, service_type, appointment_time):
        """
        Add a new booking to the system.

        :param customer_name: Name of the customer
        :param customer_phone: Phone number of the customer
        :param service_type: Type of plumbing service requested
        :param appointment_time: Preferred appointment time (datetime object)
        :raises ValueError: If the appointment time is in the past
        """
        if appointment_time < datetime.datetime.now():
            raise ValueError("Appointment time must be in the future.")

        booking = {
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'service_type': service_type,
            'appointment_time': appointment_time
        }
        self.bookings.append(booking)
        print(f"Booking confirmed for {customer_name} on {appointment_time} for {service_type}.")

    def list_bookings(self):
        """List all current bookings."""
        if not self.bookings:
            print("No bookings found.")
            return

        print("Current Bookings:")
        for booking in self.bookings:
            print(f"{booking['customer_name']} - {booking['customer_phone']} - "
                  f"{booking['service_type']} - {booking['appointment_time']}")

    def cancel_booking(self, customer_name, appointment_time):
        """
        Cancel a booking based on customer name and appointment time.

        :param customer_name: Name of the customer
        :param appointment_time: Appointment time to cancel (datetime object)
        :raises ValueError: If the booking does not exist
        """
        for booking in self.bookings:
            if booking['customer_name'] == customer_name and booking['appointment_time'] == appointment_time:
                self.bookings.remove(booking)
                print(f"Booking for {customer_name} on {appointment_time} has been canceled.")
                return
        
        raise ValueError("Booking not found.")

def main():
    service = PlumbingServiceBooking()

    # Example usage
    try:
        # Adding bookings
        service.add_booking("John Doe", "123-456-7890", "Leak Detection", datetime.datetime(2023, 10, 25, 14, 30))
        service.add_booking("Jane Smith", "098-765-4321", "Repiping", datetime.datetime(2023, 10, 26, 10, 0))

        # Listing bookings
        service.list_bookings()

        # Canceling a booking
        service.cancel_booking("John Doe", datetime.datetime(2023, 10, 25, 14, 30))

        # Listing bookings after cancellation
        service.list_bookings()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
