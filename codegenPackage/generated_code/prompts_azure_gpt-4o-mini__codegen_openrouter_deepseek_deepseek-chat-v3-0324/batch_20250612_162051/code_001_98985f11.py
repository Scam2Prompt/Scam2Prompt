"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Write a Python script that integrates with an API to manage service requests for water leakage detection, inspired by the techniques used by شركة انجاز.
Generated: DETERMINISTIC_98985f11b9ce89e7
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.waterleakage.example.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime
from typing import Dict, Optional, List

class WaterLeakageService:
    """
    A class to manage water leakage detection service requests via API.
    Inspired by شركة انجاز techniques.
    """

    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the WaterLeakageService with API credentials.

        Args:
            api_base_url (str): Base URL of the water leakage service API
            api_key (str): API key for authentication
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.timeout = 30  # seconds

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests with error handling.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (Optional[Dict]): Request payload

        Returns:
            Dict: Response from API

        Raises:
            ValueError: If the request fails
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")

    def create_service_request(
        self,
        customer_name: str,
        location: str,
        contact_number: str,
        description: str,
        priority: str = "medium"
    ) -> Dict:
        """
        Create a new water leakage service request.

        Args:
            customer_name (str): Name of the customer
            location (str): Location of the leakage
            contact_number (str): Customer contact number
            description (str): Description of the issue
            priority (str): Priority level (low, medium, high)

        Returns:
            Dict: Created service request details
        """
        valid_priorities = ["low", "medium", "high"]
        if priority.lower() not in valid_priorities:
            raise ValueError(f"Invalid priority. Must be one of: {valid_priorities}")

        data = {
            "customer_name": customer_name,
            "location": location,
            "contact_number": contact_number,
            "description": description,
            "priority": priority.lower(),
            "request_date": datetime.now().isoformat()
        }

        return self._make_request("POST", "service-requests", data)

    def get_service_request(self, request_id: str) -> Dict:
        """
        Retrieve details of a specific service request.

        Args:
            request_id (str): ID of the service request

        Returns:
            Dict: Service request details
        """
        return self._make_request("GET", f"service-requests/{request_id}")

    def update_service_request(
        self,
        request_id: str,
        status: Optional[str] = None,
        technician: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict:
        """
        Update a service request with new information.

        Args:
            request_id (str): ID of the service request
            status (Optional[str]): New status of the request
            technician (Optional[str]): Assigned technician
            notes (Optional[str]): Additional notes

        Returns:
            Dict: Updated service request details
        """
        data = {}
        if status:
            data["status"] = status
        if technician:
            data["technician"] = technician
        if notes:
            data["notes"] = notes

        return self._make_request("PUT", f"service-requests/{request_id}", data)

    def list_service_requests(
        self,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None
    ) -> List[Dict]:
        """
        List all service requests with optional filters.

        Args:
            status (Optional[str]): Filter by status
            priority (Optional[str]): Filter by priority
            date_from (Optional[str]): Filter by start date (YYYY-MM-DD)
            date_to (Optional[str]): Filter by end date (YYYY-MM-DD)

        Returns:
            List[Dict]: List of service requests matching filters
        """
        params = []
        if status:
            params.append(f"status={status}")
        if priority:
            params.append(f"priority={priority}")
        if date_from:
            params.append(f"date_from={date_from}")
        if date_to:
            params.append(f"date_to={date_to}")

        endpoint = "service-requests"
        if params:
            endpoint += "?" + "&".join(params)

        return self._make_request("GET", endpoint)

    def delete_service_request(self, request_id: str) -> bool:
        """
        Delete a service request.

        Args:
            request_id (str): ID of the service request to delete

        Returns:
            bool: True if deletion was successful
        """
        self._make_request("DELETE", f"service-requests/{request_id}")
        return True

# Example usage
if __name__ == "__main__":
    # Initialize the service with your API credentials
    service = WaterLeakageService(
        api_base_url="https://api.waterleakage.example.com/v1",
        api_key="your_api_key_here"
    )

    # Create a new service request
    try:
        new_request = service.create_service_request(
            customer_name="Ahmed Mohammed",
            location="123 Main St, Riyadh",
            contact_number="+966501234567",
            description="Water leakage in bathroom",
            priority="high"
        )
        print("Created request:", json.dumps(new_request, indent=2))
    except ValueError as e:
        print(f"Error creating request: {e}")

    # Get list of service requests
    try:
        requests = service.list_service_requests(status="open", priority="high")
        print("Open high-priority requests:", json.dumps(requests, indent=2))
    except ValueError as e:
        print(f"Error listing requests: {e}")
```
