"""
Generated Code Metadata:
========================
Original URL: https://deafah.in
Prompt: Develop a sample application that showcases the tailored services provided by Deafah for group travel arrangements during Umrah.
Generated: DETERMINISTIC_fe05e01e057b1f12
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Deafah Umrah Group Travel Management System

This application showcases the tailored services provided by Deafah for group travel arrangements during Umrah.
It includes features for managing travelers, group itineraries, bookings, and payment tracking.
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import json
import uuid

class Traveler:
    """Represents a traveler in the Umrah group."""
    
    def __init__(self, name: str, passport_number: str, contact_number: str, special_requirements: str = ""):
        self.id = str(uuid.uuid4())
        self.name = name
        self.passport_number = passport_number
        self.contact_number = contact_number
        self.special_requirements = special_requirements
        self.booking_status = BookingStatus.PENDING
    
    def update_details(self, name: Optional[str] = None, contact_number: Optional[str] = None, 
                       special_requirements: Optional[str] = None) -> None:
        """Update traveler details."""
        if name:
            self.name = name
        if contact_number:
            self.contact_number = contact_number
        if special_requirements:
            self.special_requirements = special_requirements
    
    def to_dict(self) -> Dict:
        """Convert traveler object to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'passport_number': self.passport_number,
            'contact_number': self.contact_number,
            'special_requirements': self.special_requirements,
            'booking_status': self.booking_status.value
        }

class BookingStatus(Enum):
    """Enum for booking status."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

class Accommodation:
    """Represents accommodation details for the group."""
    
    def __init__(self, hotel_name: str, room_type: str, check_in: datetime, check_out: datetime):
        self.hotel_name = hotel_name
        self.room_type = room_type
        self.check_in = check_in
        self.check_out = check_out
    
    def to_dict(self) -> Dict:
        """Convert accommodation object to dictionary for serialization."""
        return {
            'hotel_name': self.hotel_name,
            'room_type': self.room_type,
            'check_in': self.check_in.isodate(),
            'check_out': self.check_out.isodate()
        }

class UmrahPackage:
    """Represents an Umrah package offered by Deafah."""
    
    def __init__(self, name: str, description: str, duration_days: int, price: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.duration_days = duration_days
        self.price = price
        self.accommodations = []
        self.itinerary = []
    
    def add_accommodation(self, accommodation: Accommodation) -> None:
        """Add accommodation to the package."""
        self.accommodations.append(accommodation)
    
    def add_itinerary_item(self, date: datetime, activity: str, description: str) -> None:
        """Add an item to the itinerary."""
        self.itinerary.append({
            'date': date,
            'activity': activity,
            'description': description
        })
    
    def to_dict(self) -> Dict:
        """Convert package object to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration_days': self.duration_days,
            'price': self.price,
            'accommodations': [acc.to_dict() for acc in self.accommodations],
            'itinerary': [{
                'date': item['date'].isoformat(),
                'activity': item['activity'],
                'description': item['description']
            } for item in self.itinerary]
        }

class Payment:
    """Represents a payment made by a traveler."""
    
    def __init__(self, traveler_id: str, amount: float, payment_date: datetime, method: str):
        self.id = str(uuid.uuid4())
        self.traveler_id = traveler_id
        self.amount = amount
        self.payment_date = payment_date
        self.method = method
    
    def to_dict(self) -> Dict:
        """Convert payment object to dictionary for serialization."""
        return {
            'id': self.id,
            'traveler_id': self.traveler_id,
            'amount': self.amount,
            'payment_date': self.payment_date.isodate(),
            'method': self.method
        }

class UmrahGroup:
    """Represents an Umrah group managed by Deafah."""
    
    def __init__(self, name: str, start_date: datetime, end_date: datetime, package: UmrahPackage):
        self.id = str(uuid.uuid4())
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.package = package
        self.travelers = []
        self.payments = []
        self.group_leader = None
        self.is_active = True
    
    def add_traveler(self, traveler: Traveler) -> None:
        """Add a traveler to the group."""
        self.travelers.append(traveler)
    
    def remove_traveler(self, traveler_id: str) -> bool:
        """Remove a traveler from the group."""
        for i, traveler in enumerate(self.travelers):
            if traveler.id == traveler_id:
                self.travelers.pop(i)
                return True
        return False
    
    def add_payment(self, payment: Payment) -> None:
        """Record a payment made by a traveler."""
        self.payments.append(payment)
    
    def set_group_leader(self, traveler_id: str) -> bool:
        """Set the group leader."""
        for traveler in self.travelers:
            if traveler.id == traveler_id:
                self.group_leader = traveler
                return True
        return False
    
    def to_dict(self) -> Dict:
        """Convert group object to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isodate(),
            'end_date': self.end_date.isodate(),
            'package': self.package.to_dict(),
            'travelers': [traveler.to_dict() for traveler in self.travelers],
            'payments': [payment.to_dict() for payment in self.payments],
            'group_leader': self.group_leader.id if self.group_leader else None,
            'is_active': self.is_active
        }

class DeafahUmrahSystem:
    """Main system class for managing Deafah's Umrah group travel services."""
    
    def __init__(self):
        self.groups = []
        self.packages = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load initial data (would be from database in production)."""
        # Sample package
        package = UmrahPackage(
            name="Deluxe Umrah Package",
            description="14-day Umrah package with 5-star accommodations",
            duration_days=14,
            price=5000.00
        )
        package.add_accommodation(Accommodation(
            hotel_name="Makkah Hilton",
            room_type="Deluxe Room",
            check_in=datetime(2023, 12, 1),
            check_out=datetime(2023, 12, 7)
        ))
        package.add_itinerary_item(
            date=datetime(2023, 12, 2),
            activity="Ziyarat in Makkah",
            description="Visit historical Islamic sites in Makkah"
        )
        self.packages.append(package)
    
    def create_group(self, name: str, start_date: datetime, end_date: datetime, package_id: str) -> Optional[UmrahGroup]:
        """Create a new Umrah group."""
        package = next((p for p in self.packages if p.id == package_id), None)
        if not package:
            return None
        
        group = UmrahGroup(name, start_date, end_date, package)
        self.groups.append(group)
        return group
    
    def get_group(self, group_id: str) -> Optional[UmrahGroup]:
        """Get a group by ID."""
        return next((g for g in self.groups if g.id == group_id), None)
    
    def save_data(self, filename: str = 'deafah_umrah_data.json') -> bool:
        """Save system data to a JSON file."""
        try:
            data = {
                'groups': [group.to_dict() for group in self.groups],
                'packages': [package.to_dict() for package in self.packages]
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_data(self, filename: str = 'deafah_umrah_data.json') -> bool:
        """Load system data from a JSON file."""
