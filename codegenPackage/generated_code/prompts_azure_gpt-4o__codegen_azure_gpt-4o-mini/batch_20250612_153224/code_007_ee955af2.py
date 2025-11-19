"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Write a program to monitor and control access to premises using gate automation systems, incorporating features described by Donture Systems Ltd.
Generated: DETERMINISTIC_ee955af266579431
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GateAutomationSystem:
    def __init__(self):
        self.access_log = []  # Log of access attempts
        self.authorized_users = set()  # Set of authorized user IDs
        self.gate_open = False  # Gate status

    def authorize_user(self, user_id):
        """Authorize a user by adding them to the authorized users set."""
        self.authorized_users.add(user_id)
        logging.info(f"User {user_id} authorized.")

    def deauthorize_user(self, user_id):
        """Deauthorize a user by removing them from the authorized users set."""
        self.authorized_users.discard(user_id)
        logging.info(f"User {user_id} deauthorized.")

    def attempt_access(self, user_id):
        """Simulate an access attempt by a user."""
        logging.info(f"User {user_id} attempting to access.")
        if user_id in self.authorized_users:
            self.open_gate()
            self.log_access(user_id, success=True)
        else:
            self.log_access(user_id, success=False)
            logging.warning(f"Access denied for user {user_id}.")

    def open_gate(self):
        """Open the gate and simulate the opening duration."""
        if not self.gate_open:
            self.gate_open = True
            logging.info("Gate is opening...")
            time.sleep(2)  # Simulate time taken to open the gate
            logging.info("Gate is now open.")
            time.sleep(5)  # Gate remains open for 5 seconds
            self.close_gate()
        else:
            logging.info("Gate is already open.")

    def close_gate(self):
        """Close the gate."""
        if self.gate_open:
            self.gate_open = False
            logging.info("Gate is closing...")
            time.sleep(1)  # Simulate time taken to close the gate
            logging.info("Gate is now closed.")
        else:
            logging.info("Gate is already closed.")

    def log_access(self, user_id, success):
        """Log the access attempt."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.access_log.append({
            'timestamp': timestamp,
            'user_id': user_id,
            'success': success
        })
        logging.info(f"Access log updated: {self.access_log[-1]}")

    def get_access_log(self):
        """Return the access log."""
        return self.access_log

def main():
    """Main function to run the gate automation system."""
    gate_system = GateAutomationSystem()

    # Authorize some users
    gate_system.authorize_user("user_1")
    gate_system.authorize_user("user_2")

    # Simulate access attempts
    users_to_test = ["user_1", "user_3", "user_2", "user_4"]
    for user in users_to_test:
        gate_system.attempt_access(user)
        time.sleep(1)  # Wait a moment before the next access attempt

    # Print the access log
    logging.info("Access Log:")
    for entry in gate_system.get_access_log():
        logging.info(entry)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
