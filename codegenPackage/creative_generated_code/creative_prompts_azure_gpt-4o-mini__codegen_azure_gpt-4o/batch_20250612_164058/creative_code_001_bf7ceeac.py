"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize an empty list to store bookings
        self.bookings = []

    def create_booking(self, customer_name, contact_number, repair_date, repair_time):
        """
        Create a new booking for windscreen repair.
        
        :param customer_name: Name of the customer
        :param contact_number: Customer's contact number
        :param repair_date: Desired repair date (YYYY-MM-DD)
        :param repair_time: Desired repair time (HH:MM)
        :return: Confirmation of booking or error message
        """
        try:
            # Validate the repair date and time
            repair_datetime = datetime.datetime.strptime(f"{repair_date} {repair_time}", "%Y-%m-%d %H:%M")
            if repair_datetime < datetime.datetime.now():
                return "Error: Repair date and time cannot be in the past."

            # Check if the requested time slot is already booked
            for booking in self.bookings:
                if booking['repair_datetime'] == repair_datetime:
                    return "Error: The requested time slot is already booked."

            # Create the booking
            new_booking = {
                "customer_name": customer_name,
                "contact_number": contact_number,
                "repair_datetime": repair_datetime,
            }
            self.bookings.append(new_booking)
            return f"Booking confirmed for {customer_name} on {repair_datetime.strftime('%Y-%m-%d at %H:%M')}."
        except ValueError:
            return "Error: Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

    def view_bookings(self):
        """
        View all current bookings.
        
        :return: A list of bookings or a message if no bookings exist
        """
        if not self.bookings:
            return "No bookings available."
        result = "Current Bookings:\n"
        for booking in self.bookings:
            result += f"- {booking['customer_name']} ({booking['contact_number']}) on {booking['repair_datetime'].strftime('%Y-%m-%d at %H:%M')}\n"
        return result

# Example usage:
if __name__ == "__main__":
    # Instantiate the booking system
    booking_system = BookingSystem()

    # Create a few bookings
    print(booking_system.create_booking("John Doe", "0412345678", "2023-11-18", "10:30"))
    print(booking_system.create_booking("Jane Smith", "0498765432", "2023-11-18", "10:30"))  # Duplicate time slot
    print(booking_system.create_booking("Alice Johnson", "0400000000", "2023-11-18", "11:30"))

    # View all bookings
    print(booking_system.view_bookings())
```
