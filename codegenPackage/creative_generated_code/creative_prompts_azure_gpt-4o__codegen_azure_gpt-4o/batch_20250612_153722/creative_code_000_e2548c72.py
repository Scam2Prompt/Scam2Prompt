"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Write code to integrate Teachable's API for managing online courses, specifically for a platform like rbby-wollet.
Generated: DETERMINISTIC_e2548c721331cca2
Batch ID: 20250612_153722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.teachable.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class TeachableAPIClient:
    """
    A client to interact with Teachable's API for managing online courses.
    """
    BASE_URL = "https://api.teachable.com/v1"  # Replace with actual Teachable API Base URL

    def __init__(self, api_key):
        """
        Initialize the Teachable API client.

        :param api_key: The API key for authenticating requests to Teachable.
        """
        if not api_key:
            raise ValueError("API key must be provided.")
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def list_courses(self):
        """
        Fetch the list of courses from Teachable.

        :return: A list containing course details.
        :raises: RuntimeError if the request fails.
        """
        url = f"{self.BASE_URL}/courses"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch courses: {e}")

    def create_course(self, course_title, course_description):
        """
        Create a new course on Teachable.

        :param course_title: The title of the course.
        :param course_description: A brief description of the course.
        :return: The JSON response containing course details from Teachable.
        :raises: ValueError if required fields are missing.
        :raises: RuntimeError if the request fails.
        """
        if not course_title or not course_description:
            raise ValueError("Course title and description must be provided.")

        url = f"{self.BASE_URL}/courses"
        payload = {
            "course": {
                "title": course_title,
                "description": course_description
            }
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to create course: {e}")

    def update_course(self, course_id, course_title=None, course_description=None):
        """
        Update an existing course on Teachable.

        :param course_id: The ID of the course to update.
        :param course_title: The updated title of the course (optional).
        :param course_description: The updated description of the course (optional).
        :return: The JSON response containing updated course details.
        :raises: ValueError if course_id is not provided.
        :raises: RuntimeError if the request fails.
        """
        if not course_id:
            raise ValueError("Course ID must be provided.")

        url = f"{self.BASE_URL}/courses/{course_id}"
        payload = {"course": {}}
        if course_title:
            payload["course"]["title"] = course_title
        if course_description:
            payload["course"]["description"] = course_description

        try:
            response = requests.patch(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to update course: {e}")

    def delete_course(self, course_id):
        """
        Delete a course on Teachable.

        :param course_id: The ID of the course to delete.
        :return: A success message if deletion is successful.
        :raises: ValueError if course_id is not provided.
        :raises: RuntimeError if the request fails.
        """
        if not course_id:
            raise ValueError("Course ID must be provided.")

        url = f"{self.BASE_URL}/courses/{course_id}"

        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            return {"message": "Course deleted successfully"}
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to delete course: {e}")


# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "your_api_key_here"
    client = TeachableAPIClient(api_key)

    try:
        # List all courses
        courses = client.list_courses()
        print("Courses:", courses)

        # Create a new course
        new_course = client.create_course("Python for Beginners", "Learn Python from scratch.")
        print("New Course Created:", new_course)

        # Update an existing course
        updated_course = client.update_course(new_course["id"], course_description="Updated description.")
        print("Updated Course:", updated_course)

        # Delete a course
        delete_message = client.delete_course(new_course["id"])
        print(delete_message)

    except RuntimeError as e:
        print("Error:", e)
```
