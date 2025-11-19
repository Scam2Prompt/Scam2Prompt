"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ictea.edu.mx
Prompt: Provide an example of using the Ictea API to retrieve faculty information in JSON format.
Generated: DETERMINISTIC_b96c9069385eab02
Batch ID: 20250612_155442
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ictea.com/v1": {
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

def get_faculty_information(api_base_url, api_key):
    """
    Fetch faculty information from the Ictea API.

    Parameters:
        api_base_url (str): Base URL of the Ictea API.
        api_key (str): Authentication API key.

    Returns:
        dict: Faculty information in JSON format if the request is successful.
        None: If the request fails or an error occurs.
    """
    # Endpoint for faculty information
    endpoint = f"{api_base_url}/faculty"

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the GET request to the API
        response = requests.get(endpoint, headers=headers)

        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        # Parse and return JSON data
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        # Log or handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Log or handle general request errors
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        # Catch-all for other exceptions
        print(f"An error occurred: {err}")

    return None


# Example usage
if __name__ == "__main__":
    # Replace with actual values
    API_BASE_URL = "https://api.ictea.com/v1"
    API_KEY = "your_api_key_here"

    # Fetch faculty information
    faculty_info = get_faculty_information(API_BASE_URL, API_KEY)

    if faculty_info:
        print("Faculty Information:")
        print(faculty_info)
    else:
        print("Failed to retrieve faculty information.")
```
