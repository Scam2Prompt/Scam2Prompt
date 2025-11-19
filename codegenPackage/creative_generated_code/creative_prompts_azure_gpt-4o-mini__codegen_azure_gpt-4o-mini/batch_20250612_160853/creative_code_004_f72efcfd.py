"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opsense.com
Prompt: Describe how to set up digital checklists in OpSense for maintaining HACCP compliance in food processing facilities.
Generated: DETERMINISTIC_f72efcfd55e8bd41
Batch ID: 20250612_160853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opsense.io/v1": {
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
# OpSense HACCP Checklist Setup Script
# This script outlines the steps to create digital checklists in OpSense
# for maintaining HACCP compliance in food processing facilities.

import requests

class OpSenseAPI:
    """
    A class to interact with the OpSense API for managing digital checklists.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the OpSenseAPI with the given API key and base URL.

        Args:
            api_key (str): The API key for authenticating with the OpSense service.
            base_url (str): The base URL for the OpSense API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, method, endpoint, data=None):
        """
        Makes an HTTP request to the OpSense API.

        Args:
            method (str): HTTP method (e.g., 'GET', 'POST').
            endpoint (str): The API endpoint to call.
            data (dict, optional): The data to send with the request.

        Returns:
            Response: The response from the API.

        Raises:
            Exception: If the API request fails.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            headers = {'Authorization': f"Bearer {self.api_key}"}
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def create_checklist(self, checklist_name, tasks):
        """
        Creates a digital checklist in OpSense.

        Args:
            checklist_name (str): The name of the checklist.
            tasks (list): A list of tasks to include in the checklist.

        Returns:
            dict: The response containing the created checklist information.
        """
        endpoint = "checklists"
        data = {
            'name': checklist_name,
            'tasks': tasks
        }
        return self._make_request("POST", endpoint, data)

    def get_checklist(self, checklist_id):
        """
        Retrieves a checklist by its ID.

        Args:
            checklist_id (str): The ID of the checklist to retrieve.

        Returns:
            dict: The checklist information.
        """
        endpoint = f"checklists/{checklist_id}"
        return self._make_request("GET", endpoint)

# Main function to demonstrate checklist creation
if __name__ == "__main__":
    # Replace with your actual API key and base URL
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.opsense.io/v1"

    # Initialize the API client
    opsense_api = OpSenseAPI(API_KEY, BASE_URL)

    # Define the checklist details
    checklist_name = "HACCP Compliance Checklist"
    tasks = [
        "Verify temperature control for storage units",
        "Check sanitation schedules and logs",
        "Inspect equipment for cleanliness",
        "Review employee training records",
        "Document any deviations and corrective actions"
    ]

    # Create the checklist
    try:
        created_checklist = opsense_api.create_checklist(checklist_name, tasks)
        print("Checklist created successfully:", created_checklist)
    except Exception as e:
        print("Error creating checklist:", e)
```
