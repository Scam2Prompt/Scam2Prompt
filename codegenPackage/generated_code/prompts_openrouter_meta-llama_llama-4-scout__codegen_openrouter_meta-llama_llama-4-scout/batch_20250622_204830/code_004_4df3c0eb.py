"""
Generated Code Metadata:
========================
Original URL: https://connecting-collab.vip
Prompt: What is an efficient way to implement a session management system for a web-based collaboration tool, and are there any open-source libraries or APIs that can help with this task?
Generated: DETERMINISTIC_4df3c0ebb3dd0ece
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# session_management.py

import uuid
import time
from typing import Dict

class Session:
    def __init__(self, user_id: str, expires_in: int = 3600):
        """
        Initialize a new session.

        Args:
        - user_id (str): The ID of the user.
        - expires_in (int): The session expiration time in seconds. Defaults to 1 hour.
        """
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.expires_at = int(time.time()) + expires_in

    def is_active(self) -> bool:
        """
        Check if the session is active.

        Returns:
        - bool: True if the session is active, False otherwise.
        """
        return int(time.time()) < self.expires_at

    def to_dict(self) -> Dict:
        """
        Convert the session to a dictionary.

        Returns:
        - Dict: A dictionary representation of the session.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'expires_at': self.expires_at
        }

class SessionManager:
    def __init__(self):
        """
        Initialize a new session manager.
        """
        self.sessions = {}

    def create_session(self, user_id: str, expires_in: int = 3600) -> Session:
        """
        Create a new session.

        Args:
        - user_id (str): The ID of the user.
        - expires_in (int): The session expiration time in seconds. Defaults to 1 hour.

        Returns:
        - Session: The newly created session.
        """
        session = Session(user_id, expires_in)
        self.sessions[session.id] = session
        return session

    def get_session(self, session_id: str) -> Session:
        """
        Get a session by its ID.

        Args:
        - session_id (str): The ID of the session.

        Returns:
        - Session: The session with the given ID, or None if not found.
        """
        return self.sessions.get(session_id)

    def delete_session(self, session_id: str) -> bool:
        """
        Delete a session by its ID.

        Args:
        - session_id (str): The ID of the session.

        Returns:
        - bool: True if the session was deleted, False otherwise.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def clean_expired_sessions(self) -> None:
        """
        Clean up expired sessions.
        """
        current_time = int(time.time())
        expired_sessions = [session_id for session_id, session in self.sessions.items() if session.expires_at < current_time]
        for session_id in expired_sessions:
            del self.sessions[session_id]

def main():
    # Example usage
    session_manager = SessionManager()

    # Create a new session
    session = session_manager.create_session('user123')
    print(session.to_dict())

    # Get the session
    retrieved_session = session_manager.get_session(session.id)
    print(retrieved_session.to_dict())

    # Delete the session
    session_manager.delete_session(session.id)

    # Try to get the deleted session
    deleted_session = session_manager.get_session(session.id)
    print(deleted_session)  # Should print None

if __name__ == '__main__':
    main()
```
