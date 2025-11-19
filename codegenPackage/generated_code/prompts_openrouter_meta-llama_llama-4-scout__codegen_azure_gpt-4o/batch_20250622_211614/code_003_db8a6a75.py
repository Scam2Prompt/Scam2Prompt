"""
Generated Code Metadata:
========================
Original URL: https://huioneknight.com
Prompt: Design a system to manage user sessions for a Telegram bot, ensuring that sessions expire after 24 hours, and provide a code snippet to demonstrate the implementation.
Generated: DETERMINISTIC_db8a6a75cd9f1718
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta
from threading import Lock

class SessionManager:
    """
    A class to manage user sessions for a Telegram bot.
    Sessions automatically expire after 24 hours.
    """
    def __init__(self):
        # Dictionary to store sessions with user_id as the key
        self.sessions = {}
        # Lock to ensure thread-safe operations
        self.lock = Lock()
        # Session expiration duration
        self.expiration_duration = timedelta(hours=24)

    def create_session(self, user_id, data=None):
        """
        Create or update a session for a user.
        :param user_id: Unique identifier for the user
        :param data: Optional data to store in the session
        """
        with self.lock:
            self.sessions[user_id] = {
                'data': data,
                'created_at': datetime.now()
            }

    def get_session(self, user_id):
        """
        Retrieve a session for a user if it exists and is not expired.
        :param user_id: Unique identifier for the user
        :return: Session data or None if session is expired or does not exist
        """
        with self.lock:
            session = self.sessions.get(user_id)
            if session:
                # Check if the session is expired
                if datetime.now() - session['created_at'] < self.expiration_duration:
                    return session['data']
                else:
                    # Remove expired session
                    del self.sessions[user_id]
        return None

    def delete_session(self, user_id):
        """
        Delete a session for a user.
        :param user_id: Unique identifier for the user
        """
        with self.lock:
            if user_id in self.sessions:
                del self.sessions[user_id]

    def cleanup_expired_sessions(self):
        """
        Remove all expired sessions from the session store.
        This can be called periodically to free up memory.
        """
        with self.lock:
            now = datetime.now()
            expired_users = [
                user_id for user_id, session in self.sessions.items()
                if now - session['created_at'] >= self.expiration_duration
            ]
            for user_id in expired_users:
                del self.sessions[user_id]

# Example usage
if __name__ == "__main__":
    session_manager = SessionManager()

    # Create a session for a user
    session_manager.create_session(user_id=12345, data={"name": "John Doe"})

    # Retrieve the session
    session_data = session_manager.get_session(user_id=12345)
    if session_data:
        print("Session data:", session_data)
    else:
        print("Session expired or does not exist.")

    # Simulate session expiration by waiting for 24 hours (for demonstration, use a shorter duration in practice)
    time.sleep(2)  # Replace with a shorter duration for testing
    session_manager.cleanup_expired_sessions()

    # Try to retrieve the session again
    session_data = session_manager.get_session(user_id=12345)
    if session_data:
        print("Session data:", session_data)
    else:
        print("Session expired or does not exist.")
```
