"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Write code to implement a feature for booking virtual care sessions with healthcare professionals, similar to the online session booking functionality described on the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_e37374dedfbe3953
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# booking_system.py
import uuid
from datetime import datetime, timedelta

class BookingError(Exception):
    """Custom Exception for handling booking errors."""
    pass

class VirtualCareSession:
    """
    A class to represent a virtual care session booking.
    """

    def __init__(self, session_id, patient_name, healthcare_professional, session_datetime):
        """
        Initializes a VirtualCareSession object.
        
        Args:
            session_id (str): Unique ID for the session.
            patient_name (str): Name of the patient.
            healthcare_professional (str): Name of the healthcare professional.
            session_datetime (datetime): Scheduled date and time for the session.
        """
        self.session_id = session_id
        self.patient_name = patient_name
        self.healthcare_professional = healthcare_professional
        self.session_datetime = session_datetime
        self.is_confirmed = False

    def confirm_session(self):
        """
        Confirms the session.
        """
        self.is_confirmed = True

    def __str__(self):
        """
        Returns a string representation of the session.
        """
        return f"Session ID: {self.session_id} | Patient: {self.patient_name} | Professional: {self.healthcare_professional} | Date/Time: {self.session_datetime} | Confirmed: {self.is_confirmed}"

class VirtualCareBookingSystem:
    """
    A system for managing virtual care session bookings.
    """

    def __init__(self):
        """
        Initializes a VirtualCareBookingSystem object.
        """
        self.sessions = {}

    def book_session(self, patient_name, healthcare_professional, session_datetime):
        """
        Books a new virtual care session.
        
        Args:
            patient_name (str): Name of the patient.
            healthcare_professional (str): Name of the healthcare professional.
            session_datetime (datetime): Desired date and time for the session.
            
        Returns:
            VirtualCareSession: The booked session object.
            
        Raises:
            BookingError: If the session datetime has already passed or conflicts with an existing session.
        """
        # Validate session datetime
        if session_datetime < datetime.now():
            raise BookingError("Cannot book a session in the past.")
        
        # Check for conflicts
        for session in self.sessions.values():
            if (session.healthcare_professional == healthcare_professional and 
                session.session_datetime == session_datetime):
                raise BookingError("This healthcare professional is already booked for the specified datetime.")

        # Create a new session
        session_id = str(uuid.uuid4())
        new_session = VirtualCareSession(session_id, patient_name, healthcare_professional, session_datetime)
        self.sessions[session_id] = new_session
        return new_session

    def confirm_session(self, session_id):
        """
        Confirms a booked session.
        
        Args:
            session_id (str): The unique ID of the session to confirm.
            
        Raises:
            BookingError: If the session ID is invalid or already confirmed.
        """
        session = self.sessions.get(session_id)
        if not session:
            raise BookingError("Invalid session ID.")
        if session.is_confirmed:
            raise BookingError("Session is already confirmed.")
        
        session.confirm_session()

    def list_sessions(self):
        """
        Lists all booked sessions.
        
        Returns:
            list: A list of all session objects.
        """
        return list(self.sessions.values())

# Example usage:
if __name__ == "__main__":
    try:
        booking_system = VirtualCareBookingSystem()

        # Book a session
        session_datetime = datetime.now() + timedelta(days=1)  # Schedule for tomorrow
        new_session = booking_system.book_session("John Doe", "Dr. Smith", session_datetime)
        print(f"New session booked successfully: {new_session}")

        # Confirm the session
        booking_system.confirm_session(new_session.session_id)
        print("Session confirmed successfully.")

        # List all sessions
        print("\nAll booked sessions:")
        for session in booking_system.list_sessions():
            print(session)

    except BookingError as e:
        print(f"Booking error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
