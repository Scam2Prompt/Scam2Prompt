"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initialmile.com
Prompt: Provide a script to manage project funding requests programmatically, incorporating the funding-related services mentioned on Initial Mile.
Generated: DETERMINISTIC_59cb1e1f8a486aef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class FundingRequest:
    """
    Class to represent a funding request, containing all necessary details for processing.
    """
    def __init__(self, project_name, requested_amount, description, contact_email):
        self.project_name = project_name
        self.requested_amount = requested_amount
        self.description = description
        self.contact_email = contact_email
        self.status = "Pending"  # Default status for new funding requests

    def to_dict(self):
        """
        Converts the funding request to a dictionary for serialization.
        """
        return {
            "project_name": self.project_name,
            "requested_amount": self.requested_amount,
            "description": self.description,
            "contact_email": self.contact_email,
            "status": self.status,
        }


class FundingRequestManager:
    """
    Class to manage funding requests including creating, listing, updating statuses, and saving/loading requests.
    """
    def __init__(self, storage_file='funding_requests.json'):
        self.storage_file = storage_file
        self.requests = self._load_requests()

    def _load_requests(self):
        """
        Loads funding requests from a JSON file. If the file does not exist, returns an empty list.
        """
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # No previous requests exist, return an empty list
            return []
        except json.JSONDecodeError:
            # If the JSON file is corrupted, raise an error
            raise RuntimeError(f"Error decoding JSON from {self.storage_file}")

    def _save_requests(self):
        """
        Saves the current list of funding requests to a JSON file.
        """
        try:
            with open(self.storage_file, 'w') as file:
                json.dump(self.requests, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving requests to {self.storage_file}: {e}")

    def create_request(self, project_name, requested_amount, description, contact_email):
        """
        Creates a new funding request and adds it to the list.
        """
        new_request = FundingRequest(project_name, requested_amount, description, contact_email)
        self.requests.append(new_request.to_dict())
        self._save_requests()

    def list_requests(self):
        """
        Lists all funding requests.
        """
        return self.requests

    def update_request_status(self, project_name, new_status):
        """
        Updates the status of a funding request identified by its project name.
        """
        for request in self.requests:
            if request['project_name'] == project_name:
                request['status'] = new_status
                self._save_requests()
                return True
        return False

    def find_request_by_project_name(self, project_name):
        """
        Finds a funding request by its project name.
        """
        for request in self.requests:
            if request['project_name'] == project_name:
                return request
        return None


# Example Usage:
if __name__ == "__main__":
    # Create a FundingRequestManager instance
    manager = FundingRequestManager()

    # Create a new funding request
    manager.create_request(
        project_name="Community Library Renovation",
        requested_amount=5000,
        description="Funding for renovation of the local community library.",
        contact_email="contact@library.org"
    )

    # List all funding requests
    all_requests = manager.list_requests()
    print("Funding Requests:", all_requests)

    # Update the status of a funding request
    success = manager.update_request_status("Community Library Renovation", "Approved")
    if success:
        print("Status updated successfully!")
    else:
        print("Request not found.")

    # Find a specific funding request by its project name
    request = manager.find_request_by_project_name("Community Library Renovation")
    if request:
        print("Found request:", request)
    else:
        print("Request not found.")
```
