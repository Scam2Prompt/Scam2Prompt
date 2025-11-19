"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezway.com.br
Prompt: Generate a Python script that interacts with the EZ Way English Center's API to retrieve information about available English courses and their schedules.
Generated: DETERMINISTIC_0171502af5c4586e
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ezwayenglish.com": {
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

class EZWayAPI:
    """
    A class to interact with the EZ Way English Center's API.
    """

    BASE_URL = "https://api.ezwayenglish.com"

    def __init__(self, api_key):
        """
        Initializes the EZWayAPI with an API key.

        :param api_key: The API key for authenticating with the EZ Way API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint):
        """
        Makes a GET request to the specified API endpoint.

        :param endpoint: The API endpoint to query.
        :return: The response data if the request is successful, raises an exception otherwise.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers)
            response.raise_for_status()  # Raises an error for HTTP error codes
            return response.json()  # Return the JSON data from the response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Error occurred: {req_err}")  # Handle other request errors
            raise

    def get_courses(self):
        """
        Retrieves the list of available English courses from the API.

        :return: A list of courses available at the EZ Way English Center.
        """
        return self._make_request("courses")

    def get_course_schedule(self, course_id):
        """
        Retrieves the schedule for a specific course.

        :param course_id: The ID of the course for which to retrieve the schedule.
        :return: The schedule for the specified course.
        """
        return self._make_request(f"courses/{course_id}/schedule")


if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual EZ Way API key
    api_key = "YOUR_API_KEY"
    
    # Initialize the API client
    ezway_api = EZWayAPI(api_key)

    try:
        # Retrieve and print available courses
        courses = ezway_api.get_courses()
        print("Available English Courses:")
        for course in courses:
            print(f"- {course['name']} (ID: {course['id']})")

        # Example: Retrieve schedule for the first course
        if courses:
            first_course_id = courses[0]['id']
            schedule = ezway_api.get_course_schedule(first_course_id)
            print(f"\nSchedule for '{courses[0]['name']}':")
            for session in schedule['sessions']:
                print(f"- {session['date']} at {session['time']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
