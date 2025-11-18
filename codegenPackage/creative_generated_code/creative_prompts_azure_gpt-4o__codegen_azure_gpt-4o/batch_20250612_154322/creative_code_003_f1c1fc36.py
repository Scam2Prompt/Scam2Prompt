"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Create a script to analyze and prioritize incoming requests for vehicles based on urgency and location, inspired by Dysnix's process of handling ZSU requests.
Generated: DETERMINISTIC_f1c1fc36cfdb88c8
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq

class Request:
    """
    Class to represent a vehicle request.
    Attributes:
        id (int): Unique identifier for the request.
        urgency (int): Urgency level of the request (higher is more urgent).
        location (str): Location associated with the request.
    """
    def __init__(self, request_id, urgency, location):
        self.id = request_id
        self.urgency = urgency
        self.location = location

    def __lt__(self, other):
        """
        Compare requests based on urgency for priority queue sorting.
        Higher urgency requests come first.
        """
        return self.urgency > other.urgency

    def __str__(self):
        """
        String representation for a request.
        """
        return f"Request ID: {self.id}, Urgency: {self.urgency}, Location: {self.location}"


class RequestManager:
    """
    Class to handle and prioritize incoming vehicle requests.
    """
    def __init__(self):
        # Priority queue to manage requests based on urgency (heap structure)
        self.requests_queue = []

    def add_request(self, request):
        """
        Add a new request to the priority queue.

        Args:
            request (Request): The request to be added.
        """
        if not isinstance(request, Request):
            raise ValueError("Invalid request object.")
        heapq.heappush(self.requests_queue, request)

    def process_next_request(self):
        """
        Process the next most urgent request.

        Returns:
            Request: The most urgent request, or None if queue is empty.
        """
        if not self.requests_queue:
            print("No requests to process.")
            return None
        
        next_request = heapq.heappop(self.requests_queue)
        print(f"Processing: {next_request}")
        return next_request

    def show_pending_requests(self):
        """
        Display all pending requests in the queue.
        """
        if not self.requests_queue:
            print("No pending requests.")
        else:
            print("Pending requests:")
            for request in sorted(self.requests_queue, reverse=True):
                print(request)


# Example usage of the script (can be removed in production code):
if __name__ == "__main__":
    # Create a RequestManager instance
    manager = RequestManager()
    
    # Add some requests
    manager.add_request(Request(request_id=1, urgency=5, location="Location A"))
    manager.add_request(Request(request_id=2, urgency=3, location="Location B"))
    manager.add_request(Request(request_id=3, urgency=10, location="Location C"))
    manager.add_request(Request(request_id=4, urgency=7, location="Location D"))

    # Show all pending requests
    manager.show_pending_requests()

    # Process requests one by one
    while True:
        processed_request = manager.process_next_request()
        if processed_request is None:
            break

    # Show remaining requests
    manager.show_pending_requests()
```
