"""
Generated Code Metadata:
========================
Original URL: https://repositorio.sip.cl
Prompt: Design a simple API wrapper for Sistema Alexia Classroom using Python or JavaScript.
Generated: DETERMINISTIC_7f639c21b3cf3d4f
Batch ID: 20250622_212137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Optional, Dict, Any, List

class AlexiaClassroomAPI:
    """
    A simple API wrapper for Sistema Alexia Classroom.
    Handles authentication and provides methods to interact with the API endpoints.
    """

    def __init__(self, base_url: str, client_id: str, client_secret: str):
        """
        Initialize the API wrapper with base URL and credentials.

        Args:
            base_url: The base URL of the Alexia Classroom API
            client_id: Client ID for authentication
            client_secret: Client secret for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.session = requests.Session()

    def _get_auth_headers(self) -> Dict[str, str]:
        """
        Get authorization headers with the current access token.

        Returns:
            Dictionary containing Authorization header

        Raises:
            RuntimeError: If not authenticated
        """
        if not self.access_token:
            raise RuntimeError("Not authenticated. Call authenticate() first.")
        return {"Authorization": f"Bearer {self.access_token}"}

    def authenticate(self) -> None:
        """
        Authenticate with the API using client credentials.
        Stores the access token for subsequent requests.
        """
        auth_url = f"{self.base_url}/oauth/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        try:
            response = self.session.post(auth_url, data=data)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Authentication failed: {str(e)}")

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, 
                     data: Optional[Dict] = None) -> Any:
        """
        Internal method to make API requests.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (without base URL)
            params: Query parameters
            data: Request body data

        Returns:
            Parsed JSON response

        Raises:
            RuntimeError: For request errors or API errors
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = self._get_auth_headers()

        try:
            response = self.session.request(
                method,
                url,
                headers=headers,
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"API request failed: {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {str(e)}")

    def get_courses(self, page: int = 1, per_page: int = 10) -> List[Dict]:
        """
        Get a list of courses.

        Args:
            page: Page number
            per_page: Items per page

        Returns:
            List of course dictionaries
        """
        params = {
            "page": page,
            "per_page": per_page
        }
        return self._make_request("GET", "/api/v1/courses", params=params)

    def get_course(self, course_id: int) -> Dict:
        """
        Get details for a specific course.

        Args:
            course_id: ID of the course to retrieve

        Returns:
            Course details dictionary
        """
        return self._make_request("GET", f"/api/v1/courses/{course_id}")

    def create_assignment(self, course_id: int, title: str, description: str, 
                         due_date: str, points: int = 100) -> Dict:
        """
        Create a new assignment in a course.

        Args:
            course_id: ID of the course
            title: Assignment title
            description: Assignment description
            due_date: Due date in ISO format
            points: Maximum points (default: 100)

        Returns:
            Created assignment details
        """
        data = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "points": points
        }
        return self._make_request(
            "POST", 
            f"/api/v1/courses/{course_id}/assignments", 
            data=data
        )

    def get_student_submissions(self, course_id: int, assignment_id: int) -> List[Dict]:
        """
        Get student submissions for an assignment.

        Args:
            course_id: ID of the course
            assignment_id: ID of the assignment

        Returns:
            List of submission dictionaries
        """
        return self._make_request(
            "GET", 
            f"/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions"
        )

    def grade_submission(self, course_id: int, assignment_id: int, 
                         student_id: int, grade: float, feedback: str = "") -> Dict:
        """
        Grade a student submission.

        Args:
            course_id: ID of the course
            assignment_id: ID of the assignment
            student_id: ID of the student
            grade: Numeric grade
            feedback: Optional feedback

        Returns:
            Updated submission details
        """
        data = {
            "grade": grade,
            "feedback": feedback
        }
        return self._make_request(
            "PUT",
            f"/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{student_id}",
            data=data
        )
```
