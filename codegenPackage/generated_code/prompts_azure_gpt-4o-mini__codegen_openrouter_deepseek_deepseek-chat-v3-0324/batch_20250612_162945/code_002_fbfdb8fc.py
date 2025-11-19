"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Create an API call to retrieve information about tailored driving courses, similar to those mentioned in the My Difference Between.com article.
Generated: DETERMINISTIC_fbfdb8fc5ec05247
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Any, Optional

class DrivingCourseAPI:
    """
    A class to interact with a driving course API to retrieve information about tailored driving courses.
    
    Attributes:
        base_url (str): The base URL of the API.
        headers (Dict[str, str]): Headers to be included in the API requests.
    """
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize the DrivingCourseAPI with the base URL and optional API key.
        
        Args:
            base_url (str): The base URL of the API.
            api_key (Optional[str]): API key for authentication. Defaults to None.
        """
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
    
    def get_driving_courses(self, filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieve information about tailored driving courses based on optional filters.
        
        Args:
            filters (Optional[Dict[str, Any]]): A dictionary of filters to apply to the query.
                Example: {"course_type": "defensive", "location": "New York"}
        
        Returns:
            Dict[str, Any]: A dictionary containing the API response.
        
        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        endpoint = f"{self.base_url}/driving-courses"
        try:
            response = requests.get(
                endpoint,
                headers=self.headers,
                params=filters
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {e}")
    
    def get_course_details(self, course_id: str) -> Dict[str, Any]:
        """
        Retrieve detailed information about a specific driving course.
        
        Args:
            course_id (str): The unique identifier for the driving course.
        
        Returns:
            Dict[str, Any]: A dictionary containing the API response.
        
        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        endpoint = f"{self.base_url}/driving-courses/{course_id}"
        try:
            response = requests.get(
                endpoint,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"API request failed: {e}")
```
