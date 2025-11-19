"""
Generated Code Metadata:
========================
Original URL: https://baturjeeptour.my.id
Prompt: Generate a code snippet for a booking system that allows users to select a Jeep tour in Bali, including options for sunrise and sunset tours at Mount Batur.
Generated: DETERMINISTIC_3b41e6b2204cf7db
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, List, Dict

class TourType(Enum):
    """Enum representing the type of Jeep tour."""
    SUNRISE = "Sunrise"
    SUNSET = "Sunset"

class BookingStatus(Enum):
    """Enum representing the booking status."""
    CONFIRMED = "Confirmed"
    PENDING = "Pending"
    CANCELLED = "Cancelled"

class JeepTourBooking:
    """Class representing a Jeep tour booking in Bali."""
    
    def __init__(self, customer_name: str, tour_date: datetime.date, tour_type: TourType, participants: int):
        """
        Initialize a Jeep tour booking.
        
        Args:
            customer_name (str): Name of the customer making the booking.
            tour_date (datetime.date): Date of the tour.
            tour_type (TourType): Type of tour (Sunrise/Sunset).
            participants (int): Number of participants.
        """
        self.customer_name = customer_name
        self.tour_date = tour_date
        self.tour_type = tour_type
        self.participants = participants
        self.booking_time = datetime.datetime.now()
        self.status = BookingStatus.PENDING
        self.booking_id = self._generate_booking_id()
        
    def _generate_booking_id(self) -> str:
        """Generate a unique booking ID."""
        timestamp = int(self.booking_time.timestamp())
        return f"JTB-{timestamp}-{self.tour_type.value[:3].upper()}"
    
    def confirm_booking(self) -> None:
        """Confirm the booking."""
        if self.status == BookingStatus.PENDING:
            self.status = BookingStatus.CONFIRMED
    
    def cancel_booking(self) -> None:
        """Cancel the booking."""
        if self.status != BookingStatus.CANCELLED:
            self.status = BookingStatus.CANCELLED
    
    def get_booking_details(self) -> Dict:
        """Return booking details as a dictionary."""
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "tour_date": self.tour_date.strftime("%Y-%m-%d"),
            "tour_type": self.tour_type.value,
            "participants": self.participants,
            "booking_time": self.booking_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status.value
        }

class BookingSystem:
    """Class representing the Jeep tour booking system."""
    
    def __init__(self):
        """Initialize the booking system with an empty list of bookings."""
        self.bookings: List[JeepTourBooking] = []
    
    def create_booking(self, customer_name: str, tour_date: str, tour_type: str, participants: int) -> Optional[JeepTourBooking]:
        """
        Create a new Jeep tour booking.
        
        Args:
            customer_name (str): Name of the customer.
            tour_date (str): Date of the tour in 'YYYY-MM-DD' format.
            tour_type (str): Type of tour ('Sunrise' or 'Sunset').
            participants (int): Number of participants.
            
        Returns:
            Optional[JeepTourBooking]: The created booking or None if invalid.
        """
        try:
            date_obj = datetime.datetime.strptime(tour_date, "%Y-%m-%d").date()
            if date_obj < datetime.date.today():
                raise ValueError("Tour date cannot be in the past.")
            
            if participants <= 0:
                raise ValueError("Number of participants must be positive.")
            
            try:
                tour_type_enum = TourType[tour_type.upper()]
            except KeyError:
                raise ValueError("Invalid tour type. Must be 'Sunrise' or 'Sunset'.")
            
            booking = JeepTourBooking(customer_name, date_obj, tour_type_enum, participants)
            self.bookings.append(booking)
            return booking
            
        except ValueError as e:
            print(f"Error creating booking: {e}")
            return None
    
    def get_booking_by_id(self, booking_id: str) -> Optional[JeepTourBooking]:
        """
        Retrieve a booking by its ID.
        
        Args:
            booking_id (str): The booking ID to search for.
            
        Returns:
            Optional[JeepTourBooking]: The booking if found, None otherwise.
        """
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None
    
    def cancel_booking(self, booking_id: str) -> bool:
        """
        Cancel a booking by its ID.
        
        Args:
            booking_id (str): The booking ID to cancel.
            
        Returns:
            bool: True if cancellation was successful, False otherwise.
        """
        booking = self.get_booking_by_id(booking_id)
        if booking:
            booking.cancel_booking()
            return True
        return False
    
    def get_all_bookings(self) -> List[Dict]:
        """
        Get details of all bookings.
        
        Returns:
            List[Dict]: List of booking details dictionaries.
        """
        return [booking.get_booking_details() for booking in self.bookings]

# Example usage
if __name__ == "__main__":
    system = BookingSystem()
    
    # Create a booking
    booking = system.create_booking(
        "John Doe",
        "2023-12-25",
        "Sunrise",
        4
    )
    
    if booking:
        print("Booking created successfully!")
        print(booking.get_booking_details())
        
        # Confirm the booking
        booking.confirm_booking()
        print(f"Booking status: {booking.status.value}")
        
        # Get all bookings
        print("\nAll bookings:")
        for b in system.get_all_bookings():
            print(b)
```
