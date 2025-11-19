"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: Can you provide a code snippet for a booking system that allows users to schedule text-based counselling sessions, inspired by the features of Text Counselling Online?
Generated: DETERMINISTIC_cca11cc5bcc73277
Batch ID: 20250612_162050
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
        # Initialize an empty list to hold all bookings
        self.bookings = []

    def create_booking(self, user_name, date_str, time_str):
        """
        Create a new booking for a counselling session.
        
        :param user_name: Name of the user creating the booking.
        :param date_str: Date of the counselling session (format: 'YYYY-MM-DD').
        :param time_str: Time of the counselling session (format: 'HH:MM').
        :return: Confirmation message or error message.
        """
        try:
            # Parse the date and time strings into datetime objects
            session_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            session_time = datetime.datetime.strptime(time_str, '%H:%M').time()
            
            # Check if the booking is in the future
            now = datetime.datetime.now()
            session_datetime = datetime.datetime.combine(session_date, session_time)
            if session_datetime <= now:
                return "Error: You can only book sessions in the future."
            
            # Check for time slot conflicts
            for booking in self.bookings:
                if booking['date'] == session_date and booking['time'] == session_time:
                    return "Error: This time slot is already booked."
            
            # Add the new booking to the list
            new_booking = {
                'user_name': user_name,
                'date': session_date,
                'time': session_time
            }
            self.bookings.append(new_booking)
            return f"Booking confirmed for {user_name} on {date_str} at {time_str}."
        
        except ValueError as e:
            # Handle invalid date/time format
            return f"Error: Invalid date or time format. {str(e)}"

    def view_bookings(self):
        """
        View all scheduled bookings.
        
        :return: A list of bookings or a message if there are no bookings.
        """
        if not self.bookings:
            return "No bookings available."
        
        booking_list = []
        for booking in self.bookings:
            booking_list.append(
                f"User: {booking['user_name']}, Date: {booking['date']}, Time: {booking['time']}"
            )
        return '\n'.join(booking_list)

    def cancel_booking(self, user_name, date_str, time_str):
        """
        Cancel an existing booking.
        
        :param user_name: Name of the user cancelling the booking.
        :param date_str: Date of the counselling session to cancel (format: 'YYYY-MM-DD').
        :param time_str: Time of the counselling session to cancel (format: 'HH:MM').
        :return: Confirmation or error message.
        """
        try:
            # Parse the date and time strings into datetime objects
            session_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            session_time = datetime.datetime.strptime(time_str, '%H:%M').time()
            
            # Find and remove the booking
            for booking in self.bookings:
                if (booking['user_name'] == user_name and 
                    booking['date'] == session_date and 
                    booking['time'] == session_time):
                    self.bookings.remove(booking)
                    return f"Booking cancelled for {user_name} on {date_str} at {time_str}."
            
            return "Error: Booking not found."
        
        except ValueError as e:
            # Handle invalid date/time format
            return f"Error: Invalid date or time format. {str(e)}"

# Example usage:
if __name__ == "__main__":
    system = BookingSystem()
    
    print(system.create_booking("Alice", "2023-12-01", "14:00"))  # Successful booking
    print(system.create_booking("Bob", "2023-12-01", "14:00"))    # Conflict with Alice's booking
    print(system.create_booking("Charlie", "2023-11-01", "10:00"))  # Future booking
    
    print("\nCurrent bookings:")
    print(system.view_bookings())  # View all bookings
    
    print("\nCancelling a booking:")
    print(system.cancel_booking("Alice", "2023-12-01", "14:00"))  # Cancel Alice's booking
    
    print("\nCurrent bookings:")
    print(system.view_bookings())  # View remaining bookings
```
