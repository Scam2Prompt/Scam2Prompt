"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Illustrate how to implement a booking system for Chalet Roc Remi that accommodates group sizes up to 11 people, with features for selecting room types and meal plans.
Generated: DETERMINISTIC_9f3daf39d22ad3ed
Batch ID: 20250612_160526
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
from typing import List, Dict, Optional

class RoomType(Enum):
    """Enum representing different room types available."""
    SINGLE = "Single"
    DOUBLE = "Double"
    FAMILY = "Family"
    SUITE = "Suite"

class MealPlan(Enum):
    """Enum representing different meal plan options."""
    NONE = "No meals"
    BREAKFAST = "Breakfast only"
    HALF_BOARD = "Half board (Breakfast and Dinner)"
    FULL_BOARD = "Full board (All meals)"

class BookingStatus(Enum):
    """Enum representing booking statuses."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class Room:
    """Class representing a room in the chalet."""
    def __init__(self, room_id: str, room_type: RoomType, capacity: int, price_per_night: float):
        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_available = True

    def __str__(self):
        return f"{self.room_type.value} Room (ID: {self.room_id}, Capacity: {self.capacity}, Price/Night: €{self.price_per_night})"

class Booking:
    """Class representing a booking in the system."""
    def __init__(
        self,
        booking_id: str,
        guest_name: str,
        group_size: int,
        rooms: List[Room],
        check_in: datetime.date,
        check_out: datetime.date,
        meal_plan: MealPlan,
        status: BookingStatus = BookingStatus.PENDING
    ):
        if group_size > 11:
            raise ValueError("Group size cannot exceed 11 people")
        
        total_capacity = sum(room.capacity for room in rooms)
        if group_size > total_capacity:
            raise ValueError("Selected rooms cannot accommodate the group size")
        
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.group_size = group_size
        self.rooms = rooms
        self.check_in = check_in
        self.check_out = check_out
        self.meal_plan = meal_plan
        self.status = status
        self.created_at = datetime.datetime.now()

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of the booking."""
        nights = (self.check_out - self.check_in).days
        room_cost = sum(room.price_per_night for room in self.rooms) * nights
        
        meal_cost = 0
        if self.meal_plan == MealPlan.BREAKFAST:
            meal_cost = 15 * self.group_size * nights
        elif self.meal_plan == MealPlan.HALF_BOARD:
            meal_cost = 35 * self.group_size * nights
        elif self.meal_plan == MealPlan.FULL_BOARD:
            meal_cost = 50 * self.group_size * nights
        
        return room_cost + meal_cost

    def confirm_booking(self):
        """Confirm the booking."""
        self.status = BookingStatus.CONFIRMED
        for room in self.rooms:
            room.is_available = False

    def cancel_booking(self):
        """Cancel the booking."""
        self.status = BookingStatus.CANCELLED
        for room in self.rooms:
            room.is_available = True

    def __str__(self):
        return (
            f"Booking ID: {self.booking_id}\n"
            f"Guest: {self.guest_name}\n"
            f"Group Size: {self.group_size}\n"
            f"Rooms: {', '.join(str(room) for room in self.rooms)}\n"
            f"Dates: {self.check_in} to {self.check_out}\n"
            f"Meal Plan: {self.meal_plan.value}\n"
            f"Status: {self.status.value}\n"
            f"Total Cost: €{self.calculate_total_cost():.2f}"
        )

class ChaletBookingSystem:
    """Main class for the chalet booking system."""
    def __init__(self):
        self.rooms = self._initialize_rooms()
        self.bookings: Dict[str, Booking] = {}
        self.next_booking_id = 1

    def _initialize_rooms(self) -> List[Room]:
        """Initialize the available rooms in the chalet."""
        return [
            Room("R101", RoomType.SINGLE, 1, 80),
            Room("R102", RoomType.SINGLE, 1, 80),
            Room("R201", RoomType.DOUBLE, 2, 120),
            Room("R202", RoomType.DOUBLE, 2, 120),
            Room("R301", RoomType.FAMILY, 4, 180),
            Room("R302", RoomType.FAMILY, 4, 180),
            Room("R401", RoomType.SUITE, 3, 200),
            Room("R402", RoomType.SUITE, 3, 200),
        ]

    def get_available_rooms(self, room_type: Optional[RoomType] = None) -> List[Room]:
        """Get available rooms, optionally filtered by room type."""
        return [
            room for room in self.rooms 
            if room.is_available and (room_type is None or room.room_type == room_type)
        ]

    def create_booking(
        self,
        guest_name: str,
        group_size: int,
        room_ids: List[str],
        check_in: datetime.date,
        check_out: datetime.date,
        meal_plan: MealPlan
    ) -> Booking:
        """Create a new booking."""
        if check_in >= check_out:
            raise ValueError("Check-out date must be after check-in date")
        
        if check_in < datetime.date.today():
            raise ValueError("Check-in date cannot be in the past")
        
        selected_rooms = []
        for room_id in room_ids:
            room = next((r for r in self.rooms if r.room_id == room_id), None)
            if not room:
                raise ValueError(f"Room with ID {room_id} not found")
            if not room.is_available:
                raise ValueError(f"Room {room_id} is not available")
            selected_rooms.append(room)
        
        booking_id = f"B{self.next_booking_id:04d}"
        self.next_booking_id += 1
        
        booking = Booking(
            booking_id=booking_id,
            guest_name=guest_name,
            group_size=group_size,
            rooms=selected_rooms,
            check_in=check_in,
            check_out=check_out,
            meal_plan=meal_plan
        )
        
        self.bookings[booking_id] = booking
        return booking

    def get_booking(self, booking_id: str) -> Optional[Booking]:
        """Retrieve a booking by its ID."""
        return self.bookings.get(booking_id)

    def cancel_booking(self, booking_id: str) -> None:
        """Cancel a booking."""
        booking = self.get_booking(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        booking.cancel_booking()

    def confirm_booking(self, booking_id: str) -> None:
        """Confirm a booking."""
        booking = self.get_booking(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        booking.confirm_booking()

# Example usage
if __name__ == "__main__":
    system = ChaletBookingSystem()
    
    # Display available rooms
    print("Available Rooms:")
    for room in system.get_available_rooms():
        print(f"- {room}")
    
    # Create a booking
    try:
        booking = system.create_booking(
            guest_name="John Smith",
            group_size=5,
            room_ids=["R301", "R201"],
            check_in=datetime.date(2023, 12, 15),
            check_out=datetime.date(2023, 12, 20),
            meal_plan=MealPlan.HALF_BOARD
        )
        booking.confirm_booking()
        print("\nBooking Created:")
        print(booking)
    except ValueError as e:
        print(f"Error creating booking: {e}")
```
