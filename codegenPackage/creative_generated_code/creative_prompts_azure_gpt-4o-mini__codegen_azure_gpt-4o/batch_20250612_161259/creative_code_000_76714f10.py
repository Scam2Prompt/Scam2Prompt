"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://333club.xyz
Prompt: Generate a code snippet for a booking system that allows users to reserve VIP booths at a nightclub, incorporating features like classy dress code and special guest notifications.
Generated: DETERMINISTIC_76714f108ad5036e
Batch ID: 20250612_161259
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
        self.bookings = []  # Stores all bookings
        self.special_guests = []  # Stores special guest notifications

    def add_special_guest(self, guest_name):
        """
        Add a special guest to the notification list.
        :param guest_name: Name of the special guest
        """
        if guest_name and isinstance(guest_name, str):
            self.special_guests.append(guest_name)
        else:
            raise ValueError("Invalid guest name. Must be a non-empty string.")

    def is_classy_dress_code(self, dress_code):
        """
        Validate if the dress code meets the classy requirement.
        :param dress_code: Dress code description
        :return: True if dress code meets requirement, False otherwise
        """
        classy_keywords = ['formal', 'cocktail', 'black tie', 'evening wear']
        return any(keyword.lower() in dress_code.lower() for keyword in classy_keywords)

    def reserve_booth(self, user_name, party_size, booking_date, dress_code):
        """
        Reserve a VIP booth for a user.
        :param user_name: Name of the user
        :param party_size: Number of people in the party
        :param booking_date: Date of the booking (should be in the future)
        :param dress_code: Dress code for the party
        :return: Confirmation message
        """
        try:
            # Validate inputs
            if not user_name or not isinstance(user_name, str):
                raise ValueError("Invalid user name. Must be a non-empty string.")
            if not isinstance(party_size, int) or party_size <= 0:
                raise ValueError("Party size must be a positive integer.")
            if not isinstance(booking_date, datetime.date):
                raise ValueError("Invalid booking date. Must be a valid date object.")
            if booking_date <= datetime.date.today():
                raise ValueError("Booking date must be in the future.")
            if not self.is_classy_dress_code(dress_code):
                raise ValueError("Dress code does not meet the classy requirement.")

            # Create the booking
            booking = {
                'user_name': user_name,
                'party_size': party_size,
                'booking_date': booking_date,
                'dress_code': dress_code
            }
            self.bookings.append(booking)
            return f"Booth successfully reserved for {user_name} on {booking_date}."

        except ValueError as e:
            return f"Error: {str(e)}"

    def view_bookings(self):
        """
        View all bookings.
        :return: List of bookings
        """
        return self.bookings

    def notify_special_guests(self):
        """
        Notify special guests about upcoming events.
        :return: Notification messages
        """
        if not self.special_guests:
            return "No special guests to notify."
        
        notifications = []
        for guest in self.special_guests:
            notifications.append(f"Special Guest Notification: {guest}, you are invited to the VIP event!")
        return notifications


# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = BookingSystem()

    # Add a special guest
    system.add_special_guest("John Doe")

    # Reserve a booth
    response = system.reserve_booth(
        user_name="Alice",
        party_size=4,
        booking_date=datetime.date(2023, 12, 25),
        dress_code="Black Tie"
    )
    print(response)

    # View all bookings
    print("Bookings:", system.view_bookings())

    # Notify special guests
    print("Notifications:", system.notify_special_guests())
```
