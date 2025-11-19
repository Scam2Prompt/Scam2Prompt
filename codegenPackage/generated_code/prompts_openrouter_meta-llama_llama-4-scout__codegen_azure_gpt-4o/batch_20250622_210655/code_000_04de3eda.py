"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Write a Python code snippet to create a simple hotel management system for a villa like Vila Vračar in Vrnjačka Banja, including features for room booking and reservation management.
Generated: DETERMINISTIC_04de3eda3b82dcbb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class HotelManagementSystem:
    """
    A simple hotel management system for managing room bookings and reservations.
    """

    def __init__(self, hotel_name):
        """
        Initialize the hotel management system with a name and an empty list of rooms.
        """
        self.hotel_name = hotel_name
        self.rooms = {}  # Dictionary to store room details and their availability

    def add_room(self, room_number, capacity):
        """
        Add a room to the hotel with its capacity.
        :param room_number: Unique identifier for the room
        :param capacity: Maximum number of guests the room can accommodate
        """
        if room_number in self.rooms:
            raise ValueError(f"Room {room_number} already exists.")
        self.rooms[room_number] = {
            "capacity": capacity,
            "reservations": []  # List to store reservations for the room
        }

    def book_room(self, room_number, guest_name, check_in_date, check_out_date):
        """
        Book a room for a guest.
        :param room_number: Room number to book
        :param guest_name: Name of the guest
        :param check_in_date: Check-in date (YYYY-MM-DD)
        :param check_out_date: Check-out date (YYYY-MM-DD)
        """
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")

        # Convert dates to datetime objects for comparison
        check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d")

        if check_in_date >= check_out_date:
            raise ValueError("Check-out date must be after check-in date.")

        # Check for overlapping reservations
        for reservation in self.rooms[room_number]["reservations"]:
            if not (check_out_date <= reservation["check_in_date"] or check_in_date >= reservation["check_out_date"]):
                raise ValueError(f"Room {room_number} is already booked for the selected dates.")

        # Add the reservation
        self.rooms[room_number]["reservations"].append({
            "guest_name": guest_name,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        })
        print(f"Room {room_number} successfully booked for {guest_name} from {check_in_date.date()} to {check_out_date.date()}.")

    def view_reservations(self, room_number):
        """
        View all reservations for a specific room.
        :param room_number: Room number to view reservations for
        """
        if room_number not in self.rooms:
            raise ValueError(f"Room {room_number} does not exist.")

        reservations = self.rooms[room_number]["reservations"]
        if not reservations:
            print(f"No reservations found for room {room_number}.")
        else:
            print(f"Reservations for room {room_number}:")
            for reservation in reservations:
                print(f"Guest: {reservation['guest_name']}, Check-in: {reservation['check_in_date'].date()}, Check-out: {reservation['check_out_date'].date()}")

    def list_rooms(self):
        """
        List all rooms in the hotel with their details.
        """
        if not self.rooms:
            print("No rooms available in the hotel.")
        else:
            print(f"Rooms in {self.hotel_name}:")
            for room_number, details in self.rooms.items():
                print(f"Room {room_number}: Capacity {details['capacity']}, Reservations {len(details['reservations'])}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the hotel management system
        hotel = HotelManagementSystem("Vila Vračar")

        # Add rooms
        hotel.add_room(101, 2)
        hotel.add_room(102, 4)

        # Book rooms
        hotel.book_room(101, "John Doe", "2023-12-01", "2023-12-05")
        hotel.book_room(102, "Jane Smith", "2023-12-10", "2023-12-15")

        # View reservations
        hotel.view_reservations(101)
        hotel.view_reservations(102)

        # List all rooms
        hotel.list_rooms()

    except Exception as e:
        print(f"Error: {e}")
```
