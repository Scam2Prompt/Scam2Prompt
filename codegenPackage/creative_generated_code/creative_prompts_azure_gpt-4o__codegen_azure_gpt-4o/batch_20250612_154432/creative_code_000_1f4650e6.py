"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python script to simulate a plumbing service booking system for Certified Plumbers Graham, TX, including fields for service type (e.g., leak detection, repiping), customer details, and preferred appointment time.
Generated: DETERMINISTIC_1f4650e6e7052d67
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PlumbingServiceBooking:
    """Class to simulate a plumbing service booking system."""

    def __init__(self):
        # Initialize bookings as an empty list
        self.bookings = []

    def create_booking(self, customer_name, customer_phone, service_type, preferred_time):
        """
        Create a new booking.
        
        Args:
            customer_name (str): Name of the customer.
            customer_phone (str): Phone number of the customer.
            service_type (str): Type of plumbing service (e.g., leak detection, repiping).
            preferred_time (str): Preferred appointment time in "YYYY-MM-DD HH:MM" format.
        
        Returns:
            dict: The created booking record.
        """
        try:
            # Validate preferred_time format
            appointment_time = datetime.datetime.strptime(preferred_time, "%Y-%m-%d %H:%M")
            
            # Create a booking record
            booking = {
                "customer_name": customer_name,
                "customer_phone": customer_phone,
                "service_type": service_type,
                "preferred_time": appointment_time,
                "booking_id": len(self.bookings) + 1  # Generate a unique booking ID
            }
            
            # Append the booking to the list
            self.bookings.append(booking)
            return booking
        
        except ValueError as error:
            # Handle invalid date-time format
            raise ValueError("Preferred time format is invalid. Use 'YYYY-MM-DD HH:MM'.") from error

    def view_bookings(self):
        """
        Return all bookings.
        
        Returns:
            list: List of all booking records.
        """
        return self.bookings

    def cancel_booking(self, booking_id):
        """
        Cancel a booking by booking ID.
        
        Args:
            booking_id (int): ID of the booking to be canceled.
        
        Returns:
            bool: True if booking was successfully canceled, False otherwise.
        """
        for booking in self.bookings:
            if booking["booking_id"] == booking_id:
                self.bookings.remove(booking)
                return True  # Successfully canceled
        return False  # Booking ID not found


# Main script
if __name__ == "__main__":
    # Create an instance of the booking system
    booking_system = PlumbingServiceBooking()
    
    # Example usage
    print("Welcome to Certified Plumbers Graham, TX Booking System!")
    
    # Create bookings
    try:
        booking1 = booking_system.create_booking(
            customer_name="John Doe",
            customer_phone="123-456-7890",
            service_type="Leak Detection",
            preferred_time="2023-10-15 14:30"
        )
        print(f"Booking created: {booking1}")
        
        booking2 = booking_system.create_booking(
            customer_name="Jane Smith",
            customer_phone="321-654-0987",
            service_type="Repiping",
            preferred_time="2023-10-16 09:00"
        )
        print(f"Booking created: {booking2}")
    except ValueError as ve:
        print(f"Error creating booking: {ve}")
    
    # View all bookings
    print("Current bookings:")
    for booking in booking_system.view_bookings():
        print(booking)
    
    # Cancel a booking
    booking_id_to_cancel = 1
    if booking_system.cancel_booking(booking_id_to_cancel):
        print(f"Successfully canceled booking with ID {booking_id_to_cancel}.")
    else:
        print(f"Failed to cancel booking with ID {booking_id_to_cancel}.")
    
    # View bookings after cancellation
    print("Bookings after cancellation:")
    for booking in booking_system.view_bookings():
        print(booking)
```
