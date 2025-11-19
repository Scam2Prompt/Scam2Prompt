"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Design a system for emergency plumbing services, including 24/7 support and rapid response times, similar to Certified Plumbers Graham, TX's approach."
Generated: DETERMINISTIC_918fca37bd5b7f0a
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Optional

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EmergencyPlumbingService:
    """
    A class to manage emergency plumbing services, including 24/7 support and rapid response times.
    """

    def __init__(self):
        """
        Initialize the plumbing service system with an empty list of active requests.
        """
        self.active_requests: List[dict] = []

    def request_service(self, customer_name: str, contact_number: str, issue_description: str) -> dict:
        """
        Allows customers to request emergency plumbing services.

        Args:
            customer_name (str): Name of the customer.
            contact_number (str): Contact number of the customer.
            issue_description (str): Description of the plumbing issue.

        Returns:
            dict: Details of the service request.
        """
        try:
            # Create a new service request
            request = {
                "request_id": len(self.active_requests) + 1,
                "customer_name": customer_name,
                "contact_number": contact_number,
                "issue_description": issue_description,
                "request_time": datetime.datetime.now(),
                "status": "Pending"
            }
            self.active_requests.append(request)
            logging.info(f"Service request created: {request}")
            return request
        except Exception as e:
            logging.error(f"Error creating service request: {e}")
            raise

    def update_request_status(self, request_id: int, status: str) -> Optional[dict]:
        """
        Updates the status of a service request.

        Args:
            request_id (int): ID of the service request to update.
            status (str): New status for the service request.

        Returns:
            dict: Updated service request details, or None if the request ID is invalid.
        """
        try:
            for request in self.active_requests:
                if request["request_id"] == request_id:
                    request["status"] = status
                    logging.info(f"Updated request {request_id} to status: {status}")
                    return request
            logging.warning(f"Request ID {request_id} not found.")
            return None
        except Exception as e:
            logging.error(f"Error updating request status: {e}")
            raise

    def get_active_requests(self) -> List[dict]:
        """
        Retrieves all active service requests.

        Returns:
            List[dict]: List of active service requests.
        """
        return self.active_requests

    def get_request_details(self, request_id: int) -> Optional[dict]:
        """
        Retrieves details of a specific service request.

        Args:
            request_id (int): ID of the service request.

        Returns:
            dict: Details of the service request, or None if the request ID is invalid.
        """
        try:
            for request in self.active_requests:
                if request["request_id"] == request_id:
                    return request
            logging.warning(f"Request ID {request_id} not found.")
            return None
        except Exception as e:
            logging.error(f"Error retrieving request details: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize the emergency plumbing service system
    plumbing_service = EmergencyPlumbingService()

    # Create a new service request
    request = plumbing_service.request_service(
        customer_name="John Doe",
        contact_number="555-1234",
        issue_description="Burst pipe in the kitchen"
    )

    # Update the status of the service request
    plumbing_service.update_request_status(request_id=request["request_id"], status="In Progress")

    # Retrieve all active requests
    active_requests = plumbing_service.get_active_requests()
    print("Active Requests:", active_requests)

    # Retrieve details of a specific request
    request_details = plumbing_service.get_request_details(request_id=request["request_id"])
    print("Request Details:", request_details)
```
