"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script to manage hotel room reservations and pricing using a simple PMS system, considering revenue management techniques.
Generated: DETERMINISTIC_8845a19c9eaf409b
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Room:
    """
    Represents a hotel room with a room number, type, and base price.
    """
    def __init__(self, room_number, room_type, base_price):
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.is_reserved = False

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}) - ${self.base_price:.2f}"


class Reservation:
    """
    Represents a reservation with a guest name, room, check-in and check-out dates, and total price.
    """
    def __init__(self, guest_name, room, check_in_date, check_out_date):
        self.guest_name = guest_name
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """
        Calculates the total price of the reservation based on the number of nights and room price.
        Applies revenue management techniques (e.g., weekend pricing).
        """
        num_nights = (self.check_out_date - self.check_in_date).days
        total_price = 0
        for i in range(num_nights):
            day = self.check_in_date + datetime.timedelta(days=i)
            if day.weekday() in (4, 5):  # Friday and Saturday (weekend pricing)
                total_price += self.room.base_price * 1.2  # 20% increase for weekends
            else:
                total_price += self.room.base_price
        return total_price

    def __str__(self):
        return (f"Reservation for {self.guest_name} in Room {self.room.room_number} "
                f"from {self.check_in_date} to {self.check_out_date} - Total: ${self.total_price:.2f}")


class HotelPMS:
    """
    A simple Property Management System (PMS) for managing hotel rooms and reservations.
    """
    def __init__(self):
        self.rooms = []
        self.reservations = []

    def add_room(self, room_number, room_type, base_price):
        """
        Adds a new room to the hotel.
        """
        room = Room(room_number, room_type, base_price)
        self.rooms.append(room)

    def list_rooms(self):
        """
        Lists all rooms in the hotel.
        """
        for room in self.rooms:
            print(room)

    def make_reservation(self, guest_name, room_number, check_in_date, check_out_date):
        """
        Makes a reservation for a guest if the room is available.
        """
        try:
            room = next(r for r in self.rooms if r.room_number == room_number)
            if room.is_reserved:
                print(f"Room {room_number} is already reserved.")
                return
            reservation = Reservation(guest_name, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            room.is_reserved = True
            print(f"Reservation successful: {reservation}")
        except StopIteration:
            print(f"Room {room_number} does not exist.")
        except Exception as e:
            print(f"An error occurred while making the reservation: {e}")

    def cancel_reservation(self, guest_name, room_number):
        """
        Cancels a reservation for a guest.
        """
        try:
            reservation = next(r for r in self.reservations if r.guest_name == guest_name and r.room.room_number == room_number)
            self.reservations.remove(reservation)
            reservation.room.is_reserved = False
            print(f"Reservation for {guest_name} in Room {room_number} has been canceled.")
        except StopIteration:
            print(f"No reservation found for {guest_name} in Room {room_number}.")
        except Exception as e:
            print(f"An error occurred while canceling the reservation: {e}")

    def list_reservations(self):
        """
        Lists all reservations in the hotel.
        """
        for reservation in self.reservations:
            print(reservation)


# Example usage
if __name__ == "__main__":
    # Initialize the PMS system
    hotel_pms = HotelPMS()

    # Add rooms to the hotel
    hotel_pms.add_room(101, "Single", 100.00)
    hotel_pms.add_room(102, "Double", 150.00)
    hotel_pms.add_room(103, "Suite", 250.00)

    # List available rooms
    print("Available rooms:")
    hotel_pms.list_rooms()

    # Make reservations
    print("\nMaking reservations:")
    hotel_pms.make_reservation("John Doe", 101, datetime.date(2023, 10, 20), datetime.date(2023, 10, 23))
    hotel_pms.make_reservation("Jane Smith", 102, datetime.date(2023, 10, 21), datetime.date(2023, 10, 22))

    # List reservations
    print("\nCurrent reservations:")
    hotel_pms.list_reservations()

    # Cancel a reservation
    print("\nCanceling a reservation:")
    hotel_pms.cancel_reservation("John Doe", 101)

    # List reservations after cancellation
    print("\nReservations after cancellation:")
    hotel_pms.list_reservations()

    # List rooms after cancellation
    print("\nAvailable rooms after cancellation:")
    hotel_pms.list_rooms()
```
