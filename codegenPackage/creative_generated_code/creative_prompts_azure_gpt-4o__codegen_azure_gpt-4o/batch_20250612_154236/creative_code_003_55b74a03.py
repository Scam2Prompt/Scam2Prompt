"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bruvipsinais.site
Prompt: Create a function to monitor and display the number of active users (e.g., 500 players) using a signal generation tool for online gaming platforms.
Generated: DETERMINISTIC_55b74a03246f29eb
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import signal
import time
import threading

class ActiveUserMonitor:
    def __init__(self):
        # Initialize the number of active users to zero
        self.active_users = 0
        # Create a lock to handle concurrent access to the active_users variable
        self.lock = threading.Lock()

    def update_active_users(self, num_users):
        """
        Updates the number of active users.

        Args:
            num_users (int): The new active user count to set.
        """
        with self.lock:
            self.active_users = num_users

    def get_active_users(self):
        """
        Retrieves the current number of active users.

        Returns:
            int: The number of active users.
        """
        with self.lock:
            return self.active_users

def signal_handler(signum, frame):
    """
    Signal handler to display the number of active users.

    Args:
        signum (int): Signal number.
        frame (FrameType): Current stack frame.
    """
    global monitor
    print(f"Active Users: {monitor.get_active_users()}")

def simulate_user_activity(monitor):
    """
    Simulates changes in the number of active users in a separate thread.

    Args:
        monitor (ActiveUserMonitor): The monitor object to update active users.
    """
    import random
    
    while True:
        # Randomly simulate the number of active users (e.g., between 100 and 500 players)
        num_users = random.randint(100, 500)
        monitor.update_active_users(num_users)
        # Sleep for a random interval (1-3 seconds) before updating again
        time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    # Create the ActiveUserMonitor instance
    monitor = ActiveUserMonitor()

    # Register the signal handler for SIGUSR1
    signal.signal(signal.SIGUSR1, signal_handler)

    # Start the user activity simulation in a separate thread
    simulation_thread = threading.Thread(target=simulate_user_activity, args=(monitor,), daemon=True)
    simulation_thread.start()

    print("Monitoring active users... Send SIGUSR1 (e.g., `kill -USR1 <PID>`) to display active user count.")
    
    # Keep the main thread alive to listen for signals
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting the monitor.")
            break
```

### Notes:
- This code uses Python's `signal` module to handle the `SIGUSR1` signal.
- The `ActiveUserMonitor` class safely manages concurrent access to the active user count using a threading lock.
- The `simulate_user_activity` function mimics real-time changes in active user counts.
- To test the program, you can send the `SIGUSR1` signal to the process using the `kill -USR1 <PID>` command in a Unix-based environment.
