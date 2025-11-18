"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pos.graphixals.top
Prompt: Write code to log user activity during login attempts in a Point of Sale system for auditing purposes.
Generated: DETERMINISTIC_39c72c0e6bdd48d1
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging settings
logging.basicConfig(
    filename='user_activity.log',  # Log file name
    level=logging.INFO,            # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def log_login_attempt(username: str, success: bool):
    """
    Logs a user's login attempt.

    Args:
        username (str): The username of the user attempting to log in.
        success (bool): Indicates whether the login attempt was successful or not.
    """
    try:
        # Create a log message
        status = "SUCCESS" if success else "FAILURE"
        log_message = f"User '{username}' attempted to log in: {status}"
        
        # Log the message
        logging.info(log_message)

    except Exception as e:
        logging.error(f"Error logging login attempt for user '{username}': {str(e)}")

def main():
    """
    Main function to simulate login attempts.
    Replace this with actual login logic in production.
    """
    # Simulate login attempts
    users = [
        ("user1", True),   # Successful login
        ("user2", False),  # Failed login
        ("user3", True),   # Successful login
        ("user4", False)   # Failed login
    ]
    
    for username, success in users:
        log_login_attempt(username, success)

if __name__ == "__main__":
    main()
```
