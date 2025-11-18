"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: Generate code to automate the creation of a course on Teachable using its API, including setting navigation links and user settings.
Generated: DETERMINISTIC_4abce8a2f3400a56
Batch ID: 20250612_153907
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{subdomain}.teachable.com/api/v1/": {
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
import json

class TeachableAPI:
    def __init__(self, api_key, subdomain):
        """
        Initializes the TeachableAPI with the provided API key and subdomain.

        :param api_key: The API key for authenticating with Teachable
        :param subdomain: The subdomain of the Teachable site
        """
        self.api_key = api_key
        self.base_url = f"https://{subdomain}.teachable.com/api/v1/"

    def create_course(self, course_data):
        """
        Creates a new course using the Teachable API.

        :param course_data: A dictionary containing course details
        :return: The JSON response from the Teachable API
        """
        url = f"{self.base_url}courses"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(course_data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating course: {e}")
            return None

    def set_navigation_links(self, course_id, navigation_links):
        """
        Sets the navigation links for the specified course.

        :param course_id: The ID of the course
        :param navigation_links: A list of navigation links to set
        :return: The JSON response from the Teachable API
        """
        url = f"{self.base_url}courses/{course_id}/navigation_links"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.put(url, headers=headers, data=json.dumps(navigation_links))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error setting navigation links: {e}")
            return None

    def set_user_settings(self, course_id, user_settings):
        """
        Updates user settings for the specified course.

        :param course_id: The ID of the course
        :param user_settings: A dictionary containing user settings
        :return: The JSON response from the Teachable API
        """
        url = f"{self.base_url}courses/{course_id}/user_settings"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.put(url, headers=headers, data=json.dumps(user_settings))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating user settings: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'
    SUBDOMAIN = 'your_subdomain_here'

    teachable_api = TeachableAPI(API_KEY, SUBDOMAIN)

    # Define course data
    course_data = {
        "course": {
            "title": "New Course Title",
            "description": "Description of the course",
            "price": 100,
            "visible_to": "all"
        }
    }

    # Create a new course
    course_response = teachable_api.create_course(course_data)
    if course_response:
        course_id = course_response['id']

        # Define navigation links
        navigation_links = [
            {"title": "Home", "url": "/home"},
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"}
        ]

        # Set navigation links for the newly created course
        teachable_api.set_navigation_links(course_id, navigation_links)

        # Define user settings
        user_settings = {
            "settings": {
                "allow_comments": True,
                "visibility": "public"
            }
        }

        # Update user settings for the course
        teachable_api.set_user_settings(course_id, user_settings)
```
