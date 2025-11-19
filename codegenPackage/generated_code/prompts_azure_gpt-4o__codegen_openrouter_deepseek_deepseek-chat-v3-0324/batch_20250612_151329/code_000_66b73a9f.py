"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write Python code to simulate a hotel reservation system that incorporates revenue management principles as described in Hampton's Hotel Institute's course on Hotel Operations Management. Include features like pricing accommodation and managing sales.
Generated: DETERMINISTIC_66b73a9ffc954ba2
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum
import random
import json
import os

class RoomType(Enum):
    """Enumeration of room types available in the hotel."""
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"
    PRESIDENTIAL = "Presidential"

class ReservationStatus(Enum):
    """Enumeration of reservation statuses."""
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    CHECKED_IN = "Checked In"
    CHECKED_OUT = "Checked Out"
    NO_SHOW = "No Show"

class Season(Enum):
    """Enumeration of seasonal pricing periods."""
    LOW = "Low"
    SHOULDER = "Shoulder"
    HIGH = "High"
    PEAK = "Peak"

class RevenueManagementStrategy:
    """Base class for revenue management strategies."""
    def calculate_price(self, base_price: float, demand_factor: float, days_until_checkin: int) -> float:
        """Calculate the dynamic price based on various factors."""
        raise NotImplementedError

class DynamicPricingStrategy(RevenueManagementStrategy):
    """Implements dynamic pricing based on demand and time until check-in."""
    def calculate_price(self, base_price: float, demand_factor: float, days_until_checkin: int) -> float:
        """Calculate price with dynamic adjustments."""
        if days_until_checkin <= 7:
            return base_price * (1 + demand_factor * 0.5)
        elif days_until_checkin <= 30:
            return base_price * (1 + demand_factor * 0.3)
        else:
            return base_price * (1 + demand_factor * 0.1)

class Room:
    """Represents a hotel room with its attributes."""
    def __init__(self, room_number: str, room_type: RoomType, base_price: float):
        self.room_number = room_number
        self.room_type = room_type
        self.base_price = base_price
        self.is_available = True

    def __str__(self):
        return f"{self.room_number} - {self.room_type.value} (${self.base_price:.2f}/night)"

class Guest:
    """Represents a guest making a reservation."""
    def __init__(self, guest_id: str, name: str, email: str, phone: str):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.guest_id})"

class Reservation:
    """Represents a hotel reservation."""
    def __init__(self, reservation_id: str, guest: Guest, room: Room, 
                 check_in: datetime.date, check_out: datetime.date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.status = ReservationStatus.CONFIRMED
        self.total_price = 0.0
        self.calculate_total_price()

    def calculate_total_price(self):
        """Calculate total price based on stay duration and room price."""
        nights = (self.check_out - self.check_in).days
        self.total_price = self.room.base_price * nights

    def update_status(self, new_status: ReservationStatus):
        """Update the reservation status."""
        self.status = new_status

    def __str__(self):
        return (f"Reservation {self.reservation_id}: {self.guest.name} in {self.room.room_type.value} "
                f"from {self.check_in} to {self.check_out} (Status: {self.status.value})")

class Hotel:
    """Represents a hotel with rooms and reservations."""
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.reservations: List[Reservation] = []
        self.revenue_management_strategy = DynamicPricingStrategy()
        self.seasonal_multipliers = {
            Season.LOW: 0.8,
            Season.SHOULDER: 1.0,
            Season.HIGH: 1.2,
            Season.PEAK: 1.5
        }
        self.load_data()

    def add_room(self, room: Room):
        """Add a room to the hotel inventory."""
        self.rooms.append(room)

    def find_available_rooms(self, room_type: Optional[RoomType] = None, 
                            check_in: Optional[datetime.date] = None, 
                            check_out: Optional[datetime.date] = None) -> List[Room]:
        """Find available rooms matching criteria."""
        available_rooms = []
        
        for room in self.rooms:
            if not room.is_available:
                continue
                
            if room_type and room.room_type != room_type:
                continue
                
            if check_in and check_out:
                if not self.is_room_available(room, check_in, check_out):
                    continue
                    
            available_rooms.append(room)
            
        return available_rooms

    def is_room_available(self, room: Room, check_in: datetime.date, check_out: datetime.date) -> bool:
        """Check if a room is available for given dates."""
        for reservation in self.reservations:
            if reservation.room == room and reservation.status != ReservationStatus.CANCELLED:
                if (check_in < reservation.check_out and check_out > reservation.check_in):
                    return False
        return True

    def determine_season(self, date: datetime.date) -> Season:
        """Determine the season for a given date."""
        month = date.month
        if month in [12, 1, 2]:  # Winter - Peak for some locations
            return Season.PEAK
        elif month in [6, 7, 8]:  # Summer - High season
            return Season.HIGH
        elif month in [3, 4, 5, 9, 10, 11]:  # Spring/Fall - Shoulder season
            return Season.SHOULDER
        else:
            return Season.LOW

    def calculate_dynamic_price(self, room: Room, check_in: datetime.date, booking_date: datetime.date) -> float:
        """Calculate price using revenue management strategy."""
        days_until_checkin = (check_in - booking_date).days
        season = self.determine_season(check_in)
        base_price = room.base_price * self.seasonal_multipliers[season]
        
        # Simulate demand factor (0-1) based on random for demo purposes
        demand_factor = random.uniform(0.1, 0.9)
        
        return self.revenue_management_strategy.calculate_price(
            base_price, demand_factor, days_until_checkin
        )

    def make_reservation(self, guest: Guest, room: Room, 
                        check_in: datetime.date, check_out: datetime.date) -> Optional[Reservation]:
        """Create a new reservation if room is available."""
        if not self.is_room_available(room, check_in, check_out):
            return None
            
        room.is_available = False
        reservation_id = f"RES-{len(self.reservations)+1:04d}"
        reservation = Reservation(reservation_id, guest, room, check_in, check_out)
        
        # Apply dynamic pricing
        booking_date = datetime.date.today()
        dynamic_price = self.calculate_dynamic_price(room, check_in, booking_date)
        room.base_price = dynamic_price  # Update price for this reservation
        reservation.calculate_total_price()
        
        self.reservations.append(reservation)
        self.save_data()
        return reservation

    def cancel_reservation(self, reservation_id: str) -> bool:
        """Cancel a reservation by ID."""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.update_status(ReservationStatus.CANCELLED)
                reservation.room.is_available = True
                self.save_data()
                return True
        return False

    def check_in_guest(self, reservation_id: str) -> bool:
        """Check in a guest for their reservation."""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                if reservation.status == ReservationStatus.CONFIRMED:
                    reservation.update_status(ReservationStatus.CHECKED_IN)
                    self.save_data()
                    return True
        return False

    def check_out_guest(self, reservation_id: str) -> bool:
        """Check out a guest and make room available."""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                if reservation.status == ReservationStatus.CHECKED_IN:
                    reservation.update_status(ReservationStatus.CHECKED_OUT)
                    reservation.room.is_available = True
                    self.save_data()
                    return True
        return False

    def get_daily_occupancy(self, date: datetime.date) -> float:
        """Calculate daily occupancy percentage."""
        total_rooms = len(self.rooms)
        if total_rooms == 0:
            return 0.0
            
        occupied = 0
        for reservation
