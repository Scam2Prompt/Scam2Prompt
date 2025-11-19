"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peptok.site
Prompt: Write a code snippet that demonstrates error handling when using the Peptok API.
Generated: DETERMINISTIC_4e0d0c457735c813
Batch ID: 20250612_162409
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.peptok.com/v1/message": {
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

def fetch_peptok_message(api_url, api_key):
    """
    Fetches a motivational message from the Peptok API.

    Parameters:
    api_url (str): The endpoint URL of the Peptok API.
    api_key (str): Your API key for authentication.

    Returns:
    str: A motivational message from the API, or an error message in case of failure.

    Raises:
    ValueError: If the API response contains unexpected data or status code.
    """
    try:
        # Setting up headers for authentication
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Sending the GET request to the Peptok API
        response = requests.get(api_url, headers=headers)

        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the expected key is in the response
        if "message" not in data:
            raise ValueError("Unexpected response format: 'message' key is missing")

        # Return the motivational message
        return data["message"]

    except requests.exceptions.HTTPError as http_err:
        # Log and handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
        return "Failed to fetch a message due to an HTTP error."

    except requests.exceptions.RequestException as req_err:
        # Log and handle other request-related errors
        print(f"Request error occurred: {req_err}")
        return "Failed to fetch a message due to a network error."

    except ValueError as val_err:
        # Log and handle value errors
        print(f"Value error occurred: {val_err}")
        return "Failed to fetch a message due to an unexpected API response."

    except Exception as err:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {err}")
        return "Failed to fetch a message due to an unknown error."


# Example usage:
if __name__ == "__main__":
    # Replace with your actual API endpoint and API key
    API_URL = "https://api.peptok.com/v1/message"
    API_KEY = "your_api_key_here"

    motivational_message = fetch_peptok_message(API_URL, API_KEY)
    print(f"Motivational Message: {motivational_message}")
```
