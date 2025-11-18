"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a hotel management system that tracks room availability, guest check-ins, and services offered (e.g., breakfast, WiFi, air conditioning), inspired by Hostal Koltin Suchitoto's amenities.
Generated: DETERMINISTIC_be7e6c5a199e11d4
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Room:
    """Class to represent a hotel room."""

    def __init__(self, room_number, room_type, amenities):
        """
        Initialize a new room.

        :param room_number: Unique identifier for the room
        :param room_type: Type of room (e.g., 'single', 'double', 'suite')
        :param amenities: List of amenities available in the room
        """
        self.room_number = room_number
        self.room_type = room_type
        self.amenities = amenities
        self.is_available = True

    def check_in(self):
        """Check in a guest and mark the room as unavailable."""
        if not self.is_available:
            raise Exception("Room is already occupied.")
        self.is_available = False

    def check_out(self):
        """Check out a guest and mark the room as available."""
        if self.is_available:
            raise Exception("Room is already available.")
        self.is_available = True


class Guest:
    """Class to represent a hotel guest."""

    def __init__(self, name, contact_info):
        """
        Initialize a new guest.

        :param name: Name of the guest
        :param contact_info: Contact information of the guest
        """
        self.name = name
        self.contact_info = contact_info


class Hotel:
    """Class to represent the hotel management system."""

    def __init__(self):
        """Initialize the hotel with an empty room list and guest list."""
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        """Add a new room to the hotel."""
        self.rooms.append(room)

    def find_available_room(self, room_type):
        """
        Find an available room of a specific type.

        :param room_type: The type of room to search for
        :return: Available room or None
        """
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
                return room
        return None

    def check_in_guest(self, guest, room_type):
        """
        Check in a guest by finding an available room.

        :param guest: Guest object to check in
        :param room_type: The type of room requested
        :raises Exception: If no available room is found
        """
        room = self.find_available_room(room_type)
        if room is None:
            raise Exception("No available rooms of type: {}".format(room_type))
        room.check_in()
        self.guests.append(guest)

    def check_out_guest(self, guest):
        """
        Check out a guest and free up their room.

        :param guest: Guest object to check out
        :raises Exception: If the guest is not found
        """
        for room in self.rooms:
            if not room.is_available:
                room.check_out()
                self.guests.remove(guest)
                return
        raise Exception("Guest not found or no room occupied.")

    def list_rooms(self):
        """Print the list of rooms and their availability."""
        for room in self.rooms:
            status = "Available" if room.is_available else "Occupied"
            print(f"Room {room.room_number} ({room.room_type}): {status}")


# Example usage:

if __name__ == "__main__":
    # Create hotel instance
    hotel = Hotel()

    # Add rooms to the hotel
    hotel.add_room(Room(101, 'single', ['WiFi', 'Air Conditioning']))
    hotel.add_room(Room(102, 'double', ['WiFi', 'Breakfast']))
    hotel.add_room(Room(201, 'suite', ['WiFi', 'Breakfast', 'Air Conditioning']))

    # Check room status
    print("Current room status:")
    hotel.list_rooms()

    # Create a guest
    guest1 = Guest("Alice Smith", "alice.smith@example.com")

    # Check in guest
    try:
        hotel.check_in_guest(guest1, 'double')
        print("Checked in guest:", guest1.name)
    except Exception as e:
        print("Error during check-in:", e)

    # Check room status
    print("\nRoom status after check-in:")
    hotel.list_rooms()

    # Check out guest
    try:
        hotel.check_out_guest(guest1)
        print("Checked out guest:", guest1.name)
    except Exception as e:
        print("Error during check-out:", e)

    # Final room status
    print("\nFinal room status:")
    hotel.list_rooms()
```
