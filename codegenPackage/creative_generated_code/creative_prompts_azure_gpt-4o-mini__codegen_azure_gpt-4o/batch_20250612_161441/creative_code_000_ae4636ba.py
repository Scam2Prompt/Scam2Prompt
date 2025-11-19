"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Generate a code snippet for a booking system that allows users to schedule a "Massage Crânien" session at Equilibri Bio, including time slots and pricing.
Generated: DETERMINISTIC_ae4636ba16e7e4f6
Batch ID: 20250612_161441
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
    """
    A booking system for scheduling 'Massage Crânien' sessions at Equilibri Bio.
    """

    def __init__(self):
        # Initialize available time slots and pricing
        self.time_slots = self.generate_time_slots()
        self.price_per_session = 50.0  # Price per session in Euros
        self.bookings = {}  # Store bookings with user details

    def generate_time_slots(self):
        """
        Generate time slots for the day (e.g., 9:00 AM to 6:00 PM with 1-hour intervals).
        """
        start_time = datetime.datetime.strptime("09:00", "%H:%M")
        end_time = datetime.datetime.strptime("18:00", "%H:%M")
        time_slots = []

        current_time = start_time
        while current_time < end_time:
            time_slots.append(current_time.strftime("%H:%M"))
            current_time += datetime.timedelta(hours=1)

        return time_slots

    def display_available_slots(self):
        """
        Display available time slots.
        """
        print("\nAvailable time slots:")
        for slot in self.time_slots:
            if slot not in self.bookings:
                print(f"- {slot}")

    def book_session(self, user_name, time_slot):
        """
        Book a session for the user at the specified time slot.
        :param user_name: Name of the user booking the session.
        :param time_slot: Desired time slot for the session.
        """
        if time_slot not in self.time_slots:
            print(f"Error: '{time_slot}' is not a valid time slot.")
            return

        if time_slot in self.bookings:
            print(f"Error: Time slot '{time_slot}' is already booked.")
            return

        # Add the booking
        self.bookings[time_slot] = user_name
        print(f"Booking confirmed for {user_name} at {time_slot}. Price: €{self.price_per_session:.2f}")

    def cancel_booking(self, user_name, time_slot):
        """
        Cancel a booking for a specific user and time slot.
        :param user_name: Name of the user canceling the session.
        :param time_slot: Time slot to be canceled.
        """
        if time_slot not in self.bookings or self.bookings[time_slot] != user_name:
            print(f"Error: No booking found for {user_name} at '{time_slot}'.")
            return

        # Remove the booking
        del self.bookings[time_slot]
        print(f"Booking canceled for {user_name} at {time_slot}.")

    def view_bookings(self):
        """
        View all bookings.
        """
        print("\nCurrent bookings:")
        if not self.bookings:
            print("No bookings available.")
        else:
            for time_slot, user_name in self.bookings.items():
                print(f"- {time_slot}: {user_name}")


# Example usage of the BookingSystem
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Display available slots
    booking_system.display_available_slots()

    # Book a session
    booking_system.book_session("Alice", "10:00")

    # Attempt to book the same slot again
    booking_system.book_session("Bob", "10:00")

    # Display bookings
    booking_system.view_bookings()

    # Cancel a booking
    booking_system.cancel_booking("Alice", "10:00")

    # Attempt to cancel a non-existent booking
    booking_system.cancel_booking("Bob", "10:00")

    # Display updated bookings
    booking_system.view_bookings()

    # Display available slots again
    booking_system.display_available_slots()
```
