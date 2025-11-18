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
import time
from collections import defaultdict

# Configuration
MAX_FAILED_ATTEMPTS = 5  # Number of failed attempts before alerting
ALERT_THRESHOLD_SECONDS = 300  # Time window in seconds to monitor failed attempts

# Dictionary to store failed attempts: {username: [(timestamp)]}
failed_attempts = defaultdict(list)

def log_failed_attempt(username):
    """
    Log a failed login attempt for a given username.
    If the failed attempts exceed the limit within the threshold window, trigger an alert.
    """
    current_time = time.time()
    failed_attempts[username].append(current_time)

    # Clean up old attempts outside the threshold window
    failed_attempts[username] = [
        timestamp for timestamp in failed_attempts[username]
        if current_time - timestamp <= ALERT_THRESHOLD_SECONDS
    ]

    if len(failed_attempts[username]) >= MAX_FAILED_ATTEMPTS:
        trigger_alert(username)

def trigger_alert(username):
    """
    Trigger an alert for a specific username after exceeding failed attempt limits.
    """
    print(f"ALERT: Multiple failed login attempts detected for user '{username}'.")

def simulate_failed_login(username):
    """
    Simulate a failed login attempt and logging mechanism.
    """
    try:
        # Simulating a failed login scenario
        log_failed_attempt(username)
    except Exception as e:
        print(f"Error: Failed to log login attempt for user '{username}'. Reason: {e}")

# Example Usage
if __name__ == "__main__":
    simulate_failed_login("admin")
    simulate_failed_login("admin")
    simulate_failed_login("admin")
    simulate_failed_login("admin")
    simulate_failed_login("admin")
    simulate_failed_login("admin")  # At this point, the alert should trigger
```
