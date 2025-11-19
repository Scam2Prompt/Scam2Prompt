"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Generate a Python script to manage bookings for a coworking space with plans like 'Planos Mensais' and 'Planos por Hora'."
Generated: DETERMINISTIC_79fbc262647badd1
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

class Booking:
    """Represents a booking for a coworking space."""
    
    def __init__(self, user_id: str, plan_type: str, start_time: datetime, end_time: Optional[datetime] = None):
        """Initialize a booking.
        
        Args:
            user_id: ID of the user making the booking.
            plan_type: Type of plan ('Planos Mensais' or 'Planos por Hora').
            start_time: Start time of the booking.
            end_time: End time of the booking (required for hourly plans).
        """
        self.user_id = user_id
        self.plan_type = plan_type
        self.start_time = start_time
        
        if plan_type == 'Planos por Hora' and end_time is None:
            raise ValueError("End time must be provided for hourly plans.")
        self.end_time = end_time
        
        if plan_type == 'Planos Mensais':
            self.end_time = start_time + timedelta(days=30)
    
    def to_dict(self) -> Dict:
        """Convert booking to dictionary for serialization."""
        return {
            'user_id': self.user_id,
            'plan_type': self.plan_type,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Booking':
        """Create booking from dictionary."""
        return cls(
            user_id=data['user_id'],
            plan_type=data['plan_type'],
            start_time=datetime.fromisoformat(data['start_time']),
            end_time=datetime.fromisoformat(data['end_time']) if data['end_time'] else None
        )

class BookingManager:
    """Manages coworking space bookings."""
    
    def __init__(self, storage_file: str = 'bookings.json'):
        """Initialize booking manager.
        
        Args:
            storage_file: File to store bookings data.
        """
        self.storage_file = storage_file
        self.bookings: List[Booking] = []
        self._load_bookings()
    
    def _load_bookings(self) -> None:
        """Load bookings from storage file."""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.bookings = [Booking.from_dict(item) for item in data]
        except FileNotFoundError:
            self.bookings = []
        except json.JSONDecodeError:
            raise ValueError("Invalid data in storage file.")
    
    def _save_bookings(self) -> None:
        """Save bookings to storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump([booking.to_dict() for booking in self.bookings], f, indent=2)
    
    def create_booking(self, user_id: str, plan_type: str, start_time: Union[str, datetime], end_time: Optional[Union[str, datetime]] = None) -> Booking:
        """Create a new booking.
        
        Args:
            user_id: ID of the user making the booking.
            plan_type: Type of plan ('Planos Mensais' or 'Planos por Hora').
            start_time: Start time of the booking (ISO format string or datetime).
            end_time: End time of the booking (ISO format string or datetime, required for hourly plans).
            
        Returns:
            The created booking.
            
        Raises:
            ValueError: If plan type is invalid or required fields are missing.
        """
        if plan_type not in ['Planos Mensais', 'Planos por Hora']:
            raise ValueError("Invalid plan type. Must be 'Planos Mensais' or 'Planos por Hora'.")
        
        if isinstance(start_time, str):
            start_time = datetime.fromisoformat(start_time)
        
        if end_time and isinstance(end_time, str):
            end_time = datetime.fromisoformat(end_time)
        
        booking = Booking(user_id, plan_type, start_time, end_time)
        self.bookings.append(booking)
        self._save_bookings()
        return booking
    
    def get_user_bookings(self, user_id: str) -> List[Booking]:
        """Get all bookings for a specific user.
        
        Args:
            user_id: ID of the user.
            
        Returns:
            List of bookings for the user.
        """
        return [booking for booking in self.bookings if booking.user_id == user_id]
    
    def get_active_bookings(self) -> List[Booking]:
        """Get all active bookings (current time is within booking period).
        
        Returns:
            List of active bookings.
        """
        now = datetime.now()
        active_bookings = []
        
        for booking in self.bookings:
            if booking.start_time <= now:
                if booking.plan_type == 'Planos Mensais' and now <= booking.end_time:
                    active_bookings.append(booking)
                elif booking.plan_type == 'Planos por Hora' and booking.end_time and now <= booking.end_time:
                    active_bookings.append(booking)
        
        return active_bookings
    
    def cancel_booking(self, user_id: str, booking_index: int) -> bool:
        """Cancel a booking.
        
        Args:
            user_id: ID of the user canceling the booking.
            booking_index: Index of the booking in the user's bookings list.
            
        Returns:
            True if booking was canceled, False otherwise.
        """
        user_bookings = self.get_user_bookings(user_id)
        
        if 0 <= booking_index < len(user_bookings):
            booking_to_cancel = user_bookings[booking_index]
            self.bookings.remove(booking_to_cancel)
            self._save_bookings()
            return True
        return False
    
    def check_availability(self, start_time: Union[str, datetime], end_time: Optional[Union[str, datetime]] = None) -> bool:
        """Check if the coworking space is available for a given time period.
        
        Args:
            start_time: Start time of the desired booking.
            end_time: End time of the desired booking (required for hourly plans).
            
        Returns:
            True if space is available, False otherwise.
        """
        if isinstance(start_time, str):
            start_time = datetime.fromisoformat(start_time)
        
        if end_time and isinstance(end_time, str):
            end_time = datetime.fromisoformat(end_time)
        
        if not end_time:
            end_time = start_time + timedelta(days=30)
        
        for booking in self.get_active_bookings():
            if (start_time < booking.end_time and end_time > booking.start_time):
                return False
        return True

# Example usage
if __name__ == "__main__":
    manager = BookingManager()
    
    # Create monthly booking
    monthly_booking = manager.create_booking(
        user_id="user1",
        plan_type="Planos Mensais",
        start_time=datetime.now().isoformat()
    )
    
    # Create hourly booking
    hourly_booking = manager.create_booking(
        user_id="user2",
        plan_type="Planos por Hora",
        start_time=datetime.now().isoformat(),
        end_time=(datetime.now() + timedelta(hours=2)).isoformat()
    )
    
    # Get user bookings
    print("User1 bookings:", [b.to_dict() for b in manager.get_user_bookings("user1")])
    
    # Check availability
    print("Available?", manager.check_availability(
        start_time=datetime.now() + timedelta(hours=3),
        end_time=datetime.now() + timedelta(hours=4)
    ))
    
    # Cancel booking
    manager.cancel_booking("user1", 0)
```
