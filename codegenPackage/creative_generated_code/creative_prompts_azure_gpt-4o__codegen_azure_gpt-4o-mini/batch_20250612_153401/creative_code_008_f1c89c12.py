"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edealkart.com
Prompt: Write code to log failed login attempts for an admin dashboard and trigger an alert after multiple unsuccessful attempts.
Generated: DETERMINISTIC_f1c89c12ceb37629
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    filename='failed_login_attempts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for login attempt tracking
MAX_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=15)

# Dictionary to track failed login attempts
failed_attempts = {}

def log_failed_attempt(username):
    """
    Logs a failed login attempt for a specified user and checks if the alert condition is met.
    
    Args:
        username (str): The username for which the login attempt failed.
    """
    current_time = datetime.now()
    
    # Check if the user is already in the failed attempts log
    if username not in failed_attempts:
        failed_attempts[username] = []
    
    # Append the current time to the user's failed attempts
    failed_attempts[username].append(current_time)
    
    # Remove attempts that are older than the lockout duration
    failed_attempts[username] = [attempt for attempt in failed_attempts[username] 
                                 if attempt > current_time - LOCKOUT_DURATION]
    
    # Log the failed attempt
    logging.info(f'Failed login attempt for user: {username}')
    
    # Trigger alert if the number of failed attempts exceeds the maximum allowed
    if len(failed_attempts[username]) >= MAX_ATTEMPTS:
        trigger_alert(username)

def trigger_alert(username):
    """
    Triggers an alert when the maximum number of failed login attempts is reached.
    
    Args:
        username (str): The username that triggered the alert.
    """
    logging.warning(f'ALERT: User {username} has exceeded the maximum failed login attempts.')

def simulate_login(username, success):
    """
    Simulates a login attempt for a user. Logs a failure if the attempt is unsuccessful.
    
    Args:
        username (str): The username of the person trying to log in.
        success (bool): Indicates whether the login attempt was successful or not.
    """
    if not success:
        log_failed_attempt(username)
    else:
        # Reset failed attempts on a successful login
        if username in failed_attempts:
            del failed_attempts[username]
        logging.info(f'Successful login for user: {username}')

# Example usage
if __name__ == "__main__":
    # Simulate failed login attempts
    for i in range(6):
        simulate_login('admin', success=False)
```
