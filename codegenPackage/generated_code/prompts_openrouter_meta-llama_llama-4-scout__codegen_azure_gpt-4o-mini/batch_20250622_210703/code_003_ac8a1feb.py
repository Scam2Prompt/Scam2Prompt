"""
Generated Code Metadata:
========================
Original URL: https://breakthroughstudio.in
Prompt: Create a code snippet to manage online bookings and demo sessions for a fitness studio, specifically designed for suspension training services like Breakthrough Studio.
Generated: DETERMINISTIC_ac8a1febd914efb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class Session:
    """Class representing a training session."""
    
    def __init__(self, session_id, date_time, duration, max_participants):
        self.session_id = session_id
        self.date_time = date_time
        self.duration = duration  # in minutes
        self.max_participants = max_participants
        self.participants = []

    def is_full(self):
        """Check if the session is full."""
        return len(self.participants) >= self.max_participants

    def add_participant(self, participant):
        """Add a participant to the session if not full."""
        if self.is_full():
            raise BookingError("Session is full.")
        self.participants.append(participant)

    def to_dict(self):
        """Convert session details to a dictionary."""
        return {
            "session_id": self.session_id,
            "date_time": self.date_time.isoformat(),
            "duration": self.duration,
            "max_participants": self.max_participants,
            "participants": self.participants
        }

class BookingManager:
    """Class to manage bookings for fitness sessions."""
    
    def __init__(self):
        self.sessions = []

    def create_session(self, date_time, duration, max_participants):
        """Create a new training session."""
        session_id = len(self.sessions) + 1
        new_session = Session(session_id, date_time, duration, max_participants)
        self.sessions.append(new_session)
        return new_session

    def book_session(self, session_id, participant):
        """Book a participant into a session."""
        session = self.get_session(session_id)
        if session is None:
            raise BookingError("Session not found.")
        session.add_participant(participant)

    def get_session(self, session_id):
        """Retrieve a session by its ID."""
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        return None

    def get_all_sessions(self):
        """Get a list of all sessions."""
        return [session.to_dict() for session in self.sessions]

    def save_sessions_to_file(self, filename):
        """Save session data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_all_sessions(), file, indent=4)
        except IOError as e:
            raise BookingError(f"Error saving sessions to file: {e}")

# Example usage
if __name__ == "__main__":
    booking_manager = BookingManager()
    
    # Create a session
    session_time = datetime.now() + timedelta(days=1)  # Schedule for tomorrow
    booking_manager.create_session(session_time, duration=60, max_participants=10)

    # Book a participant
    try:
        booking_manager.book_session(1, "John Doe")
        print("Booking successful.")
    except BookingError as e:
        print(f"Booking failed: {e}")

    # Save sessions to a file
    try:
        booking_manager.save_sessions_to_file("sessions.json")
        print("Sessions saved successfully.")
    except BookingError as e:
        print(f"Failed to save sessions: {e}")
```
