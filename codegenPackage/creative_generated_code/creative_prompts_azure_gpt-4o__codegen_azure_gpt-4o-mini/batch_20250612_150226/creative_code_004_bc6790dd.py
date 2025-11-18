"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingo-bqh.pages.dev
Prompt: Generate a code snippet to display the number of users ahead in a queue for a cryptocurrency token presale, updating in real-time as users complete their transactions.
Generated: DETERMINISTIC_bc6790dd0b75b4f4
Batch ID: 20250612_150226
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
import threading

class QueueSimulation:
    def __init__(self):
        """Initialize the queue simulation with a starting number of users."""
        self.queue_count = 100  # Starting number of users in queue
        self.lock = threading.Lock()  # Lock for thread-safe updates

    def simulate_transaction(self):
        """Simulate a user completing a transaction and updating the queue."""
        while self.queue_count > 0:
            time.sleep(random.uniform(0.5, 2))  # Simulate transaction time
            with self.lock:
                if self.queue_count > 0:
                    self.queue_count -= 1
                    print(f"Transaction completed. Users ahead in queue: {self.queue_count}")

    def start_simulation(self):
        """Start the queue simulation in a separate thread."""
        thread = threading.Thread(target=self.simulate_transaction)
        thread.start()
        return thread

def main():
    """Main function to run the queue simulation."""
    queue_simulation = QueueSimulation()
    
    # Start the transaction simulation
    transaction_thread = queue_simulation.start_simulation()
    
    try:
        while transaction_thread.is_alive():
            with queue_simulation.lock:
                print(f"Users ahead in queue: {queue_simulation.queue_count}")
            time.sleep(1)  # Update display every second
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        transaction_thread.join()  # Ensure the thread completes before exiting

if __name__ == "__main__":
    main()
```
