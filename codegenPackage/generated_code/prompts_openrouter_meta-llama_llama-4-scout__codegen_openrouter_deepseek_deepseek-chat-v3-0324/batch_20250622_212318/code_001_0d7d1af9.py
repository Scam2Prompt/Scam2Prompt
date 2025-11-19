"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Write a Python script to create a simple booking system for a villa rental service like Villa Andreas in Kefalonia, considering check-in and check-out times, and minimum stay requirements."
Generated: DETERMINISTIC_0d7d1af9ba7fda4e
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional, Tuple

class VillaBookingSystem:
    """
    A simple booking system for villa rentals with check-in/out times and minimum stay requirements.
    """
    
    def __init__(self, villa_name: str, min_stay_days: int = 3):
        """
        Initialize the booking system.
        
        Args:
            villa_name: Name of the villa
            min_stay_days: Minimum number of days required for a booking (default: 3)
        """
        self.villa_name = villa_name
        self.min_stay_days = min_stay_days
        self.bookings: Dict[int, Dict[str, datetime.date]] = {}
        self.next_booking_id = 1
        
    def is_date_range_valid(self, check_in: datetime.date, check_out: datetime.date) -> Tuple[bool, Optional[str]]:
        """
        Validate a date range for booking.
        
        Args:
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if check_in >= check_out:
            return False, "Check-out date must be after check-in date"
            
        stay_days = (check_out - check_in).days
        if stay_days < self.min_stay_days:
            return False, f"Minimum stay requirement is {self.min_stay_days} days"
            
        if check_in < datetime.date.today():
            return False, "Cannot book dates in the past"
            
        return True, None
        
    def is_available(self, check_in: datetime.date, check_out: datetime.date) -> Tuple[bool, Optional[str]]:
        """
        Check if the villa is available for the given date range.
        
        Args:
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            Tuple of (is_available, error_message)
        """
        is_valid, error_msg = self.is_date_range_valid(check_in, check_out)
        if not is_valid:
            return False, error_msg
            
        for booking in self.bookings.values():
            existing_check_in = booking['check_in']
            existing_check_out = booking['check_out']
            
            if (check_in < existing_check_out) and (check_out > existing_check_in):
                return False, "Villa is already booked for the selected dates"
                
        return True, None
        
    def add_booking(self, guest_name: str, check_in: datetime.date, check_out: datetime.date) -> Tuple[Optional[int], Optional[str]]:
        """
        Add a new booking if dates are available.
        
        Args:
            guest_name: Name of the guest
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            Tuple of (booking_id, error_message)
        """
        is_available, error_msg = self.is_available(check_in, check_out)
        if not is_available:
            return None, error_msg
            
        booking_id = self.next_booking_id
        self.bookings[booking_id] = {
            'guest_name': guest_name,
            'check_in': check_in,
            'check_out': check_out
        }
        self.next_booking_id += 1
        return booking_id, None
        
    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancel an existing booking.
        
        Args:
            booking_id: ID of the booking to cancel
            
        Returns:
            True if cancellation was successful, False otherwise
        """
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False
        
    def get_bookings(self) -> List[Dict]:
        """
        Get all current bookings.
        
        Returns:
            List of booking dictionaries
        """
        return [{'id': k, **v} for k, v in self.bookings.items()]
        
    def get_booking(self, booking_id: int) -> Optional[Dict]:
        """
        Get a specific booking by ID.
        
        Args:
            booking_id: ID of the booking to retrieve
            
        Returns:
            Booking dictionary if found, None otherwise
        """
        return self.bookings.get(booking_id, None)
        
    def get_available_dates(self, start_date: datetime.date, end_date: datetime.date) -> List[Tuple[datetime.date, datetime.date]]:
        """
        Get all available date ranges between start_date and end_date.
        
        Args:
            start_date: Start of date range to check
            end_date: End of date range to check
            
        Returns:
            List of available (check_in, check_out) date ranges
        """
        if start_date >= end_date:
            return []
            
        # Sort bookings by check-in date
        sorted_bookings = sorted(
            self.bookings.values(),
            key=lambda x: x['check_in']
        )
        
        available_dates = []
        current_date = start_date
        
        for booking in sorted_bookings:
            if booking['check_in'] > end_date:
                break
                
            if current_date < booking['check_in']:
                available_dates.append((current_date, booking['check_in']))
                
            if booking['check_out'] > current_date:
                current_date = booking['check_out']
                
        if current_date < end_date:
            available_dates.append((current_date, end_date))
            
        # Filter out ranges that don't meet minimum stay
        available_dates = [
            (ci, co) for ci, co in available_dates 
            if (co - ci).days >= self.min_stay_days
        ]
        
        return available_dates


def main():
    """Example usage of the VillaBookingSystem."""
    villa = VillaBookingSystem("Villa Andreas", min_stay_days=3)
    
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    next_week = today + datetime.timedelta(days=7)
    two_weeks = today + datetime.timedelta(days=14)
    
    # Test booking
    booking_id, error = villa.add_booking("John Doe", next_week, two_weeks)
    if error:
        print(f"Booking failed: {error}")
    else:
        print(f"Booking successful! ID: {booking_id}")
    
    # Check availability
    available_dates = villa.get_available_dates(tomorrow, two_weeks + datetime.timedelta(days=30))
    print("\nAvailable date ranges:")
    for ci, co in available_dates:
        print(f"{ci} to {co} ({(co - ci).days} days)")
    
    # List all bookings
    print("\nCurrent bookings:")
    for booking in villa.get_bookings():
        print(f"ID: {booking['id']}, Guest: {booking['guest_name']}, Dates: {booking['check_in']} to {booking['check_out']}")


if __name__ == "__main__":
    main()
```
