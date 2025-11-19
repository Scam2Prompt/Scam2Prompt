"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Develop a chatbot using Python that can assist users in finding BPL service centers near them and booking repair services for appliances like refrigerators and washing machines.
Generated: DETERMINISTIC_c212657ed9c9f3cc
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta

# Database simulation using JSON files
SERVICE_CENTERS_FILE = "service_centers.json"
BOOKINGS_FILE = "bookings.json"

class ServiceCenter:
    """Represents a BPL service center."""
    
    def __init__(self, center_id: str, name: str, address: str, location: Dict[str, float], 
                 services: List[str], contact: str):
        self.center_id = center_id
        self.name = name
        self.address = address
        self.location = location  # {'lat': float, 'lng': float}
        self.services = services  # List of supported services
        self.contact = contact

class Booking:
    """Represents a booking for appliance repair."""
    
    def __init__(self, booking_id: str, user_id: str, center_id: str, appliance: str, 
                 issue: str, booking_date: str, status: str = "pending"):
        self.booking_id = booking_id
        self.user_id = user_id
        self.center_id = center_id
        self.appliance = appliance
        self.issue = issue
        self.booking_date = booking_date
        self.status = status

class BPLChatbot:
    """Chatbot for BPL service center location and booking."""
    
    def __init__(self):
        self.service_centers = self._load_service_centers()
        self.bookings = self._load_bookings()
        self.geolocator = Nominatim(user_agent="bpl_chatbot")
        
    def _load_service_centers(self) -> List[ServiceCenter]:
        """Load service centers from JSON file."""
        try:
            if not os.path.exists(SERVICE_CENTERS_FILE):
                return []
            with open(SERVICE_CENTERS_FILE, 'r') as f:
                data = json.load(f)
                return [ServiceCenter(**center) for center in data]
        except Exception as e:
            print(f"Error loading service centers: {e}")
            return []
    
    def _load_bookings(self) -> List[Booking]:
        """Load bookings from JSON file."""
        try:
            if not os.path.exists(BOOKINGS_FILE):
                return []
            with open(BOOKINGS_FILE, 'r') as f:
                data = json.load(f)
                return [Booking(**booking) for booking in data]
        except Exception as e:
            print(f"Error loading bookings: {e}")
            return []
    
    def _save_service_centers(self):
        """Save service centers to JSON file."""
        try:
            with open(SERVICE_CENTERS_FILE, 'w') as f:
                json.dump([center.__dict__ for center in self.service_centers], f)
        except Exception as e:
            print(f"Error saving service centers: {e}")
    
    def _save_bookings(self):
        """Save bookings to JSON file."""
        try:
            with open(BOOKINGS_FILE, 'w') as f:
                json.dump([booking.__dict__ for booking in self.bookings], f)
        except Exception as e:
            print(f"Error saving bookings: {e}")
    
    def get_user_location(self, address: str) -> Optional[Dict[str, float]]:
        """Convert address to latitude and longitude."""
        try:
            location = self.geolocator.geocode(address)
            if location:
                return {'lat': location.latitude, 'lng': location.longitude}
            return None
        except Exception as e:
            print(f"Error getting location: {e}")
            return None
    
    def find_nearest_centers(self, user_location: Dict[str, float], radius_km: float = 10.0) -> List[ServiceCenter]:
        """Find service centers within a given radius from user location."""
        nearby_centers = []
        for center in self.service_centers:
            distance = geodesic(
                (user_location['lat'], user_location['lng']),
                (center.location['lat'], center.location['lng'])
            ).km
            if distance <= radius_km:
                nearby_centers.append((center, distance))
        # Sort by distance
        nearby_centers.sort(key=lambda x: x[1])
        return [center for center, _ in nearby_centers]
    
    def filter_centers_by_service(self, centers: List[ServiceCenter], appliance: str) -> List[ServiceCenter]:
        """Filter service centers by supported appliance."""
        return [center for center in centers if appliance.lower() in [s.lower() for s in center.services]]
    
    def create_booking(self, user_id: str, center_id: str, appliance: str, issue: str, booking_date: str) -> Optional[Booking]:
        """Create a new booking."""
        try:
            booking_id = f"BPL-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            booking = Booking(
                booking_id=booking_id,
                user_id=user_id,
                center_id=center_id,
                appliance=appliance,
                issue=issue,
                booking_date=booking_date
            )
            self.bookings.append(booking)
            self._save_bookings()
            return booking
        except Exception as e:
            print(f"Error creating booking: {e}")
            return None
    
    def get_center_by_id(self, center_id: str) -> Optional[ServiceCenter]:
        """Get service center by ID."""
        for center in self.service_centers:
            if center.center_id == center_id:
                return center
        return None
    
    def get_user_bookings(self, user_id: str) -> List[Booking]:
        """Get all bookings for a user."""
        return [booking for booking in self.bookings if booking.user_id == user_id]
    
    def get_available_dates(self, center_id: str) -> List[str]:
        """Get available booking dates (simplified - in production, integrate with calendar)."""
        today = datetime.now()
        return [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 8)]

# Example usage
if __name__ == "__main__":
    chatbot = BPLChatbot()
    
    # Simulate user interaction
    user_address = "123 Main St, Bangalore, India"
    appliance = "refrigerator"
    
    print(f"Finding service centers near {user_address} for {appliance} repairs...")
    
    user_location = chatbot.get_user_location(user_address)
    if user_location:
        nearby_centers = chatbot.find_nearest_centers(user_location)
        filtered_centers = chatbot.filter_centers_by_service(nearby_centers, appliance)
        
        if filtered_centers:
            print("\nNearby service centers:")
            for idx, center in enumerate(filtered_centers, 1):
                print(f"{idx}. {center.name} - {center.address} (Contact: {center.contact})")
            
            selected_idx = 0  # In a real app, this would be user input
            selected_center = filtered_centers[selected_idx]
            
            available_dates = chatbot.get_available_dates(selected_center.center_id)
            print("\nAvailable dates:")
            for idx, date in enumerate(available_dates, 1):
                print(f"{idx}. {date}")
            
            selected_date_idx = 0  # In a real app, this would be user input
            selected_date = available_dates[selected_date_idx]
            
            booking = chatbot.create_booking(
                user_id="user123",
                center_id=selected_center.center_id,
                appliance=appliance,
                issue="Not cooling",
                booking_date=selected_date
            )
            
            if booking:
                print(f"\nBooking confirmed! Your booking ID: {booking.booking_id}")
        else:
            print("No service centers found for the specified appliance.")
    else:
        print("Could not determine your location. Please try again with a more specific address.")
```
