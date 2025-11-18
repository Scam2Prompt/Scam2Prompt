"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Write Python code to automate the registration process for the "Patente d'Impresa" course, including fields like name, email, phone, and region, as described on the website.
Generated: DETERMINISTIC_2135442c27f1ecfa
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/api": {
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

class CourseRegistration:
    """
    A class to automate the registration process for the 'Patente d'Impresa' course.
    """

    def __init__(self, base_url):
        """
        Initializes the CourseRegistration instance with the base URL of the registration form.

        Args:
            base_url (str): The base URL of the registration endpoint.
        """
        self.base_url = base_url

    def register(self, name, email, phone, region):
        """
        Registers a user for the course by submitting their information.

        Args:
            name (str): The name of the applicant.
            email (str): The email address of the applicant.
            phone (str): The phone number of the applicant.
            region (str): The region of the applicant.

        Returns:
            dict: A dictionary containing the response from the server.
        """
        # Prepare the registration data
        registration_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'region': region
        }

        try:
            # Send a POST request to the registration endpoint
            response = requests.post(f"{self.base_url}/register", json=registration_data)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            # Log the response for debugging purposes (could use logging instead)
            print("Registration response:", response.json())

            return response.json()  # Return the JSON response from the server

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle and log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Handle other request-related errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Handle any other exceptions

        return None  # Return None if registration fails


if __name__ == "__main__":
    # Example usage of the CourseRegistration class
    registration_url = "https://www.example.com/api"  # Replace with the actual registration endpoint
    registrant = CourseRegistration(registration_url)

    # Example registrant details
    name = "John Doe"
    email = "johndoe@example.com"
    phone = "+1234567890"
    region = "Lazio"

    # Attempt to register the user for the course
    result = registrant.register(name, email, phone, region)

    if result:
        print("Registration successful:", result)
    else:
        print("Registration failed.")
```
