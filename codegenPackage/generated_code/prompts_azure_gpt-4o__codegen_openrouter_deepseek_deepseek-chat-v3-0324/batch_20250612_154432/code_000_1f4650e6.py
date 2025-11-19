"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python script to simulate a plumbing service booking system for Certified Plumbers Graham, TX, including fields for service type (e.g., leak detection, repiping), customer details, and preferred appointment time.
Generated: DETERMINISTIC_1f4650e6e7052d67
Batch ID: 20250612_154432
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
from enum import Enum
import uuid
import os

class ServiceType(Enum):
    LEAK_DETECTION = "Leak Detection"
    REPIPING = "Repiping"
    DRAIN_CLEANING = "Drain Cleaning"
    WATER_HEATER = "Water Heater Installation/Repair"
    TOILET_REPAIR = "Toilet Repair"
    OTHER = "Other"

class BookingStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class PlumbingServiceBooking:
    def __init__(self):
        self.bookings_file = "plumbing_bookings.json"
        self._initialize_bookings_file()

    def _initialize_bookings_file(self):
        """Initialize the bookings file if it doesn't exist."""
        if not os.path.exists(self.bookings_file):
            with open(self.bookings_file, 'w') as f:
                json.dump([], f)

    def _load_bookings(self):
        """Load all bookings from the file."""
        try:
            with open(self.bookings_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_bookings(self, bookings):
        """Save bookings to the file."""
        with open(self.bookings_file, 'w') as f:
            json.dump(bookings, f, indent=4)

    def _validate_appointment_time(self, appointment_time):
        """Validate that the appointment time is in the future."""
        try:
            appointment_datetime = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
            if appointment_datetime < datetime.now():
                raise ValueError("Appointment time must be in the future.")
            return True
        except ValueError as e:
            raise ValueError(f"Invalid appointment time format or value: {e}")

    def create_booking(self, service_type, customer_details, appointment_time):
        """
        Create a new plumbing service booking.
        
        Args:
            service_type (ServiceType): Type of plumbing service.
            customer_details (dict): Customer information including name, phone, and address.
            appointment_time (str): Preferred appointment time in 'YYYY-MM-DD HH:MM' format.
            
        Returns:
            dict: The created booking with a unique ID and status.
        """
        try:
            # Validate inputs
            if not isinstance(service_type, ServiceType):
                raise ValueError("Invalid service type.")
            
            required_customer_fields = ['name', 'phone', 'address']
            if not all(field in customer_details for field in required_customer_fields):
                raise ValueError("Customer details must include name, phone, and address.")
            
            self._validate_appointment_time(appointment_time)
            
            # Create booking
            booking_id = str(uuid.uuid4())
            booking = {
                'id': booking_id,
                'service_type': service_type.value,
                'customer_details': customer_details,
                'appointment_time': appointment_time,
                'status': BookingStatus.PENDING.value,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Save booking
            bookings = self._load_bookings()
            bookings.append(booking)
            self._save_bookings(bookings)
            
            return booking
        except Exception as e:
            raise ValueError(f"Failed to create booking: {e}")

    def get_booking(self, booking_id):
        """Retrieve a booking by its ID."""
        bookings = self._load_bookings()
        for booking in bookings:
            if booking['id'] == booking_id:
                return booking
        raise ValueError("Booking not found.")

    def update_booking_status(self, booking_id, new_status):
        """Update the status of a booking."""
        if not isinstance(new_status, BookingStatus):
            raise ValueError("Invalid booking status.")
            
        bookings = self._load_bookings()
        updated = False
        
        for booking in bookings:
            if booking['id'] == booking_id:
                booking['status'] = new_status.value
                updated = True
                break
                
        if not updated:
            raise ValueError("Booking not found.")
            
        self._save_bookings(bookings)
        return True

    def get_all_bookings(self):
        """Retrieve all bookings."""
        return self._load_bookings()

    def get_bookings_by_status(self, status):
        """Retrieve bookings by their status."""
        if not isinstance(status, BookingStatus):
            raise ValueError("Invalid booking status.")
            
        bookings = self._load_bookings()
        return [b for b in bookings if b['status'] == status.value]

# Example usage
if __name__ == "__main__":
    booking_system = PlumbingServiceBooking()
    
    # Create a booking
    try:
        customer = {
            'name': 'John Doe',
            'phone': '555-123-4567',
            'address': '123 Main St, Graham, TX'
        }
        appointment_time = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
        
        new_booking = booking_system.create_booking(
            service_type=ServiceType.LEAK_DETECTION,
            customer_details=customer,
            appointment_time=appointment_time
        )
        print(f"Created booking: {json.dumps(new_booking, indent=4)}")
        
        # Retrieve all bookings
        all_bookings = booking_system.get_all_bookings()
        print(f"All bookings: {json.dumps(all_bookings, indent=4)}")
        
    except Exception as e:
        print(f"Error: {e}")
```
