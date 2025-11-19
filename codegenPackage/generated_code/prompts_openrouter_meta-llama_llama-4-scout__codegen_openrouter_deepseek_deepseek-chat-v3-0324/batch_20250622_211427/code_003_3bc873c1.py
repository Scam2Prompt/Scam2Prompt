"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Design a system for managing travel bookings, including air charter, hotel reservations, and airport transfers, using a library like Python's `datetime` and `pandas`.
Generated: DETERMINISTIC_3bc873c12f26e7ae
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import pandas as pd
from typing import Optional, Dict, List, Union
from enum import Enum, auto

class BookingType(Enum):
    AIR_CHARTER = auto()
    HOTEL_RESERVATION = auto()
    AIRPORT_TRANSFER = auto()

class BookingStatus(Enum):
    CONFIRMED = auto()
    PENDING = auto()
    CANCELLED = auto()
    COMPLETED = auto()

class TravelBookingSystem:
    """
    A system for managing travel bookings including air charter, hotel reservations, and airport transfers.
    Uses pandas DataFrames for storage and datetime for handling dates.
    """
    
    def __init__(self):
        self.bookings = pd.DataFrame(columns=[
            'booking_id',
            'booking_type',
            'customer_name',
            'start_date',
            'end_date',
            'details',
            'status'
        ])
        self.next_booking_id = 1
    
    def create_booking(
        self,
        booking_type: BookingType,
        customer_name: str,
        start_date: datetime.datetime,
        end_date: Optional[datetime.datetime] = None,
        details: Optional[Dict[str, Union[str, int, float]]] = None
    ) -> int:
        """
        Create a new travel booking.
        
        Args:
            booking_type: Type of booking (AIR_CHARTER, HOTEL_RESERVATION, AIRPORT_TRANSFER)
            customer_name: Name of the customer making the booking
            start_date: Start date/time of the booking
            end_date: End date/time of the booking (optional for some types)
            details: Additional booking details as a dictionary
            
        Returns:
            booking_id: The ID of the newly created booking
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        if not customer_name:
            raise ValueError("Customer name is required")
        if not isinstance(start_date, datetime.datetime):
            raise ValueError("Start date must be a datetime object")
        
        if booking_type == BookingType.HOTEL_RESERVATION and end_date is None:
            raise ValueError("End date is required for hotel reservations")
        if booking_type == BookingType.AIRPORT_TRANSFER and end_date is not None:
            raise ValueError("End date should not be provided for airport transfers")
        
        booking_id = self.next_booking_id
        self.next_booking_id += 1
        
        new_booking = {
            'booking_id': booking_id,
            'booking_type': booking_type.name,
            'customer_name': customer_name,
            'start_date': start_date,
            'end_date': end_date,
            'details': details if details else {},
            'status': BookingStatus.CONFIRMED.name
        }
        
        self.bookings = self.bookings.append(new_booking, ignore_index=True)
        return booking_id
    
    def update_booking_status(self, booking_id: int, new_status: BookingStatus) -> None:
        """
        Update the status of a booking.
        
        Args:
            booking_id: ID of the booking to update
            new_status: New status to set
            
        Raises:
            ValueError: If booking ID doesn't exist
        """
        if booking_id not in self.bookings['booking_id'].values:
            raise ValueError(f"Booking ID {booking_id} not found")
        
        self.bookings.loc[self.bookings['booking_id'] == booking_id, 'status'] = new_status.name
    
    def get_booking(self, booking_id: int) -> Optional[Dict]:
        """
        Retrieve a booking by ID.
        
        Args:
            booking_id: ID of the booking to retrieve
            
        Returns:
            Dictionary containing booking details, or None if not found
        """
        booking = self.bookings[self.bookings['booking_id'] == booking_id]
        if booking.empty:
            return None
        
        return booking.iloc[0].to_dict()
    
    def get_bookings_by_customer(self, customer_name: str) -> List[Dict]:
        """
        Retrieve all bookings for a specific customer.
        
        Args:
            customer_name: Name of the customer
            
        Returns:
            List of dictionaries containing booking details
        """
        customer_bookings = self.bookings[self.bookings['customer_name'] == customer_name]
        return customer_bookings.to_dict('records')
    
    def get_upcoming_bookings(self, days_ahead: int = 30) -> List[Dict]:
        """
        Retrieve bookings scheduled within the next X days.
        
        Args:
            days_ahead: Number of days in the future to look for bookings
            
        Returns:
            List of dictionaries containing upcoming booking details
        """
        now = datetime.datetime.now()
        future_date = now + datetime.timedelta(days=days_ahead)
        
        upcoming = self.bookings[
            (self.bookings['start_date'] >= now) & 
            (self.bookings['start_date'] <= future_date) &
            (self.bookings['status'] == BookingStatus.CONFIRMED.name)
        ]
        return upcoming.to_dict('records')
    
    def cancel_booking(self, booking_id: int) -> None:
        """
        Cancel a booking by changing its status to CANCELLED.
        
        Args:
            booking_id: ID of the booking to cancel
            
        Raises:
            ValueError: If booking ID doesn't exist
        """
        self.update_booking_status(booking_id, BookingStatus.CANCELLED)
    
    def _validate_dates(self, start_date: datetime.datetime, end_date: Optional[datetime.datetime]) -> None:
        """
        Internal method to validate date ranges.
        
        Args:
            start_date: Start date/time
            end_date: End date/time (optional)
            
        Raises:
            ValueError: If dates are invalid
        """
        if end_date and start_date > end_date:
            raise ValueError("Start date cannot be after end date")
        if start_date < datetime.datetime.now():
            raise ValueError("Start date cannot be in the past")

# Example usage
if __name__ == "__main__":
    system = TravelBookingSystem()
    
    # Create some bookings
    try:
        hotel_booking = system.create_booking(
            booking_type=BookingType.HOTEL_RESERVATION,
            customer_name="John Doe",
            start_date=datetime.datetime(2023, 12, 15),
            end_date=datetime.datetime(2023, 12, 20),
            details={"hotel": "Grand Hotel", "room_type": "Deluxe"}
        )
        
        transfer_booking = system.create_booking(
            booking_type=BookingType.AIRPORT_TRANSFER,
            customer_name="Jane Smith",
            start_date=datetime.datetime(2023, 12, 15, 8, 30),
            details={"pickup": "JFK Airport", "dropoff": "Grand Hotel", "vehicle": "Luxury Sedan"}
        )
        
        # Get upcoming bookings
        upcoming = system.get_upcoming_bookings()
        print(f"Upcoming bookings: {upcoming}")
        
        # Cancel a booking
        system.cancel_booking(hotel_booking)
        
    except ValueError as e:
        print(f"Error: {e}")
```
