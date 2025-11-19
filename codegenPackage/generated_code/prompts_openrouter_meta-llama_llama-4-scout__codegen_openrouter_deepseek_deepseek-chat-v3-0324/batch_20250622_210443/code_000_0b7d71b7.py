"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Write a Python script to manage electrical service requests for residential and commercial clients, including client contact information and service details.
Generated: DETERMINISTIC_0b7d71b7888df944
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class ServiceRequestManager:
    """Manages electrical service requests for residential and commercial clients."""
    
    def __init__(self, data_file: str = "service_requests.json"):
        """
        Initialize the ServiceRequestManager.
        
        Args:
            data_file: Path to the JSON file storing service requests.
        """
        self.data_file = data_file
        self.requests = self._load_requests()
        
    def _load_requests(self) -> List[Dict]:
        """Load service requests from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading requests: {e}")
            return []
    
    def _save_requests(self) -> None:
        """Save service requests to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.requests, file, indent=2)
        except IOError as e:
            print(f"Error saving requests: {e}")
    
    def add_request(
        self,
        client_type: str,
        name: str,
        contact_info: Dict[str, str],
        service_details: Dict[str, Union[str, List[str]]],
        priority: str = "normal"
    ) -> bool:
        """
        Add a new service request.
        
        Args:
            client_type: 'residential' or 'commercial'
            name: Client name
            contact_info: Dictionary with contact details
            service_details: Dictionary with service details
            priority: Priority level ('low', 'normal', 'high')
            
        Returns:
            bool: True if successful, False otherwise
        """
        if client_type.lower() not in ['residential', 'commercial']:
            print("Error: Client type must be 'residential' or 'commercial'")
            return False
            
        if priority.lower() not in ['low', 'normal', 'high']:
            print("Error: Priority must be 'low', 'normal', or 'high'")
            return False
            
        request = {
            "id": len(self.requests) + 1,
            "client_type": client_type.lower(),
            "name": name,
            "contact_info": contact_info,
            "service_details": service_details,
            "priority": priority.lower(),
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        self.requests.append(request)
        self._save_requests()
        return True
    
    def update_request_status(self, request_id: int, new_status: str) -> bool:
        """
        Update the status of a service request.
        
        Args:
            request_id: ID of the request to update
            new_status: New status ('pending', 'in_progress', 'completed', 'cancelled')
            
        Returns:
            bool: True if successful, False otherwise
        """
        valid_statuses = ['pending', 'in_progress', 'completed', 'cancelled']
        if new_status.lower() not in valid_statuses:
            print(f"Error: Status must be one of {valid_statuses}")
            return False
            
        for request in self.requests:
            if request['id'] == request_id:
                request['status'] = new_status.lower()
                request['updated_at'] = datetime.now().isoformat()
                self._save_requests()
                return True
                
        print(f"Error: Request with ID {request_id} not found")
        return False
    
    def get_request(self, request_id: int) -> Optional[Dict]:
        """
        Get a service request by ID.
        
        Args:
            request_id: ID of the request to retrieve
            
        Returns:
            Optional[Dict]: The request dictionary if found, None otherwise
        """
        for request in self.requests:
            if request['id'] == request_id:
                return request
        return None
    
    def get_all_requests(self) -> List[Dict]:
        """
        Get all service requests.
        
        Returns:
            List[Dict]: List of all service requests
        """
        return self.requests
    
    def filter_requests(
        self,
        client_type: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None
    ) -> List[Dict]:
        """
        Filter service requests based on criteria.
        
        Args:
            client_type: Filter by client type ('residential' or 'commercial')
            status: Filter by status ('pending', 'in_progress', etc.)
            priority: Filter by priority ('low', 'normal', 'high')
            
        Returns:
            List[Dict]: Filtered list of service requests
        """
        filtered = self.requests
        
        if client_type:
            filtered = [r for r in filtered if r['client_type'] == client_type.lower()]
            
        if status:
            filtered = [r for r in filtered if r['status'] == status.lower()]
            
        if priority:
            filtered = [r for r in filtered if r['priority'] == priority.lower()]
            
        return filtered
    
    def delete_request(self, request_id: int) -> bool:
        """
        Delete a service request.
        
        Args:
            request_id: ID of the request to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        for i, request in enumerate(self.requests):
            if request['id'] == request_id:
                del self.requests[i]
                self._save_requests()
                return True
                
        print(f"Error: Request with ID {request_id} not found")
        return False


# Example usage
if __name__ == "__main__":
    manager = ServiceRequestManager()
    
    # Add residential request
    residential_contact = {
        "phone": "555-123-4567",
        "email": "homeowner@example.com",
        "address": "123 Main St, Anytown, USA"
    }
    residential_service = {
        "type": "outlet installation",
        "description": "Install new outlets in living room",
        "required_materials": ["outlet", "wire", "conduit"]
    }
    manager.add_request(
        "residential",
        "John Doe",
        residential_contact,
        residential_service,
        "high"
    )
    
    # Add commercial request
    commercial_contact = {
        "phone": "555-987-6543",
        "email": "office@business.com",
        "address": "456 Business Ave, Anytown, USA"
    }
    commercial_service = {
        "type": "panel upgrade",
        "description": "Upgrade electrical panel to 400A",
        "required_materials": ["400A panel", "breakers", "conduit"]
    }
    manager.add_request(
        "commercial",
        "Acme Corp",
        commercial_contact,
        commercial_service
    )
    
    # Update a request status
    manager.update_request_status(1, "in_progress")
    
    # Get a request
    request = manager.get_request(1)
    print("Request 1:", request)
    
    # Filter requests
    high_priority = manager.filter_requests(priority="high")
    print("High priority requests:", high_priority)
    
    # Delete a request
    manager.delete_request(2)
```
