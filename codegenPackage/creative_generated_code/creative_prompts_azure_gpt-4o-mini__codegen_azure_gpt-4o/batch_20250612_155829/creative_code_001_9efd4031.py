"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarparasanar.com.mx
Prompt: Write a Python script that integrates with an API to manage user registrations for online courses and workshops focused on emotional healing and personal growth.
Generated: DETERMINISTIC_9efd40318f1ec234
Batch ID: 20250612_155829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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

# Constants for API integration
API_BASE_URL = "https://api.example.com/v1"  # Replace with actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Function to handle API requests
def api_request(endpoint, method="GET", data=None):
    """
    Sends a request to the API and returns the response.

    Args:
        endpoint (str): API endpoint to hit.
        method (str): HTTP method ('GET', 'POST', etc.).
        data (dict): Data to be sent with the request (for POST/PUT requests).

    Returns:
        dict: Parsed JSON response from the API.

    Raises:
        Exception: If the request fails or returns an error status.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send request based on method type
        if method.upper() == "GET":
            response = requests.get(url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method")

        # Raise error for HTTP response codes >= 400
        response.raise_for_status()

        # Return parsed JSON data
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    except ValueError as ve:
        raise Exception(f"Invalid data or request setup: {ve}")

# Function to register a user for a course
def register_user(name, email, course_id):
    """
    Registers a user for a specific course.

    Args:
        name (str): Name of the user.
        email (str): Email of the user.
        course_id (str): ID of the course to register for.

    Returns:
        dict: Confirmation of the registration.

    Raises:
        Exception: If registration fails.
    """
    endpoint = "registrations"
    data = {
        "name": name,
        "email": email,
        "course_id": course_id
    }
    
    try:
        response = api_request(endpoint, method="POST", data=data)
        return response
    except Exception as e:
        raise Exception(f"Failed to register user: {e}")

# Function to list available courses
def list_courses():
    """
    Fetches the list of available courses.

    Returns:
        list: List of courses with their IDs and details.

    Raises:
        Exception: If fetching courses fails.
    """
    endpoint = "courses"
    
    try:
        response = api_request(endpoint, method="GET")
        return response.get("courses", [])
    except Exception as e:
        raise Exception(f"Failed to fetch courses: {e}")

# Main script to interact with the API
if __name__ == "__main__":
    try:
        # List available courses
        print("Fetching available courses...")
        courses = list_courses()
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course['name']} (ID: {course['id']}) - {course['description']}")

        # Prompt user for registration details
        print("\nRegister for a course:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        course_index = int(input("Enter the course number you'd like to register for: ")) - 1

        # Validate course selection
        if course_index < 0 or course_index >= len(courses):
            print("Invalid course selection.")
        else:
            course_id = courses[course_index]['id']
            confirmation = register_user(name, email, course_id)
            print(f"Registration successful: {json.dumps(confirmation, indent=2)}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
