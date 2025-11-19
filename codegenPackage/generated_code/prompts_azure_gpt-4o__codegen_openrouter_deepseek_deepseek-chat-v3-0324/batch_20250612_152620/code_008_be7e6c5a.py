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
import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple


class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"


class ServiceType(Enum):
    BREAKFAST = "Breakfast"
    WIFI = "WiFi"
    AIR_CONDITIONING = "Air Conditioning"
    LAUNDRY = "Laundry"


class RoomStatus(Enum):
    AVAILABLE = "Available"
    OCCUPIED = "Occupied"
    MAINTENANCE = "Maintenance"


class Guest:
    def __init__(self, name: str, passport_id: str, phone: str, email: str):
        self.name = name
        self.passport_id = passport_id
        self.phone = phone
        self.email = email


class Room:
    def __init__(self, number: int, room_type: RoomType, price_per_night: float, status: RoomStatus = RoomStatus.AVAILABLE):
        self.number = number
        self.type = room_type
        self.price = price_per_night
        self.status = status
        self.services: List[ServiceType] = []

    def add_service(self, service: ServiceType) -> bool:
        if service not in self.services:
            self.services.append(service)
            return True
        return False

    def remove_service(self, service: ServiceType) -> bool:
        if service in self.services:
            self.services.remove(service)
            return True
        return False


class Booking:
    def __init__(self, room: Room, guest: Guest, check_in: datetime.date, check_out: datetime.date):
        self.room = room
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.services_used: List[ServiceType] = []
        self.total_cost: float = 0.0
        self.calculate_total()

    def add_service(self, service: ServiceType) -> bool:
        if service not in self.services_used and service in self.room.services:
            self.services_used.append(service)
            self.calculate_total()
            return True
        return False

    def remove_service(self, service: ServiceType) -> bool:
        if service in self.services_used:
            self.services_used.remove(service)
            self.calculate_total()
            return True
        return False

    def calculate_total(self) -> None:
        nights = (self.check_out - self.check_in).days
        service_cost = len(self.services_used) * 10  # $10 per service per stay
        self.total_cost = (self.room.price * nights) + service_cost


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: Dict[int, Room] = {}
        self.bookings: List[Booking] = []
        self.guests: List[Guest] = []

    def add_room(self, room: Room) -> bool:
        if room.number in self.rooms:
            return False
        self.rooms[room.number] = room
        return True

    def remove_room(self, room_number: int) -> bool:
        if room_number in self.rooms:
            del self.rooms[room_number]
            return True
        return False

    def check_in(self, room_number: int, guest: Guest, check_in: datetime.date, check_out: datetime.date) -> Optional[Booking]:
        if room_number not in self.rooms:
            return None
        
        room = self.rooms[room_number]
        if room.status != RoomStatus.AVAILABLE:
            return None

        # Check for date conflicts
        for booking in self.bookings:
            if booking.room.number == room_number:
                if not (check_out <= booking.check_in or check_in >= booking.check_out):
                    return None

        room.status = RoomStatus.OCCUPIED
        self.guests.append(guest)
        booking = Booking(room, guest, check_in, check_out)
        self.bookings.append(booking)
        return booking

    def check_out(self, room_number: int) -> Optional[float]:
        if room_number not in self.rooms:
            return None
        
        room = self.rooms[room_number]
        if room.status != RoomStatus.OCCUPIED:
            return None

        booking = None
        for b in self.bookings:
            if b.room.number == room_number and b.check_out >= datetime.date.today():
                booking = b
                break

        if not booking:
            return None

        room.status = RoomStatus.AVAILABLE
        self.bookings.remove(booking)
        return booking.total_cost

    def get_available_rooms(self, room_type: Optional[RoomType] = None) -> List[Room]:
        available = []
        for room in self.rooms.values():
            if room.status == RoomStatus.AVAILABLE:
                if room_type is None or room.type == room_type:
                    available.append(room)
        return available

    def get_room_services(self, room_number: int) -> Optional[List[ServiceType]]:
        if room_number not in self.rooms:
            return None
        return self.rooms[room_number].services.copy()

    def add_room_service(self, room_number: int, service: ServiceType) -> bool:
        if room_number not in self.rooms:
            return False
        return self.rooms[room_number].add_service(service)

    def remove_room_service(self, room_number: int, service: ServiceType) -> bool:
        if room_number not in self.rooms:
            return False
        return self.rooms[room_number].remove_service(service)

    def get_current_guests(self) -> List[Tuple[Guest, Room]]:
        current_guests = []
        for booking in self.bookings:
            if booking.check_in <= datetime.date.today() <= booking.check_out:
                current_guests.append((booking.guest, booking.room))
        return current_guests


# Example usage
if __name__ == "__main__":
    hotel = Hotel("Hostal Koltin Suchitoto")
    
    # Add rooms
    room101 = Room(101, RoomType.SINGLE, 50.0)
    room102 = Room(102, RoomType.DOUBLE, 75.0)
    room201 = Room(201, RoomType.SUITE, 120.0)
    
    hotel.add_room(room101)
    hotel.add_room(room102)
    hotel.add_room(room201)
    
    # Add services to rooms
    room101.add_service(ServiceType.WIFI)
    room101.add_service(ServiceType.AIR_CONDITIONING)
    room102.add_service(ServiceType.WIFI)
    room102.add_service(ServiceType.BREAKFAST)
    room201.add_service(ServiceType.WIFI)
    room201.add_service(ServiceType.AIR_CONDITIONING)
    room201.add_service(ServiceType.BREAKFAST)
    room201.add_service(ServiceType.LAUNDRY)
    
    # Create guests
    guest1 = Guest("John Doe", "P12345678", "+123456789", "john@example.com")
    guest2 = Guest("Jane Smith", "P87654321", "+987654321", "jane@example.com")
    
    # Check in guests
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    booking1 = hotel.check_in(101, guest1, today, tomorrow)
    booking2 = hotel.check_in(201, guest2, today, today + datetime.timedelta(days=3))
    
    if booking1:
        booking1.add_service(ServiceType.WIFI)
    
    if booking2:
        booking2.add_service(ServiceType.BREAKFAST)
        booking2.add_service(ServiceType.LAUNDRY)
    
    # Display current guests
    print("Current Guests:")
    for guest, room in hotel.get_current_guests():
        print(f"{guest.name} in Room {room.number}")
    
    # Check out
    total = hotel.check_out(101)
    if total is not None:
        print(f"Room 101 checked out. Total: ${total:.2f}")
```
