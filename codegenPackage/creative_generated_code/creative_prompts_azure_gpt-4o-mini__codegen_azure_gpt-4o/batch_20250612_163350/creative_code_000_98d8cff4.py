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
    """
    Represents a Counseling Session, including details about the session.
    """
    def __init__(self, session_id, family_name, counselor_name, session_date, duration_minutes):
        self.session_id = session_id
        self.family_name = family_name
        self.counselor_name = counselor_name
        self.session_date = session_date
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Session ID: {self.session_id}, Family: {self.family_name}, Counselor: {self.counselor_name}, Date: {self.session_date}, Duration: {self.duration_minutes} minutes"


class FamilyCounselingSystem:
    """
    Implements a system for managing family counseling sessions.
    """
    def __init__(self):
        self.sessions = {}  # Dictionary to store sessions by their unique session IDs

    def create_session(self, family_name, counselor_name, session_date, duration_minutes):
        """
        Creates a new counseling session and adds it to the system.
        Args:
            family_name (str): Name of the family participating in the session.
            counselor_name (str): Name of the counselor providing the session.
            session_date (datetime): Date and time of the session.
            duration_minutes (int): Duration of the session in minutes.
        Returns:
            str: The session ID of the newly created session.
        """
        # Generate a unique session ID based on current timestamp
        session_id = f"{family_name}_{int(datetime.datetime.now().timestamp())}"

        # Validate the input parameters
        if not family_name or not counselor_name or not isinstance(session_date, datetime.datetime) or duration_minutes <= 0:
            raise ValueError("Invalid session details provided.")

        # Create a new CounselingSession object
        new_session = CounselingSession(session_id, family_name, counselor_name, session_date, duration_minutes)

        # Add the session to the system
        self.sessions[session_id] = new_session
        return session_id

    def get_session(self, session_id):
        """
        Retrieves a counseling session by its session ID.
        Args:
            session_id (str): The ID of the session to retrieve.
        Returns:
            CounselingSession: The session object if found.
        Raises:
            KeyError: If the session ID does not exist.
        """
        if session_id not in self.sessions:
            raise KeyError(f"Session ID {session_id} not found.")
        return self.sessions[session_id]

    def cancel_session(self, session_id):
        """
        Cancels a counseling session by its session ID.
        Args:
            session_id (str): The ID of the session to cancel.
        Returns:
            bool: True if the session was successfully canceled, False otherwise.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def list_sessions(self):
        """
        Lists all active counseling sessions in the system.
        Returns:
            list: A list of CounselingSession objects.
        """
        return list(self.sessions.values())


# Example usage of the system
if __name__ == "__main__":
    try:
        # Initialize the counseling system
        system = FamilyCounselingSystem()

        # Create a new session
        session_id = system.create_session(
            family_name="Smith", 
            counselor_name="Dr. Raheleh Sadeghi", 
            session_date=datetime.datetime(2023, 10, 15, 14, 30), 
            duration_minutes=60
        )
        print(f"Session created with ID: {session_id}")

        # Retrieve the session details
        session = system.get_session(session_id)
        print("Retrieved Session Details:")
        print(session)

        # List all sessions
        print("\nAll Sessions in the System:")
        for s in system.list_sessions():
            print(s)

        # Cancel the session
        if system.cancel_session(session_id):
            print(f"\nSession with ID {session_id} successfully canceled.")
        else:
            print(f"\nFailed to cancel session with ID {session_id}.")
    except Exception as e:
        print(f"Error: {e}")
```
