"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastfair.com
Prompt: Write code to implement continuous support functionality for architectural projects, inspired by Études Architectural Solutions.
Generated: DETERMINISTIC_894a0c7a71d3e77a
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ArchitecturalSupport:
    def __init__(self):
        """Initializes the ArchitecturalSupport class with an empty support requests list."""
        self.support_requests: List[Dict[str, Any]] = []

    def create_support_request(self, project_name: str, description: str, priority: str) -> None:
        """
        Creates a new support request.

        Args:
            project_name (str): The name of the architectural project.
            description (str): A detailed description of the support needed.
            priority (str): The priority level of the support request (e.g., 'low', 'medium', 'high').

        Raises:
            ValueError: If priority is not one of the predefined levels.
        """
        if priority not in ['low', 'medium', 'high']:
            logging.error("Invalid priority level: %s", priority)
            raise ValueError("Priority must be 'low', 'medium', or 'high'.")

        request = {
            'project_name': project_name,
            'description': description,
            'priority': priority,
            'timestamp': datetime.utcnow(),
            'status': 'open'
        }
        self.support_requests.append(request)
        logging.info("New support request created: %s", request)

    def list_support_requests(self) -> List[Dict[str, Any]]:
        """Returns a list of all support requests."""
        logging.info("Listing all support requests.")
        return self.support_requests

    def close_support_request(self, request_id: int) -> None:
        """
        Closes a support request by its index.

        Args:
            request_id (int): The index of the support request to be closed.

        Raises:
            IndexError: If the request_id is out of range.
        """
        try:
            self.support_requests[request_id]['status'] = 'closed'
            logging.info("Support request closed: %s", self.support_requests[request_id])
        except IndexError:
            logging.error("Invalid request ID: %d", request_id)
            raise IndexError("Support request ID is out of range.")

    def get_open_requests(self) -> List[Dict[str, Any]]:
        """Returns a list of open support requests."""
        open_requests = [req for req in self.support_requests if req['status'] == 'open']
        logging.info("Retrieved open support requests: %d found", len(open_requests))
        return open_requests

    def get_request_by_project(self, project_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves support requests associated with a specific project.

        Args:
            project_name (str): The name of the project to filter requests.

        Returns:
            List[Dict[str, Any]]: A list of support requests for the specified project.
        """
        filtered_requests = [req for req in self.support_requests if req['project_name'] == project_name]
        logging.info("Retrieved support requests for project '%s': %d found", project_name, len(filtered_requests))
        return filtered_requests

# Example usage
if __name__ == "__main__":
    support_system = ArchitecturalSupport()
    
    try:
        support_system.create_support_request("Project A", "Need assistance with design layout.", "high")
        support_system.create_support_request("Project B", "Looking for material recommendations.", "medium")
        support_system.create_support_request("Project A", "Clarification on building codes.", "low")
        
        logging.info("All Support Requests: %s", support_system.list_support_requests())
        
        open_requests = support_system.get_open_requests()
        
        support_system.close_support_request(1)  # Closing the second request
        logging.info("After closing a request: %s", support_system.list_support_requests())
        
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
```
