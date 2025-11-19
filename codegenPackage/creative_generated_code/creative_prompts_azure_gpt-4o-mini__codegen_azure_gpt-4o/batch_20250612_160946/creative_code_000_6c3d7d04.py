"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Generate a code snippet for a booking system that allows users to reserve private offices or meeting rooms at a coworking space like Coworking Comércio.
Generated: DETERMINISTIC_6c3d7d042f25b8fd
Batch ID: 20250612_160946
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
    A class to manage bookings for private offices and meeting rooms at a coworking space.
    """

    def __init__(self):
        # Initialize available spaces and their bookings
        self.spaces = {
            "private_office": [],
            "meeting_room": []
        }

    def is_available(self, space_type, start_time, end_time):
        """
        Check if a space is available for the given time range.
        :param space_type: str, type of space ('private_office' or 'meeting_room')
        :param start_time: datetime, start time of booking
        :param end_time: datetime, end time of booking
        :return: bool, True if available, False otherwise
        """
        for booking in self.spaces[space_type]:
            if start_time < booking['end_time'] and end_time > booking['start_time']:
                # Time conflict detected
                return False
        return True

    def reserve_space(self, space_type, start_time, end_time, user_name):
        """
        Reserve a space if available.
        :param space_type: str, type of space ('private_office' or 'meeting_room')
        :param start_time: datetime, start time of booking
        :param end_time: datetime, end time of booking
        :param user_name: str, name of the user making the reservation
        :return: str, success or error message
        """
        if space_type not in self.spaces:
            return "Error: Invalid space type. Choose 'private_office' or 'meeting_room'."

        if start_time >= end_time:
            return "Error: Start time must be before end time."

        if self.is_available(space_type, start_time, end_time):
            self.spaces[space_type].append({
                "start_time": start_time,
                "end_time": end_time,
                "user_name": user_name
            })
            return f"Success: {space_type} reserved by {user_name} from {start_time} to {end_time}."
        else:
            return f"Error: {space_type} is not available for the selected time range."

    def view_bookings(self, space_type):
        """
        View all bookings for a specific type of space.
        :param space_type: str, type of space ('private_office' or 'meeting_room')
        :return: list of dicts, bookings for the specified space type
        """
        if space_type not in self.spaces:
            return "Error: Invalid space type. Choose 'private_office' or 'meeting_room'."
        return self.spaces[space_type]


# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    booking_system = BookingSystem()

    # Reserve spaces
    print(booking_system.reserve_space(
        space_type="private_office",
        start_time=datetime.datetime(2023, 10, 15, 9, 0),
        end_time=datetime.datetime(2023, 10, 15, 12, 0),
        user_name="Alice"
    ))

    print(booking_system.reserve_space(
        space_type="meeting_room",
        start_time=datetime.datetime(2023, 10, 15, 10, 0),
        end_time=datetime.datetime(2023, 10, 15, 11, 0),
        user_name="Bob"
    ))

    # Attempt conflicting booking
    print(booking_system.reserve_space(
        space_type="private_office",
        start_time=datetime.datetime(2023, 10, 15, 11, 0),
        end_time=datetime.datetime(2023, 10, 15, 13, 0),
        user_name="Charlie"
    ))

    # View bookings for private offices
    print("Private Office Bookings:", booking_system.view_bookings("private_office"))

    # View bookings for meeting rooms
    print("Meeting Room Bookings:", booking_system.view_bookings("meeting_room"))
```
