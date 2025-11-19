"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Write a Python script to book a room at the San Land Eco-Lodge, including a function to check availability and another to make a reservation.
Generated: DETERMINISTIC_d5a341248617752f
Batch ID: 20250622_211850
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

# File to store reservations data
RESERVATIONS_FILE = "reservations.json"

class SanLandEcoLodge:
    """
    A class to handle room bookings at San Land Eco-Lodge.
    Includes methods to check availability and make reservations.
    """
    
    def __init__(self):
        """Initialize the lodge with existing reservations or create empty storage."""
        self.reservations = self._load_reservations()
    
    def _load_reservations(self) -> Dict[str, List[Dict]]:
        """Load reservations from file or return empty dict if file doesn't exist."""
        try:
            if os.path.exists(RESERVATIONS_FILE):
                with open(RESERVATIONS_FILE, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading reservations: {e}")
            return {}

    def _save_reservations(self) -> None:
        """Save current reservations to file."""
        try:
            with open(RESERVATIONS_FILE, 'w') as f:
                json.dump(self.reservations, f, indent=2)
        except IOError as e:
            print(f"Error saving reservations: {e}")

    def check_availability(self, room_type: str, check_in: str, check_out: str) -> bool:
        """
        Check if a room of specified type is available for given dates.
        
        Args:
            room_type: Type of room (e.g., 'standard', 'deluxe')
            check_in: Check-in date in YYYY-MM-DD format
            check_out: Check-out date in YYYY-MM-DD format
            
        Returns:
            bool: True if available, False otherwise
        """
        try:
            # Validate dates
            check_in_date = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()
            
            if check_out_date <= check_in_date:
                print("Error: Check-out date must be after check-in date")
                return False
                
            # Check for overlapping reservations
            if room_type not in self.reservations:
                return True
                
            for reservation in self.reservations[room_type]:
                res_check_in = datetime.datetime.strptime(reservation['check_in'], "%Y-%m-%d").date()
                res_check_out = datetime.datetime.strptime(reservation['check_out'], "%Y-%m-%d").date()
                
                if not (check_out_date <= res_check_in or check_in_date >= res_check_out):
                    return False
                    
            return True
            
        except ValueError as e:
            print(f"Invalid date format: {e}. Please use YYYY-MM-DD.")
            return False

    def make_reservation(self, room_type: str, check_in: str, check_out: str, guest_name: str, 
                         guest_email: str) -> Tuple[bool, Optional[str]]:
        """
        Make a reservation if the room is available.
        
        Args:
            room_type: Type of room (e.g., 'standard', 'deluxe')
            check_in: Check-in date in YYYY-MM-DD format
            check_out: Check-out date in YYYY-MM-DD format
            guest_name: Name of the guest
            guest_email: Email of the guest
            
        Returns:
            Tuple: (success: bool, reservation_id: str or error_message: str)
        """
        if not self.check_availability(room_type, check_in, check_out):
            return False, "Room not available for the selected dates"
            
        try:
            reservation_id = f"RES-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
            reservation = {
                'id': reservation_id,
                'room_type': room_type,
                'check_in': check_in,
                'check_out': check_out,
                'guest_name': guest_name,
                'guest_email': guest_email,
                'status': 'confirmed'
            }
            
            if room_type not in self.reservations:
                self.reservations[room_type] = []
                
            self.reservations[room_type].append(reservation)
            self._save_reservations()
            
            return True, reservation_id
            
        except Exception as e:
            return False, f"Error creating reservation: {e}"

# Example usage
if __name__ == "__main__":
    lodge = SanLandEcoLodge()
    
    # Check availability
    available = lodge.check_availability("deluxe", "2023-12-15", "2023-12-20")
    print(f"Room available: {available}")
    
    # Make reservation
    success, result = lodge.make_reservation(
        room_type="deluxe",
        check_in="2023-12-15",
        check_out="2023-12-20",
        guest_name="John Doe",
        guest_email="john@example.com"
    )
    
    if success:
        print(f"Reservation successful! ID: {result}")
    else:
        print(f"Reservation failed: {result}")
```
