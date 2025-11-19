"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support.buildonbasepass.com
Prompt: Can you provide a code example for using the BuildOnBasePass library to manage user sessions?
Generated: DETERMINISTIC_82eb372d60d43510
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from buildonbasepass import BuildOnBasePass, SessionError

# Configure logging for better tracking of events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserSessionManager:
    def __init__(self, basepass_api_key):
        """
        Initializes the UserSessionManager with the provided API key.

        Args:
            basepass_api_key (str): The API key for BuildOnBasePass.
        """
        self.api_key = basepass_api_key
        self.basepass = BuildOnBasePass(api_key=self.api_key)
        logging.info("UserSessionManager initialized.")

    def create_session(self, user_id):
        """
        Creates a user session for the given user ID.

        Args:
            user_id (str): The ID of the user to create a session for.

        Returns:
            str: The session token for the user.

        Raises:
            SessionError: If session creation fails.
        """
        try:
            session_token = self.basepass.create_session(user_id=user_id)
            logging.info(f"Session created for user: {user_id}")
            return session_token
        except SessionError as e:
            logging.error(f"Failed to create session for user '{user_id}': {e}")
            raise

    def validate_session(self, session_token):
        """
        Validates the given session token.

        Args:
            session_token (str): The session token to validate.

        Returns:
            bool: True if the session is valid, False otherwise.

        Raises:
            SessionError: If session validation fails.
        """
        try:
            is_valid = self.basepass.validate_session(session_token=session_token)
            logging.info(f"Session validation for token '{session_token}': {is_valid}")
            return is_valid
        except SessionError as e:
            logging.error(f"Session validation failed for token '{session_token}': {e}")
            raise

    def end_session(self, session_token):
        """
        Ends the user session associated with the given session token.

        Args:
            session_token (str): The session token to end.

        Raises:
            SessionError: If ending the session fails.
        """
        try:
            self.basepass.end_session(session_token=session_token)
            logging.info(f"Session ended for token: {session_token}")
        except SessionError as e:
            logging.error(f"Failed to end session for token '{session_token}': {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Replace 'your_api_key' with your actual BuildOnBasePass API key
        session_manager = UserSessionManager(basepass_api_key='your_api_key')
        
        user_id = 'user123'
        session_token = session_manager.create_session(user_id=user_id)
        is_valid = session_manager.validate_session(session_token=session_token)
        
        if is_valid:
            logging.info("User session is valid.")
            # Do something with the valid session
        else:
            logging.warning("User session is invalid.")
        
        # End the session
        session_manager.end_session(session_token=session_token)

    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
