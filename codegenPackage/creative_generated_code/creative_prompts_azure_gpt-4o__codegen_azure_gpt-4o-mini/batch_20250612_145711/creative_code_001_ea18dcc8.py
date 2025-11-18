"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collab.top
Prompt: Recommend libraries or APIs for managing session expiration and renewal in web applications.
Generated: DETERMINISTIC_ea18dcc870d7a8d0
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# session_manager.py

import time
from datetime import timedelta, datetime

class SessionManager:
    """
    A class to manage user sessions, including expiration and renewal.
    """

    def __init__(self, session_timeout_minutes=30):
        """
        Initializes the SessionManager with a specified session timeout.

        :param session_timeout_minutes: Session timeout duration in minutes.
        """
        self.session_timeout = timedelta(minutes=session_timeout_minutes)
        self.sessions = {}

    def create_session(self, user_id):
        """
        Creates a new session for a given user.

        :param user_id: The unique identifier for the user.
        :return: A dictionary containing the session information.
        """
        if user_id in self.sessions:
            raise ValueError("Session already exists for this user.")

        session_data = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'expires_at': datetime.now() + self.session_timeout,
        }
        self.sessions[user_id] = session_data
        return session_data

    def renew_session(self, user_id):
        """
        Renews the session for a given user.

        :param user_id: The unique identifier for the user.
        :return: Updated session data.
        """
        if user_id not in self.sessions:
            raise ValueError("Session does not exist for this user.")

        self.sessions[user_id]['expires_at'] = datetime.now() + self.session_timeout
        return self.sessions[user_id]

    def is_session_active(self, user_id):
        """
        Checks if the session for a given user is currently active.

        :param user_id: The unique identifier for the user.
        :return: True if the session is active, False otherwise.
        """
        if user_id not in self.sessions:
            return False

        session_data = self.sessions[user_id]
        return datetime.now() < session_data['expires_at']

    def expire_session(self, user_id):
        """
        Expires the session for a given user.

        :param user_id: The unique identifier for the user.
        """
        if user_id in self.sessions:
            del self.sessions[user_id]

    def cleanup_expired_sessions(self):
        """
        Cleans up all expired sessions from the session store.
        """
        current_time = datetime.now()
        expired_users = [user_id for user_id, session in self.sessions.items()
                         if session['expires_at'] < current_time]
        
        for user_id in expired_users:
            self.expire_session(user_id)

# Example usage:
if __name__ == "__main__":
    manager = SessionManager(session_timeout_minutes=5)
    
    # Creating a session
    try:
        session = manager.create_session(user_id="user123")
        print("Session created:", session)
        
        # Checking if session is active
        print("Is session active?", manager.is_session_active("user123"))
        
        # Renewing session
        renewed_session = manager.renew_session("user123")
        print("Session renewed:", renewed_session)
        
        # Cleanup expired sessions
        time.sleep(6)  # Simulating a wait for the session to expire
        manager.cleanup_expired_sessions()
        print("After cleanup, is session active?", manager.is_session_active("user123"))
    
    except ValueError as e:
        print("Error:", e)
```
