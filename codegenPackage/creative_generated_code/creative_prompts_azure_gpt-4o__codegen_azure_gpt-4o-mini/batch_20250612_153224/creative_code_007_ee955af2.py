"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Write a program to monitor and control access to premises using gate automation systems, incorporating features described by Donture Systems Ltd.
Generated: DETERMINISTIC_ee955af266579431
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class GateAutomationSystem:
    def __init__(self):
        self.access_log = []
        self.is_gate_open = False

    def log_access(self, user_id, action):
        """Log access attempts with user ID and action."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.access_log.append({'timestamp': timestamp, 'user_id': user_id, 'action': action})

    def check_access(self, user_id):
        """Simulate user access check (in real scenarios, this could call a database)."""
        return random.choice([True, False])  # Randomly allow or deny access for simulation purposes

    def open_gate(self, user_id):
        """Open the gate if access is granted."""
        if self.check_access(user_id):
            self.is_gate_open = True
            self.log_access(user_id, 'Opened Gate')
            print(f"Gate opened for user: {user_id}")
            time.sleep(2)  # Simulate time the gate is open
            self.close_gate()
        else:
            self.log_access(user_id, 'Access Denied')
            print(f"Access denied for user: {user_id}")

    def close_gate(self):
        """Close the gate."""
        self.is_gate_open = False
        print("Gate closed.")

    def display_access_log(self):
        """Display the access log."""
        print("Access Log:")
        for entry in self.access_log:
            print(f"{entry['timestamp']} - User: {entry['user_id']}, Action: {entry['action']}")

def main():
    """Main function to run the gate automation system."""
    gate_system = GateAutomationSystem()
    
    # Example user IDs
    user_ids = ['user_01', 'user_02', 'user_03']

    # Simulate access attempts
    for user_id in user_ids:
        gate_system.open_gate(user_id)
        time.sleep(1)  # Wait between attempts

    # Display the access log at the end
    gate_system.display_access_log()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
