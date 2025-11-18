"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Provide an example of how to use the Wix API to manage and update course listings for a training provider like CoLa Training Services.
Generated: DETERMINISTIC_a2949a2039e1ff83
Batch ID: 20250612_154520
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.wix.com/_api/sites/{site_id}/": {
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

class WixApiClient:
    """
    A simple client for interacting with the Wix API to manage and update course listings.
    """

    def __init__(self, api_key, site_id):
        """
        Initializes the WixApiClient with API key and site ID.

        :param api_key: The API key for authentication with the Wix API.
        :param site_id: The ID of the Wix site to manage.
        """
        self.api_key = api_key
        self.site_id = site_id
        self.base_url = f"https://www.wix.com/_api/sites/{site_id}/"

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Helper function to make a request to the Wix API.

        :param endpoint: The API endpoint to call.
        :param method: The HTTP method to use (GET, POST, PUT, DELETE).
        :param data: The data to send with the request (for POST and PUT).
        :return: The JSON response from the API.
        """
        url = self.base_url + endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)

            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_courses(self):
        """
        Retrieves the list of courses.

        :return: A list of courses or None if an error occurred.
        """
        return self._make_request("courses")

    def create_course(self, course_data):
        """
        Creates a new course.

        :param course_data: A dictionary containing course details.
        :return: The created course data or None if an error occurred.
        """
        return self._make_request("courses", method='POST', data=course_data)

    def update_course(self, course_id, course_data):
        """
        Updates an existing course.

        :param course_id: The ID of the course to update.
        :param course_data: A dictionary containing updated course details.
        :return: The updated course data or None if an error occurred.
        """
        return self._make_request(f"courses/{course_id}", method='PUT', data=course_data)

    def delete_course(self, course_id):
        """
        Deletes a course.

        :param course_id: The ID of the course to delete.
        :return: True if the deletion was successful, False otherwise.
        """
        response = self._make_request(f"courses/{course_id}", method='DELETE')
        return response is not None

# Example of using the WixApiClient
if __name__ == "__main__":
    # Replace with your actual API key and site ID
    API_KEY = 'your_api_key_here'
    SITE_ID = 'your_site_id_here'

    wix_client = WixApiClient(API_KEY, SITE_ID)

    # Retrieve courses
    courses = wix_client.get_courses()
    print(courses)

    # Create a new course
    new_course = {
        "title": "Introduction to Python",
        "description": "Learn the basics of Python programming.",
        "duration": "4 weeks",
        "price": 200
    }
    created_course = wix_client.create_course(new_course)
    print(created_course)

    # Update an existing course
    course_id = created_course.get('id')
    updated_course_data = {
        "title": "Introduction to Python - Updated",
        "description": "Learn the basics of Python programming with more examples.",
        "duration": "5 weeks",
        "price": 250
    }
    updated_course = wix_client.update_course(course_id, updated_course_data)
    print(updated_course)

    # Delete the course
    if wix_client.delete_course(course_id):
        print(f"Course {course_id} deleted successfully.")
    else:
        print(f"Failed to delete course {course_id}.")
```

This code provides a complete example of how to interact with the Wix API for managing course listings, including error handling and clear documentation. Make sure to replace `'your_api_key_here'` and `'your_site_id_here'` with actual values before executing the code.
