"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Generate a Python script that utilizes SMART Training Resources' courseware to enhance employability skills in students.
Generated: DETERMINISTIC_99e7b9ae2dd906a9
Batch ID: 20250612_163958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.smarttraining.com/v1": {
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
import os
import json
from typing import Dict, List, Optional
import requests
from requests.exceptions import RequestException

class SMARTTrainingResourceClient:
    """
    A client to interact with SMART Training Resources API to fetch and manage courseware.
    Enhances employability skills in students by providing access to relevant courses.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.smarttraining.com/v1"):
        """
        Initialize the client with API key and base URL.

        Args:
            api_key: API key for authentication.
            base_url: Base URL for the API (defaults to production).
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make HTTP requests to the API.

        Args:
            method: HTTP method (GET, POST, etc.).
            endpoint: API endpoint.
            params: Query parameters.
            data: Request body data.

        Returns:
            Response JSON data.

        Raises:
            RequestException: If the request fails.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise RequestException(f"API request failed: {e}")

    def get_courses(self, skill_type: Optional[str] = None) -> List[Dict]:
        """
        Fetch all available courses, optionally filtered by skill type.

        Args:
            skill_type: Type of employability skill to filter by (e.g., "communication").

        Returns:
            List of course dictionaries.
        """
        params = {"skill_type": skill_type} if skill_type else None
        return self._make_request("GET", "courses", params=params).get("courses", [])

    def get_course_details(self, course_id: str) -> Dict:
        """
        Fetch detailed information about a specific course.

        Args:
            course_id: Unique identifier for the course.

        Returns:
            Course details dictionary.
        """
        return self._make_request("GET", f"courses/{course_id}")

    def enroll_student(self, course_id: str, student_email: str) -> Dict:
        """
        Enroll a student in a course.

        Args:
            course_id: Unique identifier for the course.
            student_email: Email of the student to enroll.

        Returns:
            Enrollment confirmation dictionary.
        """
        data = {"student_email": student_email}
        return self._make_request("POST", f"courses/{course_id}/enroll", data=data)

    def get_student_progress(self, student_email: str) -> List[Dict]:
        """
        Fetch progress of a student across all enrolled courses.

        Args:
            student_email: Email of the student.

        Returns:
            List of progress dictionaries for each enrolled course.
        """
        return self._make_request("GET", f"students/{student_email}/progress").get("progress", [])

    def download_course_materials(self, course_id: str, download_dir: str = "materials") -> str:
        """
        Download all materials for a course.

        Args:
            course_id: Unique identifier for the course.
            download_dir: Directory to save materials (default: "materials").

        Returns:
            Path to the downloaded materials directory.

        Raises:
            OSError: If directory creation or file writing fails.
        """
        materials = self._make_request("GET", f"courses/{course_id}/materials").get("materials", [])
        
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        course_dir = os.path.join(download_dir, course_id)
        if not os.path.exists(course_dir):
            os.makedirs(course_dir)

        for material in materials:
            try:
                response = requests.get(material["url"])
                response.raise_for_status()
                file_path = os.path.join(course_dir, material["name"])
                with open(file_path, "wb") as f:
                    f.write(response.content)
            except (RequestException, OSError) as e:
                raise OSError(f"Failed to download material {material['name']}: {e}")

        return course_dir


# Example usage
if __name__ == "__main__":
    # Load configuration from environment variables
    API_KEY = os.getenv("SMART_API_KEY")
    if not API_KEY:
        raise ValueError("SMART_API_KEY environment variable not set")

    client = SMARTTrainingResourceClient(API_KEY)

    try:
        # Fetch courses for communication skills
        courses = client.get_courses(skill_type="communication")
        print("Available communication courses:", json.dumps(courses, indent=2))

        if courses:
            # Enroll a student in the first course
            course_id = courses[0]["id"]
            enrollment = client.enroll_student(course_id, "student@example.com")
            print("Enrollment confirmation:", json.dumps(enrollment, indent=2))

            # Download course materials
            materials_path = client.download_course_materials(course_id)
            print(f"Materials downloaded to: {materials_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
