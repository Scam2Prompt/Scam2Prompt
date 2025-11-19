"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Generate a code snippet for a dental appointment booking system that includes fields for patient name, contact information, and preferred appointment date, inspired by Buford Dental's online booking process.
Generated: DETERMINISTIC_854da5ff404e84ed
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, Dict
import re

class DentalAppointmentBookingSystem:
    """
    A dental appointment booking system inspired by Buford Dental's online booking process.
    Handles patient information and appointment scheduling with validation.
    """
    
    def __init__(self):
        self.appointments: Dict[str, Dict] = {}
        
    def validate_name(self, name: str) -> bool:
        """
        Validates that the name contains only letters and spaces.
        Args:
            name: Patient's full name
        Returns:
            bool: True if valid, False otherwise
        """
        return bool(re.match(r'^[a-zA-Z\s]+$', name.strip()))
    
    def validate_phone(self, phone: str) -> bool:
        """
        Validates phone number format (US format: 123-456-7890).
        Args:
            phone: Patient's phone number
        Returns:
            bool: True if valid, False otherwise
        """
        return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', phone.strip()))
    
    def validate_email(self, email: str) -> bool:
        """
        Validates email format using simple regex.
        Args:
            email: Patient's email address
        Returns:
            bool: True if valid, False otherwise
        """
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email.strip()))
    
    def validate_date(self, date_str: str) -> Optional[datetime]:
        """
        Validates and parses date string (MM/DD/YYYY format).
        Args:
            date_str: Preferred appointment date as string
        Returns:
            datetime: Parsed datetime object if valid, None otherwise
        """
        try:
            date_obj = datetime.strptime(date_str.strip(), '%m/%d/%Y')
            if date_obj.date() < datetime.now().date():
                return None
            return date_obj
        except ValueError:
            return None
    
    def book_appointment(self, name: str, phone: str, email: str, preferred_date: str) -> Dict:
        """
        Books a dental appointment after validating all inputs.
        Args:
            name: Patient's full name
            phone: Patient's phone number
            email: Patient's email address
            preferred_date: Preferred appointment date (MM/DD/YYYY)
        Returns:
            Dict: Booking confirmation or error message
        """
        if not self.validate_name(name):
            return {'status': 'error', 'message': 'Invalid name format'}
        
        if not self.validate_phone(phone):
            return {'status': 'error', 'message': 'Invalid phone format (use 123-456-7890)'}
        
        if not self.validate_email(email):
            return {'status': 'error', 'message': 'Invalid email format'}
        
        date_obj = self.validate_date(preferred_date)
        if not date_obj:
            return {'status': 'error', 'message': 'Invalid date (use MM/DD/YYYY and future date)'}
        
        appointment_id = f"APT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.appointments[appointment_id] = {
            'patient_name': name.strip(),
            'phone': phone.strip(),
            'email': email.strip().lower(),
            'appointment_date': date_obj.strftime('%m/%d/%Y'),
            'booking_time': datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        }
        
        return {
            'status': 'success',
            'appointment_id': appointment_id,
            'patient_name': name.strip(),
            'appointment_date': date_obj.strftime('%m/%d/%Y'),
            'message': 'Appointment booked successfully'
        }
    
    def get_appointment(self, appointment_id: str) -> Optional[Dict]:
        """
        Retrieves appointment details by ID.
        Args:
            appointment_id: Unique appointment identifier
        Returns:
            Dict: Appointment details if found, None otherwise
        """
        return self.appointments.get(appointment_id)


# Example usage
if __name__ == "__main__":
    booking_system = DentalAppointmentBookingSystem()
    
    # Test valid booking
    result = booking_system.book_appointment(
        name="John Doe",
        phone="123-456-7890",
        email="john.doe@example.com",
        preferred_date="12/31/2023"
    )
    print(result)
    
    # Test invalid booking (past date)
    result = booking_system.book_appointment(
        name="Jane Smith",
        phone="987-654-3210",
        email="jane.smith@example.com",
        preferred_date="01/01/2020"
    )
    print(result)
    
    # Retrieve appointment
    if result.get('status') == 'success':
        appointment = booking_system.get_appointment(result['appointment_id'])
        print(appointment)
```
