"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Provide code examples for implementing a 24-hour service scheduling system for water pipeline maintenance, inspired by Aktiv Rørteknikk AS's round-the-clock service model.
Generated: DETERMINISTIC_f72812eb8687f006
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import logging
from typing import List, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceRequest:
    """Class to represent a service request for water pipeline maintenance."""
    
    def __init__(self, request_id: int, description: str, requested_time: datetime):
        self.request_id = request_id
        self.description = description
        self.requested_time = requested_time
        self.status = 'Pending'  # Initial status of the service request

    def __repr__(self):
        return f"ServiceRequest(id={self.request_id}, description='{self.description}', status='{self.status}')"


class ServiceScheduler:
    """Class to manage the scheduling of service requests."""
    
    def __init__(self):
        self.requests: List[ServiceRequest] = []  # List to hold service requests

    def add_request(self, description: str, requested_time: Optional[datetime] = None) -> ServiceRequest:
        """Add a new service request to the scheduler."""
        if requested_time is None:
            requested_time = datetime.now()  # Default to current time if not provided
        
        request_id = len(self.requests) + 1  # Simple ID generation
        new_request = ServiceRequest(request_id, description, requested_time)
        self.requests.append(new_request)
        logging.info(f"Added new service request: {new_request}")
        return new_request

    def process_requests(self):
        """Process all pending service requests."""
        for request in self.requests:
            if request.status == 'Pending':
                self.handle_request(request)

    def handle_request(self, request: ServiceRequest):
        """Handle a specific service request."""
        try:
            # Simulate request handling
            logging.info(f"Processing request: {request}")
            # Here you would implement the actual maintenance logic
            request.status = 'Completed'  # Update status after processing
            logging.info(f"Completed request: {request}")
        except Exception as e:
            logging.error(f"Error processing request {request.request_id}: {e}")
            request.status = 'Failed'  # Update status on failure

    def get_pending_requests(self) -> List[ServiceRequest]:
        """Return a list of pending service requests."""
        return [request for request in self.requests if request.status == 'Pending']


# Example usage
if __name__ == "__main__":
    scheduler = ServiceScheduler()
    
    # Adding service requests
    scheduler.add_request("Fix leak in main pipeline")
    scheduler.add_request("Inspect water quality", datetime.now() + timedelta(hours=1))
    
    # Process all requests
    scheduler.process_requests()
    
    # Display pending requests
    pending_requests = scheduler.get_pending_requests()
    logging.info(f"Pending requests: {pending_requests}")
```
