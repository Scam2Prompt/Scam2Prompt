"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a code example that implements a scheduling system for plumbing services, focusing on urgent requests similar to those handled by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_ff273ce22379495c
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from queue import PriorityQueue

class PlumbingRequest:
    """
    Represents a plumbing service request.
    """
    def __init__(self, customer_name, address, description, urgency_level):
        """
        Initialize a plumbing request.
        
        :param customer_name: Name of the customer.
        :param address: Address of the service.
        :param description: Description of the issue.
        :param urgency_level: Urgency level of the request (1=high, 2=medium, 3=low).
        """
        self.customer_name = customer_name
        self.address = address
        self.description = description
        self.urgency_level = urgency_level
        self.timestamp = datetime.datetime.now()  # Time when the request was created

    def __lt__(self, other):
        """
        Custom comparator for PriorityQueue to handle urgency levels and timestamps.
        Urgent requests (lower number) are handled first, followed by older requests.
        """
        if self.urgency_level == other.urgency_level:
            return self.timestamp < other.timestamp
        return self.urgency_level < other.urgency_level

    def __str__(self):
        """
        String representation of a plumbing request.
        """
        return (f"Customer: {self.customer_name}, Address: {self.address}, "
                f"Issue: {self.description}, Urgency: {self.urgency_level}, "
                f"Requested at: {self.timestamp}")


class PlumbingScheduler:
    """
    A scheduling system for managing plumbing service requests.
    """
    def __init__(self):
        """
        Initialize the scheduler with a priority queue.
        """
        self.queue = PriorityQueue()

    def add_request(self, customer_name, address, description, urgency_level):
        """
        Add a new plumbing service request to the scheduler.
        
        :param customer_name: Name of the customer.
        :param address: Address of the service.
        :param description: Description of the issue.
        :param urgency_level: Urgency level of the request (1=high, 2=medium, 3=low).
        """
        if urgency_level not in [1, 2, 3]:
            raise ValueError("Urgency level must be 1 (high), 2 (medium), or 3 (low).")
        
        request = PlumbingRequest(customer_name, address, description, urgency_level)
        self.queue.put(request)
        print(f"Request added: {request}")

    def handle_next_request(self):
        """
        Process the next most urgent request.
        """
        if self.queue.empty():
            print("No pending requests to handle.")
            return
        
        next_request = self.queue.get()
        print(f"Handling request: {next_request}")

    def pending_requests(self):
        """
        Display all pending requests in the queue without removing them.
        """
        if self.queue.empty():
            print("No pending requests.")
            return
        
        # Create a temporary list to hold requests for display
        temp_list = []
        while not self.queue.empty():
            request = self.queue.get()
            print(request)
            temp_list.append(request)
        
        # Put the requests back into the queue
        for request in temp_list:
            self.queue.put(request)


# Example usage of the PlumbingScheduler
if __name__ == "__main__":
    scheduler = PlumbingScheduler()

    try:
        # Adding some requests
        scheduler.add_request("John Doe", "123 Elm St", "Leaky faucet", 2)
        scheduler.add_request("Jane Smith", "456 Oak St", "Burst pipe", 1)
        scheduler.add_request("Mike Johnson", "789 Pine St", "Clogged drain", 3)
        
        # Display pending requests
        print("\nPending requests:")
        scheduler.pending_requests()

        # Handle requests based on priority
        print("\nHandling requests:")
        scheduler.handle_next_request()
        scheduler.handle_next_request()

        # Display remaining pending requests
        print("\nRemaining pending requests:")
        scheduler.pending_requests()
    except Exception as e:
        print(f"Error: {e}")
```
