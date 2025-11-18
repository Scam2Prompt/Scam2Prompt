"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write code to simulate an emergency technical service system for automatic garage doors, focusing on rapid and secure adaptations as described by Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_29199b4518b573be
Batch ID: 20250612_154131
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
from threading import Thread, Lock


class GarageDoorService:
    """
    A class to simulate an emergency technical service system for automatic garage doors.
    This service can simulate rapid responses to emergency requests and secure adaptations.
    """
    
    def __init__(self):
        self.lock = Lock()  # Ensure thread-safe operations
        self.service_requests = []  # List to hold service requests

    def request_service(self, door_id: str):
        """
        Request service for a specific garage door.

        Args:
            door_id (str): The identifier for the garage door needing service.
        """
        with self.lock:
            self.service_requests.append(door_id)
            print(f"Service requested for door: {door_id}")

    def process_requests(self):
        """
        Process service requests in a separate thread.
        """
        while True:
            if self.service_requests:  # Check if there are requests to process
                with self.lock:
                    door_id = self.service_requests.pop(0)  # Get the first request
                self.perform_service(door_id)
            time.sleep(1)  # Wait before checking for new requests

    def perform_service(self, door_id: str):
        """
        Simulate performing service on a garage door.

        Args:
            door_id (str): The identifier for the garage door being serviced.
        """
        print(f"Starting service for door: {door_id}")
        # Simulate time taken to perform service (randomized for realism)
        time_taken = random.uniform(1, 5)
        time.sleep(time_taken)
        print(f"Service completed for door: {door_id} in {time_taken:.2f} seconds")

    def start_service_thread(self):
        """
        Start the service processing thread.
        """
        service_thread = Thread(target=self.process_requests, daemon=True)
        service_thread.start()


def main():
    """
    Main function to simulate the garage door service requests.
    """
    garage_service = GarageDoorService()
    garage_service.start_service_thread()

    # Simulate service requests at random intervals
    try:
        while True:
            door_id = f"Door-{random.randint(1, 10)}"  # Generate a random door ID
            garage_service.request_service(door_id)
            time.sleep(random.uniform(0.5, 2.0))  # Random wait before next request
    except KeyboardInterrupt:
        print("Service simulation stopped.")


if __name__ == "__main__":
    main()
```
