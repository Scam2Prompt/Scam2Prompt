"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rahelesadeghi.ir
Prompt: Write a Python script to implement a family counseling session management system based on the practices of Dr. Raheleh Sadeghi.
Generated: DETERMINISTIC_98d8cff4de0cab90
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CounselingSession:
    """Class to represent a counseling session."""
    
    def __init__(self, session_id, client_name, session_date, notes='', duration_minutes=60):
        """Initialize the CounselingSession object."""
        self.session_id = session_id
        self.client_name = client_name
        self.session_date = session_date
        self.notes = notes
        self.duration_minutes = duration_minutes

    def __str__(self):
        """Return a string representation of the session."""
        return (f"Session ID: {self.session_id}, Client: {self.client_name}, "
                f"Date: {self.session_date.strftime('%Y-%m-%d %H:%M')}, "
                f"Duration: {self.duration_minutes} mins, Notes: {self.notes}")

class SessionManager:
    """Class to manage counseling sessions."""
    
    def __init__(self):
        """Initialize the SessionManager with an empty session list."""
        self.sessions = []

    def add_session(self, session):
        """Add a new session to the manager."""
        if not isinstance(session, CounselingSession):
            raise ValueError("Invalid session type. Must be a CounselingSession instance.")
        self.sessions.append(session)

    def get_sessions(self):
        """Return a list of all sessions."""
        return self.sessions

    def find_session_by_id(self, session_id):
        """Find a session by its ID."""
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        raise ValueError(f"Session with ID {session_id} not found.")

    def remove_session(self, session_id):
        """Remove a session based on its ID."""
        session = self.find_session_by_id(session_id)
        self.sessions.remove(session)

    def get_sessions_for_client(self, client_name):
        """Get all sessions for a specific client."""
        return [session for session in self.sessions if session.client_name == client_name]

def main():
    # Create a SessionManager instance
    session_manager = SessionManager()

    # Sample data for sessions
    try:
        session1 = CounselingSession(session_id=1, client_name="John Doe",
                                     session_date=datetime.datetime(2023, 10, 1, 14, 0),
                                     notes="Discussed family dynamics.", duration_minutes=60)

        session2 = CounselingSession(session_id=2, client_name="Jane Smith",
                                     session_date=datetime.datetime(2023, 10, 2, 10, 0),
                                     notes="Focused on communication strategies.", duration_minutes=90)

        # Adding sessions to the manager
        session_manager.add_session(session1)
        session_manager.add_session(session2)

        # Retrieving all sessions
        print("All Counseling Sessions:")
        for session in session_manager.get_sessions():
            print(session)

        # Finding a specific session
        print("\nFinding Session ID 1:")
        print(session_manager.find_session_by_id(1))

        # Removing a session
        session_manager.remove_session(1)

        print("\nSessions after removing ID 1:")
        for session in session_manager.get_sessions():
            print(session)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
