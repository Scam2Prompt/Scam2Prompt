"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Recommend tools or APIs for implementing a "Save and Listen Later" feature for a digital radio platform, similar to Radio S's "Sačuvaj, slušaj kad god poželiš."
Generated: DETERMINISTIC_0b8f6c2d98f4147f
Batch ID: 20250612_150234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/radio": {
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
import json
import requests

class SaveAndListenLater:
    """
    A class to implement the 'Save and Listen Later' feature for a digital radio platform.
    This class interacts with a storage API to save user-selected radio programs and 
    retrieves them for later listening.
    """

    def __init__(self, api_url):
        """
        Initializes the SaveAndListenLater class with the specified API URL.

        :param api_url: str - The base URL of the storage API.
        """
        self.api_url = api_url

    def save_program(self, program_id, user_id):
        """
        Saves a radio program for a user.

        :param program_id: str - The ID of the radio program to save.
        :param user_id: str - The ID of the user saving the program.
        :return: dict - Response from the API.
        """
        try:
            payload = {
                'user_id': user_id,
                'program_id': program_id
            }
            response = requests.post(f"{self.api_url}/save", json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the API response as a JSON object
        except requests.RequestException as e:
            # Handle any request exceptions, e.g., network issues, timeouts, etc.
            print(f"Error saving program {program_id} for user {user_id}: {e}")
            return None

    def get_saved_programs(self, user_id):
        """
        Retrieves the list of saved programs for a user.

        :param user_id: str - The ID of the user whose saved programs to retrieve.
        :return: list - A list of saved programs, or None on error.
        """
        try:
            response = requests.get(f"{self.api_url}/saved/{user_id}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the API response as a JSON object
        except requests.RequestException as e:
            # Handle any request exceptions
            print(f"Error retrieving saved programs for user {user_id}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_URL = "https://api.example.com/v1/radio"  # Replace with your actual API URL
    radio_service = SaveAndListenLater(API_URL)

    # Save a program
    response = radio_service.save_program("program_123", "user_456")
    if response:
        print("Program saved:", response)

    # Retrieve saved programs
    saved_programs = radio_service.get_saved_programs("user_456")
    if saved_programs:
        print("Saved Programs:", saved_programs)
```
