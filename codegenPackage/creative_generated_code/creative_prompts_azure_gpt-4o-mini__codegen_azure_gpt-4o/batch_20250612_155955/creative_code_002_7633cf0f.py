"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microlab.world
Prompt: What are the best practices for managing user sessions in a MicroLab application?
Generated: DETERMINISTIC_7633cf0fc686ad99
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: session_manager.py

import uuid
from datetime import datetime, timedelta
from typing import Dict

# Best practice: Use a secure, random library for session IDs and enforce expiration times.

class SessionManager:
    """
    A class to manage user sessions in a MicroLab application.
    Ensures secure session handling with expiration and proper cleanup.
    """
    
    def __init__(self, session_timeout_minutes: int = 30):
        """
        Initialize the session manager.
        
        :param session_timeout_minutes: Duration (in minutes) for session expiration.
        """
        self.sessions: Dict[str, Dict] = {}  # Store sessions with session_id as the key
        self.session_timeout = timedelta(minutes=session_timeout_minutes)

    def create_session(self, user_id: str) -> str:
        """
        Create a new session for a user.
        
        :param user_id: The ID of the user.
        :return: The newly generated session ID.
        """
        session_id = str(uuid.uuid4())  # Generate a unique session ID
        self.sessions[session_id] = {
            "user_id": user_id,
            "created_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + self.session_timeout,
        }
        return session_id

    def validate_session(self, session_id: str) -> bool:
        """
        Validate if a session ID is active and not expired.
        
        :param session_id: The session ID to validate.
        :return: True if valid, False otherwise.
        """
        session = self.sessions.get(session_id)
        if not session:
            return False
        if session["expires_at"] < datetime.utcnow():
            # Session has expired; clean up
            self.delete_session(session_id)
            return False
        return True

    def delete_session(self, session_id: str) -> bool:
        """
        Delete a session by its ID.
        
        :param session_id: The session ID to delete.
        :return: True if deleted successfully, False otherwise.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False

    def cleanup_expired_sessions(self):
        """
        Remove all expired sessions from the session store.
        This method can be run periodically (e.g., as part of a background task).
        """
        expired_sessions = [
            session_id for session_id, session in self.sessions.items()
            if session["expires_at"] < datetime.utcnow()
        ]
        for session_id in expired_sessions:
            self.delete_session(session_id)


# Example Usage
if __name__ == "__main__":
    session_manager = SessionManager(session_timeout_minutes=30)

    # Create a session for a user
    user_id = "user123"
    session_id = session_manager.create_session(user_id)
    print(f"Created session: {session_id}")

    # Validate the session
    is_valid = session_manager.validate_session(session_id)
    print(f"Is session valid? {is_valid}")

    # Simulate session expiration (for demonstration purposes)
    import time
    time.sleep(1)  # Short delay to simulate time passage
    session_manager.sessions[session_id]["expires_at"] = datetime.utcnow() - timedelta(seconds=1)

    # Validate the session again after manual expiration
    is_valid = session_manager.validate_session(session_id)
    print(f"Is session valid after expiration? {is_valid}")

    # Cleanup expired sessions
    session_manager.cleanup_expired_sessions()
    print("Expired sessions have been cleaned up.")
```
