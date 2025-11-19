"""
Generated Code Metadata:
========================
Original URL: https://samaalnaser.co
Prompt: Create a Python script that automates the workflow for a hospitality management system, inspired by the services offered by Sama Al-Naser Group.
Generated: DETERMINISTIC_f86a170a75de9090
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hospitality Management System Automation Script
Inspired by Sama Al-Naser Group services

This script automates various workflows for a hospitality management system,
including room booking, guest management, and service requests.
"""

import json
import datetime
import logging
from typing import Dict, List, Optional, Tuple
import uuid
import os
from enum import Enum, auto


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hospitality_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class RoomType(Enum):
    """Enumeration of room types available in the hotel."""
    STANDARD = auto()
    DELUXE = auto()
    SUITE = auto()
    PRESIDENTIAL = auto()


class BookingStatus(Enum):
    """Enumeration of booking statuses."""
    CONFIRMED = auto()
    CHECKED_IN = auto()
    CHECKED_OUT = auto()
    CANCELLED = auto()


class Guest:
    """Class representing a guest in the hospitality system."""
    
    def __init__(self, guest_id: str, name: str, email: str, phone: str):
        """
        Initialize a Guest object.
        
        Args:
            guest_id: Unique identifier for the guest
            name: Full name of the guest
            email: Email address of the guest
            phone: Phone number of the guest
        """
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone
        self.preferences: Dict[str, str] = {}
    
    def add_preference(self, key: str, value: str) -> None:
        """Add a preference for the guest."""
        self.preferences[key] = value
    
    def to_dict(self) -> Dict:
        """Convert Guest object to dictionary for serialization."""
        return {
            'guest_id': self.guest_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'preferences': self.preferences
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Guest':
        """Create Guest object from dictionary."""
        guest = cls(
            data['guest_id'],
            data['name'],
            data['email'],
            data['phone']
        )
        guest.preferences = data.get('preferences', {})
        return guest


class Room:
    """Class representing a hotel room."""
    
    def __init__(self, room_number: str, room_type: RoomType, rate: float):
        """
        Initialize a Room object.
        
        Args:
            room_number: Unique room number/identifier
            room_type: Type of the room (from RoomType enum)
            rate: Daily rate for the room
        """
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.amenities: List[str] = []
        self.is_available = True
    
    def add_amenity(self, amenity: str) -> None:
        """Add an amenity to the room."""
        self.amenities.append(amenity)
    
    def to_dict(self) -> Dict:
        """Convert Room object to dictionary for serialization."""
        return {
            'room_number': self.room_number,
            'room_type': self.room_type.name,
            'rate': self.rate,
            'amenities': self.amenities,
            'is_available': self.is_available
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Room':
        """Create Room object from dictionary."""
        room = cls(
            data['room_number'],
            RoomType[data['room_type']],
            data['rate']
        )
        room.amenities = data.get('amenities', [])
        room.is_available = data.get('is_available', True)
        return room


class Booking:
    """Class representing a room booking."""
    
    def __init__(
        self,
        booking_id: str,
        guest_id: str,
        room_number: str,
        check_in: datetime.date,
        check_out: datetime.date,
        status: BookingStatus = BookingStatus.CONFIRMED
    ):
        """
        Initialize a Booking object.
        
        Args:
            booking_id: Unique booking identifier
            guest_id: ID of the guest making the booking
            room_number: Room number being booked
            check_in: Check-in date
            check_out: Check-out date
            status: Current status of the booking
        """
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out
        self.status = status
        self.special_requests: List[str] = []
        self.total_cost: Optional[float] = None
    
    def calculate_cost(self, room_rate: float) -> float:
        """Calculate total cost of the booking."""
        days = (self.check_out - self.check_in).days
        self.total_cost = room_rate * days
        return self.total_cost
    
    def add_special_request(self, request: str) -> None:
        """Add a special request to the booking."""
        self.special_requests.append(request)
    
    def update_status(self, new_status: BookingStatus) -> None:
        """Update the booking status."""
        self.status = new_status
    
    def to_dict(self) -> Dict:
        """Convert Booking object to dictionary for serialization."""
        return {
            'booking_id': self.booking_id,
            'guest_id': self.guest_id,
            'room_number': self.room_number,
            'check_in': self.check_in.isoformat(),
            'check_out': self.check_out.isoformat(),
            'status': self.status.name,
            'special_requests': self.special_requests,
            'total_cost': self.total_cost
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Booking':
        """Create Booking object from dictionary."""
        booking = cls(
            data['booking_id'],
            data['guest_id'],
            data['room_number'],
            datetime.date.fromisoformat(data['check_in']),
            datetime.date.fromisoformat(data['check_out']),
            BookingStatus[data['status']]
        )
        booking.special_requests = data.get('special_requests', [])
        booking.total_cost = data.get('total_cost')
        return booking


class ServiceRequest:
    """Class representing a service request from a guest."""
    
    def __init__(
        self,
        request_id: str,
        guest_id: str,
        room_number: str,
        service_type: str,
        description: str,
        timestamp: datetime.datetime = datetime.datetime.now()
    ):
        """
        Initialize a ServiceRequest object.
        
        Args:
            request_id: Unique request identifier
            guest_id: ID of the guest making the request
            room_number: Room number where service is requested
            service_type: Type of service requested
            description: Detailed description of the request
            timestamp: When the request was made
        """
        self.request_id = request_id
        self.guest_id = guest_id
        self.room_number = room_number
        self.service_type = service_type
        self.description = description
        self.timestamp = timestamp
        self.is_fulfilled = False
        self.notes: str = ""
    
    def fulfill_request(self, notes: str = "") -> None:
        """Mark the request as fulfilled."""
        self.is_fulfilled = True
        self.notes = notes
    
    def to_dict(self) -> Dict:
        """Convert ServiceRequest object to dictionary for serialization."""
        return {
            'request_id': self.request_id,
            'guest_id': self.guest_id,
            'room_number': self.room_number,
            'service_type': self.service_type,
            'description': self.description,
            'timestamp': self.timestamp.isoformat(),
            'is_fulfilled': self.is_fulfilled,
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ServiceRequest':
        """Create ServiceRequest object from dictionary."""
        request = cls(
            data['request_id'],
            data['guest_id'],
            data['room_number'],
            data['service_type'],
            data['description'],
            datetime.datetime.fromisoformat(data['timestamp'])
        )
        request.is_fulfilled = data.get('is_fulfilled', False)
        request.notes = data.get('notes', "")
        return request


class HospitalitySystem:
    """Main class for the hospitality management system."""
    
    DATA_FILES = {
        'guests': 'guests.json',
        'rooms': 'rooms.json',
        'bookings': 'bookings.json',
        'service_requests': 'service_requests.json'
    }
    
    def __init__(self):
        """Initialize the hospitality system."""
        self.guests: Dict[str, Guest] = {}
        self.rooms: Dict[str, Room] = {}
        self.bookings: Dict
