"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyusd-mixer.com
Prompt: Write code to validate and process session tokens for a PayPal USD mixer service, including error handling for expired or manually destroyed sessions.
Generated: DETERMINISTIC_a9a20a3dbe540f58
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import jwt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
SECRET_KEY = 'your_secret_key'  # Should be an environment variable in production
SESSION_EXPIRATION_TIME = 3600  # Token valid for 1 hour

class SessionTokenError(Exception):
    """Custom exception for session token related errors."""
    pass

def create_session_token(user_id):
    """
    Create a JWT session token for a user.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        str: Encoded JWT session token.
    """
    try:
        # Define token payload with expiration
        payload = {
            'user_id': user_id,
            'exp': time.time() + SESSION_EXPIRATION_TIME
        }
        # Encode the token
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        logging.info(f"Token created for user_id: {user_id}")
        return token
    except Exception as e:
        logging.error(f"Error creating session token: {str(e)}")
        raise SessionTokenError("Failed to create session token.")

def validate_session_token(token):
    """
    Validate a session token and return the user ID if valid.

    Args:
        token (str): The JWT session token.

    Returns:
        str: The user ID extracted from the token.

    Raises:
        SessionTokenError: If the token is invalid or expired.
    """
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        logging.info(f"Token validated for user_id: {payload['user_id']}")
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        logging.warning("Token has expired.")
        raise SessionTokenError("Session token has expired.")
    except jwt.InvalidTokenError:
        logging.warning("Invalid session token.")
        raise SessionTokenError("Invalid session token.")

def destroy_session(user_id):
    """
    Simulate destroying a user session by logging the action.

    Args:
        user_id (str): The unique identifier for the user.
    """
    logging.info(f"Session destroyed for user_id: {user_id}")
    # In production, you would implement logic to invalidate the token, e.g., blacklist it.

# Example usage:
if __name__ == "__main__":
    user_id = "user123"
    
    # Create a session token
    token = create_session_token(user_id)
    
    # Validate the session token
    try:
        validated_user_id = validate_session_token(token)
        print(f"Validated user ID: {validated_user_id}")
    except SessionTokenError as e:
        print(f"Session token error: {str(e)}")
    
    # Destroy the session
    destroy_session(user_id)
```
