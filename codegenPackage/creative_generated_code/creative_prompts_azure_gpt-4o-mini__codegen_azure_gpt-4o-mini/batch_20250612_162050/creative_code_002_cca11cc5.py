"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: Can you provide a code snippet for a booking system that allows users to schedule text-based counselling sessions, inspired by the features of Text Counselling Online?
Generated: DETERMINISTIC_cca11cc5bcc73277
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class CounsellingSession:
    """Class to represent a counselling session."""

    def __init__(self, user_id, session_time):
        self.user_id = user_id
        self.session_time = session_time
        self.session_id = None

    def __repr__(self):
        return f"<CounsellingSession(user_id={self.user_id}, session_time={self.session_time})>"


class BookingSystem:
    """Class to manage the booking system for counselling sessions."""

    def __init__(self):
        self.sessions = []  # List to store booked sessions
        self.load_sessions()  # Load existing sessions if available

    def book_session(self, user_id: int, session_time: str) -> str:
        """
        Book a counselling session for a user.

        :param user_id: ID of the user booking the session
        :param session_time: Time of the session in 'YYYY-MM-DD HH:MM' format
        :return: Confirmation message or error
        """
        try:
            # Validate and parse the session time
            session_time_dt = datetime.strptime(session_time, '%Y-%m-%d %H:%M')
            if session_time_dt < datetime.now():
                return "Error: Session time must be in the future."

            # Check for conflicts with existing sessions
            if any(session.session_time == session_time_dt for session in self.sessions):
                return "Error: This time slot is already booked."

            # Create and store the new session
            new_session = CounsellingSession(user_id, session_time_dt)
            self.sessions.append(new_session)
            self.save_sessions()  # Save sessions to file
            return f"Session booked successfully: {new_session}"

        except ValueError as ve:
            return f"Error: Invalid date format. {ve}"

    def load_sessions(self):
        """Load existing sessions from a JSON file."""
        try:
            with open('sessions.json', 'r') as file:
                session_data = json.load(file)
                for session in session_data:
                    session_time = datetime.fromisoformat(session['session_time'])
                    self.sessions.append(CounsellingSession(session['user_id'], session_time))
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is corrupted, start with an empty session list
            self.sessions = []

    def save_sessions(self):
        """Save current sessions to a JSON file."""
        session_data = [{'user_id': session.user_id, 'session_time': session.session_time.isoformat()} for session in self.sessions]
        with open('sessions.json', 'w') as file:
            json.dump(session_data, file)

    def list_sessions(self):
        """
        List all booked sessions.

        :return: List of session details
        """
        return [str(session) for session in self.sessions]


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    print(booking_system.book_session(1, '2023-12-01 15:00'))  # Book a session
    print(booking_system.list_sessions())  # List all sessions
```
