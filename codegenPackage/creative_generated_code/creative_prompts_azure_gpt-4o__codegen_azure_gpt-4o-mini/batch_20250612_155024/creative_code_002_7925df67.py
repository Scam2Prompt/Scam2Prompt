"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Generate code for setting up access monitoring in a cloud environment using an IAM system like Techmaestropus. Include functionality for real-time threat detection and logging user activity.
Generated: DETERMINISTIC_7925df67a84d0a35
Batch ID: 20250612_155024
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
import time

# Mock class representing the IAM system (Techmaestropus)
class TechmaestropusIAM:
    def __init__(self):
        # Initialize user activity log
        self.activity_log = []

    def log_activity(self, user_id, action):
        """Logs user activity with timestamp."""
        timestamp = datetime.now().isoformat()
        self.activity_log.append({
            'user_id': user_id,
            'action': action,
            'timestamp': timestamp
        })
        logging.info(f"Activity logged: {user_id} performed {action} at {timestamp}")

    def detect_threat(self):
        """Simulate real-time threat detection."""
        # Placeholder for threat detection logic
        # In a real-world scenario, this could involve checking user behaviors,
        # comparing against known attack signatures, etc.
        if self.activity_log and len(self.activity_log) > 10:  # Example condition
            logging.warning("Potential threat detected! Review user activities.")
            return True
        return False

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    iam_system = TechmaestropusIAM()

    try:
        # Simulating user activities
        user_actions = ["login", "view_resource", "update_resource", "logout"] * 3

        for user_id in range(1, 6):  # Simulating 5 users
            for action in user_actions:
                iam_system.log_activity(user_id, action)
                time.sleep(0.5)  # Simulate time delay between actions

            # Detect threats after user activities
            if iam_system.detect_threat():
                # Here we can add further actions, such as notifying an admin
                logging.info("Admin notified for potential threat.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        # Log final activity states
        logging.info("Final activity log:")
        for log in iam_system.activity_log:
            logging.info(log)

if __name__ == "__main__":
    main()
```
