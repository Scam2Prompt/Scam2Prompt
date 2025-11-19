"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate a Python script that automates the booking process for a residential cleaning service, similar to the offerings of Maria HouseKeepers in San Fernando Valley, CA.
Generated: DETERMINISTIC_abdbca8534d4c4aa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, Optional, Tuple

# Constants
CONFIG_FILE = "config.json"
BOOKINGS_FILE = "bookings.json"
SERVICES = {
    "standard": {"name": "Standard Cleaning", "price": 120, "duration": 2},
    "deep": {"name": "Deep Cleaning", "price": 200, "duration": 4},
    "move_in_out": {"name": "Move-In/Move-Out Cleaning", "price": 250, "duration": 5}
}
TIME_SLOTS = ["09:00", "11:00", "13:00", "15:00"]

class BookingSystem:
    def __init__(self):
        self.config = self._load_config()
        self.bookings = self._load_bookings()

    def _load_config(self) -> Dict:
        """Load configuration from file or create default."""
        default_config = {
            "company_name": "Maria HouseKeepers",
            "location": "San Fernando Valley, CA",
            "contact_email": "bookings@mariahousekeepers.com",
            "contact_phone": "(818) 555-1234"
        }
        
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            else:
                with open(CONFIG_FILE, 'w') as f:
                    json.dump(default_config, f, indent=4)
                return default_config
        except Exception as e:
            print(f"Error loading config: {e}")
            return default_config

    def _load_bookings(self) -> Dict:
        """Load existing bookings from file or initialize empty."""
        try:
            if os.path.exists(BOOKINGS_FILE):
                with open(BOOKINGS_FILE, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading bookings: {e}")
            return {}

    def _save_bookings(self) -> None:
        """Save current bookings to file."""
        try:
            with open(BOOKINGS_FILE, 'w') as f:
                json.dump(self.bookings, f, indent=4)
        except Exception as e:
            print(f"Error saving bookings: {e}")

    def _validate_date(self, date_str: str) -> Tuple[bool, Optional[datetime.date]]:
        """Validate date format and ensure it's in the future."""
        try:
            booking_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            today = datetime.date.today()
            
            if booking_date < today:
                return False, None
            return True, booking_date
        except ValueError:
            return False, None

    def _validate_time_slot(self, time_slot: str) -> bool:
        """Validate time slot format and availability."""
        return time_slot in TIME_SLOTS

    def _validate_service(self, service_type: str) -> bool:
        """Validate service type exists."""
        return service_type in SERVICES

    def _is_slot_available(self, date: str, time_slot: str) -> bool:
        """Check if time slot is available for given date."""
        if date not in self.bookings:
            return True
        
        for booking in self.bookings[date]:
            if booking["time_slot"] == time_slot:
                return False
        return True

    def get_available_dates(self) -> Dict:
        """Get available dates and time slots."""
        available_dates = {}
        today = datetime.date.today()
        
        for i in range(1, 31):  # Next 30 days
            date = today + datetime.timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            
            available_slots = []
            for slot in TIME_SLOTS:
                if self._is_slot_available(date_str, slot):
                    available_slots.append(slot)
            
            if available_slots:
                available_dates[date_str] = available_slots
                
        return available_dates

    def create_booking(
        self,
        customer_name: str,
        customer_email: str,
        customer_phone: str,
        service_type: str,
        date: str,
        time_slot: str,
        address: str,
        special_requests: str = ""
    ) -> Dict:
        """Create a new booking."""
        # Validate inputs
        is_valid_date, booking_date = self._validate_date(date)
        if not is_valid_date:
            return {"success": False, "message": "Invalid date or date in the past"}
        
        if not self._validate_time_slot(time_slot):
            return {"success": False, "message": "Invalid time slot"}
        
        if not self._validate_service(service_type):
            return {"success": False, "message": "Invalid service type"}
        
        if not all([customer_name, customer_email, customer_phone, address]):
            return {"success": False, "message": "Missing required customer information"}
        
        # Check availability
        date_str = booking_date.strftime("%Y-%m-%d")
        if not self._is_slot_available(date_str, time_slot):
            return {"success": False, "message": "Time slot not available"}
        
        # Create booking
        booking_id = f"BK-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        service = SERVICES[service_type]
        
        booking = {
            "booking_id": booking_id,
            "customer_name": customer_name,
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "service_type": service_type,
            "service_name": service["name"],
            "price": service["price"],
            "duration": service["duration"],
            "date": date_str,
            "time_slot": time_slot,
            "address": address,
            "special_requests": special_requests,
            "status": "confirmed",
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save booking
        if date_str not in self.bookings:
            self.bookings[date_str] = []
        self.bookings[date_str].append(booking)
        self._save_bookings()
        
        return {
            "success": True,
            "message": "Booking created successfully",
            "booking_id": booking_id,
            "booking_details": booking
        }

    def get_booking(self, booking_id: str) -> Dict:
        """Retrieve booking details by ID."""
        for date in self.bookings:
            for booking in self.bookings[date]:
                if booking["booking_id"] == booking_id:
                    return {
                        "success": True,
                        "booking": booking
                    }
        return {"success": False, "message": "Booking not found"}

    def cancel_booking(self, booking_id: str) -> Dict:
        """Cancel an existing booking."""
        for date in self.bookings:
            for i, booking in enumerate(self.bookings[date]):
                if booking["booking_id"] == booking_id:
                    if booking["status"] == "cancelled":
                        return {"success": False, "message": "Booking already cancelled"}
                    
                    self.bookings[date][i]["status"] = "cancelled"
                    self._save_bookings()
                    return {
                        "success": True,
                        "message": "Booking cancelled successfully"
                    }
        return {"success": False, "message": "Booking not found"}

def main():
    """Command-line interface for the booking system."""
    booking_system = BookingSystem()
    print(f"Welcome to {booking_system.config['company_name']}")
    print(f"Location: {booking_system.config['location']}")
    print("Available services:")
    for service_code, service in SERVICES.items():
        print(f"  {service_code}: {service['name']} (${service['price']}, {service['duration']} hours)")
    
    while True:
        print("\nMenu:")
        print("1. Check available dates")
        print("2. Make a booking")
        print("3. View booking details")
        print("4. Cancel booking")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            available_dates = booking_system.get_available_dates()
            print("\nAvailable Dates and Time Slots:")
            for date, slots in available_dates.items():
                print(f"{date}: {', '.join(slots)}")
        
        elif choice == "2":
            print("\nNew Booking:")
            customer_name = input("Full Name: ")
            customer_email = input("Email: ")
            customer_phone = input("Phone: ")
            address = input("Address: ")
            print("Available service types:")
            for service_code in SERVICES:
                print(f"- {service_code}")
            service_type = input("Service Type: ")
            special_requests = input("Special Requests (optional): ")
            
            available_dates = booking_system.get_available_dates()
            print("\nAvailable Dates:")
            for date in available_dates:
                print(f"- {date}")
            date = input
