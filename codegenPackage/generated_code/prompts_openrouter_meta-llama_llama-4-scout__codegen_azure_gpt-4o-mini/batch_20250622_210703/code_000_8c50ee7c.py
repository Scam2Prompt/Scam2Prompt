"""
Generated Code Metadata:
========================
Original URL: https://gardennovaera.com.br
Prompt: Write a Python program to manage hotel room bookings, including types like casal com hidromassagem, casal, and solteiro, with options for add-ons like breakfast.
Generated: DETERMINISTIC_8c50ee7cee72edfa
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Room:
    """Class representing a hotel room."""
    
    def __init__(self, room_type, has_jacuzzi=False):
        """
        Initialize a Room instance.

        :param room_type: Type of the room (e.g., 'casal com hidromassagem', 'casal', 'solteiro').
        :param has_jacuzzi: Boolean indicating if the room has a jacuzzi.
        """
        self.room_type = room_type
        self.has_jacuzzi = has_jacuzzi
        self.is_booked = False
        self.add_ons = []

    def book(self):
        """Book the room if it is not already booked."""
        if self.is_booked:
            raise Exception("Room is already booked.")
        self.is_booked = True

    def cancel(self):
        """Cancel the booking of the room."""
        if not self.is_booked:
            raise Exception("Room is not booked.")
        self.is_booked = False

    def add_add_on(self, add_on):
        """Add an add-on service to the room booking.

        :param add_on: The add-on service to be added (e.g., 'breakfast').
        """
        self.add_ons.append(add_on)

    def get_details(self):
        """Get the details of the room including booking status and add-ons."""
        return {
            "room_type": self.room_type,
            "has_jacuzzi": self.has_jacuzzi,
            "is_booked": self.is_booked,
            "add_ons": self.add_ons
        }


class Hotel:
    """Class representing a hotel with room management capabilities."""
    
    def __init__(self):
        """Initialize the Hotel with an empty list of rooms."""
        self.rooms = []

    def add_room(self, room):
        """Add a room to the hotel.

        :param room: Room instance to be added to the hotel.
        """
        self.rooms.append(room)

    def book_room(self, room_type, has_jacuzzi=False):
        """Book a room of a specific type.

        :param room_type: Type of the room to book.
        :param has_jacuzzi: Boolean indicating if the room has a jacuzzi.
        :return: The booked room instance.
        """
        for room in self.rooms:
            if room.room_type == room_type and room.has_jacuzzi == has_jacuzzi and not room.is_booked:
                room.book()
                return room
        raise Exception("No available room of the specified type.")

    def cancel_booking(self, room):
        """Cancel the booking of a specified room.

        :param room: Room instance to cancel the booking for.
        """
        room.cancel()

    def get_available_rooms(self):
        """Get a list of available rooms in the hotel."""
        return [room.get_details() for room in self.rooms if not room.is_booked]


# Example usage
if __name__ == "__main__":
    # Create a hotel instance
    hotel = Hotel()

    # Add rooms to the hotel
    hotel.add_room(Room('casal com hidromassagem', has_jacuzzi=True))
    hotel.add_room(Room('casal'))
    hotel.add_room(Room('solteiro'))

    # Book a room
    try:
        booked_room = hotel.book_room('casal com hidromassagem', has_jacuzzi=True)
        booked_room.add_add_on('breakfast')
        print("Booked Room Details:", booked_room.get_details())
    except Exception as e:
        print("Booking Error:", e)

    # Get available rooms
    available_rooms = hotel.get_available_rooms()
    print("Available Rooms:", available_rooms)

    # Cancel booking
    try:
        hotel.cancel_booking(booked_room)
        print("Booking cancelled successfully.")
    except Exception as e:
        print("Cancellation Error:", e)

    # Check available rooms after cancellation
    available_rooms_after_cancellation = hotel.get_available_rooms()
    print("Available Rooms after Cancellation:", available_rooms_after_cancellation)
```
