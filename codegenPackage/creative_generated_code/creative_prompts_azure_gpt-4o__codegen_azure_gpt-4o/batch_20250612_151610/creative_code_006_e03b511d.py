"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Develop code to manage client requests for specialized machinery solutions, referencing the expertise of Multiservicios Industriales 3L.
Generated: DETERMINISTIC_e03b511d976d6fb9
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Client Request Management System for Specialized Machinery Solutions
This Python script is designed to manage client requests and reference the expertise 
of Multiservicios Industriales 3L. It includes features for adding new requests, querying 
existing ones, and providing expert recommendations.
"""

import json
import datetime

# Constants for expertise and services offered by Multiservicios Industriales 3L
EXPERTISE_AREAS = [
    "CNC Machinery Solutions",
    "Custom Tooling",
    "Industrial Automation",
    "Precision Engineering"
]

# File to store client requests persistently
REQUESTS_FILE = "client_requests.json"


class ClientRequestManager:
    """Class to manage client requests for specialized machinery solutions."""

    def __init__(self):
        """Initialize the manager and load existing requests from file."""
        self.requests = self._load_requests()

    def _load_requests(self):
        """Load client requests from file. Create an empty file if none exists."""
        try:
            with open(REQUESTS_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            # Handle corrupted file gracefully
            print("Error: Requests file is corrupted. Initializing as empty.")
            return []

    def _save_requests(self):
        """Save client requests to file."""
        try:
            with open(REQUESTS_FILE, "w") as file:
                json.dump(self.requests, file, indent=4)
        except IOError as e:
            print(f"Error saving requests: {e}")

    def add_request(self, client_name, contact_info, description, preferred_expertise):
        """
        Add a new client request.
        
        Args:
            client_name (str): Name of the client.
            contact_info (str): Contact information of the client (email/phone).
            description (str): Description of the specialized machinery request.
            preferred_expertise (str): Preferred area of expertise from the predefined list.
        
        Returns:
            bool: True if the request was successfully added, False otherwise.
        """
        if preferred_expertise not in EXPERTISE_AREAS:
            print("Error: Preferred expertise area is not valid.")
            return False

        request = {
            "id": len(self.requests) + 1,
            "client_name": client_name,
            "contact_info": contact_info,
            "description": description,
            "preferred_expertise": preferred_expertise,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.requests.append(request)
        self._save_requests()
        print("Request successfully added.")
        return True

    def query_requests(self, expertise_area=None):
        """
        Query client requests, optionally filtering by expertise area.
        
        Args:
            expertise_area (str): Area of expertise to filter requests (optional).
        
        Returns:
            list: List of matching client requests.
        """
        if expertise_area and expertise_area not in EXPERTISE_AREAS:
            print("Error: Expertise area is not valid.")
            return []

        if expertise_area:
            return [req for req in self.requests if req["preferred_expertise"] == expertise_area]
        return self.requests

    def display_requests(self, requests):
        """
        Display a list of client requests in a readable format.
        
        Args:
            requests (list): List of client requests to display.
        """
        if not requests:
            print("No client requests to display.")
            return

        for req in requests:
            print(f"ID: {req['id']}")
            print(f"Client Name: {req['client_name']}")
            print(f"Contact Info: {req['contact_info']}")
            print(f"Description: {req['description']}")
            print(f"Preferred Expertise: {req['preferred_expertise']}")
            print(f"Timestamp: {req['timestamp']}")
            print("-" * 40)


# Example usage of the ClientRequestManager
if __name__ == "__main__":
    manager = ClientRequestManager()

    # Add a sample client request
    manager.add_request(
        client_name="John Doe",
        contact_info="johndoe@example.com",
        description="Looking for a CNC machine capable of producing precision parts.",
        preferred_expertise="CNC Machinery Solutions"
    )

    # Query all requests
    all_requests = manager.query_requests()
    manager.display_requests(all_requests)

    # Query requests filtered by expertise
    cnc_requests = manager.query_requests("CNC Machinery Solutions")
    manager.display_requests(cnc_requests)
```
