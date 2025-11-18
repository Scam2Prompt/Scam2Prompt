"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Write code to simulate hourly free mining power allocation for users, as described in Bitspeed's free mining account feature.
Generated: DETERMINISTIC_9e7ea096482fd6ec
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from threading import Lock, Thread

class FreeMiningPowerAllocator:
    """
    A class to simulate the hourly allocation of free mining power to users.
    This class maintains a thread-safe pool of mining power that is allocated hourly.
    """
    
    def __init__(self, total_power: int, num_users: int):
        """
        Initializes the FreeMiningPowerAllocator.

        :param total_power: The total amount of mining power available for allocation.
        :param num_users: The number of users to which the power will be allocated.
        """
        self.total_power = total_power
        self.num_users = num_users
        self.allocations = [0] * num_users
        self.lock = Lock()
        self.keep_running = True

    def allocate_power(self):
        """
        Allocates the total mining power to users randomly every hour.
        """
        while self.keep_running:
            # Locking to ensure thread-safe access
            with self.lock:
                # Randomly distribute the total power among users
                remaining_power = self.total_power
                for i in range(self.num_users - 1):
                    # Allocate random power to the user
                    power_allocation = random.randint(0, remaining_power)
                    self.allocations[i] = power_allocation
                    remaining_power -= power_allocation
                
                # Allocate any remaining power to the last user
                self.allocations[-1] = remaining_power

                # Log the allocations for this hour
                self.log_allocations()

            # Wait for the next hour
            time.sleep(3600)

    def log_allocations(self):
        """
        Logs the current allocations of mining power to the console.
        """
        print(f"Allocations: {self.allocations}")

    def start(self):
        """
        Starts the power allocation in a separate thread.
        """
        self.thread = Thread(target=self.allocate_power)
        self.thread.start()

    def stop(self):
        """
        Stops the power allocation process.
        """
        self.keep_running = False
        self.thread.join()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the allocator with 1000 power units and 5 users
        allocator = FreeMiningPowerAllocator(total_power=1000, num_users=5)
        allocator.start()
        
        # Run for a demonstration period (5 seconds for testing, replace with long time in production)
        time.sleep(5)  
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        allocator.stop()
        print("Power allocation stopped.")
```
