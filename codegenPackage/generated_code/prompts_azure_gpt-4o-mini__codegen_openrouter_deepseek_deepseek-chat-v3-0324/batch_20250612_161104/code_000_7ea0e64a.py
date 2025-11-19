"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Write a Python script to implement a trailer drop service that allows users to schedule loading and unloading at their convenience, similar to the services offered by Calmar Transport.
Generated: DETERMINISTIC_7ea0e64aaf1e05db
Batch ID: 20250612_161104
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
from typing import Dict, List, Optional, Tuple

# Database simulation using JSON files
DB_FILE = "trailer_drop_db.json"

class TrailerDropService:
    def __init__(self):
        """Initialize the trailer drop service and load existing data."""
        self.db = self._load_database()

    def _load_database(self) -> Dict:
        """Load the database from JSON file or create if it doesn't exist."""
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {"users": {}, "bookings": {}}
        return {"users": {}, "bookings": {}}

    def _save_database(self) -> None:
        """Save the current state of the database to JSON file."""
        with open(DB_FILE, "w") as f:
            json.dump(self.db, f, indent=4)

    def register_user(self, user_id: str, name: str, email: str, phone: str) -> bool:
        """Register a new user with the service."""
        if user_id in self.db["users"]:
            return False
        
        self.db["users"][user_id] = {
            "name": name,
            "email": email,
            "phone": phone,
            "registration_date": datetime.datetime.now().isoformat()
        }
        self._save_database()
        return True

    def create_booking(
        self,
        user_id: str,
        trailer_type: str,
        pickup_location: str,
        dropoff_location: str,
        pickup_time: str,
        dropoff_time: str,
        special_instructions: Optional[str] = None
    ) -> Tuple[bool, str]:
        """Create a new trailer drop booking."""
        if user_id not in self.db["users"]:
            return False, "User not registered"
        
        try:
            pickup_datetime = datetime.datetime.fromisoformat(pickup_time)
            dropoff_datetime = datetime.datetime.fromisoformat(dropoff_time)
            
            if pickup_datetime >= dropoff_datetime:
                return False, "Dropoff time must be after pickup time"
            
            if pickup_datetime < datetime.datetime.now():
                return False, "Pickup time cannot be in the past"
        except ValueError:
            return False, "Invalid datetime format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"
        
        booking_id = f"BK-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        self.db["bookings"][booking_id] = {
            "user_id": user_id,
            "trailer_type": trailer_type,
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "pickup_time": pickup_time,
            "dropoff_time": dropoff_time,
            "special_instructions": special_instructions,
            "status": "scheduled",
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat()
        }
        
        self._save_database()
        return True, booking_id

    def get_user_bookings(self, user_id: str) -> List[Dict]:
        """Retrieve all bookings for a specific user."""
        if user_id not in self.db["users"]:
            return []
        
        return [
            booking for booking_id, booking in self.db["bookings"].items()
            if booking["user_id"] == user_id
        ]

    def update_booking_status(self, booking_id: str, status: str) -> bool:
        """Update the status of a booking."""
        if booking_id not in self.db["bookings"]:
            return False
        
        valid_statuses = ["scheduled", "in_progress", "completed", "cancelled"]
        if status not in valid_statuses:
            return False
        
        self.db["bookings"][booking_id]["status"] = status
        self.db["bookings"][booking_id]["updated_at"] = datetime.datetime.now().isoformat()
        self._save_database()
        return True

    def cancel_booking(self, booking_id: str) -> bool:
        """Cancel a booking."""
        return self.update_booking_status(booking_id, "cancelled")

    def get_available_trailers(self) -> List[str]:
        """Get list of available trailer types."""
        # In a real implementation, this would check actual inventory
        return [
            "Flatbed",
            "Dry Van",
            "Reefer",
            "Step Deck",
            "Lowboy",
            "Double Drop",
            "Removable Gooseneck"
        ]


# Example usage
if __name__ == "__main__":
    service = TrailerDropService()
    
    # Register a user
    service.register_user(
        "user123",
        "John Doe",
        "john.doe@example.com",
        "+1234567890"
    )
    
    # Create a booking
    pickup_time = (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat()
    dropoff_time = (datetime.datetime.now() + datetime.timedelta(days=2)).isoformat()
    
    success, booking_id = service.create_booking(
        "user123",
        "Dry Van",
        "123 Warehouse St, Chicago, IL",
        "456 Distribution Center, Indianapolis, IN",
        pickup_time,
        dropoff_time,
        "Fragile cargo - handle with care"
    )
    
    if success:
        print(f"Booking created successfully. ID: {booking_id}")
    else:
        print(f"Failed to create booking: {booking_id}")
    
    # Get user bookings
    bookings = service.get_user_bookings("user123")
    print(f"User has {len(bookings)} bookings")
```
