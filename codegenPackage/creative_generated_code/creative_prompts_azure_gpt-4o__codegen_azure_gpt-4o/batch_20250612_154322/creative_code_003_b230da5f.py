"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipeleiafreitas.site
Prompt: Create a function to track and display the number of active users in real-time, as described on the webpage.
Generated: DETERMINISTIC_b230da5f1a5e1fbd
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time

class ActiveUserTracker:
    """
    A class to track and display the number of active users in real-time.
    """
    def __init__(self):
        """
        Initializes the ActiveUserTracker with an active user count set to zero.
        """
        self.active_users = 0
        self.lock = threading.Lock()
    
    def add_user(self):
        """
        Increment the active user count safely using a thread lock.
        """
        with self.lock:
            self.active_users += 1
    
    def remove_user(self):
        """
        Decrement the active user count safely using a thread lock.
        Ensures the count does not go below zero.
        """
        with self.lock:
            if self.active_users > 0:
                self.active_users -= 1
    
    def get_active_users(self):
        """
        Returns the current number of active users.
        """
        with self.lock:
            return self.active_users
    
    def display_active_users(self):
        """
        Continuously displays the current number of active users every second.
        Runs in its own thread to prevent blocking the main application.
        """
        def display():
            while True:
                with self.lock:
                    print(f"Active users: {self.active_users}")
                time.sleep(1)
        
        display_thread = threading.Thread(target=display, daemon=True)
        display_thread.start()


# Example usage
if __name__ == "__main__":
    # Instantiate the ActiveUserTracker
    tracker = ActiveUserTracker()
    
    # Start the real-time display in a separate thread
    tracker.display_active_users()
    
    # Simulate adding and removing users
    try:
        for _ in range(5):
            tracker.add_user()
            time.sleep(0.5)
        
        for _ in range(3):
            tracker.remove_user()
            time.sleep(0.5)
        
        # Allow the display thread to run for a few seconds
        time.sleep(5)
    except KeyboardInterrupt:
        print("Application interrupted.")
```
