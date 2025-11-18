"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Write Python code to integrate with an online course platform API that allows users to browse and filter products, similar to the functionality described on the rabbie-wall--extension-docs website.
Generated: DETERMINISTIC_c7839b6a9128431e
Batch ID: 20250612_153722
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/courses": {
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

class CoursePlatformAPI:
    """
    A class to interact with the online course platform API.
    This class allows users to browse and filter available courses.
    """

    BASE_URL = "https://api.example.com/courses"  # Replace with actual API endpoint

    def __init__(self, api_key):
        """
        Initializes the API client with the provided API key.
        
        :param api_key: str - The API key to authenticate requests.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the API and handles errors.

        :param endpoint: str - The API endpoint to call.
        :param params: dict - Additional parameters for the request.
        :return: dict - The JSON response from the API.
        :raises Exception: If the request fails or returns an error.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

    def browse_courses(self, category=None, level=None, price_range=None):
        """
        Retrieves a list of courses, with optional filtering by category, level, and price range.

        :param category: str - The category to filter courses by (e.g., 'Programming').
        :param level: str - The level to filter courses by (e.g., 'Beginner', 'Intermediate').
        :param price_range: tuple - A tuple of (min_price, max_price) to filter courses by price.
        :return: list - A list of courses matching the filter criteria.
        """
        params = {}
        if category:
            params['category'] = category
        if level:
            params['level'] = level
        if price_range:
            params['min_price'], params['max_price'] = price_range

        endpoint = self.BASE_URL
        return self._make_request(endpoint, params)

    def get_course_details(self, course_id):
        """
        Retrieves detailed information about a specific course.

        :param course_id: str - The ID of the course to retrieve.
        :return: dict - Detailed information about the course.
        :raises Exception: If the course cannot be found or if an error occurs.
        """
        endpoint = f"{self.BASE_URL}/{course_id}"
        return self._make_request(endpoint)

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    api_client = CoursePlatformAPI(API_KEY)

    try:
        filtered_courses = api_client.browse_courses(category="Programming", level="Beginner", price_range=(0, 100))
        for course in filtered_courses:
            print(course)

        course_details = api_client.get_course_details(course_id="12345")  # Replace with a valid course ID
        print(course_details)

    except Exception as e:
        print(f"An error occurred: {e}")
```
