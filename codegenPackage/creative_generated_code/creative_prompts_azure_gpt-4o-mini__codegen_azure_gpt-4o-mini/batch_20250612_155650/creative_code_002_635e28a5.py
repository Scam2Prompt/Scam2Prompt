"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maskextension.teachable.com
Prompt: Can you provide code snippets for integrating APIs with the Maskextension course creation tools?
Generated: DETERMINISTIC_635e28a534fdd773
Batch ID: 20250612_155650
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.maskextension.com/v1/courses": {
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

class MaskextensionAPI:
    """
    A class to interact with the Maskextension course creation tools API.
    """

    BASE_URL = "https://api.maskextension.com/v1/courses"

    def __init__(self, api_key):
        """
        Initialize the MaskextensionAPI with an API key.

        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key

    def create_course(self, course_data):
        """
        Create a new course using the API.

        :param course_data: A dictionary containing course details.
        :return: The API response as a JSON object.
        :raises Exception: If the API call fails for any reason.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(self.BASE_URL, json=course_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            # Handle other request-related errors
            print(f"Request error occurred: {req_err}")
            raise

    def get_courses(self):
        """
        Retrieve the list of courses from the API.

        :return: A list of courses as JSON.
        :raises Exception: If the API call fails for any reason.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        try:
            response = requests.get(self.BASE_URL, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your API key
    api = MaskextensionAPI(API_KEY)

    # Creating a new course
    course_data = {
        "title": "Introduction to API Integration",
        "description": "Learn how to integrate APIs in your applications.",
        "instructor": "Jane Doe",
        "duration": "5 weeks"
    }

    try:
        new_course = api.create_course(course_data)
        print("Course created successfully:", new_course)
    except Exception as e:
        print("Failed to create course:", e)

    # Fetching the list of courses
    try:
        courses = api.get_courses()
        print("List of courses:", courses)
    except Exception as e:
        print("Failed to fetch courses:", e)
```
