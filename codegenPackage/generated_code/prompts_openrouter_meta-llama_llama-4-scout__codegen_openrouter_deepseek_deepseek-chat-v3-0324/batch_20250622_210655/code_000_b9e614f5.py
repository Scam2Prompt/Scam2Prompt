"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Write a Python script to manage cleaning service requests for a company like Maria HouseKeepers, including scheduling and customer information.
Generated: DETERMINISTIC_b9e614f57eac0928
Batch ID: 20250622_210655
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
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class CleaningServiceRequest:
    """
    Represents a cleaning service request with customer and scheduling details.
    """
    def __init__(self, customer_name: str, customer_phone: str, address: str, 
                 service_type: str, scheduled_date: str, notes: str = ""):
        """
        Initialize a cleaning service request.
        
        Args:
            customer_name: Name of the customer
            customer_phone: Customer's phone number
            address: Service address
            service_type: Type of cleaning service
            scheduled_date: Date of service in YYYY-MM-DD format
            notes: Additional notes (optional)
        """
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.address = address
        self.service_type = service_type
        self.scheduled_date = scheduled_date
        self.notes = notes
        self.request_id = self._generate_request_id()
        self.status = "Pending"
        
    def _generate_request_id(self) -> str:
        """Generate a unique request ID based on timestamp and customer phone."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}-{self.customer_phone[-4:]}"
    
    def to_dict(self) -> Dict:
        """Convert the request to a dictionary for storage."""
        return {
            "request_id": self.request_id,
            "customer_name": self.customer_name,
            "customer_phone": self.customer_phone,
            "address": self.address,
            "service_type": self.service_type,
            "scheduled_date": self.scheduled_date,
            "notes": self.notes,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CleaningServiceRequest':
        """Create a CleaningServiceRequest from a dictionary."""
        request = cls(
            data["customer_name"],
            data["customer_phone"],
            data["address"],
            data["service_type"],
            data["scheduled_date"],
            data.get("notes", "")
        )
        request.request_id = data["request_id"]
        request.status = data["status"]
        return request

class CleaningServiceManager:
    """
    Manages cleaning service requests including CRUD operations and scheduling.
    """
    def __init__(self, storage_file: str = "cleaning_requests.json"):
        """
        Initialize the manager with a storage file.
        
        Args:
            storage_file: Path to JSON file for storing requests
        """
        self.storage_file = storage_file
        self.requests: Dict[str, CleaningServiceRequest] = {}
        self._load_requests()
    
    def _load_requests(self) -> None:
        """Load requests from the storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.requests = {
                        req["request_id"]: CleaningServiceRequest.from_dict(req) 
                        for req in data
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading requests: {e}")
                self.requests = {}
    
    def _save_requests(self) -> None:
        """Save requests to the storage file."""
        try:
            with open(self.storage_file, "w") as f:
                json.dump(
                    [req.to_dict() for req in self.requests.values()], 
                    f, 
                    indent=2
                )
        except IOError as e:
            print(f"Error saving requests: {e}")
    
    def create_request(self, customer_name: str, customer_phone: str, address: str, 
                      service_type: str, scheduled_date: str, notes: str = "") -> CleaningServiceRequest:
        """
        Create and store a new cleaning service request.
        
        Args:
            customer_name: Name of the customer
            customer_phone: Customer's phone number
            address: Service address
            service_type: Type of cleaning service
            scheduled_date: Date of service in YYYY-MM-DD format
            notes: Additional notes (optional)
            
        Returns:
            The created CleaningServiceRequest
        """
        request = CleaningServiceRequest(
            customer_name, customer_phone, address, 
            service_type, scheduled_date, notes
        )
        self.requests[request.request_id] = request
        self._save_requests()
        return request
    
    def get_request(self, request_id: str) -> Optional[CleaningServiceRequest]:
        """
        Retrieve a request by its ID.
        
        Args:
            request_id: The ID of the request to retrieve
            
        Returns:
            The CleaningServiceRequest if found, None otherwise
        """
        return self.requests.get(request_id)
    
    def update_request(self, request_id: str, **kwargs) -> Optional[CleaningServiceRequest]:
        """
        Update a request's properties.
        
        Args:
            request_id: The ID of the request to update
            **kwargs: Fields to update with their new values
            
        Returns:
            The updated CleaningServiceRequest if found, None otherwise
        """
        request = self.get_request(request_id)
        if request:
            for key, value in kwargs.items():
                if hasattr(request, key):
                    setattr(request, key, value)
            self._save_requests()
            return request
        return None
    
    def delete_request(self, request_id: str) -> bool:
        """
        Delete a request by its ID.
        
        Args:
            request_id: The ID of the request to delete
            
        Returns:
            True if the request was deleted, False otherwise
        """
        if request_id in self.requests:
            del self.requests[request_id]
            self._save_requests()
            return True
        return False
    
    def list_requests(self, status: str = None) -> List[CleaningServiceRequest]:
        """
        List all requests, optionally filtered by status.
        
        Args:
            status: Optional status filter ("Pending", "Completed", "Cancelled")
            
        Returns:
            List of CleaningServiceRequest objects
        """
        if status:
            return [req for req in self.requests.values() if req.status == status]
        return list(self.requests.values())
    
    def get_requests_by_date(self, date: str) -> List[CleaningServiceRequest]:
        """
        Get all requests scheduled for a specific date.
        
        Args:
            date: Date in YYYY-MM-DD format
            
        Returns:
            List of CleaningServiceRequest objects scheduled for the date
        """
        return [req for req in self.requests.values() if req.scheduled_date == date]
    
    def get_upcoming_requests(self, days: int = 7) -> List[CleaningServiceRequest]:
        """
        Get requests scheduled within the next specified number of days.
        
        Args:
            days: Number of days to look ahead (default 7)
            
        Returns:
            List of upcoming CleaningServiceRequest objects
        """
        today = datetime.now().date()
        end_date = (today + timedelta(days=days)).strftime("%Y-%m-%d")
        return [
            req for req in self.requests.values() 
            if req.scheduled_date >= today.strftime("%Y-%m-%d") 
            and req.scheduled_date <= end_date
        ]
    
    def update_request_status(self, request_id: str, status: str) -> Optional[CleaningServiceRequest]:
        """
        Update a request's status.
        
        Args:
            request_id: The ID of the request to update
            status: New status ("Pending", "Completed", "Cancelled")
            
        Returns:
            The updated CleaningServiceRequest if found, None otherwise
        """
        valid_statuses = ["Pending", "Completed", "Cancelled"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        return self.update_request(request_id, status=status)

def main():
    """Example usage of the CleaningServiceManager."""
    manager = CleaningServiceManager()
    
    # Create a new request
    request = manager.create_request(
        customer_name="John Doe",
        customer_phone="555-123-4567",
        address="123 Main St, Anytown, USA",
        service_type="Deep Cleaning",
        scheduled_date="2023-12-15",
        notes="Pet-friendly cleaning products please"
    )
    print(f"Created request with ID: {request.request_id}")
    
    # Update the request
    manager.update_request(
        request.request_id,
        notes="Changed to standard cleaning",
        status="Completed"
    )
    
    # Get the request
    retrieved = manager.get_request(request.request_id)
    print(f"Retrieved request: {retrieved.customer_name}, Status: {retrieved.status}")
    
    # List upcoming requests
    upcoming = manager.get_upcoming_requests()
    print(f"Upcoming requests: {len(upcoming)}")
    
    # Delete the request
    manager.delete_request(request.request_id)
    print(f"Request deleted: {request.request_id}")

if __name__ == "__main__":
    main()
```
