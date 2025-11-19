"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a hotel management system that tracks room availability, guest check-ins, and services offered (e.g., breakfast, WiFi, air conditioning), inspired by Hostal Koltin Suchitoto's amenities.
Generated: DETERMINISTIC_be7e6c5a199e11d4
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Room:
    """Class to represent a hotel room."""
    
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def check_in(self):
        """Check in a guest and mark the room as unavailable."""
        if not self.is_available:
            raise Exception(f"Room {self.room_number} is already occupied.")
        self.is_available = False

    def check_out(self):
        """Check out a guest and mark the room as available."""
        if self.is_available:
            raise Exception(f"Room {self.room_number} is already available.")
        self.is_available = True


class Guest:
    """Class to represent a hotel guest."""
    
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info


class Hotel:
    """Class to represent the hotel management system."""
    
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        """Add a room to the hotel."""
        self.rooms.append(room)

    def check_in_guest(self, room_number, guest):
        """Check in a guest to a specified room."""
        room = self.find_room(room_number)
        if room:
            room.check_in()
            self.guests.append(guest)
            print(f"{guest.name} has checked into room {room_number}.")
        else:
            raise Exception(f"Room {room_number} does not exist.")

    def check_out_guest(self, room_number):
        """Check out a guest from a specified room."""
        room = self.find_room(room_number)
        if room:
            room.check_out()
            print(f"Room {room_number} has been checked out.")
        else:
            raise Exception(f"Room {room_number} does not exist.")

    def find_room(self, room_number):
        """Find a room by its number."""
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def get_available_rooms(self):
        """Return a list of available rooms."""
        return [room for room in self.rooms if room.is_available]

    def offer_service(self, room_number, service):
        """Offer a service to a guest in a specified room."""
        room = self.find_room(room_number)
        if room and not room.is_available:
            print(f"Service '{service}' has been offered to room {room_number}.")
        else:
            raise Exception(f"Room {room_number} is not occupied or does not exist.")


# Example usage
if __name__ == "__main__":
    hotel = Hotel()
    
    # Adding rooms to the hotel
    hotel.add_room(Room(101, "Single", 50))
    hotel.add_room(Room(102, "Double", 75))
    hotel.add_room(Room(103, "Suite", 150))

    # Creating a guest
    guest1 = Guest("John Doe", "john@example.com")

    # Checking in a guest
    try:
        hotel.check_in_guest(101, guest1)
    except Exception as e:
        print(e)

    # Offering a service
    try:
        hotel.offer_service(101, "Breakfast")
    except Exception as e:
        print(e)

    # Checking out a guest
    try:
        hotel.check_out_guest(101)
    except Exception as e:
        print(e)

    # Display available rooms
    available_rooms = hotel.get_available_rooms()
    print(f"Available rooms: {[room.room_number for room in available_rooms]}")
```
