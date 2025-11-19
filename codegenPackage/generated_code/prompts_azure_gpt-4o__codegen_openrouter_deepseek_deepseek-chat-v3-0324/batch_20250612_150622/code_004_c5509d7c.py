"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to rent out Workshops and SPACE in Big Time, including a feature to calculate rental fees based on user-defined parameters.
Generated: DETERMINISTIC_c5509d7ca66b7c74
Batch ID: 20250612_150622
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


class SpaceType(Enum):
    WORKSHOP = "workshop"
    OPEN_SPACE = "open_space"


class RentalStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    MAINTENANCE = "maintenance"


class Space:
    def __init__(
        self,
        space_id: str,
        name: str,
        space_type: SpaceType,
        base_price_per_hour: float,
        capacity: int,
        status: RentalStatus = RentalStatus.AVAILABLE,
    ):
        self.space_id = space_id
        self.name = name
        self.space_type = space_type
        self.base_price_per_hour = base_price_per_hour
        self.capacity = capacity
        self.status = status
        self.bookings: List[Booking] = []

    def is_available(self, start_time: datetime.datetime, end_time: datetime.datetime) -> bool:
        if self.status != RentalStatus.AVAILABLE:
            return False

        for booking in self.bookings:
            if not (end_time <= booking.start_time or start_time >= booking.end_time):
                return False
        return True

    def calculate_rental_fee(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_people: int,
        discount: float = 0.0,
    ) -> float:
        duration_hours = (end_time - start_time).total_seconds() / 3600
        base_fee = self.base_price_per_hour * duration_hours

        # Apply capacity surcharge if exceeded
        if num_people > self.capacity:
            excess = num_people - self.capacity
            base_fee *= 1 + (excess * 0.1)  # 10% surcharge per excess person

        # Apply discount if any
        final_fee = base_fee * (1 - discount)
        return round(final_fee, 2)


class Booking:
    def __init__(
        self,
        booking_id: str,
        space: Space,
        customer_id: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_people: int,
        discount: float = 0.0,
    ):
        self.booking_id = booking_id
        self.space = space
        self.customer_id = customer_id
        self.start_time = start_time
        self.end_time = end_time
        self.num_people = num_people
        self.discount = discount
        self.total_fee = space.calculate_rental_fee(start_time, end_time, num_people, discount)


class RentalSystem:
    def __init__(self):
        self.spaces: Dict[str, Space] = {}
        self.bookings: Dict[str, Booking] = {}

    def add_space(self, space: Space) -> None:
        if space.space_id in self.spaces:
            raise ValueError(f"Space with ID {space.space_id} already exists")
        self.spaces[space.space_id] = space

    def remove_space(self, space_id: str) -> None:
        if space_id not in self.spaces:
            raise ValueError(f"Space with ID {space_id} not found")
        del self.spaces[space_id]

    def get_available_spaces(
        self,
        space_type: Optional[SpaceType] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> List[Space]:
        available_spaces = []
        for space in self.spaces.values():
            if space_type and space.space_type != space_type:
                continue
            if start_time and end_time and not space.is_available(start_time, end_time):
                continue
            available_spaces.append(space)
        return available_spaces

    def create_booking(
        self,
        space_id: str,
        customer_id: str,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_people: int,
        discount: float = 0.0,
    ) -> Booking:
        if space_id not in self.spaces:
            raise ValueError(f"Space with ID {space_id} not found")

        space = self.spaces[space_id]

        if not space.is_available(start_time, end_time):
            raise ValueError(f"Space {space_id} is not available for the requested time")

        if num_people <= 0:
            raise ValueError("Number of people must be positive")

        if discount < 0 or discount >= 1:
            raise ValueError("Discount must be between 0 and 1")

        booking_id = f"B-{datetime.datetime.now().timestamp()}"
        booking = Booking(
            booking_id=booking_id,
            space=space,
            customer_id=customer_id,
            start_time=start_time,
            end_time=end_time,
            num_people=num_people,
            discount=discount,
        )

        space.bookings.append(booking)
        self.bookings[booking_id] = booking
        return booking

    def cancel_booking(self, booking_id: str) -> None:
        if booking_id not in self.bookings:
            raise ValueError(f"Booking with ID {booking_id} not found")

        booking = self.bookings[booking_id]
        booking.space.bookings.remove(booking)
        del self.bookings[booking_id]

    def get_booking_details(self, booking_id: str) -> Dict:
        if booking_id not in self.bookings:
            raise ValueError(f"Booking with ID {booking_id} not found")

        booking = self.bookings[booking_id]
        return {
            "booking_id": booking.booking_id,
            "space_id": booking.space.space_id,
            "space_name": booking.space.name,
            "customer_id": booking.customer_id,
            "start_time": booking.start_time,
            "end_time": booking.end_time,
            "num_people": booking.num_people,
            "discount": booking.discount,
            "total_fee": booking.total_fee,
        }


# Example usage
if __name__ == "__main__":
    system = RentalSystem()

    # Add some spaces
    workshop1 = Space(
        space_id="WS-001",
        name="Woodworking Workshop",
        space_type=SpaceType.WORKSHOP,
        base_price_per_hour=50.0,
        capacity=10,
    )
    open_space1 = Space(
        space_id="OS-001",
        name="Main Event Space",
        space_type=SpaceType.OPEN_SPACE,
        base_price_per_hour=100.0,
        capacity=50,
    )
    system.add_space(workshop1)
    system.add_space(open_space1)

    # Create a booking
    now = datetime.datetime.now()
    start_time = now + datetime.timedelta(days=1)
    end_time = start_time + datetime.timedelta(hours=3)

    try:
        booking = system.create_booking(
            space_id="WS-001",
            customer_id="CUST-123",
            start_time=start_time,
            end_time=end_time,
            num_people=8,
            discount=0.1,  # 10% discount
        )
        print(f"Booking created. Total fee: ${booking.total_fee}")
    except ValueError as e:
        print(f"Error creating booking: {e}")

    # Get booking details
    try:
        details = system.get_booking_details(booking.booking_id)
        print("Booking details:", details)
    except ValueError as e:
        print(f"Error getting booking details: {e}")
```
