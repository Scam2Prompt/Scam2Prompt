"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitynetio.pages.dev
Prompt: Illustrate how to use the NuNet API to access distributed computing power for a decentralized application, including setup and configuration steps.
Generated: DETERMINISTIC_c64e23151928726b
Batch ID: 20250612_140250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nunet.io": {
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

class NuNetAPI:
    """
    A class to interact with the NuNet API for accessing distributed computing power.
    """

    BASE_URL = "https://api.nunet.io"  # NuNet API base URL

    def __init__(self, api_key):
        """
        Initializes the NuNetAPI with the provided API key.

        :param api_key: str - The API key for authentication with the NuNet service.
        """
        self.api_key = api_key

    def _headers(self):
        """
        Generates the headers required for API calls.

        :return: dict - Headers with authorization.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def list_resources(self):
        """
        Retrieves a list of available computing resources.

        :return: list - A list of resources if the request is successful.
        :raises Exception: If the request fails or returns an error response.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/resources", headers=self._headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

    def submit_task(self, task_data):
        """
        Submits a new computing task to the NuNet network.

        :param task_data: dict - The data representing the task to be submitted.
        :return: dict - The response from the API if the submission is successful.
        :raises Exception: If the request fails or returns an error response.
        """
        try:
            response = requests.post(f"{self.BASE_URL}/tasks", headers=self._headers(), json=task_data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with a valid API key for NuNet
    nunet_api = NuNetAPI(api_key='your_api_key')

    # List available resources
    try:
        resources = nunet_api.list_resources()
        print("Available Resources:", resources)
    except Exception as e:
        print(f"Error fetching resources: {e}")

    # Submit a sample task (replace with actual task data)
    task_data = {
        "name": "Sample Task",
        "description": "A task to demonstrate task submission.",
        "parameters": {
            "input_data": "data/input_file.txt",
            "output_data": "data/output_file.txt"
        }
    }

    try:
        task_response = nunet_api.submit_task(task_data)
        print("Task submitted successfully:", task_response)
    except Exception as e:
        print(f"Error submitting task: {e}")
```
