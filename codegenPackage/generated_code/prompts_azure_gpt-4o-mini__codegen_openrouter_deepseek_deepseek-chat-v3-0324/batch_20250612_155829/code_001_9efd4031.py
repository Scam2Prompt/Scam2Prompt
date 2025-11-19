"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Write a Python script that integrates with an API to manage user registrations for online courses and workshops focused on emotional healing and personal growth.
Generated: DETERMINISTIC_9efd40318f1ec234
Batch ID: 20250612_155829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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
from typing import Dict, Optional, List
from datetime import datetime

class CourseRegistrationAPI:
    """
    A class to interact with an API for managing user registrations for online courses and workshops.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the API client with base URL and API key.
        
        Args:
            base_url (str): The base URL of the API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make HTTP requests to the API.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): API endpoint to call.
            data (Optional[Dict]): Data to send with the request.
        
        Returns:
            Dict: JSON response from the API.
        
        Raises:
            ValueError: If the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise ValueError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            raise ValueError(f"Request error occurred: {err}")
        except json.JSONDecodeError as json_err:
            raise ValueError(f"Failed to decode JSON response: {json_err}")

    def get_courses(self) -> List[Dict]:
        """
        Retrieve a list of available courses and workshops.
        
        Returns:
            List[Dict]: List of courses with their details.
        """
        return self._make_request('GET', 'courses')

    def get_course_details(self, course_id: str) -> Dict:
        """
        Get details for a specific course.
        
        Args:
            course_id (str): The ID of the course to retrieve.
        
        Returns:
            Dict: Course details.
        """
        return self._make_request('GET', f'courses/{course_id}')

    def register_user(self, course_id: str, user_data: Dict) -> Dict:
        """
        Register a user for a course.
        
        Args:
            course_id (str): The ID of the course to register for.
            user_data (Dict): User details including name, email, etc.
        
        Returns:
            Dict: Registration confirmation details.
        """
        required_fields = ['name', 'email', 'phone']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
        
        return self._make_request('POST', f'courses/{course_id}/registrations', user_data)

    def cancel_registration(self, registration_id: str) -> Dict:
        """
        Cancel a user's registration for a course.
        
        Args:
            registration_id (str): The ID of the registration to cancel.
        
        Returns:
            Dict: Cancellation confirmation details.
        """
        return self._make_request('DELETE', f'registrations/{registration_id}')

    def get_user_registrations(self, user_email: str) -> List[Dict]:
        """
        Retrieve all registrations for a specific user.
        
        Args:
            user_email (str): The email of the user to look up.
        
        Returns:
            List[Dict]: List of registrations for the user.
        """
        return self._make_request('GET', f'registrations?email={user_email}')

    def update_registration(self, registration_id: str, updates: Dict) -> Dict:
        """
        Update a user's registration details.
        
        Args:
            registration_id (str): The ID of the registration to update.
            updates (Dict): Fields to update and their new values.
        
        Returns:
            Dict: Updated registration details.
        """
        return self._make_request('PUT', f'registrations/{registration_id}', updates)


# Example usage
if __name__ == "__main__":
    # Initialize the API client
    api = CourseRegistrationAPI(
        base_url="https://api.example.com/v1",
        api_key="your_api_key_here"
    )

    try:
        # Get available courses
        courses = api.get_courses()
        print("Available courses:", courses)

        # Register a user for a course
        registration = api.register_user(
            course_id="course123",
            user_data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "+1234567890",
                "notes": "Interested in emotional healing workshops"
            }
        )
        print("Registration successful:", registration)

        # Get user's registrations
        user_registrations = api.get_user_registrations("jane@example.com")
        print("User registrations:", user_registrations)

    except ValueError as e:
        print(f"Error: {e}")
```
