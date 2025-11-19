"""
Generated Code Metadata:
========================
Original URL: https://1iiinch.teachable.com
Prompt: Generate code to automate the creation of a course on Teachable using its API, including setting navigation links and user settings.
Generated: DETERMINISTIC_4abce8a2f3400a56
Batch ID: 20250612_153907
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{subdomain}.teachable.com/api/v1": {
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

class TeachableAPI:
    """
    A class to interact with the Teachable API for course creation and management.
    """

    def __init__(self, api_key, subdomain):
        """
        Initializes the TeachableAPI with the provided API key and subdomain.

        :param api_key: The API key for authenticating with the Teachable API.
        :param subdomain: The subdomain of the Teachable account.
        """
        self.api_key = api_key
        self.base_url = f"https://{subdomain}.teachable.com/api/v1"

    def create_course(self, course_data):
        """
        Creates a new course on Teachable.

        :param course_data: A dictionary containing course details.
        :return: The response from the API.
        """
        url = f"{self.base_url}/courses"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=course_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def set_navigation_links(self, course_id, navigation_links):
        """
        Sets navigation links for a specific course.

        :param course_id: The ID of the course to update.
        :param navigation_links: A list of navigation links to set.
        :return: The response from the API.
        """
        url = f"{self.base_url}/courses/{course_id}/navigation_links"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.put(url, json={"navigation_links": navigation_links}, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def update_user_settings(self, user_id, settings):
        """
        Updates user settings for a specific user.

        :param user_id: The ID of the user to update.
        :param settings: A dictionary containing user settings to update.
        :return: The response from the API.
        """
        url = f"{self.base_url}/users/{user_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.patch(url, json=settings, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key and subdomain
    API_KEY = "your_api_key"
    SUBDOMAIN = "your_subdomain"

    teachable_api = TeachableAPI(API_KEY, SUBDOMAIN)

    # Create a new course
    course_data = {
        "course": {
            "name": "New Course",
            "description": "This is a new course created via API.",
            "price": 1000,
            "published": True
        }
    }
    course_response = teachable_api.create_course(course_data)
    print("Course created:", course_response)

    # Set navigation links for the created course
    if course_response:
        course_id = course_response['id']
        navigation_links = [
            {"title": "Home", "url": "/"},
            {"title": "About", "url": "/about"},
            {"title": "Contact", "url": "/contact"}
        ]
        nav_response = teachable_api.set_navigation_links(course_id, navigation_links)
        print("Navigation links set:", nav_response)

    # Update user settings
    user_id = "user_id_here"  # Replace with actual user ID
    user_settings = {
        "user": {
            "email": "new_email@example.com",
            "first_name": "John",
            "last_name": "Doe"
        }
    }
    user_response = teachable_api.update_user_settings(user_id, user_settings)
    print("User settings updated:", user_response)
```
