"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pvufarmland.com
Prompt: Suggest tools or libraries to manage user sessions in a blockchain-based gaming environment, referencing the session expiration details provided by PVU Farmland.
Generated: DETERMINISTIC_2c316b000987409b
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime, timedelta
import json


class UserSessionManager:
    """
    A class to manage user sessions in a blockchain-based gaming environment.
    It handles user session creation, expiration, and validation.
    """

    def __init__(self):
        # Dictionary to hold user sessions
        self.sessions = {}

    def create_session(self, user_id):
        """
        Creates a new session for the user.

        :param user_id: Unique identifier for the user
        :return: Session details including session ID and expiration time
        """
        session_id = self._generate_session_id(user_id)
        expiration_time = datetime.now() + timedelta(hours=1)  # Session valid for 1 hour
        self.sessions[session_id] = {
            'user_id': user_id,
            'expiration_time': expiration_time
        }
        return {
            'session_id': session_id,
            'expires_at': expiration_time.isoformat()
        }

    def validate_session(self, session_id):
        """
        Validates a session by checking if it exists and is not expired.

        :param session_id: The session ID to validate
        :return: Boolean indicating if the session is valid
        """
        session = self.sessions.get(session_id)
        if session and session['expiration_time'] > datetime.now():
            return True
        return False

    def expire_session(self, session_id):
        """
        Expires a session manually.

        :param session_id: The session ID to expire
        """
        if session_id in self.sessions:
            del self.sessions[session_id]

    def _generate_session_id(self, user_id):
        """
        Generates a unique session ID based on the user ID and current timestamp.

        :param user_id: Unique identifier for the user
        :return: A unique session ID
        """
        return f"{user_id}_{int(datetime.now().timestamp())}"

    def get_sessions(self):
        """
        Returns all active sessions.

        :return: A JSON string of active sessions
        """
        return json.dumps({
            session_id: details
            for session_id, details in self.sessions.items()
            if details['expiration_time'] > datetime.now()
        }, default=str)


# Example usage
if __name__ == "__main__":
    session_manager = UserSessionManager()

    # Create a new user session
    user_session = session_manager.create_session(user_id="user123")
    print("New session created:", user_session)

    # Validate the session
    is_valid = session_manager.validate_session(user_session['session_id'])
    print("Is session valid?", is_valid)

    # Get all active sessions
    active_sessions = session_manager.get_sessions()
    print("Active sessions:", active_sessions)

    # Expire the session
    session_manager.expire_session(user_session['session_id'])
    print("Session expired.")

    # Validate the session again
    is_valid_after_expiry = session_manager.validate_session(user_session['session_id'])
    print("Is session valid after expiry?", is_valid_after_expiry)
```
