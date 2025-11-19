"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Write a Python script that integrates with a law firm's API to submit a personal injury case request, ensuring it captures details like accident type and client contact information.
Generated: DETERMINISTIC_2ef05d7e991af64b
Batch ID: 20250612_163423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lawfirm.com": {
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

class LawFirmAPIClient:
    """A client to interact with the law firm's API for submitting personal injury case requests."""

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the API client with the base URL and API key.

        Args:
            base_url (str): The base URL of the law firm's API.
            api_key (str): The API key for authenticating requests.
        """
        self.base_url = base_url
        self.api_key = api_key

    def submit_case(self, accident_type: str, client_info: dict) -> dict:
        """
        Submits a personal injury case request to the law firm's API.

        Args:
            accident_type (str): The type of accident involved in the case.
            client_info (dict): A dictionary containing the client's contact information.

        Returns:
            dict: The response from the API after submitting the case.

        Raises:
            ValueError: If any required field is missing in the client_info.
            requests.exceptions.RequestException: For any HTTP-related errors.
        """
        # Validate client information
        required_fields = ['name', 'email', 'phone']
        for field in required_fields:
            if field not in client_info:
                raise ValueError(f"Missing required field: {field}")

        # Prepare the payload for the API request
        payload = {
            'accident_type': accident_type,
            'client_info': client_info
        }

        # Set headers for the API request
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        # Submit the case to the API
        try:
            response = requests.post(f"{self.base_url}/submit_case", json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise


if __name__ == "__main__":
    # Example usage of the LawFirmAPIClient
    BASE_URL = "https://api.lawfirm.com"
    API_KEY = "your_api_key_here"

    client = LawFirmAPIClient(BASE_URL, API_KEY)

    # Sample accident type and client information
    accident_type = "Car Accident"
    client_info = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '123-456-7890'
    }

    try:
        response = client.submit_case(accident_type, client_info)
        print("Case submitted successfully:", response)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Failed to submit case: {e}")
```
